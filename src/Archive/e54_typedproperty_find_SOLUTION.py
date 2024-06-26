def typedproperty(name, expected_type):
    private_name = f"_{name}"

    @property
    def value(self):
        return getattr(self, private_name)

    @value.setter
    def value(self, val):
        if not isinstance(val, expected_type):
            raise TypeError(f"Expected {expected_type}")
        setattr(self, private_name, val)

    return value


def Float(name):
    return typedproperty(name, float)


def Integer(name):
    return typedproperty(name, int)


def String(name):
    return typedproperty(name, str)
