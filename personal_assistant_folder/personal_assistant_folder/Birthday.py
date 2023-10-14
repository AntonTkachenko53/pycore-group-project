from datetime import datetime
from Field import Field

class Birthday(Field):
    def __init__(self, value):
        super().__init__(value)
        self.validate()

    def _check_valid_date(self, date_str):
        try:
            datetime.strptime(date_str, self.DATE_FORMAT)
            return True
        except ValueError:
            return False

    def _normalize_year(self):
        today = datetime.now()
        return self.value.replace(year=today.year)

    def validate(self):
        date_str = str(self.value)
        if not self._check_valid_date(date_str):
            raise ValueError("Invalid date format for birthday")

        components = date_str.split('.')
        day, month, year = map(int, components)

        try:
            datetime(year, month, day)
        except ValueError:
            raise ValueError("Invalid birthday date")

        self.value = self._normalize_year()