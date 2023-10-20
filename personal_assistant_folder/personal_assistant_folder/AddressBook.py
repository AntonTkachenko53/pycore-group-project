from personal_assistant_folder.Record import Record
from personal_assistant_folder.Serialization import Serialization


class AddressBook:
    MIN_LENGTH_ADD = 2
    MAX_LENGTH_ADD = 5

    def __init__(self, filename):
        self.filename = filename
        self.records = Serialization.load_from_file(self.filename)

    def add_record(self, user_input):
        """
        тут введений інпут може містити тільки значення, від двох до п'яти, котрі записуються в record,
        
        порядок наступний: name, phone, далі ключові аргументи, котрі за замовчуванням = None: birthday, email, address.
        """
        commands = user_input.strip().split(';')

        if not (self.MIN_LENGTH_ADD <= len(commands) <= self.MAX_LENGTH_ADD):
            raise ValueError('Enter correct info to add a record')

        name, phone, *args = commands  # Розпакування перших двох значень та всіх інших у змінну args

        for record in self.records:
            if name == record.name._value:
                raise ValueError('Contact with this name already exists')

        try:
            contact = Record(name, phone, *args)
            self.records.append(contact)

            Serialization.save_to_file(self.records, self.filename)

            return True

        except ValueError:
            raise ValueError('Invalid info to create a record')

    def find_record(self, value):
        for record in self.records:
            if str(record.name) == value:
                return record

        return None

    def find_records(self, searching_str: str):
        result = [
            record for record in self.records if
            searching_str in f"{record.name._value} {record.phone._value} "
                             f"{record.birthday._value if record.birthday else ''} "
                             f"{record.email._value if record.email else ''} "
                             f"{record.address._value if record.address else ''}"
        ]

        if not result:
            result.append('Nothing found!')

        return result

    def delete_record(self, record_to_delete: str):
        result = False
        for record in self.records:
            if record_to_delete == record.name._value:
                self.records.remove(record)
                Serialization.save_to_file(self.records, self.filename)
                result = True
        return result

    def edit_record(self, record_name, data, field=None):
        if not record_name:
            raise ValueError(f"Record with name '{record_name}' not found")

        try:
            if not field:
                commands = data.strip().split(';')
                if len(commands) < 2 or len(commands) > self.MAX_LENGTH_ADD:
                    raise ValueError('Enter correct info to edit a record')

                # Оновити запис в залежності від кількості аргументів
                record_name.edit_name(commands[0])
                record_name.edit_phone(commands[1])

                if len(commands) >= 3:
                    record_name.edit_birthday(commands[2])

                if len(commands) >= 4:
                    record_name.edit_email(commands[3])

                if len(commands) == 5:
                    record_name.edit_address(commands[4])

            # Оновити конкретне поле, якщо вказано
            else:
                if field == 'name':
                    record_name.edit_name(data)
                elif field == 'phone':
                    record_name.edit_phone(data)
                elif field == 'birthday':
                    record_name.edit_birthday(data)
                elif field == 'email':
                    record_name.edit_email(data)
                elif field == 'address':
                    record_name.edit_address(data)
                else:
                    raise ValueError("Invalid field name for editing")

            Serialization.save_to_file(self.records, self.filename)

            return True

        except ValueError:
            raise ValueError("Invalid data for editing\nExample: name;phone;birthday;email;address, or a single one")

    def get_upcoming_birthday_contacts(self, days):
        upcoming_birthdays = []
        for record in self.records:
            days_to_birthday = record.birthday.days_to_birthday() if record.birthday else ''
            if days_to_birthday == int(days):
                upcoming_birthdays.append(record)
        if not upcoming_birthdays:
            raise ValueError(f"Nothing found!")
        return upcoming_birthdays
