class User:
    """Represents a user entity.

    Args:
        user_id (int): The user's ID.
        username (str): The username of the user.
    """

    def __init__(self, user_id, username):
        self._id = user_id
        self.username = username
