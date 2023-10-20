from personal_assistant_folder.Field import Field


class Content(Field):
    MAX_LENGTH = 512

    def __init__(self, value):
        super().__init__(value)
        self.validate(value)

    def validate(self, value):
        text = value.strip()

        if text and len(text) > self.MAX_LENGTH:
            raise ValueError(f"The content length must be less {self.MAX_LENGTH} characters")
