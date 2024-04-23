from repositories.house_repository import (
    house_repository as default_house_repository )
from repositories.user_repository import (
    user_repository as default_user_repository )
from repositories.administrator_repository import (
    administrator_repository as default_administrator_repository )

class HouseService():
    def __init__(self, user_repository, house_repository,  administrator_repository):
        self._user_repository = user_repository
        self._house_repository = house_repository
        self._administrator_repository = administrator_repository
        self._user = None

    def register(self, username_entry, password_entry):
        if self._user_repository.register(username_entry, password_entry):
            return self.login(username_entry,password_entry)
        return False

    def login(self, username_entry, password_entry):
        user = self._user_repository.login(username_entry, password_entry)
        if user:
            return user
        return False

    def administrator_login(self, username_entry, password_entry):
        administrator = self._administrator_repository.login(username_entry, password_entry)
        if administrator:
            return administrator
        return False

    def get_users_house_id(self, user_id):
        return self._house_repository.get_users_house_id(user_id)

    def get_users_house(self, user_id):
        return self._house_repository.get_users_house(user_id)

    def update_house(self, user_id, new_parameters):
        print("houes service is trying to update the house")
        house_id = self.get_users_house_id(user_id)
        if house_id:
            self._house_repository.update_house(house_id, new_parameters)
            return
        self._house_repository.create_house(user_id, new_parameters)

    def get_energy_consumption(self, house_id):
        #house_id = self._house_repository.get_users_house_id(user_id)
        result = self._house_repository.calculate_energy_consumption(house_id)
        return result

    def get_pollution(self, house_id):
        #house_id = self._house_repository.get_users_house_id(user_id)
        result = self._house_repository.calculate_pollution(house_id)
        return result


house_service = HouseService(
    default_user_repository,
    default_house_repository,
    default_administrator_repository 
)
