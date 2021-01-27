

from backend.model_building.model_training import *
from backend.data_preprocessing.data_loading import load_encoded_data

from sklearn.metrics import accuracy_score,classification_report, confusion_matrix


def predict(model, X_test, y_test):
 X_train_encoded, y_train, X_test_encoded, y_test, encoder = load_encoded_data()
 y_hat = model.predict(X_test_encoded)

 print("Accuracy Score: ", "\n")
 print(accuracy_score(y_test, y_hat))
#  print("Confusion Matrix:", "\n")
#  print(confusion_matrix(y_test, y_hat))
#  print("Classification Report: ", "\n")
#  print(classification_report(y_test, y_hat))
