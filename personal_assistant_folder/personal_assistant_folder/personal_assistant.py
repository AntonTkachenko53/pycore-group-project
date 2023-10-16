import os
from sorting_files.Sorting import Sorting
from AddressBook import AddressBook
from NotesList import NotesList
from Serialization import Serialization
from Pagination import Paginator

"""
PythonCore 17 group №6 personal assistant project
"""

FILE_CONTACTS = 'contacts.bin'
FILE_NOTES = 'notes.bin'

menu_main = [
    "*** Menu ***",
    "1. AddressBook",
    "2. Notes",
    "3. Sorting Files",
    "4. Exit"
]
menu_addressbook = [
    "*** AddressBook Menu ***",
    "1. Find",
    "2. Add",
    "3. Edit",
    "4. Delete",
    "5. Show All",
    "6. Exit"
]
menu_single_contact = [
    "*** Edit Contact Menu ***",
    "1. Name",
    "2. Phone",
    "3. Email",
    "4. Address",
    "5. Birthday",
    "6. Edit all contact",
    "7. Exit"
]
menu_noteslist = [
    "*** NotesList Menu ***",
    "1. Find",
    "2. Add",
    "3. Edit",
    "4. Delete",
    "5. Show All",
    "6. Exit"
]
menu_single_note = [
    "*** Edit Contact Menu ***",
    "1. Title",
    "2. Content",
    "3. Tags",
    "4. Edit all",
    "5. Exit"
]


# addressbook = AddressBook(FILE_CONTACTS)
# noteslist = NotesList(FILE_NOTES)

# Очистка консоли при переходе между разделами меню
def clear_console():
    if os.name == 'nt':  # Windows
        os.system('cls')
    else:  # MacOS и Linux
        os.system('clear')


def invalid_type():
    clear_console()
    print("Invalid choice. try again.")


def wait_to_continue():
    print()
    input('Press enter to continue')


def print_menu_items(list: list) -> None:
    print("------------------")
    for item in list:
        print(item)
    print("------------------")
    print()


