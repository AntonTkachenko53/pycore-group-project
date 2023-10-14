from Field import Field


class Name(Field):
    def __init__(self, value):
        super().__init__(value)
        self.validate()

    def validate(self):
        check_name = self._value.strip()
        if len(check_name) < 3 or check_name.isdigit():
            raise ValueError("Invalid name. Name should be 3+ chars length and don`t consist only with numbers")
