from personal_assistant_folder.Field import Field
import datetime

class Birthday(Field):
    def __init__(self, birthdate):
        super().__init__(birthdate)
        self.validate()

    def validate(self):
        try:
            datetime.datetime.strptime(self._value, '%d.%m.%Y')
        except ValueError:
            raise ValueError("correct format is 03.10.1990")

    def days_to_birthday(self):
        current_date = datetime.date.today()
        next_birthday = datetime.datetime.strptime(self._value, '%d.%m.%Y').date().replace(year=current_date.year)
        if next_birthday < current_date:
            next_birthday = next_birthday.replace(year=current_date.year + 1)
        days_to_birthday = (next_birthday - current_date).days
        return days_to_birthday