from collections import UserDict
from Record import Record


class AddressBook(UserDict):

    def add_record(self, name, phone):
        try:
            self.data[name] = Record(name, phone)
        except ValueError:
            pass
