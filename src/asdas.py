from repositories.user_repository import user_repository 
from repositories.house_repository import house_repository

class HouseService():
    """Class responsible for most of the logic"""

    def __init__(
        self, 
        house_repository, 
        user_repository
    ):
        """HouseService constructors. Uses dependency injection to handle house and user repositories.

        Args:
            house_repository: 
                makes it possible to save information about houses and calculate emissions etc
            user_repository:
                makes it possible to stay logged in and view one's own houses
        """
        self._house_repository = house_repository
        self._user_repository = user_repository
        self._user = None

    def login(self, username, password):
        """Function responsible for handling information from user at login"""

        #For now:
        if username == "m":
            if password == "m":
                return True
        return False
               
    def registration(self, username, password):
        """Function responsible for handling information from user at login"""

        #For now:
        if username == "m":
            if password == "m":
                return True
        return False


house_service = HouseService(
  house_repository, 
  user_repository
)
