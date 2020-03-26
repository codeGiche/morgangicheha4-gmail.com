from flask import Flask
from flask_restx import Api, Resource, fields
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
import os


app = Flask(__name__)

authorizations = {"apikey": {"type": "apikey", "in": "header","name": "X-API-Key"}}

# cofiguring db
app.config[
    "SQLALCHEMY_DATABASE_URI"
] = os.environ.get("DB_RESTX")
app.config["SECRET_KEY"] = os.urandom(24)
api = Api(
    app,
     authorizations=authorizations,
    title="Task management api",
    description="task manager api",
    version="1.0",
    author="Giche",
   
)
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

if __name__ == "__main__":
    app.run(debug=True)
