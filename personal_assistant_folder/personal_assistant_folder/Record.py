from Address import Address
from Email import Email
from Name import Name
from Phone import Phone
from Birthday import Birthday

class Record:
    def __init__(self, name, phone, birthday=None, email=None, address=None):
        self.name = Name(name)
        self.phone = Phone(phone)
        self.birthday = Birthday(birthday) if birthday else None
        self.email = Email(email) if email else None
        self.address = Address(address) if address else None

    def add_edit(self, info, value):
        if info == "phone":
            try:
                self.phone = Phone(value)
            except ValueError:
                pass
        elif info == "email":
            try:
                self.email = Email(value)
            except ValueError:
                pass
        elif info == "name":
            try:
                self.name = Name(value)
            except ValueError:
                pass
        elif info == "birthday":
            try:
                self.birthday = Birthday(value)
            except ValueError:
                pass
        elif info == "address":
            try:
                self.address = Address(value)
            except ValueError:
                pass

    def remove(self, info):
        if info == "email":
            self.email = None
        elif info == "address":
            self.address = None
        elif info == "birthday":
            self.address = None