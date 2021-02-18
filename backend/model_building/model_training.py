"""
https://www.kaggle.com/kabure/predicting-credit-risk-model-pipeline
"""
from sklearn.model_selection import KFold, cross_val_score
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.naive_bayes import GaussianNB
from sklearn.svm import SVC
from xgboost import XGBClassifier
import matplotlib.pyplot as plt
import pickle
from backend.util.static import PATHS, dataset, params

def train_model(X_train, y_train, chosen_model):
    """Trains the chosen model on the complete training set."""
    chosen_model.fit(X_train, y_train.values.ravel()) # .values.ravel() because of Random Forest error

    return chosen_model

def save_trained_model(trained_model, model_name):
    """Save a trained model"""
    filepath = PATHS["04_trained_models"] + model_name + ".sav"
    pickle.dump(trained_model, open(filepath, 'wb'))

def load_trained_model(model_name):
    """Load a trained model and return it"""
    filepath = PATHS["04_trained_models"] + model_name + ".sav"
    loaded_model = pickle.load(open(filepath, 'rb'))
    return loaded_model


def model_selection(model_name):
    """Select a model. Todo: validation?"""
    if model_name == "Extreme Gradient Boosting":
        chosen_model = XGBClassifier(use_label_encoder=False)
    elif model_name == "Logistic Regression":
        chosen_model = LogisticRegression()
    elif model_name == "Decision Tree":
        chosen_model = DecisionTreeClassifier(criterion='gini', max_depth=3)
    elif model_name == "Random Forest":
        chosen_model = RandomForestClassifier(max_depth=50, max_features=10, n_estimators=200, random_state=2)
    elif model_name == "Support Vector Machine":
        chosen_model = SVC(gamma='auto')
    else:
        raise AssertionError("Error in if-else statement")

    return chosen_model, model_name


def model_selection_old(X_train, y_train, seed=7):
    """Gets the training data and trains different models"""

    # prepare models
    models = []
    models_not_used = []
    models.append(('LR', LogisticRegression()))
    models.append(('LDA', LinearDiscriminantAnalysis()))
    models.append(('KNN', KNeighborsClassifier()))
    models.append(('CART', DecisionTreeClassifier()))
    models.append(('NB', GaussianNB()))
    models_not_used.append(('RF', RandomForestClassifier()))
    models_not_used.append(('SVM', SVC(gamma='auto')))
    models.append(('XGB', XGBClassifier()))

    # evaluate each model in turn
    results = []
    names = []
    scoring = 'f1_macro'

    for name, model in models:
        kfold = KFold(n_splits=30, random_state=seed)
        cv_results = cross_val_score(model, X_train, y_train, cv=kfold, scoring=scoring)
        results.append(cv_results)
        names.append(name)
        msg = "%s: %f (%f)" % (name, cv_results.mean(), cv_results.std())
        print(msg)

    if params["plot"]:
        print("Close plot and then choose model..")

        # boxplot algorithm comparison
        fig = plt.figure(figsize=(11, 6))
        fig.suptitle('Algorithm Comparison')
        ax = fig.add_subplot(111)
        plt.boxplot(results)
        ax.set_xticklabels(names)
        plt.show()

        var = int(input("""Which model do you want to choose?: 
                    LR:1
                    LDA:2
                    KNN:3
                    CART:4
                    NB:5
                    RF:6
                    SVM:7
                    XGB:8 """))
    else:
        # always choose logistic Regression
        var=params["model"]

    if var not in [1, 2, 3, 4, 5, 6, 7, 8]:
        raise AssertionError("Choose correctly..")
    else:
        if var == 1:
            model = LogisticRegression()
        elif var == 2:
            model = LinearDiscriminantAnalysis()
        elif var == 3:
            model = KNeighborsClassifier()
        elif var == 4:
            model = DecisionTreeClassifier()
        elif var == 5:
            model = GaussianNB()
        elif var == 6:
            model = RandomForestClassifier()
        elif var == 7:
            model = SVC()
        elif var == 8:
            model = XGBClassifier()

    return model