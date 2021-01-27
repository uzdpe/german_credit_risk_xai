"""File for storing paths and other information"""


import os
from platform import system as getSystem
import shap

PATH_SEP = '\\' if getSystem() == 'Windows' else '/'

PATHS = {
    # ----------------------------------------------------------------------------------------
    # Should contain all paths!!!
    # ----------------------------------------------------------------------------------------
    # data
    "01_data_raw": os.path.join("backend", "data", "01_data_raw") + PATH_SEP,
    "02_data_preprocessed": os.path.join("backend", "data", "02_data_preprocessed") + PATH_SEP,
    "03_data_outputs": os.path.join("backend", "data", "03_data_outputs" + PATH_SEP),
    "04_trained_models": os.path.join("backend", "data", "04_trained_models" + PATH_SEP),

}


dataset = {
    "german_credit_dataset": {
        "dataset_name": "credit_risk.csv",
        "categorical_features_indices": [0, 2, 3, 5, 6, 8, 9, 10, 12, 14, 15, 17, 19, 20],
        "numerical_features_indices": [1, 4, 7, 11, 13, 16, 18],
        "num_features": ["Duration", "Credit amount", "Instalment percent of disposible income",
                         "Present residence since", "Age", "Number of existing credits at this bank",
                         "Number of people being liable to provide maintenance for"],
        "cat_features": ["Checking account", "Credit history", "Purpose", "Saving accounts",
                         "Length of current employment", "Sex", "Marital status",
                         "Other debtors / guarantors",
                         "Property", "Other installment plans", "Housing", "Job", "Telephone",
                         "Foreign Worker"],
        "label_indices": [21],
    }
}


params = {
    "dataset": "german_credit_dataset",
}


