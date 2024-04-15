from database_connection import get_database_connection
from entities.user import User


class UserRepository():
    # ,user):. The class should take user entity as injected dependency
    def __init__(self, connection):
        self._connection = connection

    def login(self, username, password):
        if not self.check_if_username_exists(username):
            print("Username doesn't exist")
            return False

        cursor = self._connection.cursor()
        data = (username, password)
        print("User attempts to log in")

        cursor.execute('''
            SELECT 
                id,username
            FROM
                users
            WHERE
                username=? 
            AND
                password=?
        ''', data)

        result = cursor.fetchone()

        print(f"result of login query: {result}")

        user_id = result['id']
        username = result['username']
        print("User object:")
        print(f"user_user_id:{id},username:{username}")
        user = User(user_id, username)
        if result:
            return user
        return False

    def register(self, username, password):
        if self.check_if_username_exists(username):
            print("Username taken")
            return False

        cursor = self._connection.cursor()
        data = (username, password)
        print("User being created")
        cursor.execute('''
            INSERT INTO users(
                username,
                password)
            VALUES
                (?,?)
        ''', data)
        self._connection.commit()
        print("User created")
        return True

    def check_if_username_exists(self, username):
        cursor = self._connection.cursor()

        cursor.execute('''
            SELECT username 
            FROM users 
            WHERE username=?
        ''', (username,))

        result = cursor.fetchone()
        print(f"result: {result}")
        if result:
            return True
        return False


user_repository = UserRepository(get_database_connection())
