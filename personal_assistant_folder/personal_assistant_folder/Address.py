from personal_assistant_folder.Field import Field


class Address(Field):
    def __init__(self, value):
        super().__init__(value)
        self.validate(value)
