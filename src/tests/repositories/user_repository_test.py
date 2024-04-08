import unittest
from repositories.user_repository import user_repository
from initialize_database import initialize_database

class TestUserRepository(unittest.TestCase):
    def setUp(self):
        #to implement: user_repository.delete_all()
        initialize_database()
        cursor = user_repository._connection.cursor()

        cursor.execute('''
            INSERT INTO users(
                username,
                password)
            VALUES
                ("x","x")
        ''')
    
    def test_user_cannot_register_under_existing_username(self):
        result = user_repository.register("x","x")

        self.assertEqual(result, False)

    def test_new_user_can_register_and_persits_in_database(self):
        result = user_repository.register("newuserpersists","x")
        result = user_repository.check_if_username_exists("newuserpersists")

        self.assertEqual(result, True)

    def test_new_user_can_register_and_log_in_afterwards(self):
        registration_result = user_repository.register("newuser","x")
        login_result = user_repository.login("newuser", "x")

        self.assertEqual(registration_result, True)
        self.assertEqual(login_result, True)

    def test_a_user_register_noone_can_take_their_name(self):
        registration_result = user_repository.register("newuser","x")
        login_result = user_repository.login("newuser", "x")

        another_registration_result = user_repository.register("newuser","y")

        self.assertEqual(registration_result, True)
        self.assertEqual(login_result, True)
        self.assertEqual(another_registration_result , False)
        
    def test_if_nonexistent_user_can_log_in(self):
        result = user_repository.login(
                "notexistingusername",
                "somepassword"
        )

        self.assertEqual(result, False)

    def test_a_user_can_be_fetched(self):
        result = user_repository.check_if_username_exists("x")

        self.assertEqual(result, True)

    def test_a_nonexisting_user_cannot_be_fetched(self):
        result = user_repository.check_if_username_exists("nonexistingusername")

        self.assertEqual(result, False)


