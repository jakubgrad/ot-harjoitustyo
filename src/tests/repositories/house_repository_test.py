import unittest
from repositories.house_repository import house_repository
from initialize_database import initialize_database


class TestHouseRepository(unittest.TestCase):
    def setUp(self):
        # to implement: house_repository.delete_all()
        initialize_database()
        cursor = house_repository._connection.cursor()

        cursor.execute('''
            INSERT INTO users(
                username,
                password)
            VALUES
                ("x","x")
        ''')

        cursor.execute('''
            INSERT INTO houses(
                user_id,
                parameters)
            VALUES
                (1,"3,3")
        ''')

    def test_a_new_user_doesnt_have_a_house(self):
        user_id = 1234
        result = house_repository.get_users_house_id(user_id)
        self.assertEqual(result, False)

    def test_an_existing_user_can_get_a_house(self):
        user_id = 5
        house_repository.create_house(user_id, "sample_parameters")
        has_house = house_repository.get_users_house_id(user_id)

        self.assertNotEqual(has_house, False)

    def test_a_house_can_be_created_and_fetched(self):
        user_id = 100
        house_repository.create_house(user_id, "sample_parameters")
        house_id = house_repository.get_users_house_id(user_id)
        parameters = house_repository.fetch_house_parameters(house_id)

        self.assertEqual(parameters, "sample_parameters")

    def test_a_house_can_be_created_and_modified(self):
        user_id = 100
        house_repository.create_house(user_id, "sample_parameters")
        house_id = house_repository.get_users_house_id(user_id)
        house_repository.update_house(house_id, "new_parameters")
        parameters = house_repository.fetch_house_parameters(house_id)

        self.assertEqual(parameters, "new_parameters")

    def test_calculating_pollution_works(self):
        house_id = 1
        result = house_repository.calculate_pollution(house_id)

        self.assertIsInstance(result, (int, float))

    def test_calculating_energy_consumption_works(self):
        house_id = 1
        result = house_repository.calculate_pollution(house_id)

        self.assertIsInstance(result, (int, float))

    # def test_a_house_can_be_created_by_a_registered_user(self):
