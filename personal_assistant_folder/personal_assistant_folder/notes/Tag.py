from personal_assistant_folder.Field import Field


class Tag(Field):
    MIN_LENGTH = 4
    MAX_LENGTH = 40

    def __init__(self, value):
        super().__init__(value)
        self.validate(value)

    def validate(self, value):
        tag = value.strip()

        if not tag:
            raise ValueError(f"Tag can't be empty")

        if not (self.MIN_LENGTH <= len(tag) <= self.MAX_LENGTH):
            raise ValueError(f"The tag length must be from {self.MIN_LENGTH} to {self.MAX_LENGTH} characters")

        if not tag.startswith('#'):
            raise ValueError("Tag must starts with '#'")

    def __hash__(self):
        return hash(self.value)

    def __eq__(self, other):
        return isinstance(other, Tag) and self.value == other.value
