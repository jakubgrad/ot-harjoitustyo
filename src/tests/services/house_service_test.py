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
        #would be nice to have:
        #todo_repository.delete_all()
        #user_repository.delete_all()

    def test_one_equals_one(self):

        self.assertEqual(1, 1)

