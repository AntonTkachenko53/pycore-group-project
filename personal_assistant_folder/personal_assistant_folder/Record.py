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

    def add(self, info, value):
        if info == "phone":
            self.phones = Phone(value)  # Оновіть об'єкт Phone замість створення списку
        elif info == "email":
            self.email = Email(value)
        elif info == "address":
            self.address = Address(value)

    def remove(self, info):
        if info == "email":
            self.email = None
        elif info == "address":
            self.address = None

    def edit(self, info, value):
        if info == "phone":
            self.phones.number = value
        elif info == "email":
            self.email = Email(value)
        elif info == "address":
            self.address = Address(value)
