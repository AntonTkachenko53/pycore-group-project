from Field import Field


class Name(Field):
    def __init__(self, value, min_length=3, max_length=50):
        super().__init__(value)
        self.min_length = min_length
        self.max_length = max_length
        self.validate()

    def validate(self):
        if self._value is not None:
            stripped_name = self._value.strip()
            if (
                len(stripped_name) < self.min_length
                or len(stripped_name) > self.max_length
            ):
                raise ValueError(
                    f"Invalid name. The name must be between {self.min_length} до {self.max_length} characters."
                )
            if not stripped_name.isalpha():
                raise ValueError("Invalid name. The name must contain only letters.")


name = Name("John Doe", min_length=2, max_length=30)
try:
    name.value = "123"
except ValueError as e:
    print(str(e))
