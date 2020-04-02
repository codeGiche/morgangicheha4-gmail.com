from main import app
import json
from tests.skeleton_test import Skeleton_test

class Login_test(Skeleton_test):
    """This class test login"""
    def test_login(self):
        # first we register
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

        self.assertEqual(response.status_code,200)
        self.assertNotEqual(response.status_code,201)

