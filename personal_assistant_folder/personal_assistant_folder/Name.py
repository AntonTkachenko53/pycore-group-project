from Field import Field


class Name(Field):
    def __init__(self, value):
        super().__init__(value)
        self.validate()

    def validate(self):
        if len(self._value) < 3 or self._value.isdigit():
            raise ValueError("Invalid name. Name should be 3+ chars length and don`t consist only with numbers")
