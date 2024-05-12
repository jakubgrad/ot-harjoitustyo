class Administrator:
    """Represents an administrator entity.

    Attributes:
        user_id (int): The administrator's ID.
        username (str): The username of the administrator.
    """

    def __init__(self, user_id, username):
        self._id = user_id
        self.username = username
