from datetime import datetime
from Field import Field

class Birthday(Field):
    def validate(self):
        self._check_type()
        self._check_future_date()
        self._check_birth_year()

    def _check_type(self):
        if not isinstance(self.value, datetime):
            raise ValueError("Birthday must be a datetime object")

    def _check_future_date(self):
        now = datetime.now()
        if self.value > now:
            raise ValueError("Birthday cannot be in the future")

    def _check_birth_year(self):
        if self.value.year < 1900:
            raise ValueError("Year of birth cannot be earlier than 1900")

    def _normalize_year(self):
        now = datetime.now()
        return self.value.replace(year=now.year)

    def validate_and_normalize(self):
        self._check_type()
        self._check_future_date()
        self._check_birth_year()
        return self._normalize_year()