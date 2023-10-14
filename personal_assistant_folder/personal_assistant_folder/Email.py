from Field import Field
import re


class Email(Field):
    def __init__(self, value):
        super().__init__(value)
        self.validate()

    def validate(self):
        if self._value is not None:
            if len(self._value) > 128:
                raise ValueError("Email is too long.")
            email_pattern = r"^[\w\.-]+@[\w\.-]+\.\w+$"
            if not re.match(email_pattern, self._value):
                raise ValueError("Invalid email format.")


email = Email("test@example.com")
try:
    email.value = "invalid-email"
except ValueError as e:
    print(str(e))
