from datetime import datetime
from Field import Field

class Birthday(Field):
    DATE_FORMAT = '%d.%m.%Y'

    def __init__(self, value):
        super().__init__(value)
        self.validate()

    def _check_valid_date(self, date):
        try:
            datetime.strptime(date, self.DATE_FORMAT)
            return True
        except ValueError:
            return False

    def _normalize_year(self):
        today = datetime.now()
        return self.value.replace(year=today.year)

    def validate(self):
        if not self._check_valid_date(self.value.strftime(self.DATE_FORMAT)):
            raise ValueError("Invalid date format for birthday")
        self.value = self._normalize_year()

    def days_until_birthday(self):
        today = datetime.now()
        next_birthday = self.value.replace(year=today.year)

        if today > next_birthday:
            next_birthday = next_birthday.replace(year=today.year + 1)

        days_until_birthday = (next_birthday - today).days
        return days_until_birthday