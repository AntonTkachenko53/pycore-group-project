from personal_assistant_folder.Menu import show_menu
from personal_assistant_folder.AddressBook import AddressBook
from personal_assistant_folder.NotesList import NotesList

"""
PythonCore 17 group №6 personal assistant project
"""

# BASE CONSTANTS
FILE_CONTACTS = 'contacts.bin'
FILE_NOTES = 'notes.bin'
ITEMS_PER_PAGE = 10

# Initializing objects
addressbook = AddressBook(FILE_CONTACTS)
noteslist = NotesList(FILE_NOTES)

# Start menu
show_menu(addressbook, noteslist, ITEMS_PER_PAGE)
