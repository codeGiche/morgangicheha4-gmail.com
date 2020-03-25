from main import db,ma,fields

class Users_model(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    fullname = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(80),nullable=False, unique=True)
    password = db.Column(db.String(), nullable=False)

    tasks = db.relationship('Task_model', backref='user', lazy=True)
    # category = db.relationship('Category',backref=db.backref('user', lazy=True))


    def create(self):
        """this method adds to the users table"""
        db.session.add(self)
        db.session.commit()
    
    @classmethod
    def get_single_user_with_id(cls,id):
        user= cls.query.filter_by(id=id).first()
        if user:
            return user
        else: 
            return False

# serializing and deserializing data
class UserSchema(ma.Schema):
    class Meta:
        fields = ("id","fullname", "email")

user_schema = UserSchema() #for one object
users_schema = UserSchema(many=True)