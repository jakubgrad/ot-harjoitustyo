import unittest
from repositories.model_repository import model_repository
from initialize_database import initialize_database
#from entities.house import House

class TestModelRepository(unittest.TestCase):
    def setUp(self):
        initialize_database()  

    def test_find_min_year(self):
        year = "1995"
        result = model_repository.find_min_year(year)

        self.assertEqual(result, 1990)  


    def test_get_model(self):
        result = model_repository.get_model()

        self.assertIsNotNone(result)

    def test_update_model(self):
        info = {
            "min_year": 1990,
            "max_year": 2000,
            "ha_energy_consumption": 50,
            "ha_pollution": 10
        }
        result = model_repository.update_model(info)

        self.assertTrue(result)



