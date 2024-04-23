class House:
    def __init__(self, house_id, parameters):
        self._id = house_id
        self._parameters = parameters

    def unpack_parameters(self):
        try:
            # generated code begins
            parameter_list = [int(x) for x in self._parameters.split(',')]
            p1 = parameter_list[0]
            p2 = parameter_list[1]
            # generated code ends
            return p1, p2
        except ValueError:
            return 0, 0
        except AttributeError:
            return 0, 0
