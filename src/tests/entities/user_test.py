import unittest
from entities.user import User


class TestUser(unittest.TestCase):
    def setUp(self):
        self.user = User(4, "username")

    def test_users_username_is_accessible(self):
        self.assertEqual(self.user.username, "username")
