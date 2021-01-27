
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





if __name__ == '__main__':
 initialize()
 df=load_data(type="raw")
 #explore_data(df)
 #data_exploration(df)


 X_train_encoded, y_train, X_test_encoded, y_test, encoder = data_loading.load_encoded_data()
 # Choose a model and train it
 model, model_name = model_training.model_selection(input("Select Model: "))
 print("Trained model: " , model_name)
 X_test =data_loading.train_test_split(df)
 model = model_training.train_model(X_train_encoded, y_train, model)
 model_training.save_trained_model(model, model_name)
 #print("Training score data: ")
 #print(model.score(X_train_encoded, y_train))
 #good: 20, bad:35

 i = int(input("Enter instance:"))
 print("Instance chosen: ", i)
 print(X_test_encoded.iloc[i])
 print(y_test.iloc[i])
 print(X_test)
 print(df.iloc[i])
 predict(model, X_test_encoded, y_test)
 j = int(input("Enter prediction [0 or 1]:"))
 y_hat = model.predict(X_test_encoded)

 print("Predicted class by the model: ", y_hat[i])
 #print("True Prediction:", y_test.iloc[i])

if i==y_hat[i]:
    print("correct")
else:
    o=input("Need Explanation?")

if o=="yes" and model_name=="Logistic Regression":
 print("slopes:", model.coef_)
 print("intercept:", model.intercept_)
 from matplotlib import pyplot

#  # get importance
 importance = model.coef_[0]
 # summarize feature importance
 for s, v in enumerate(importance):
  if abs(v)>=0.5:
    print('Feature: %0d, Score: %.5f' % (s, v))
 # plot feature importance
 pyplot.bar([x for x in range(len(importance))], importance)
 pyplot.show()

elif model_name=="Extreme Gradient Boosting":
 import matplotlib.pylab as plt
 fig1=plt.gcf()
 plot_importance(model, max_num_features=25)
 plt.draw()
 #fig1.savefig('xgboost.png', figsize=(50, 40), dpi=1000)
 plt.show()
 print("Fertig")




 