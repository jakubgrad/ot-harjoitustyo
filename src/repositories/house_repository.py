
from database_connection import get_database_connection
from entities.house import House

class HouseRepository:
    """Repository class for handling house data in the database.

    Args:
        connection: Database connection object.

    Attributes:
        _connection: Database connection object.
    """

    def __init__(self, connection):
        """Constructor for the HouseRepository class.

        Args:
            connection: Database connection object.
        """
        self._connection = connection

    def create_house(self, user_id, parameters):
        """Creates a new house entry in the database.

        Args:
            user_id: ID of the user associated with the house.
            parameters: Parameters of the house.

        Returns:
            None
        """
        cursor = self._connection.cursor()
        data = (user_id, parameters)
        cursor.execute('''
            INSERT INTO houses (
                user_id,
                parameters)
            VALUES
                (?,?)
        ''', data)

        self._connection.commit()

    def calculate_pollution(self, house_id):
        """Calculates the pollution based on house parameters.

        Args:
            house_id: ID of the house.

        Returns:
            Pollution value calculated based on house parameters.
        """
        result = self.fetch_house_parameters(house_id)
        try:
            # generated code begins
            parameter_list = [int(x) for x in result.split(',')]
            param1 = parameter_list[0]
            param2 = parameter_list[1]
            # generated code ends
        except (ValueError, AttributeError):
            param1 = 0
            param2 = 0
        return param1 * param2 + param1 + param2

    def calculate_energy_consumption(self, house_id):
        """Calculates the energy consumption based on house parameters.

        Args:
            house_id: ID of the house.

        Returns:
            Energy consumption value calculated based on house parameters.
        """
        result = self.fetch_house_parameters(house_id)
        try:
            # generated code begins
            parameter_list = [int(x) for x in result.split(',')]
            param1 = parameter_list[0]
            param2 = parameter_list[1]
            # generated code ends
        except (ValueError, AttributeError):
            param1 = 0
            param2 = 0

        return param1 * param2 + param1 + param2

    def update_house(self, house_id, new_parameters):
        """Updates the parameters of the specified house.

        Args:
            house_id: ID of the house to be updated.
            new_parameters: New parameters for the house.

        Returns:
            None
        """
        print("house repo tries to update the house")
        cursor = self._connection.cursor()
        data = (new_parameters, house_id)
        print(f"data: {data}")
        cursor.execute('''
            UPDATE houses
            SET parameters = ?
            WHERE id = ?
        ''', data)

        self._connection.commit()

    def get_users_house_id(self, user_id):
        """Gets the ID of the house associated with the specified user.

        Args:
            user_id: ID of the user.

        Returns:
            ID of the house associated with the user if exists, False otherwise.
        """
        cursor = self._connection.cursor()

        cursor.execute('''
            SELECT id
            FROM houses 
            WHERE user_id=?
        ''', (user_id,))

        result = cursor.fetchone()
        print(f"result of checking if {user_id} has a house: {result}")
        if result:
            return result['id']
        return False

    def get_users_house(self, user_id):
        """Gets the house object associated with the specified user.

        Args:
            user_id: ID of the user.

        Returns:
            House object associated with the user if exists, False otherwise.
        """
        cursor = self._connection.cursor()

        cursor.execute('''
            SELECT id,parameters
            FROM houses 
            WHERE user_id=?
        ''', (user_id,))

        result = cursor.fetchone()

        if result:
            house_id = result['id']
            parameters = result['parameters']
            print("Inside get_user_house")
            print(f"house_id:{house_id}")
            print(f"parameters:{parameters}")
            return House(house_id, parameters)
        return False

    def fetch_house_parameters(self, house_id):
        """Fetches the parameters of the specified house from the database.

        Args:
            house_id: ID of the house.

        Returns:
            Parameters of the house if exists, False otherwise.
        """
        # if not self.get_users_house_id(user_id):
        #    print(f"{user_id} doesn't have a house, cannot fetch")
        #    return False

        cursor = self._connection.cursor()

        cursor.execute('''
            SELECT 
                id,parameters
            FROM
                houses
            WHERE
                id=? 
        ''', (house_id,))

        result = cursor.fetchone()

        if result:
            print(f"result: {result}")
            print(f"id of the house: {result['id']}")
            parameters = result['parameters']
            return parameters
        return False


house_repository = HouseRepository(get_database_connection())

