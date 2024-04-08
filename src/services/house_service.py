from repositories.user_repository import user_repository 
from repositories.house_repository import house_repository 

class HouseService():
    def __init__(self, user_repository, house_repository):
        self._user_repository = user_repository
        self._user = None



house_service = HouseService(
  user_repository,
  house_repository
)
