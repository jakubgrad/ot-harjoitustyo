from repositories.user_repository import user_repository
from repositories.house_repository import house_repository


class HouseService():
    def __init__(self, user_repository, house_repository):
        self._user_repository = user_repository
        self._house_repository = house_repository
        self._user = None

    def register(self,username_entry, password_entry):
        if self._user_repository.register(username_entry, password_entry):
            return True
        else:
            return False

    def register(self,username_entry, password_entry):
        if self._user_repository.register(username_entry, password_entry):
            return True
        else:
            return False

    def login(self,username_entry, password_entry):
        user_id = self._user_repository.login(username_entry, password_entry)
        if user_id:
            return user_id
        else:
            return False

    def get_users_house_id(self, user_id):
        return self._house_repository.get_users_house_id(user_id)

    def update_house(self, house_id, new_parameters):
        print("houes service is trying to update the house")
        self._house_repository.update_house(house_id, new_parameters)


    def get_energy_consumption(self,user_id):
        house_id = self._house_repository.get_users_house_id(user_id)
        result = self._house_repository.calculate_energy_consumption(house_id)
        return result

    def get_pollution(self,user_id):
        house_id = self._house_repository.get_users_house_id(user_id)
        result = self._house_repository.calculate_pollution(house_id)
        return result


house_service = HouseService(
    user_repository,
    house_repository
)
