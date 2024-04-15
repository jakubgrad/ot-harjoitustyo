import unittest
from services.house_service import HouseService
from repositories.user_repository import user_repository
from repositories.house_repository import house_repository


class TestHouseService(unittest.TestCase):
    def setUp(self):
        self.house_service = HouseService(
            user_repository,
            house_repository
        )
        result = self.house_service.register("user1", "pass1")
        # would be nice to have:
        # todo_repository.delete_all()
        # user_repository.delete_all()

    def test_one_equals_one(self):
        self.assertEqual(1, 1)

    def test_registering_with_new_username_works(self):
        result = self.house_service.register("new_username", "password")
        self.assertNotEqual(result, False)

    def test_registering_with_existing_username_does_not_work(self):
        result = self.house_service.register("user1", "pass1")
        self.assertEqual(result, False)

    def test_login_with_existing_username_works(self):
        result = self.house_service.login("user1", "pass1")
        self.assertNotEqual(result, False)

    def test_login_with_nonexisting_username_works(self):
        result = self.house_service.login("non_existing_user", "pass")
        self.assertEqual(result, False)
