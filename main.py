from flask import Flask,Blueprint
from flask_restx import Api, Resource, fields
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_jwt_extended import (
    JWTManager,
    jwt_required,
    create_access_token,
    get_jwt_identity,
)
import os
from werkzeug.exceptions import Unauthorized


app = Flask(__name__)



authorizations = {
    "apikey": {
        "type": "apiKey",
        "in": "header",
        "name": "Authorization",
        "description": "Type in the *value into the box below**Bearer & where jwt is token",
    }
}



app.config['RESTX_VALIDATE'] = True
app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("DB_RESTX")
# cofiguring db
app.config["SECRET_KEY"] = os.urandom(20)
app.config["JWT_SECRET_KEY"] = os.urandom(20)
# disable Try it Out for all methods
# app.config.SWAGGER_SUPPORTED_SUBMIT_METHODS = ["get", "post","put"]
api = Api(
    app,
    #to turn documentation off set doc=Flase
    authorizations=authorizations,
    title="Task management api",
    description="task manager api",
    version="1.0",
    author="Giche",
)

# error handling
@api.errorhandler(Unauthorized)
def unauthorized(error):
    return {"message": "Login is required!!"}


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

if __name__ == "__main__":
    app.run(debug=True)
