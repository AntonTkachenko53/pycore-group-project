from Field import Field
import re


class Email(Field):
    def __init__(self, value):
        super().__init__(value)
        self.validate()

    def validate(self):
        if self._value:
            email_re = re.compile(
                r"^(?![.@])[a-zA-Z0-9._-]+(?<!\.)@(?![.])(?!\.)[a-zA-Z0-9.-]+(?<![.])\.[a-zA-Z]{2,6}$"
            )

            if len(self._value) > 50:
                raise ValueError('Email is too long.')

            if not email_re.match(self._value):
                raise ValueError('Invalid email format.')
