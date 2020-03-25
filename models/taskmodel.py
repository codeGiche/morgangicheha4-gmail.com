from main import db,ma
import datetime

class Task_model(db.Model):
    __tablename__="tasks_table"
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(), nullable=False)
    description = db.Column(db.String(), nullable=False)
    completed = db.Column(db.Boolean, nullable=False, default=False)
    created_at = db.Column(db.DateTime(timezone=True), default=datetime.datetime.utcnow)

    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    # commiting to db
    def commit_to_db(self):
        db.session.add(self)
        db.session.commit()

    class TaskSchema(ma.Schema):
        class Meta:
            fields = ("id","title","description")


    task_schema = TaskSchema()
    tasks_schema = TaskSchema(many=True)