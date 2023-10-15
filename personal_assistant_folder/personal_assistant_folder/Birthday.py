from Field import Field
import datetime

class Birthday(Field):
    def __init__(self, birthdate):
        try:
            self.birthdate = datetime.datetime.strptime(birthdate, '%d.%m.%Y').date()
        except ValueError:
            raise ValueError("Incorrect date format. Vikorist format dd.mm.rrrr (for example, 03/15/1990).")

    def day_to_birthday(self):
        current_date = datetime.date.today()
        next_birthday = self.birthdate.replace(year=current_date.year)
        if next_birthday < current_date:
            next_birthday = self.birthdate.replace(year=current_date.year + 1)
        day_to_birthday = (next_birthday - current_date).days
        return day_to_birthday