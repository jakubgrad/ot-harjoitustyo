from database_connection import get_database_connection
from entities.model import Model

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
        """Calculates pollution based on given parameters.

        Args:
            parameters (tuple): A tuple containing year and type of heating.

        Returns:
            int: The calculated pollution value.
        """
        year, type_of_heating = parameters
        year = self.find_min_year(year)

        if not year:
            #means that the house is older than there is data for
            year = self.find_min_year(2021)

        cursor = self._connection.cursor()

        cursor.execute('''
            SELECT 
                pollution
            FROM
                house_age
            WHERE 
                year_min == ? 
        ''', (year,))

        house_age_pollution = cursor.fetchone()["pollution"]

        cursor.execute('''
            SELECT 
                pollution
            FROM
                types_of_heating
            WHERE 
                type == ? 
        ''', (type_of_heating,))

        type_of_heating_pollution = cursor.fetchone()["pollution"]

        return type_of_heating_pollution + house_age_pollution

    def calculate_consumption(self,parameters):
        """Calculates energy consumption based on given parameters.

        Args:
            parameters (tuple): A tuple containing year and type of heating.

        Returns:
            int: The calculated energy consumption value.
        """

        year,type_of_heating  = parameters

        if not year:
            year = self.find_min_year(2021)

        cursor = self._connection.cursor()

        cursor.execute('''
            SELECT 
                energy_consumption 
            FROM
                house_age
            WHERE 
                year_min == ? 
        ''', (year,))

        house_age_consumption = cursor.fetchone()["energy_consumption"]

        cursor.execute('''
            SELECT 
                energy_consumption
            FROM
                types_of_heating
            WHERE 
                type == ? 
        ''', (type_of_heating,))

        type_of_heating_consumption = cursor.fetchone()["energy_consumption"]

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

        if result:
            return result[0]
        return False

    def get_model(self):
        """Gets the model from the database.

        Returns:
            Model object containing data from the database.
        """

        cursor = self._connection.cursor()

        cursor.execute('''
            SELECT 
                id, 
                year_min, 
                year_max,
                energy_consumption,
                pollution
            FROM
                house_age
            ORDER BY
                year_min ASC;
        ''')

        result_house_age = cursor.fetchall()

        cursor.execute('''
            SELECT 
                id,
                type,
                name,
                energy_consumption,
                pollution
            FROM
                types_of_heating
            ORDER BY
                type ASC;
        ''')

        result_types_of_heating = cursor.fetchall()

        if result_house_age and result_types_of_heating:
            return Model(result_house_age, result_types_of_heating)
        return False

    def update_types_of_heating(self, new_toh):
        """Updates the types_of_heating table in the database.

        Args:
            new_toh: Information to be updated.

        Returns:
            True if the update is successful, False otherwise.
        """
        cursor = self._connection.cursor()

        data = tuple(new_toh.values())

        cursor.execute('''
            REPLACE INTO types_of_heating(
                type,
                name,
                energy_consumption,
                pollution)
            VALUES
                (?,?,?,?)
        ''', data)
        self._connection.commit()

        return True

    def update_house_age(self, new_house_age):
        """Updates the house age information in the database.

        Args:
            new_house_age (dict): Dictionary containing the new house age information.

        Returns:
            bool: True if the update is successful, False otherwise.
        """

        cursor = self._connection.cursor()

        data = tuple(new_house_age.values())

        cursor.execute('''
            REPLACE INTO house_age(
                year_min ,
                year_max,
                energy_consumption,
                pollution)
            VALUES
                (?,?,?,?)
        ''', data)
        self._connection.commit()

        return True

model_repository = ModelRepository(get_database_connection())
