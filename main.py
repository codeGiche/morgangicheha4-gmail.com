from flask import Flask, Blueprint
from flask_restx import Api, Resource, fields
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_jwt_extended import JWTManager,jwt_required,create_access_token,get_jwt_identity

import os
import sentry_sdk
from sentry_sdk.integrations.flask import FlaskIntegration
from werkzeug.exceptions import Unauthorized

sentry_sdk.init(
    dsn="https://ade2752e447d4f70b428fd02d0cfc85e@sentry.io/5181613",
    integrations=[FlaskIntegration()],
)
app = Flask(__name__)

blueprint = Blueprint("api",__name__,url_prefix="/api")

authorizations = {
    "apikey": {
        "type": "apiKey",
        "in": "header",
        "name": "Authorization",
        "description": "Type in the *value into the box below**Bearer & where jwt is token",
    }
}

###########################DEVELOPMENT CONFIG########################################

# app.config["RESTX_VALIDATE"] = True
app.config["PROPAGATE_EXCEPTIONS"] = False

# cofiguring db

# app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("DB_RESTX")
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://postgres:morgan8514@127.0.0.1:5432/restx"
app.config["SECRET_KEY"] = os.urandom(20)
app.config["JWT_SECRET_KEY"] = os.urandom(20)
# disable Try it Out for all methods
# app.config.SWAGGER_SUPPORTED_SUBMIT_METHODS = ["get", "post","put"]

###########################TESTING CONFIG########################################

# app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///db_test.db"






api = Api(
    blueprint,doc="/doc",
    
    # to turn documentation off set doc=Flase
    authorizations=authorizations,
    title="Task management api",
    description="task manager api",
    version="1.0",
    author="Giche",
)
app.register_blueprint(blueprint)
# error handling
@app.errorhandler(400)
def bad_request(error):
    return {"message": "Bad request"}, 400


@app.errorhandler(401)
def Unauthorized(error):
    return {"message": "Unauthorized"}, 401


@app.errorhandler(403)
def forbidden(error):
    return {"message": "Forbidden"}, 403

@app.errorhandler(404)
def not_foud(error):
    return {"message": "Request not found"}, 404


@app.errorhandler(405)
def bad_request(error):
    return {"message": "Request method is not allowed"}, 405


jwt = JWTManager(app)
db = SQLAlchemy(app)
ma = Marshmallow(app)

# importing db models
from models.usermodel import Users_model
from models.taskmodel import Task_model


@app.before_first_request
def create():
    db.create_all()


from resources.tasks import *
from resources.user import *
from resources.authentication import *

# @app.route('/debug-sentry')
# def trigger_error():
#     division_by_zero = 1 / 0

if __name__ == "__main__":
    app.run()
