from collections import UserDict
from Record import Record


class AddressBook(UserDict):

    def add_record(self, user_input):  # Інпут може місти від двох до п'яти значень, котрі записуються в record
        commands = user_input.strip().split(', ')
        min_length = 2
        max_length = 
        if len(commands)