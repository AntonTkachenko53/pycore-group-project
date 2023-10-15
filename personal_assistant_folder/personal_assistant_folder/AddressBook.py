from collections import UserDict
from Record import Record
import pickle


class AddressBook(UserDict):
    MIN_LENGTH_ADD = 2
    MAX_LENGTH_ADD = 5

    def add_record(self, user_input):
        """
        тут введений нпут може містити тільки значення, від двох до п'яти, котрі записуються в record,
        порядок наступний: name, phone, далі ключові аргументи, котрі за замовчуванням = None: birthday, email, address.
        """
        commands = user_input.strip().split(' ')
        if not (self.MIN_LENGTH_ADD <= len(commands) <= self.MAX_LENGTH_ADD):
            raise ValueError('Enter correct info to add a record')

        name, phone, *args = commands  # Розпакування перших двох значень та всіх інших у змінну args

        try:
            self.data[name] = Record(name, phone, *args)
        except ValueError:
            pass

    def find_record(self, searching_str: str):
        pass

    def iterator(self, num_of_records=5):
        records = list(self.data.values())
        for i in range(0, len(records), num_of_records):
            yield records[i:i + num_of_records]

    def save_to_file(self, filename='address_book.bin'):
        with open(filename, 'wb') as file:
            pickle.dump(self.data, file)

    def load_from_file(self, filename='address_book.bin'):
        try:
            with open(filename, 'rb') as file:
                self.data = pickle.load(file)
        except FileNotFoundError:
            print(f'File {filename} not found')
