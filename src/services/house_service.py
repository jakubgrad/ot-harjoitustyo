from repositories.user_repository import user_repository 

class HouseService():
    def __init__(self, user_repository):
        self._user_repository = user_repository
        self._user = None

    def login(self, username, password):

        #For now:
        if username == "m":
            if password == "m":
                return True
        return False
               
    def registration(self, username, password):
        #For now:
        if username == "m":
            if password == "m":
                return True
        return False


house_service = HouseService(
  user_repository
)
