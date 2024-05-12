class House:
    """Represents a house with its unique identifier and parameters.

    Attributes:
        _id (int): The unique identifier of the house.
        _parameters (tuple): A tuple containing the parameters of the house.
    """

    def __init__(self, house_id, parameters):
        self._id = house_id
        self._parameters = parameters
