from personal_assistant_folder.Field import Field
import re


class Email(Field):
    MAX_LENGTH = 128

    def __init__(self, value):
        super().__init__(value)
        self.validate(value)

    def validate(self, value):
        if value:
            email_re = re.compile(
                r"^(?![.@])[a-zA-Z0-9._-]+(?<!\.)@(?![.])(?!\.)[a-zA-Z0-9.-]+(?<![.])\.[a-zA-Z]{2,6}$"
            )

            if len(value) > self.MAX_LENGTH:
                raise ValueError('Email is too long.')

            if not email_re.match(value):
                raise ValueError('Invalid email format.')
