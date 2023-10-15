from Field import Field


class Title(Field):
    MIN_LENGTH = 3
    MAX_LENGTH = 40

    def __init__(self, value):
        super().__init__(value)
        self.validate()

    def validate(self):
        title = self._value.strip()

        if not title:
            raise ValueError(f"Title can't be empty")

        if not (self.MIN_LENGTH <= len(title) <= self.MAX_LENGTH):
            raise ValueError(f"The title length must be from {self.MIN_LENGTH} to {self.MAX_LENGTH} characters")
