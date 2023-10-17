from Record import Record
from Pagination import Paginator


class AddressBook:
    MIN_LENGTH_ADD = 2
    MAX_LENGTH_ADD = 5

    def __init__(self):
        self.records = list()

    def add_record(self, user_input):
        '''
        тут введений інпут може містити тільки значення, від двох до п'яти, котрі записуються в record,
        порядок наступний: name, phone, далі ключові аргументи, котрі за замовчуванням = None: birthday, email, address.
        '''
        commands = user_input.strip().split(' ')
        if not (self.MIN_LENGTH_ADD <= len(commands) <= self.MAX_LENGTH_ADD):
            raise ValueError('Enter correct info to add a record')

        name, phone, *args = commands  # Розпакування перших двох значень та всіх інших у змінну args

        for record in self.records:
            if name == record.name._value:
                raise ValueError('Contact with this name already exists')

        try:
            contact = Record(name, phone, *args)
            self.records.append(contact)
        except ValueError:
            raise ValueError('Invalid info to create a record')

    def find_record(self, searching_str: str):
        result = [
            record for record in self.records if
            searching_str in f"{record.name._value} {record.phone._value} "
                             f"{record.birthday._value} {record.email._value} {record.address._value}"
        ]
        return result

    def delete_record(self, record_to_delete: str):
        for record in self.records:
            if record_to_delete == record.name._value:
                self.records.remove(record)

    def show_all_by_pages(self, command, num_of_records=5):
        if command in ['n', 'p', 'q']:
            try:
                paginator = Paginator(self.records, num_of_records)
                current_page = next(paginator)
                paginator.move(command)
            except StopIteration:
                raise StopIteration('Showing stopped: quit called or end of records')
        else:
            raise ValueError('Invalid command.')
