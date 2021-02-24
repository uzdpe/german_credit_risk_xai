from flask_restful import Resource, reqparse
from flask import send_from_directory, abort
from sklearn.metrics import accuracy_score,auc,roc_auc_score

from backend.data_preprocessing import data_loading
from backend.model_building import model_training
from backend.xai_cockpit import model_explaining
from backend.util.static import PATHS, dataset, params
from backend.util.util import get_the_filenames
from backend.inference.predict import *


def initialize_routes(api):
    # New Experiment
    api.add_resource(Initialization, "/initialize_backend")
    api.add_resource(ExploreTrainingData, "/explore_training_data")
    api.add_resource(TrainNewModel, "/train_new_model")
    api.add_resource(MakePredictions, "/make_prediction")
    api.add_resource(ModelExplaining, "/model_explaining")
    api.add_resource(DisplayShapPlots, "/shapplot")
    api.add_resource(DisplayForcePlot, "/forceplot")
    api.add_resource(DisplayLimePlot, "/limeplot")
    api.add_resource(GetInstances, "/get_instances")
    api.add_resource(ReturnTrainedModels, "/return_trained_models")
    api.add_resource(LocalExplanation, "/local_explanation")
    api.add_resource(LoadDataTable, "/data_table")


class Initialization(Resource):
    """Initialize analysis by splitting data into training and testing"""
    def post(self):
        data_loading.initialize()
        return "successful initialization"


class GetInstances(Resource):
    """Returns the possible instances for the test data."""
    def get(self):
        X_train_encoded, y_train, X_test_encoded, y_test, encoder = data_loading.load_encoded_data()
        print("possible instances: ", X_test_encoded.shape[0])
        possible_instance = []
        for i in range(0, X_test_encoded.shape[0]):
            possible_instance.append(i)
        return possible_instance


class TrainNewModel(Resource):
    """Load training data. Train a new model. Save model."""
    def post(self):
        reqparse_args = reqparse.RequestParser()
        reqparse_args.add_argument("chosen_model", type=str)
        args = reqparse_args.parse_args()

        X_train_encoded, y_train, X_test_encoded, y_test, encoder = data_loading.load_encoded_data()
        # Choose a model and train it
        model, model_name = model_training.model_selection(args["chosen_model"])
        model = model_training.train_model(X_train_encoded, y_train, model)
        model_training.save_trained_model(model, model_name)
        
        return "model successfully trained"


class ReturnTrainedModels(Resource):
    """Returns the trained models in the output folder."""
    def get(self):
        model_names = get_the_filenames(PATHS["04_trained_models"], cut_of_data_format=True)
        return model_names


class MakePredictions(Resource):
    """Load the testing data and make predictions"""
    def get(self):
        reqparse_args = reqparse.RequestParser()
        reqparse_args.add_argument("chosen_model", type=str)
        args = reqparse_args.parse_args()

        model = model_training.load_trained_model(args["chosen_model"])

        X_train_encoded, y_train, X_test_encoded, y_test, encoder = data_loading.load_encoded_data()
        y_hat = model.predict(X_test_encoded)
        y_score=model.predict.proba(X_test_encoded[:,1])
        print("ChosenModel: Accuracy score", accuracy_score(y_test, y_hat))
        print("ChosenModel: AUC", roc_auc_score(y_test, y_score)) # need proba?
        return "run successfully"


class ExploreTrainingData(Resource):
    """Explore the training data"""
    def get(self):
        X_train, y_train = data_loading.load_data(type="training")
        data_loading.explore_data(X_train)
        return "done"


class ModelExplaining(Resource):
    """Initialize the explanation dashboard."""
    def post(self):
        model_names = get_the_filenames(PATHS["04_trained_models"], cut_of_data_format=True)
        for chosen_model in model_names:
            model_explaining.main_init_xai(chosen_model)
        return "success"


class LocalExplanation(Resource):
    """Local Explanation"""
    def post(self):
        reqparse_args = reqparse.RequestParser()
        reqparse_args.add_argument("chosen_model", type=str)
        reqparse_args.add_argument("chosen_instance", type=int)
        args = reqparse_args.parse_args()

        print(args["chosen_model"], args["chosen_instance"])

        model_explaining.main_local(model_name=args["chosen_model"], chosen_instance=args["chosen_instance"])

        return "local explanation calculated successfully"


class DisplayShapPlots(Resource):
    """provides the shap summary plots"""
    def post(self):
        reqparse_args = reqparse.RequestParser()
        reqparse_args.add_argument("chosen_model", type=str)
        args = reqparse_args.parse_args()

        directory = PATHS["03_data_outputs"]
        filename = args["chosen_model"] + "_" + "shap_summary_plot.png"

        try:
            return send_from_directory(directory, filename=filename, as_attachment=True)
            # return send_file(prediction_dir + args["pred_name"])   # works both
        except FileNotFoundError:
            abort(404)


class DisplayForcePlot(Resource):
    """provides the shap force plot """
    def post(self):
        reqparse_args = reqparse.RequestParser()
        reqparse_args.add_argument("chosen_model", type=str)
        reqparse_args.add_argument("chosen_instance", type=str)  # not yet needed
        directory = PATHS["03_data_outputs"]
        filename = args["chosen_model"] + "_" + "shap_force_plot.png"

        try:
            return send_from_directory(directory, filename=filename, as_attachment=True)
            # return send_file(prediction_dir + args["pred_name"])   # works both
        except FileNotFoundError:
            abort(404)


class DisplayLimePlot(Resource):
    """provides the shap force plot """
    def post(self):
        reqparse_args = reqparse.RequestParser()
        reqparse_args.add_argument("chosen_model", type=str)
        reqparse_args.add_argument("chosen_instance", type=str)  # not yet needed
        args = reqparse_args.parse_args()

        directory = PATHS["03_data_outputs"]
        filename = args["chosen_model"] + "_" + "lime_plot.png"

        print(directory + filename)

        try:
            return send_from_directory(directory, filename=filename, as_attachment=True)
            # return send_file(prediction_dir + args["pred_name"])   # works both
        except FileNotFoundError:
            abort(404)
class LoadDataTable(Resource):
    """provides data table for prediction"""
    def post(self):
        dataTable(X_test, test_instance=10)

        directory = PATHS["03_data_outputs"]
        filename = "data_table.png"
        #reqparse_args.add_argument("chosen_instance", type=str)
        print(filename)

        try:
            return send_from_directory(directory, filename=filename, as_attachment=True)
            # return send_file(prediction_dir + args["pred_name"])   # works both
        except FileNotFoundError:
            abort(404)

