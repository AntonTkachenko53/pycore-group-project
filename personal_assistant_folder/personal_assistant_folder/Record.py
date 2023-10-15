from Address import Address
from Email import Email
from Name import Name
from Phone import Phone
from Birthday import Birthday

class Record:
    def __init__(self, name, phone, birthday=None, email=None, address=None):
        self.name = Name(name)
        self.phones = Phone(phone)
        self.birthday = Birthday(birthday) if birthday else None
        self.email = Email(email) if email else None
        self.address = Address(address) if address else None

    def add(self):
        pass

    def remove(self):
        pass

    def edit(self):
        pass