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
        return (f"Name: {self.name}\nPhone: {self.phone}\nBirthday: {self.birthday}\n"
                f"Email: {self.email}\nAddress: {self.address}")
