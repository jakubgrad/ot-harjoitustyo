import unittest
from services.house_service import HouseService

from repositories.house_repository import (
    house_repository as default_house_repository)
from repositories.user_repository import (
    user_repository as default_user_repository)
from repositories.administrator_repository import (
    administrator_repository as default_administrator_repository)
from repositories.model_repository import (
    model_repository as default_model_repository)
from entities.house import House
from entities.administrator import Administrator
from entities.model import Model
from entities.user import User
from config import DEFAULT_ADMIN_USERNAME
from config import DEFAULT_ADMIN_PASSWORD


class TestHouseService(unittest.TestCase):
    def setUp(self):
        self.house_service = HouseService(
            default_user_repository,
            default_house_repository,
            default_administrator_repository,
            default_model_repository
        )
        result = self.house_service.register("user1", "pass1")

    def test_one_equals_one(self):
        self.assertEqual(1, 1)

    def test_registering_with_new_username_works(self):
        result = self.house_service.register("new_username", "password")

        self.assertNotEqual(result, False)

    def test_registering_with_existing_username_does_not_work(self):
        result = self.house_service.register("user1", "pass1")

        self.assertEqual(result, False)

    def test_login_with_existing_username_works(self):
        result = self.house_service.user_login("user1", "pass1")

        self.assertNotEqual(result, False)

    def test_login_with_nonexisting_username_works(self):
        result = self.house_service.user_login("non_existing_user", "pass")

        self.assertEqual(result, False)

    # integration testing
    def test_default_administrator_login(self):
        administrator = self.house_service.administrator_login(
             DEFAULT_ADMIN_USERNAME, DEFAULT_ADMIN_PASSWORD)

        self.assertIsInstance(administrator, Administrator)

    def test_user_login(self):
        administrator = self.house_service.administrator_login(
             DEFAULT_ADMIN_USERNAME, DEFAULT_ADMIN_PASSWORD)

        self.assertIsInstance(administrator, Administrator)

    def test_login_with_correct_username_works(self):
        user = self.house_service.user_login("user1", "pass1")

        self.assertIsInstance(user, User)

    def test_getting_the_model_works(self):
        model = self.house_service.get_model()

        self.assertIsInstance(model, Model)

    def test_getting_a_house_works(self):
        user_id = 1
        parameters = "2022,5"
        model = self.house_service.update_house(user_id, parameters)
        house = self.house_service.get_users_house(user_id)

        self.assertIsInstance(house, House)
    
    def test_getting_pollution_works(self):
        user_id = 1
        parameters = "2022,5"
        model = self.house_service.update_house(user_id, parameters)
        house = self.house_service.get_users_house(user_id)
        pollution = self.house_service.get_pollution(house._id)

        self.assertIsInstance(pollution, int)
