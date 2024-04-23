class Model:
    def __init__(self,  house_age, types_of_heating):
        self._house_age = house_age
        self._types_of_heating = types_of_heating

    def get_types_of_heating_as_dictionary(self):
        t = {}
        for i, row in enumerate(self._types_of_heating):
            t[i+1] = {"energy_consumption": row[3], "pollution": row[4]}
        return t

    def get_house_age_as_dictionary(self):
        h = {}
        for row in self._house_age:
            h[row[1]] = {"energy_consumption": row[3], "pollution": row[4]}
        return h
