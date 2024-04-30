import unittest
from repositories.administrator_repository import administrator_repository
from initialize_database import initialize_database

class TestAdministratorRepository(unittest.TestCase):
    def setUp(self):
        initialize_database()
        cursor = administrator_repository._connection.cursor()

        cursor.execute('''
            INSERT INTO administrators(
                username,
                password)
            VALUES
                ("admin", "adminpassword")
        ''')

    def test_administrator_cannot_register_under_existing_username(self):
        result = administrator_repository.register("admin", "anotherpassword")

        self.assertEqual(result, False)

    def test_new_administrator_can_register_and_persist_in_database(self):
        result = administrator_repository.register("newadmin", "newpassword")
        result = administrator_repository.check_if_administrator_name_exists("newadmin")

        self.assertEqual(result, True)

    def test_new_administrator_can_register_and_login_afterwards(self):
        registration_result = administrator_repository.register("newadmin", "x")
        login_result = administrator_repository.login("newadmin", "x")

        self.assertEqual(registration_result, True)
        self.assertNotEqual(login_result, False)

    def test_an_administrator_register_no_one_can_take_their_name(self):
        registration_result = administrator_repository.register("newadmin", "x")
        login_result = administrator_repository.login("newadmin", "x")

        another_registration_result = administrator_repository.register("newadmin", "y")

        self.assertEqual(registration_result, True)
        self.assertNotEqual(login_result, False)
        self.assertEqual(another_registration_result, False)

    def test_if_nonexistent_administrator_can_log_in(self):
        result = administrator_repository.login(
            "nonexistingadmin",
            "somepassword"
        )

        self.assertEqual(result, False)

    def test_an_administrator_can_be_fetched(self):
        result = administrator_repository.check_if_administrator_name_exists("admin")

        self.assertEqual(result, True)

    def test_a_nonexisting_administrator_cannot_be_fetched(self):
        result = administrator_repository.check_if_administrator_name_exists(
            "nonexistingadmin")

        self.assertEqual(result, False)
