from personal_assistant_folder.Field import Field


class Phone(Field):
    MAX_LENGTH = 13
    MIN_LENGTH = 9

    def __init__(self, value):
        super().__init__(value)
        self.validate(value)

    def validate(self, value):
        cleaned_number = ''.join([char for char in value if char.isdigit()])

        if len(cleaned_number) > self.MAX_LENGTH:
            raise ValueError("Phone number too long")

        if len(cleaned_number) < self.MIN_LENGTH:
            raise ValueError("Phone number too short")

        return '+' + cleaned_number if len(cleaned_number) == 12 else cleaned_number
