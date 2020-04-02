from main import app
from tests.skeleton_test import Skeleton_test
import json
class Bad_login_test(Skeleton_test):
    """Tests unsuccessfull login"""
    def test_unsucceful_login(self):
        fullname = "morgan"
        email = "morgan@gmail"
        password= "morgan"
        wrong_password="notpassword"

        register_payload=json.dumps({"fullname":fullname,"email":email,"password":password})
        login_payload = json.dumps({"email":email,"password":wrong_password})
            # response = self.app.post(url_to_register, headers={"Content-Type": "application/json"},data=payload)
        self.app.post("/api/Register",headers={"Content-Type": "application/json"}, data= register_payload)

        # posting to login endpoint
        response=self.app.post("/api/Login",headers={"Content-Type": "application/json"},data=login_payload)

        self.assertEqual(response.status_code,401)
        self.assertNotEqual(response.status_code,200)