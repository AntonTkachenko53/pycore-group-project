from Menu import show_menu
from AddressBook import AddressBook
from NotesList import NotesList

"""
PythonCore 17 group №6 personal assistant project
"""

# BASE CONCTANTS
FILE_CONTACTS = 'contacts.bin'
FILE_NOTES = 'notes.bin'
ITEMS_PER_PAGE = 10

# Initializing objects
addressbook = AddressBook(FILE_CONTACTS)
noteslist = NotesList(FILE_NOTES)

# Start menu
show_menu(addressbook, noteslist, ITEMS_PER_PAGE)
