class Model:
    """Represents a model containing house age and types of heating data.

    Args:
        house_age (list): A list containing house age data.
        types_of_heating (list): A list containing types of heating data.
    """

    def __init__(self,  house_age, types_of_heating):
        self._house_age = house_age
        self._types_of_heating = types_of_heating
