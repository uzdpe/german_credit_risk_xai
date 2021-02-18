

from lime.lime_tabular import LimeTabularExplainer
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import shap

from backend.util.static import PATHS, dataset, params
from backend.data_preprocessing import data_loading
from backend.model_building import model_training


def main_init_xai(model_name, chosen_instance=4):
    """Prepare plots and data for the xai-dashboard"""
    X_train_encoded, y_train, X_test_encoded, y_test, encoder = data_loading.load_encoded_data()
    X_test, y_test = data_loading.load_data(type="testing")
    model = model_training.load_trained_model(model_name)

    # categorical_features_indices = dataset["german_credit_dataset"]["categorical_features_indices"]
    categorical_features_names, categorical_features_indices, feature_names = data_loading.analyze_dataset()
    df_credit = data_loading.load_data(type="raw")
    df_credit = data_loading.data_preparation(df_credit)
    df_credit, categorical_encoding, categorical_encoding_label = data_loading.encoding(df_credit)

    #explain_with_lime(X_test, model, model_name, encoder, categorical_features_indices,
    #                                      categorical_encoding, categorical_encoding_label,
    #                                       feature_names, test_instance=chosen_instance)

    explain_with_shap_global(X_train_encoded, model, model_name)


def main_global(model_name):
    """Main function for the global explanations."""
    X_train_encoded, y_train, X_test_encoded, y_test, encoder = data_loading.load_encoded_data()

    print(X_train_encoded)
    print(type(X_train_encoded))

    X_test, y_test = data_loading.load_data(type="testing")
    model = model_training.load_trained_model(model_name)

    # categorical_features_indices = dataset["german_credit_dataset"]["categorical_features_indices"]
    categorical_features_names, categorical_features_indices, feature_names = data_loading.analyze_dataset()
    df_credit = data_loading.load_data(type="raw")
    df_credit = data_loading.data_preparation(df_credit)
    df_credit, categorical_encoding, categorical_encoding_label = data_loading.encoding(df_credit)

    explain_with_shap_global(X_test_encoded, model, model_name)


def main_local(model_name, chosen_instance=1):
    """Main function for local explanations"""
    X_train_encoded, y_train, X_test_encoded, y_test, encoder = data_loading.load_encoded_data()
    X_test, y_test = data_loading.load_data(type="testing")
    model = model_training.load_trained_model(model_name)



    categorical_features_names, categorical_features_indices, feature_names = data_loading.analyze_dataset()
    df_credit = data_loading.load_data(type="raw")
    df_credit = data_loading.data_preparation(df_credit)
    df_credit, categorical_encoding, categorical_encoding_label = data_loading.encoding(df_credit)

    explain_with_lime(X_test, model, model_name, encoder, categorical_features_indices, categorical_encoding,
                      categorical_encoding_label, feature_names, test_instance=chosen_instance)

    explain_with_shap_local(X_test_encoded, model, model_name, feature_names=X_test_encoded.columns.tolist()
                            , test_instance=chosen_instance)


def get_shap_explainer(model, model_name):
    """Returns the correct shap explainer.
        shap.TreeExplainer()
        shap.DeepExplainer for Neural Networks
        shap.KernelExplainer for all models (slower)
    """
    if model_name == "Extreme Gradient Boosting":
        explainer = shap.TreeExplainer(model)
    elif model_name == "Logistic Regression":
        explainer = shap.KernelExplainer(model)
    elif model_name == "Decision Tree":
        explainer = shap.TreeExplainer(model)
    elif model_name == "Random Forest":
        explainer = shap.TreeExplainer(model)
    elif model_name == "Support Vector Machine":
        explainer = shap.KernelExplainer(model)
    else:
        raise AssertionError("Error in if-else statement")
    return explainer


def explain_with_shap_local(X_test, model, model_name, feature_names, test_instance):
    """Local explanations using shap"""
    explainer = get_shap_explainer(model, model_name)
    shap_values = explainer.shap_values(X_test)

    force_plot = True
    if force_plot:
        shap.force_plot(explainer.expected_value,
                        shap_values[test_instance, :],
                        X_test.iloc[test_instance, :],
                        # feature_names=feature_names,
                        show=False,
                        matplotlib=True,
                        text_rotation=90,
                        # figsize=(25, 10)
                        )

        plt.savefig(PATHS["03_data_outputs"] + model_name + "_shap_force_plot.png")
        plt.close()
def explain_with_shap_local_dp(X_test, model, model_name, feature_names, test_instance):
    """Local explanations using shap"""
    explainer = get_shap_explainer(model, model_name)
    shap_values = explainer.shap_values(X_test)

    dependence_plot = True
    if dependence_plot:
        shap.dependence_plot("Checking_account",
                        shap_values,
                        X_test,
                        # feature_names=feature_names,
                        show=False,
                        matplotlib=True,
                        text_rotation=90,
                        # figsize=(25, 10)
                        )

        plt.savefig(PATHS["03_data_outputs"] + model_name + "_shap_dependence_plot.png")
        plt.close()

def explain_with_shap_global(X_train, model, model_name):
    """Global explanations using shap"""

    explainer = get_shap_explainer(model, model_name)
    shap_values = explainer.shap_values(X_train)

    summary_plot = True
    if summary_plot:
        shap.summary_plot(shap_values,
                          X_train,
                          # plot_type="bar",
                          show=False,
                          max_display=10,
                          )
        plt.tight_layout()
        plt.savefig(PATHS["03_data_outputs"] + model_name + "_shap_summary_plot.png")
        plt.close()


def explain_with_lime(X_test, model, model_name, encoder, categorical_features_indices, categorical_encoding,
                      class_names, feature_names, test_instance=10):
    """Explain a prediction from the test set with a trained model."""
    columns = X_test.columns.tolist()

    predict_fn = lambda x: model.predict_proba(encoder.transform(pd.DataFrame(x, columns=columns)).astype(float))

    explainer = LimeTabularExplainer(X_test.to_numpy(),
                                     mode="classification",
                                     feature_names=feature_names,
                                     class_names=class_names,
                                     categorical_features=categorical_features_indices,
                                     categorical_names=categorical_encoding,
                                     kernel_width=3)

    # might set seed?
    explanation = explainer.explain_instance(X_test.iloc[test_instance, :], predict_fn, num_features=5)

    # Show and save explanation
    # explanation.save_to_file(PATHS["03_data_outputs"] + "lime.html")

    explanation.as_pyplot_figure()
    plt.tight_layout()
    plt.savefig(PATHS["03_data_outputs"] + model_name + "_lime_plot.png")
    plt.close()

    # access the coefficients, the intercept and the R squared of the linear model
    print("Coefficients of linear model: ", explanation.local_exp)
    print("\n")
    print("Intercept: ", explanation.intercept)
    print("\n")
    print("R-squared: ", explanation.score)

