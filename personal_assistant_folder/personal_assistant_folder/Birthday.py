from datetime import datetime

class Birthday:
    def __init__(self, value):
        self.value = value

    def _check_valid_date(self, date):
        try:
            datetime.strptime(date, '%Y-%m-%d')
            return True
        except ValueError:
            return False

    def _normalize_year(self):
        today = datetime.now()
        return self.value.replace(year=today.year)

    def validate(self):
        if not self._check_valid_date(self.value.strftime('%Y-%m-%d')):
            raise ValueError("Invalid date format for birthday")
        self.value = self._normalize_year()

    def days_until_birthday(self):
        today = datetime.now()
        next_birthday = self.value.replace(year=today.year)

        if today > next_birthday:
            next_birthday = next_birthday.replace(year=today.year + 1)

        days_until_birthday = (next_birthday - today).days
        return days_until_birthday