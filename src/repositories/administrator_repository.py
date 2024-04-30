from database_connection import get_database_connection
from entities.administrator import Administrator

class AdministratorRepository:
    """Repository class for handling administrator data in the database.

    Args:
        connection: Database connection object.

    Attributes:
        _connection: Database connection object.
    """

    def __init__(self, connection):
        """Constructor for the AdministratorRepository class.

        Args:
            connection: Database connection object.
        """
        self._connection = connection

    def login(self, username, password):
        """Attempts to log in an administrator with the provided credentials.

        Args:
            username: Username of the administrator.
            password: Password of the administrator.

        Returns:
            Administrator object if login is successful, False otherwise.
        """
        if not self.check_if_administrator_name_exists(username):
            print("Username doesn't exist")
            return False

        cursor = self._connection.cursor()
        data = (username, password)
        print("Admin attempts to log in")

        cursor.execute('''
            SELECT 
                id,username
            FROM
                administrators
            WHERE
                username=? 
            AND
                password=?
        ''', data)

        result = cursor.fetchone()

        print(f"result of login query: {result}")

        user_id = result['id']
        username = result['username']
        print("administrator object:")
        print(f"administrator_id:{id},username:{username}")
        administrator = Administrator(user_id, username)
        if result:
            return administrator
        return False

    def register(self, username, password):
        """Registers a new administrator with the provided credentials.

        Args:
            username: Username of the new administrator.
            password: Password of the new administrator.

        Returns:
            True if registration is successful, False otherwise.
        """
        if self.check_if_administrator_name_exists(username):
            print("Username taken")
            return False

        cursor = self._connection.cursor()
        data = (username, password)
        print("User being created")
        cursor.execute('''
            INSERT INTO administrators(
                username,
                password)
            VALUES
                (?,?)
        ''', data)
        self._connection.commit()
        print("Administrator created")
        return True

    def check_if_administrator_name_exists(self, username):
        """Checks if an administrator with the given username exists in the database.

        Args:
            username: Username to check.

        Returns:
            True if an administrator with the given username exists, False otherwise.
        """
        cursor = self._connection.cursor()

        cursor.execute('''
            SELECT username 
            FROM administrators
            WHERE username=?
        ''', (username,))

        result = cursor.fetchone()
        print(f"result: {result}")
        if result:
            return True
        return False


administrator_repository = AdministratorRepository(get_database_connection())

