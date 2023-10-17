from Menu import show_menu
from AddressBook import AddressBook
from NotesList import NotesList

"""
PythonCore 17 group №6 personal assistant project
"""

FILE_CONTACTS = 'contacts.bin'
FILE_NOTES = 'notes.bin'
ITEMS_PER_PAGE = 10

addressbook = AddressBook(FILE_CONTACTS)
noteslist = NotesList(FILE_NOTES)

i = 1
while i <= 150:
    noteslist.add(f'title_{i};content content content;#tag_{i},#tag_{i+1},#tag_{i-1}')
    i += 1

i = 1
while i <= 30:
    addressbook.add_record(f'Name_{i};0000000000;20.01.1900;email@mail.loc;Some address 1')
    i += 1

show_menu(addressbook, noteslist, ITEMS_PER_PAGE)
