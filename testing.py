
import pandas as pd


from backend.data_preprocessing.data_loading import load_data, load_encoded_data, initialize, explore_data, data_exploration
from backend.model_building.model_training import save_trained_model
from backend.data_preprocessing import data_loading
from backend.model_building import model_training
#from backend.xai_cockpit import model_explaining
from backend.util.static import PATHS, dataset, params
from backend.util.util import get_the_filenames
from backend.inference.predict import predict
from sklearn.metrics import accuracy_score,classification_report, confusion_matrix
from xgboost import plot_importance
from xgboost import XGBClassifier
import matplotlib.pyplot as plt
from backend.xai_cockpit.model_explaining import *
from backend.inference.predict import *
import dataframe_image as dfi





if __name__ == '__main__':
 s = (input("Type 'start' to initialize: "))

 initialize()
 df=load_data(type="raw")
 s
# explore_data(df)
 data_exploration(df)


 X_train_encoded, y_train, X_test_encoded, y_test, encoder = data_loading.load_encoded_data()
 # Choose a model and train it
 model, model_name = model_training.model_selection(input("Select Model: "))
 print("Trained model: " , model_name)
 X_test =data_loading.train_test_split(df)
 model = model_training.train_model(X_train_encoded, y_train, model)
 model_training.save_trained_model(model, model_name)
 print("Training score data: ")
 print(model.score(X_train_encoded, y_train))
 #good: 20, bad:35

 i = int(input("Enter instance for prediction (0-100):"))
 print("Chosen Instance: ", i)
 print(X_test_encoded.iloc[i])
 #print(y_test.iloc[i])
 #print(X_test)
 dataTable(df, i)

 print(df.iloc[i])
 y_hat = model.predict(X_test_encoded)
 p_pred=model.predict_proba(X_test_encoded)
 print("Predicted class by the model: ", y_hat[i])
 print("Predicted % by the model: ", p_pred[i])
 #print("True Prediction:", y_test.iloc[i])

 predict(model, X_test_encoded, y_test)
 print("Enter decision for instance ", i)
 j = int(input(" [0 or 1]:"))


#if j==y_hat[i]:
#    print("correct")
#else:
#   print("incorrect")'
o=input("Type 'yes' for an Explanation: ")

if model_name=="Logistic Regression":
 print("slopes:", model.coef_)
 print("intercept:", model.intercept_)
 #print(model.summary())
 from matplotlib import pyplot

#get importance
 importance = model.coef_[0]
 # summarize feature importance
 for s, v in enumerate(importance):
  if abs(v)>=0.5:
    print('Feature: %0d, Score: %.5f' % (s, v))
 # plot feature importance
 pyplot.bar([x for x in range(len(importance))], importance)
 pyplot.show()
 print("Weiter zum Fragebogen")

elif model_name=="Extreme Gradient Boosting":
 import matplotlib.pylab as plt
 fig1=plt.gcf()
 plot_importance(model, max_num_features=25)
 plt.draw()

 #fig1.savefig('xgboost.png', figsize=(50, 40), dpi=1000)
 plt.show()
 print("Weiter zum Fragebogen")
elif model_name == "Decision Tree":
 from sklearn.tree import DecisionTreeClassifier, plot_tree


 plt.figure(figsize=(16, 6))
 plot_tree(model, filled=True, feature_names=X_test_encoded.columns,class_names=True )
 plt.show()
 print("Weiter zum Fragebogen")







 