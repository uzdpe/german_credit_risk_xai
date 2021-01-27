"""Sources:
dataset: https://archive.ics.uci.edu/ml/datasets/Statlog+%28German+Credit+Data%29
"""

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn import preprocessing
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer

from sklearn.preprocessing import StandardScaler, OneHotEncoder
from backend.util.static import PATHS, dataset, params
from backend.util.helper_functions import get_ct_feature_names
from backend.util.util import clean_folder


german_credit_dataset = dataset[params["dataset"]]


def initialize():
    """This is for the first initialization (splitting dataset and setting paths / folders) """

    # clean preprocessed and output folder
    clean_folder(folder=PATHS["02_data_preprocessed"])
    clean_folder(folder=PATHS["03_data_outputs"])
    clean_folder(folder=PATHS["04_trained_models"])

    # load the data
    df_credit = load_data()

    # Small preparation
    df_credit = data_preparation(df_credit)

    # Encode into lime format
    df_credit, categorical_encoding, categorical_encoding_label = encoding(df_credit)

    # Split the data into training and testing
    create_training_split(df_credit)


def load_data(type="raw"):
    """Loads the data, type can be raw, training, testing."""

    if type == "raw":
        df_credit = pd.read_excel(PATHS["01_data_raw"] + "credit_risk.xls", index_col=0)
        return df_credit
    elif type == "training":
        X_train = pd.read_csv(PATHS["02_data_preprocessed"] + "X_train.csv", index_col=0)
        y_train = pd.read_csv(PATHS["02_data_preprocessed"] + "y_train.csv", index_col=0)
        return X_train, y_train
    elif type == "testing":
        X_test = pd.read_csv(PATHS["02_data_preprocessed"] + "X_test.csv", index_col=0)
        y_test = pd.read_csv(PATHS["02_data_preprocessed"] + "y_test.csv", index_col=0)
        return X_test, y_test
    else:
        raise AssertionError("Error in if-else statement")

def explore_data(df_credit):
    """Explore the data."""
    print("Shape of the data")
    print(df_credit.info())

    print("Looking unique values")
    print(df_credit.nunique())

    print("Header")
    print(df_credit.head())

    # Prints unique data values
    print("Checking account : ", df_credit['Checking account'].unique())
    print("Credit history : ", df_credit['Credit history'].unique())
    print("Saving accounts : ", df_credit['Saving accounts'].unique())
    print("Length of current employment : ", df_credit['Length of current employment'].unique())

    print("Purpose : ", df_credit.Purpose.unique())
    #print("Sex : ", df_credit['Sex'].unique())
    print("Marital status : ", df_credit['Marital status'].unique())
    print("Other debtors / guarantors : ", df_credit['Other debtors / guarantors'].unique())
    print("Property ", df_credit['Property'].unique())
    #print("Other installment plans  : ", df_credit['Other installment plans'].unique())
    print("Housing : ", df_credit.Housing.unique())
    print("Job : ", df_credit.Job.unique())
    print("Telephone : ", df_credit.Telephone.unique())
    print("Foreign Worker : ", df_credit['Foreign Worker'].unique())
    #print("Risk : ", df_credit['Risk'].unique())




def create_training_split(df_credit):
    """Creates the train, val, and test split."""

    y = df_credit["Risk"] # .map({"bad": 0, "good": 1})
    X = df_credit.drop("Risk", axis=1)

    # Splitting X and y into train and test version
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.1, random_state=42)  # test size of 100

    # Save train and test set
    pd.DataFrame(X_train).to_csv(PATHS["02_data_preprocessed"] + "X_train.csv")
    pd.DataFrame(X_test).to_csv(PATHS["02_data_preprocessed"] + "X_test.csv")
    pd.DataFrame(y_train).to_csv(PATHS["02_data_preprocessed"] + "y_train.csv")
    pd.DataFrame(y_test).to_csv(PATHS["02_data_preprocessed"] + "y_test.csv")

    return X_train, X_test, y_train, y_test


def data_preparation(df_credit):
    """Small dataset fixes"""

    #df_credit.loc[(df_credit.Job == 0), 'Job'] = "unskilled and non-resident"
   # df_credit.loc[(df_credit.Job == 1), 'Job'] = "unskilled and resident"
   # df_credit.loc[(df_credit.Job == 2), 'Job'] = "skilled"
   # df_credit.loc[(df_credit.Job == 3), 'Job'] = "highly skilled"

    df_credit["Saving accounts"] = df_credit["Saving accounts"].astype(str)
    df_credit["Checking account"] = df_credit["Checking account"].astype(str)

    # interval = (18, 25, 35, 60, 120)
    # categories = ['Student', 'Young', 'Adult', 'Senior']
    # df_credit["Age_cat"] = pd.cut(df_credit.Age, interval, labels=categories)

    # df_credit['Credit amount'] = np.log(df_credit['Credit amount'])

    return df_credit


