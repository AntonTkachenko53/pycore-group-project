class Field:
    def __init__(self, value):
        self._value = value.strip()

    def __str__(self):
        return str(self._value)

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, new_value):
        self.validate(new_value)
        self._value = new_value.strip()

    def validate(self, value):
        pass
