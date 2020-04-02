import unittest
import json

from main import app,db

class Skeleton_test(unittest.TestCase):
    """This is a skeleton for all all tests"""
    def setUp(self):
        self.app = app.test_client()

    def tearDown(self):
        """teardown method deletes all record after test is run"""
        db.session.remove()
        db.drop_all()
