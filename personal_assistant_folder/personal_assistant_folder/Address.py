from Field import Field


class Address(Field):
    def __init__(self, value):
        super().__init__(value)
        self.validate()

    def validate(self):
        if not self.value:
            raise ValueError("The address cannot be empty")
