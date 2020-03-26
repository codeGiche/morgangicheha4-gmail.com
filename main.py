from flask import Flask
from flask_restx import Api, Resource, fields
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_jwt_extended import JWTManager,jwt_required,create_access_token,get_jwt_identity
import os


app = Flask(__name__)



# cofiguring db
app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("DB_RESTX")
app.config["SECRET_KEY"] = "ss"
app.config["JWT_SECRET_KEY"] = "ss"
api = Api(
    app,
    
    title="Task management api",
    description="task manager api",
    version="1.0",
    author="Giche",
)

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
