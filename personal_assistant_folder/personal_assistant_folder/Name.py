from personal_assistant_folder.Field import Field


class Name(Field):
    MIN_LENGTH = 3

    def __init__(self, value):
        super().__init__(value)
        self.validate(value)

    def validate(self, value):
        check_name = value.strip()
        if len(check_name) < self.MIN_LENGTH or check_name.isdigit():
            raise ValueError("Invalid name. Name should be 3+ chars length and don`t consist only with numbers")
