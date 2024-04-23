from database_connection import get_database_connection
from entities.house import House


class HouseRepository():
    # ,house):. The class should take house entity as injected dependency
    def __init__(self, connection):
        self._connection = connection

    def create_house(self, user_id, parameters):
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

    def create_house(self, user_id, parameters):
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
        result = self.fetch_house_parameters(house_id)
        try:
            # generated code begins
            parameter_list = [int(x) for x in result.split(',')]
            param1 = parameter_list[0]
            param2 = parameter_list[1]
            # generated code ends
        except ValueError:
            param1 = 0
            param2 = 0
        except AttributeError:
            param1 = 0
            param2 = 0
        return param1*param2+param1+param2

    def calculate_energy_consumption(self, house_id):
        result = self.fetch_house_parameters(house_id)
        try:
            # generated code begins
            parameter_list = [int(x) for x in result.split(',')]
            param1 = parameter_list[0]
            param2 = parameter_list[1]
            # generated code ends
        except ValueError:
            param1 = 0
            param2 = 0
        except AttributeError:
            param1 = 0
            param2 = 0

        return param1*param2+param1+param2

    def update_house(self, house_id, new_parameters):
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
            return House(house_id,parameters)
        return False

    def fetch_house_parameters(self, house_id):
        #if not self.get_users_house_id(user_id):
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
