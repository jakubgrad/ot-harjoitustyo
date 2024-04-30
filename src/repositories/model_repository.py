import ast
from database_connection import get_database_connection
from entities.model import Model
from entities.house import House

class ModelRepository:
    """Repository class for handling model data and evaluation.

    Args:
        connection: Database connection object.

    Attributes:
        _connection: Database connection object.
    """

    def __init__(self, connection):
        """Constructor for the ModelRepository class.

        Args:
            connection: Database connection object.
        """
        self._connection = connection

    def find_min_year(self, year):
        """Finds the minimum year from the database.

        Args:
            year: Year to be checked.

        Returns:
            Minimum year found in the database.
        """
        year = int(year)
        cursor = self._connection.cursor()
        print("Attempts to get parameters from db")

        cursor.execute('''
            SELECT 
                year_min 
            FROM
                house_age
            WHERE 
                year_min <= ?
            AND
                year_max > ?
        ''', (year, year))

        result = cursor.fetchone()
        print(f"min year found: {result}")
        if result:
            return result[0]
        return False

    def get_model(self):
        """Gets the model from the database.

        Returns:
            Model object containing data from the database.
        """
        cursor = self._connection.cursor()
        print("Attempts to get parameters from db")

        cursor.execute('''
            SELECT 
                id, 
                year_min, 
                year_max,
                energy_consumption,
                pollution
            FROM
                house_age
        ''')

        result_house_age = cursor.fetchall()

        print(f"result of house_age query: {result_house_age}")
        cursor.execute('''
            SELECT 
            id,
            type,
            name,
            energy_consumption,
            pollution
            FROM
                types_of_heating
        ''')

        result_types_of_heating = cursor.fetchall()

        print(f"result of types_of_heating query: {result_types_of_heating}")

        if result_house_age and result_types_of_heating:
            return Model(result_house_age, result_types_of_heating)
        return False

    def update_model(self, info):
        """Updates the model in the database.

        Args:
            info: Information to be updated.

        Returns:
            True if the update is successful, False otherwise.
        """
        cursor = self._connection.cursor()

        if "min_year" in info:
            min_year = info["min_year"]
            max_year = info["max_year"]
            ha_energy_consumption = info["ha_energy_consumption"]
            ha_pollution = info["ha_pollution"]

            data = (min_year, max_year, ha_energy_consumption, ha_pollution)

            cursor.execute('''
                INSERT INTO house_age(
                    year_min ,
                    year_max,
                    energy_consumption,
                    pollution)
                VALUES
                    (?,?,?,?)
            ''', data)
            self._connection.commit()
            print("house_age updated")
        else:
            type_of_heating = info["type_of_heating"]
            name = info["name"]
            energy_consumption = info["energy_consumption"]
            pollution = info["pollution"]

            data = (type_of_heating, name, energy_consumption, pollution)

            cursor.execute('''
                INSERT INTO types_of_heating(
                    type,
                    name,
                    energy_consumption,
                    pollution)
                VALUES
                    (?,?,?,?)
            ''', data)
            self._connection.commit()

        return True

model_repository = ModelRepository(get_database_connection())
