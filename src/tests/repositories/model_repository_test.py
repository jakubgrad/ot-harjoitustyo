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

    def test_update_house_age(self):
        new_house_age = {
            "min_year": 1990,
            "max_year": 2000,
            "ha_energy_consumption": 50,
            "ha_pollution": 10
        }
        result = model_repository.update_house_age(new_house_age)

        self.assertTrue(result)

    def test_update_types_of_heating(self):
        new_toh = {
            "type_of_heating": 2,
            "name": "Boilering",
            "energy_consumption": 3,
            "pollution": 5 
        }
        result = model_repository.update_house_age(new_toh)

        self.assertTrue(result)

    def test_calculating_pollution_works(self):
        parameters = (2021, 4)
        result = model_repository.calculate_pollution(parameters)

        self.assertIsInstance(result, (int, float))

    def test_calculating_energy_consumption_works(self):
        parameters = (2021, 4)
        result = model_repository.calculate_consumption(parameters)

        self.assertIsInstance(result, (int, float))



