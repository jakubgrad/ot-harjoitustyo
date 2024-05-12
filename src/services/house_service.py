from repositories.house_repository import (
    house_repository as default_house_repository)
from repositories.user_repository import (
    user_repository as default_user_repository)
from repositories.administrator_repository import (
    administrator_repository as default_administrator_repository)
from repositories.model_repository import (
    model_repository as default_model_repository)

class HouseService:
    """Service class for handling house-related operations.

    Attributes:
        _user_repository: User repository object.
        _house_repository: House repository object.
        _administrator_repository: Administrator repository object.
        _model_repository: Model repository object.
        _user: Current user object.
    """

    def __init__(self, user_repository, house_repository,
                 administrator_repository, model_repository):
        """Constructor for the HouseService class.

        Args:
            user_repository: User repository object.
            house_repository: House repository object.
            administrator_repository: Administrator repository object.
            model_repository: Model repository object.
        """
        self._user_repository = user_repository
        self._house_repository = house_repository
        self._administrator_repository = administrator_repository
        self._model_repository = model_repository
        self._user = None

    def register(self, username_entry, password_entry):
        """Registers a new user.

        Args:
            username_entry: Username of the new user.
            password_entry: Password of the new user.

        Returns:
            User object if registration is successful and login is successful, False otherwise.
        """
        if self._user_repository.register(username_entry, password_entry):
            return self.user_login(username_entry, password_entry)
        return False

    def user_login(self, username_entry, password_entry):
        """Logs in a user.

        Args:
            username_entry: Username of the user.
            password_entry: Password of the user.

        Returns:
            User object if login is successful, False otherwise.
        """
        user = self._user_repository.login(username_entry, password_entry)
        if user:
            return user
        return False

    def administrator_login(self, username_entry, password_entry):
        """Logs in an administrator.

        Args:
            username_entry: Username of the administrator.
            password_entry: Password of the administrator.

        Returns:
            Administrator object if login is successful, False otherwise.
        """
        administrator = self._administrator_repository.login(
            username_entry, password_entry)
        if administrator:
            return administrator
        return False

    def get_users_house_id(self, user_id):
        """Gets the ID of the house associated with the specified user.

        Args:
            user_id: ID of the user.

        Returns:
            ID of the house associated with the user if exists, False otherwise.
        """
        return self._house_repository.get_users_house_id(user_id)

    def get_users_house(self, user_id):
        """Gets the house object associated with the specified user.

        Args:
            user_id: ID of the user.

        Returns:
            House object associated with the user if exists, False otherwise.
        """
        return self._house_repository.get_users_house(user_id)

    def update_house(self, user_id, new_parameters):
        """Updates the parameters of the house associated with the specified user.

        Args:
            user_id: ID of the user.
            new_parameters: New parameters for the house.

        Returns:
            None
        """
        print("house service is trying to update the house")
        house_id = self.get_users_house_id(user_id)
        if house_id:
            self._house_repository.update_house(house_id, new_parameters)
            return
        self._house_repository.create_house(user_id, new_parameters)
        return

    def get_energy_consumption(self, house_id):
        """Gets the energy consumption for the specified house.

        Args:
            house_id: ID of the house.

        Returns:
            Energy consumption value.
        """

        parameters = self._house_repository.fetch_house_parameters(house_id)
        energy_consumption = self._model_repository.calculate_consumption(parameters)
        return energy_consumption

    def get_pollution(self, house_id):
        """Gets the pollution value for the specified house.

        Args:
            house_id: ID of the house.

        Returns:
            Pollution value.
        """

        parameters = self._house_repository.fetch_house_parameters(house_id)
        pollution = self._model_repository.calculate_pollution(parameters)
        return pollution

    def get_model(self):
        """Gets the model.

        Returns:
            Model object.
        """
        return self._model_repository.get_model()

    def check_equation(self, text):
        """Checks the validity of an equation.

        Args:
            text: Equation to be checked.

        Returns:
            True if the equation is valid, False otherwise.
        """
        return self._model_repository.check_equation(text)

    def update_types_of_heating(self, new_toh):
        """Updates the model with a new type of heating row

        Args:
            new_toh: new type of heating row

        Returns:
            True if the update is successful, False otherwise.
        """

        return self._model_repository.update_types_of_heating(new_toh)

    def update_house_age(self, new_house_age):
        """Updates the house age information in the database.

        Args:
            new_house_age (dict): Dictionary containing the new house age information.

        Returns:
            bool: True if the update is successful, False otherwise.
        """

        return self._model_repository.update_house_age(new_house_age)

    def create_new_admin(self,username_entry,password_entry):
        """Registers a new admin.

        Args:
            username_entry: Username of the new admin.
            password_entry: Password of the new admin.

        Returns:
            Administrator object if login is successful, False otherwise.
        """

        if self._administrator_repository.register(username_entry, password_entry):
            return self.administrator_login(username_entry, password_entry)
        return False

house_service = HouseService(
    default_user_repository,
    default_house_repository,
    default_administrator_repository,
    default_model_repository
)
