from flask import Flask
from flask_cors import CORS
from flask_restful import Api
from backend.endpoints.endpoints import initialize_routes


# APP_ROOT = os.path.dirname(os.path.abspath(__file__))
# print("APP ROOT:",  APP_ROOT)

app = Flask(__name__)


# cors = CORS(app, resorces={r'/*': {"origins": '*'}})  # can be specified with more detail
# cors = CORS(app, resources={r"/api/*": {"origins": "*"}})
cors = CORS(app)

api = Api(app)

initialize_routes(api)

if __name__ == "__main__":
	app.run(debug=True)