

from backend.model_building.model_training import *
from backend.data_preprocessing import data_loading

from backend.data_preprocessing.data_loading import load_encoded_data

from sklearn.metrics import accuracy_score,classification_report, confusion_matrix
import matplotlib as plt
import dataframe_image as dfi
import pandas as pd



def predict(model, X_test, y_test):
 X_train_encoded, y_train, X_test_encoded, y_test, encoder = load_encoded_data()
 y_hat = model.predict(X_test_encoded)

 #print("Accuracy Score: ", "\n")
 print("Accuracy Score: ", accuracy_score(y_test, y_hat))
#  print("Confusion Matrix:", "\n")
#  print(confusion_matrix(y_test, y_hat))
#  print("Classification Report: ", "\n")
#  print(classification_report(y_test, y_hat))
def dataTable(X_test, test_instance=10):
    """Save data table for chosen instance"""
    X_test, y_test =data_loading.load_data(type="testing")
    x_num=X_test.iloc[test_instance, :]
    data_table = pd.DataFrame(X_test.iloc[test_instance, :])
    dfi.export(data_table,PATHS["03_data_outputs"] + "_data_table.png")
    
