from personal_assistant_folder.Address import Address
from personal_assistant_folder.Email import Email
from personal_assistant_folder.Name import Name
from personal_assistant_folder.Phone import Phone
from personal_assistant_folder.Birthday import Birthday


class Record:
    def __init__(self, name, phone, birthday=None, email=None, address=None):
        self.name = Name(name)
        self.phone = Phone(phone)
        self.birthday = Birthday(birthday) if birthday else None
        self.email = Email(email) if email else None
        self.address = Address(address) if address else None

    def __str__(self):
        return (f"{'Name:'.ljust(10)} {self.name._value}\n"
                f"{'Phone:'.ljust(10)} {self.phone._value}\n"
                f"{'Birthday:'.ljust(10)} {self.birthday._value if self.birthday else None}\n"
                f"{'Email:'.ljust(10)} {self.email._value if self.email else None}\n"
                f"{'Address:'.ljust(10)} {self.address._value if self.address else None}")

    def edit_name(self, value):
        self.name = Name(value)

    def edit_phone(self, value):
        self.phone = Phone(value)

    def edit_birthday(self, value):
        self.birthday = Birthday(value)

    def edit_email(self, value):
        self.email = Email(value)

    def edit_address(self, value):
        self.address = Address(value)