def analyze_dataset():
    """Analyze the datasest and give back which columns contains which type of features"""
    df_credit = load_data()
    categorical_features_names = [col for col in df_credit.columns if df_credit[col].dtype == 'object']
    categorical_features_indices = german_credit_dataset["categorical_features_indices"]
    feature_names = df_credit.columns.tolist()
    return categorical_features_names, categorical_features_indices, feature_names


def encoding(df_credit):
    """Preprocessing: Encodes the categorical labels into the LIME format. This format should not be used for
    training since it is not one-hot-encoded (high multicollinearity)"""

    categorical_encoding = {}
    for col in german_credit_dataset["categorical_features_indices"]:
        label_encoder = preprocessing.LabelEncoder()
        df_credit.iloc[:, col] = label_encoder.fit_transform(df_credit.iloc[:, col])
        categorical_encoding[col] = label_encoder.classes_

    categorical_encoding_label = {}
    for col in german_credit_dataset["label_indices"]:
        label_encoder = preprocessing.LabelEncoder()
        df_credit.iloc[:, col] = label_encoder.fit_transform(df_credit.iloc[:, col])
        categorical_encoding_label = label_encoder.classes_

    return df_credit, categorical_encoding, categorical_encoding_label


def load_encoded_data():
    """Load lime-encoded training and testing data and return one-hot-encoded data."""
    X_train, y_train = load_data(type="training")
    X_test, y_test = load_data(type="testing")

    # one-hot-encode the data
    X_train_encoded, encoder, columns, encoder = build_and_fit_one_hot_encoder(X_train)
    X_test_encoded = pd.DataFrame(encoder.transform(X_test), columns=columns)
    return X_train_encoded, y_train, X_test_encoded, y_test, encoder


def build_and_fit_one_hot_encoder(X_train):
    """Returns a one hot encoder and an encoded dataset."""

    numeric_features = german_credit_dataset["num_features"]
    numeric_transformer = Pipeline(steps=[
        ('imputer', SimpleImputer(strategy='median')),
        ('scaler', StandardScaler())])

    categorical_features = german_credit_dataset["cat_features"]
    categorical_transformer = Pipeline(steps=[
        ('imputer', SimpleImputer(strategy='constant')),
        ('onehot', OneHotEncoder(handle_unknown='error', drop="first"))])

    encoder = ColumnTransformer(
        transformers=[
            ('num', numeric_transformer, numeric_features),
            ('cat', categorical_transformer, categorical_features)],
        remainder="passthrough")

    encoder.fit(X_train)
    X_train_encoded = encoder.transform(X_train)

    columns = get_ct_feature_names(encoder)
    X_train_encoded = pd.DataFrame(X_train_encoded, columns=columns)

    return X_train_encoded, encoder, columns, encoder


def one_hot_encoder_old(df_credit, nan_as_category=False):
    """OLD """
    original_columns = list(df_credit.columns)
    categorical_columns = [col for col in df_credit.columns if df_credit[col].dtype == 'object']
    df_credit = pd.get_dummies(df_credit, columns=categorical_columns, dummy_na=nan_as_category, drop_first=True)
    new_columns = [c for c in df_credit.columns if c not in original_columns]
    return df_credit, new_columns


def data_exploration(df_credit):
    """Data exploration with seaborn"""

    # ax = sns.countplot(x="Risk", data=df_credit)
   #  plt.show()

    #ax = sns.countplot(data=df_credit, x="Sex", hue="Risk")
    # plt.show()

    # ax = sns.histplot(data=df_credit, x="Credit amount", hue="Risk", element="step")
    # plt.show()

    # ax = sns.histplot(data=df_credit, x="Age", hue="Risk", element="step")
   #  plt.show()

     #ax = sns.histplot(data=df_credit, x="Duration", hue="Risk", element="step")
    # plt.show()

    #ax = sns.countplot(data=df_credit, x="Purpose", hue="Risk")
    #plt.show()

   #  ax = sns.countplot(data=df_credit, x="Saving accounts", hue="Risk")
   #  plt.show()

    #ax = sns.pairplot(data=df_credit, hue="Risk", kind="kde")
    #ax.savefig("pairplot_all.png")
    #plt.show()  # Takes a while to plot

    # plt.figure(figsize=(14, 12))
    # sns.heatmap(df_credit.astype(float).corr(),linewidths=0.1,vmax=1.0,
   #         square=True,  linecolor='white', annot=True)
   #  plt.show()

