from Field import Field
import datetime

class Birthday(Field):
    def __init__(self, birthdate):
        super().__init(birthdate)

    def validate(self):
        try:
            datetime.datetime.strptime(self.value, '%d.%m.%Y')
        except ValueError:
            raise ValueError("Incorrect date format. 03/15/1990 format 03/15/1990 (for example, 03/15/1990)")

    def day_to_birthday(self):
        current_date = datetime.date.today()
        next_birthday = datetime.datetime.strptime(self.value, '%d.%m.%Y').date().replace(year=current_date.year)
        if next_birthday < current_date:
            next_birthday = next_birthday.replace(year=current_date.year + 1)
        days_to_birthday = (next_birthday - current_date).days
        return days_to_birthday