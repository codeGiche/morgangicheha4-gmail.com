from tests.skeleton_test import Skeleton_test
from main import app
import json
import ast


class Post_task_test(Skeleton_test):
    """This test tests posting tasks"""
    def test_post_task(self):

        fullname = "morgan"
        email = "morgan@gmail"
        password= "morgan"
        wrong_password="notpassword"

        register_payload=json.dumps({"fullname":fullname,"email":email,"password":password})
        login_payload = json.dumps({"email":email,"password":password})
         # response = self.app.post(url_to_register, headers={"Content-Type": "application/json"},data=payload)
        self.app.post("http://127.0.0.1:5000/api/Register",headers={"Content-Type": "application/json"}, data= register_payload)

        # posting to login endpoint
        response=self.app.post("http://127.0.0.1:5000/api/Login",headers={"Content-Type": "application/json"},data=login_payload)
        # print(response.__dict__)
        li=[]
        k=ast.literal_eval((response._get_data_for_json(li)).decode("utf-8"))
        print(k["access_token"])