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

    def calculate_pollution(self,parameters):
        p1,p2 = parameters
        cursor = self._connection.cursor()

        year = self.find_min_year(p1)
        # type of heating
        print(f"year after find_mind_year: {year}")
        type_of_heating = p2

        print("Attempts to calculate pollution from parameters from db")

        cursor.execute('''
            SELECT 
                pollution
            FROM
                house_age
            WHERE 
                year_min == ? 
        ''', (year,))

        house_age_pollution = cursor.fetchone()["pollution"]
        print(f"houes age pollution found: {house_age_pollution }")

        cursor.execute('''
            SELECT 
                pollution
            FROM
                types_of_heating
            WHERE 
                type == ? 
        ''', (type_of_heating,))

        type_of_heating_pollution = cursor.fetchone()["pollution"]
        print(f"type_of_heating_pollution: {type_of_heating_pollution }")
        return type_of_heating_pollution + house_age_pollution 

    def calculate_consumption(self,parameters):
        p1,p2 = parameters

        cursor = self._connection.cursor()

        year = self.find_min_year(p1)
        # type of heating
        print(f"year after find_mind_year: {year}")
        type_of_heating = p2

        print("Attempts to calculate pollution from parameters from db")

        cursor.execute('''
            SELECT 
                energy_consumption 
            FROM
                house_age
            WHERE 
                year_min == ? 
        ''', (year,))

        house_age_consumption = cursor.fetchone()["energy_consumption"]
        print(f"houes age consumption found: {house_age_consumption }")

        cursor.execute('''
            SELECT 
                energy_consumption
            FROM
                types_of_heating
            WHERE 
                type == ? 
        ''', (type_of_heating,))

        type_of_heating_consumption = cursor.fetchone()["energy_consumption"]
        print(f"type_of_heating_consumption: {type_of_heating_consumption }")
        return type_of_heating_consumption + house_age_consumption 

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
