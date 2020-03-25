from main import api, fields, Resource
from models.usermodel import Users_model, user_schema, users_schema

ns_users = api.namespace("users", description="all tasks regarding users")


# this helps the user know hoe to input the data
user_model = api.model(
    "User",
    {
        "fullname": fields.String(),
        "email": fields.String(),
        "password": fields.String(),
    },
)


@ns_users.route("")
class UsersList(Resource):
    @api.expect(user_model)
    def post(self):
        """use this endpoint to create a user"""
        data = api.payload
        user_to_create = Users_model(
            fullname=data["fullname"], email=data["email"], password=data["password"]
        )
        user_to_create.create()
        # the below function turns the user to create object into json and return it to the user
        return (
            user_schema.dump(user_to_create),
            201,
        )  # 	A new resource was successfully created.

    def get(self):
        """Use this endpoint to get all users"""

        return users_schema.dump(Users_model.query.all()), 200  # ok


@ns_users.route("/<int:id>")
class Users(Resource):
    def get(self, id):
        """Use this endpoin to get one user by id"""
        queried_user = Users_model.get_single_user_with_id(id=id)
        if queried_user:
            return user_schema.dump(queried_user), 200  # ok
        else:
            return (
                ({"message": "user not found!"}),
                404,
            )  # The requested resource was not found.

        # print(Users_model.query.all())
        # user = next((filter((lambda x: x["id"] == id), users_list)), None)
        # if user:
        #     return user, 200  # ok	The request was successfully completed.
        # else:
        #     return ({"message": "user not found"},404,)  # The requested resource was not found.

    @api.expect(user_model)
    def put(self, id):
        """edit a user by id"""
        data = api.payload
        user_to_update = Users_model.query.filter_by(id=id).first()
        if user_to_update:
            if u'fullname' in data:
                user_to_update.fullname = data["fullname"]
            if u'email' in data:
                user_to_update.email = data["email"]
            if u'password' in data:
                user_to_update.password = data["password"]
            user_to_update.create()
            return user_schema.dump(user_to_update),201 #created
        else:
            return ({"message":"User not found"}),404 #not found


    def delete(self, id):
        """delete a user by id"""
        user_to_delete = Users_model.query.filter_by(id=id).first()
        if user_to_delete:
            Users_model.delete_user(id=id)
            return ({"message": "User deleted!"}), 200  # ok
        else:
            return ({"message": "User not found"}), 404  # not found

        # to_delete = next(filter((lambda x: x["id"] == id), users_list), None)
        # if to_delete:
        #     users_list.remove(to_delete)
        #     return {"message": "User deleted"}, 200  # ok
        # else:
        #     return {"message": "user not found"}, 404  # not found
