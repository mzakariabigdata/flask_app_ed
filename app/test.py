import os
import unittest
# from config import basedir
from app import create_app
from dba.models import db
import click

from dba.models import Book

class TestExample(unittest.TestCase):

    @classmethod
    def setUp(cls):
        # Happens before each test
        app = create_app(config_env="testing")
        cls.app_ctx = app.app_context()
        cls.app_ctx.push()
        cls.app_test_client = app.test_client()
        db.create_all()

    @classmethod
    def tearDown(cls):
        # Happens after each test
        db.session.remove()
        db.drop_all()
        cls.app_ctx.pop()

    def test_home_route(self):
        resp = self.app_test_client.get("/")
        self.assertEqual(resp.status_code, 200)

    def test_zak_route(self):
        resp = self.app_test_client.get("/zak")
        self.assertEqual(resp.status_code, 200)

    def test_mor_route(self):
        resp = self.app_test_client.get("/morr")
        self.assertEqual(resp.status_code, 200)

    @unittest.skip("demonstrating skipping")
    def test_nothing(self):
        self.fail("shouldn't happen")

    @unittest.skipIf(click.__version__ < '9',
                     "not supported in this library version")
    def test_format(self):
        # Tests that work for only a certain version of the library.
        pass

    # def test_user_creation(self):
    #     u = User(username="test", email="test@mail.com")
    #     u.set_password("password123")
    #     db.session.add(u)
    #     db.session.commit()
    #     u = User.query.filter_by(username="test").first()
    #     assert u.username == "test"
    #     assert u.check_password("password123")


if __name__ == "__main__":
    unittest.main()