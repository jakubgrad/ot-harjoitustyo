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

    def evaluate_equation_for_house(self, house):
        """Evaluates the energy consumption and pollution for a given house.

        Args:
            house: House object for evaluation.

        Returns:
            Tuple containing energy consumption and pollution values.
        """
        try:
            house_age, type_of_heating = house.unpack_parameters()
            house_age = self.find_min_year(house_age)

            model = self.get_model()

            types_of_heating_as_dictionary = \
                model.get_types_of_heating_as_dictionary()
            house_age_as_dictionary = \
                model.get_house_age_as_dictionary()

            energy_consumption = types_of_heating_as_dictionary[type_of_heating][
                "energy_consumption"] + \
                house_age_as_dictionary[house_age]["energy_consumption"]

            pollution = types_of_heating_as_dictionary[type_of_heating]["pollution"] + \
                house_age_as_dictionary[house_age]["pollution"]

            return energy_consumption, pollution

        except KeyError:
            print(" evaluate_equation_for_house failed")
            return False

    def check_equation(self, equation):
        """Checks the validity of an equation.

        Args:
            equation: Equation to be checked.

        Returns:
            True if the equation is valid, False otherwise.
        """
        print("equation")

        parameters = "1991" + ","+"2"
        example_house = House(1, parameters)
        try:
            print(self.evaluate_equation_for_house(example_house))
            ast.literal_eval(equation)
        except KeyError:
            print("check_equation failed")
            return False

        return True

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
            house_age = info
            min_year = house_age["min_year"]
            max_year = house_age["max_year"]
            ha_energy_consumption = house_age["ha_energy_consumption"]
            ha_pollution = house_age["ha_pollution"]

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
            return True
        else:
            print(info)
            types_of_heating = info
            type_of_heating = types_of_heating["type_of_heating"]
            name = types_of_heating["name"]
            energy_consumption = types_of_heating["energy_consumption"]
            pollution = types_of_heating["pollution"]

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
            print("types_of_heating updated")
            return True

model_repository = ModelRepository(get_database_connection())

