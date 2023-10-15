from datetime import datetime
from Field import Field

class Birthday(Field):
    DATE_FORMAT = '%d.%m.%Y'

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
        if isinstance(self.value, datetime):
            date_str = self.value.strftime(self.DATE_FORMAT)
            if not self._check_valid_date(date_str):
                raise ValueError("Invalid date of birth format")
            components = date_str.split('.')
            day, month, year = map(int, components)

            try:
                datetime(year, month, day)
            except ValueError:
                raise ValueError("Invalid date of birth")

            self.value = self._normalize_year()
        else:
            raise ValueError("Invalid input type, expected datetime object")
