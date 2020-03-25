from flask import Flask
from flask_restx import Api, Resource, fields
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

app = Flask(__name__)
# cofiguring db
app.config["SQLALCHEMY_DATABASE_URI"]="postgresql://postgres:morgan8514@127.0.0.1:5432/restx"
app.config["SECRET_KEY"]="secret"
api = Api(
    app,
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
