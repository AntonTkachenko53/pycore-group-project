"""
PythonCore 17 group №6 personal assistant project
"""
import json


class Contact:
    def __init__(self, name, address, phone_number, email, birthday):
        self.name = name
        self.address = address
        self.phone_number = phone_number
        self.email = email
        self.birthday = birthday

    def __str__(self):
        return f"Name: {self.name}\nAddress: {self.address}\nPhone: {self.phone_number}\nEmail: {self.email}\nBirthday: {self.birthday}"


contacts = []

try:
    with open("contacts.json", "r") as file:
        contacts_data = json.load(file)
        for contacts_data in contacts_data:
            contact = Contact(**contacts_data)
            contacts.append(contact)
except FileNotFoundError:
    print("File 'contacts.json' not found. Try adding contacts.")

if contacts:
    print("Contact list:\n")
    for contact in contacts:
        print(contact)
else:
    print("Contact list empty.")
