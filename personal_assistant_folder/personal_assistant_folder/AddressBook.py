from collections import UserDict
from Record import Record


class AddressBook(UserDict):

    def add_record(self, user_input):
        '''
        тут введений нпут може містити тільки значення, від двох до п'яти, котрі записуються в record,
        порядок наступний: name, phone, далі ключові аргументи, котрі за замовчуванням = None: birthday, email, address.
        '''
        commands = user_input.strip().split(' ')
        min_length = 2
        max_length = 5
        if not (min_length <= len(commands) <= max_length):
            raise ValueError('Enter correct info to add a record')

        name, phone, *args = commands  # Розпакування перших двох значень та всіх інших у змінну args

        try:
            self.data[name] = Record(name, phone, *args)
        except ValueError:
            pass

    def find_record(self, searching_str: str):
        pass
