import unittest
from services.house_service import HouseService
from repositories.user_repository import user_repository 

class TestHouseService(unittest.TestCase):
    def setUp(self):
        self.house_service = HouseService(
          user_repository
        )

    def test_if_hardwired_user_can_log_in(self):
        result = self.house_service.login("m","m")

        self.assertEqual(result, True)

    def test_if_nonexistent_user_can_log_in(self):
        result = self.house_service.login(
                "notexistingusername",
                "somepassword"
        )

        self.assertEqual(result, False)