while True:
    clear_console()
    print_menu_items(menu_main)

    choice1 = input("Where are you want to start: ")
    # AddressBook Menu
    if choice1 == "1":
        clear_console()
        while True:
            clear_console()
            print_menu_items(menu_addressbook)

            choice2 = input("Choose an item: ")
            # Find Contact
            if choice2 == "1":
                clear_console()

                try:
                    command = input("Enter info: ")
                    contacts = addressbook.find_record(command)
                    if contacts:
                        for contact in contacts:
                            print(contact)
                except ValueError as e:
                    print(e)

                wait_to_continue()
            # Add contact
            elif choice2 == "2":
                clear_console()
                print('Example: name phone email address birthday')

                try:
                    command = input("Enter info: ")
                    addressbook.add_record(command)
                except ValueError as e:
                    print(e)

                wait_to_continue()

            # Edit contact
            elif choice2 == "3":

                while True:
                    clear_console()
                    print_menu_items(menu_single_contact)

                    choice3 = input("Choose an item: ")

                    if choice3 == "1":
                        clear_console()

                        try:
                            command = input("Enter name: ")
                            print(f"New name: {command}")
                        except ValueError as e:
                            print(e)

                        wait_to_continue()
                    elif choice3 == "2":
                        clear_console()

                        try:
                            command = input("Enter phone: ")
                            print(f"New phone: {command}")
                        except ValueError as e:
                            print(e)

                        wait_to_continue()
                    elif choice3 == "3":
                        clear_console()

                        try:
                            command = input("Enter email: ")
                            print(f"New email: {command}")
                        except ValueError as e:
                            print(e)

                        wait_to_continue()
                    elif choice3 == "4":
                        clear_console()

                        try:
                            command = input("Enter address: ")
                            print(f"New address: {command}")
                        except ValueError as e:
                            print(e)

                        wait_to_continue()
                    elif choice3 == "5":
                        clear_console()

                        try:
                            command = input("Enter birthday: ")
                            print(f"New birthday: {command}")
                        except ValueError as e:
                            print(e)

                        wait_to_continue()
                    elif choice3 == "6":
                        clear_console()

                        try:
                            print('Example: name phone email address birthday')
                            command = input("Enter info: ")
                            print(f"You wrote: {command}")
                        except ValueError as e:
                            print(e)

                        wait_to_continue()
                    elif choice3 == "7":
                        clear_console()
                        break
                    else:
                        invalid_type()
            # Delete contact
            elif choice2 == "4":
                clear_console()

                try:
                    command = input("Delete (contact name): ")
                    addressbook.delete_record(command)
                except ValueError as e:
                    print(e)

                wait_to_continue()
            # Show all
            elif choice2 == "5":
                clear_console()

                try:
                    notes_paginator = Paginator(addressbook)
                    for page in notes_paginator:
                        for record in page:
                            print(record)
                        input('Press Enter to show the next page...')
                except ValueError as e:
                    print(e)

                wait_to_continue()
            elif choice2 == "6":
                clear_console()
                break
            else:
                invalid_type()

    # Notes Menu
    elif choice1 == "2":
        while True:
            clear_console()
            print_menu_items(menu_noteslist)

            choice2 = input("Choice item: ")
            # Find Note(s)
            if choice2 == "1":
                clear_console()
                try:
                    command = input("Find note(s): ")
                    # TODO: Доработать когда обновлюсь с MAIN
                    # if command.startswith('#'):
                    #     notes = noteslist.find_sort(command)
                    # else:
                    # TODO: next line move right after uncomment
                    notes = noteslist.find_note(command)

                    if notes:
                        for note in notes:
                            print(note)

                except ValueError as e:
                    print(e)

                wait_to_continue()
            # Add Note
            elif choice2 == "2":
                clear_console()
                print('Example: title;content;#tag1,#tag2')

                try:
                    command = input("Enter info: ")
                    note = noteslist.add(command)
                except ValueError as e:
                    print(e)

                print(f"Note was saved")
                wait_to_continue()

            # Edit Note
            elif choice2 == "3":
                # TODO: пересмотреть механику редактирования
                while True:
                    clear_console()
                    print_menu_items(menu_single_note)

                    choice3 = input("Choose an item: ")

                    if choice3 == "1":
                        clear_console()
                        try:
                            command = input("Enter title: ")
                            print(f"New title: {command}")
                        except ValueError as e:
                            print(e)
                        wait_to_continue()
                    elif choice3 == "2":
                        clear_console()
                        try:
                            command = input("Enter content: ")
                            print(f"New content: {command}")
                        except ValueError as e:
                            print(e)
                        wait_to_continue()
                    elif choice3 == "3":
                        clear_console()
                        try:
                            command = input("Enter tags: ")
                            print(f"New tags: {command}")
                        except ValueError as e:
                            print(e)
                        wait_to_continue()
                    elif choice3 == "4":
                        clear_console()
                        try:
                            print('Edit whole Note')
                            print('Example: title;content;#tag1,#tag2')
                            command = input("Enter info: ")
                            print(f"You wrote: {command}")
                        except ValueError as e:
                            print(e)
                        wait_to_continue()
                    elif choice3 == "5":
                        clear_console()
                        break
                    else:
                        invalid_type()

            # Delete Note
            elif choice2 == "4":
                clear_console()

                try:
                    command = input("Write Title: ")
                    noteslist.delete(command)
                except ValueError as e:
                    print(e)

                print(f"Note was deleted")

                wait_to_continue()

            elif choice2 == "5":
                clear_console()

                try:
                    notes_paginator = Paginator(noteslist)
                    for page in notes_paginator:
                        for record in page:
                            print(record)
                        input('Press Enter to show the next page...')
                except ValueError as e:
                    print(e)

                wait_to_continue()
            elif choice2 == "6":
                clear_console()
                break
            else:
                invalid_type()
    # Sorting Files
    elif choice1 == "3":
        while True:
            clear_console()

            print("--------------------")
            print("Sort files in folder")
            print("--------------------")
            print()

            choice2 = input("Folder path (or 'exit'): ")

            if choice2 == "exit":
                clear_console()
                break
            else:
                clear_console()

                try:
                    sorting = Sorting(choice2)
                    sorting.sort()
                except ValueError as e:
                    print(e)

                print('Finish')
                wait_to_continue()
                break
    # Close App
    elif choice1 == "4":
        clear_console()
        print('See you later!')
        break
    else:
        invalid_type()
