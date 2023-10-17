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

    def add_edit(self, field_name, value):
        try:
            if hasattr(self, field_name):
                setattr(self, field_name, value)
        except ValueError:
            pass

    def remove(self, field_name):
        if field_name in ['name', 'phone']:
            raise ValueError('You can`t delete contact`s name or phone')
        try:
            if hasattr(self, field_name):
                setattr(self, field_name, None)
        except ValueError:
            pass

    def __str__(self):
        return f"Name: {self.name}\nPhone: {self.phone}\nBirthday: {self.birthday}\nEmail: {self.email}\nAddress: {self.address}"
