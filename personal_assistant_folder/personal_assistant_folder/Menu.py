import os
from personal_assistant_folder.sorting_files.Sorting import Sorting
from personal_assistant_folder.Pagination import Paginator

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
    "6. Find contacts with birthdays",
    "7. Exit"
]
menu_single_contact = [
    "*** Edit Contact Menu ***",
    "1. Edit all",
    "2. Name",
    "3. Phone",
    "4. Email",
    "5. Address",
    "6. Birthday",
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
    "*** Edit Note Menu ***",
    "1. Edit all",
    "2. Title",
    "3. Content",
    "4. Tags",
    "5. Exit"
]


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
    input('Press enter to continue...')


def print_menu_items(list) -> None:
    print("------------------")
    for item in list:
        print(item)
    print("------------------")
    print()


def record_paginator(paginator):
    while True:
        clear_console()
        current_page = next(paginator)
        message = f'Page {paginator.current_page} from {paginator.total_pages} pages'
        print(message)
        print()
        for item in current_page:
            print(item)
            print('-----------------')
        print()
        print(message)
        print()
        action = input("Enter 'p' - prev page, 'n' - next page, 'q' - for exit: ").lower()
        if action == 'q':
            break
        paginator.move(action)


def submenu_addressbook(addressbook, items_per_page):
    """
    Submenu for AddressBook
    """
    while True:
        # SubMenu AddressBook
        clear_console()
        print_menu_items(menu_addressbook)

        choice2 = input("Choose an item: ")
        # Find Contact
        if choice2 == "1":
            clear_console()

            try:
                command = input("Enter info: ")
                contacts = addressbook.find_records(command)
                if contacts:
                    notes_paginator = Paginator(contacts, items_per_page)
                    record_paginator(notes_paginator)
            except ValueError as e:
                print(e)

            wait_to_continue()
        # Add contact
        elif choice2 == "2":
            clear_console()
            print('Example: name;phone;birthday;email;address')

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

                choose_record = input('Enter Title: ')
                current_record = addressbook.find_record(choose_record)
                print()
                print(current_record)
                print()
                print_menu_items(menu_single_contact)

                choice3 = input("Choose an item: ")

                if choice3 == "1":
                    clear_console()
                    try:
                        print('Edit whole Contact')
                        print('Example: name;phone;birthday;email;address')
                        command = input("Enter info: ")
                        addressbook.edit_record(current_record, command)
                    except ValueError as e:
                        print(e)
                    wait_to_continue()
                elif choice3 == "2":
                    clear_console()
                    try:
                        print('Edit Name')
                        command = input("Enter Name: ")
                        addressbook.edit_record(current_record, command, 'name')
                    except ValueError as e:
                        print(e)
                    wait_to_continue()
                elif choice3 == "3":
                    clear_console()
                    try:
                        print('Edit Phone')
                        command = input("Enter phone: ")
                        addressbook.edit_record(current_record, command, 'phone')
                    except ValueError as e:
                        print(e)
                    wait_to_continue()
                elif choice3 == "4":
                    clear_console()
                    try:
                        print('Edit Email')
                        command = input("Enter email: ")
                        addressbook.edit_record(current_record, command, 'email')
                    except ValueError as e:
                        print(e)
                    wait_to_continue()
                elif choice3 == "5":
                    clear_console()
                    try:
                        print('Edit Address')
                        command = input("Enter address: ")
                        addressbook.edit_record(current_record, command, 'address')
                    except ValueError as e:
                        print(e)
                    wait_to_continue()
                elif choice3 == "6":
                    clear_console()
                    try:
                        print('Edit Birthday')
                        command = input("Enter birthday date (dd.mm.yyyy): ")
                        addressbook.edit_record(current_record, command, 'birthday')
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
                records_by_pages = Paginator(addressbook.records, items_per_page)
                record_paginator(records_by_pages)
            except ValueError as e:
                print(e)

        elif choice2 == "6":
            clear_console()

            try:
                command = input("Enter count days: ")
                contacts = addressbook.get_upcoming_birthday_contacts(command)

                records_by_pages = Paginator(contacts, items_per_page)
                record_paginator(records_by_pages)
            except ValueError as e:
                print(e)

            wait_to_continue()

        elif choice2 == "7":
            clear_console()
            break
        else:
            invalid_type()


def submenu_notes(noteslist, items_per_page):
    while True:
        clear_console()
        print_menu_items(menu_noteslist)

        choice2 = input("Choice item: ")
        # Find Note(s)
        if choice2 == "1":
            clear_console()
            try:
                command = input("Find note(s): ")
                if command.startswith('#'):
                    notes = noteslist.find_sort(command)
                else:
                    notes = noteslist.find_notes(command)

                if notes:
                    notes_paginator = Paginator(notes, items_per_page)
                    record_paginator(notes_paginator)

            except ValueError as e:
                print(e)

            wait_to_continue()
        # Add Note
        elif choice2 == "2":
            clear_console()
            print('Example: title;content;#tag1,#tag2')

            try:
                command = input("Enter info: ")
                noteslist.add(command)
            except ValueError as e:
                print(e)

            print(f"Note was saved")
            wait_to_continue()

        # Edit Note
        elif choice2 == "3":

            while True:
                clear_console()

                choose_note = input('Enter title: ')
                current_note = noteslist.find_note(choose_note)
                print()
                print(current_note)
                print()
                print_menu_items(menu_single_note)

                choice3 = input("Choose an item: ")

                if choice3 == "1":
                    clear_console()
                    try:
                        print('Edit whole Note')
                        print('Example: title;content;#tag1,#tag2')
                        command = input("Enter info: ")
                        noteslist.edit_note(current_note, command)
                    except ValueError as e:
                        print(e)
                    wait_to_continue()
                elif choice3 == "2":
                    clear_console()
                    try:
                        print('Edit Title')
                        command = input("Enter Title: ")
                        noteslist.edit_note(current_note, command, 'title')
                    except ValueError as e:
                        print(e)
                    wait_to_continue()
                elif choice3 == "3":
                    clear_console()
                    try:
                        print('Edit Content')
                        command = input("Enter content: ")
                        noteslist.edit_note(current_note, command, 'content')
                    except ValueError as e:
                        print(e)
                    wait_to_continue()
                elif choice3 == "4":
                    clear_console()
                    try:
                        print('Edit Tags')
                        command = input("Enter content: ")
                        noteslist.edit_note(current_note, command, 'tags')
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
                notes_paginator = Paginator(noteslist.noteslist, items_per_page)
                record_paginator(notes_paginator)
            except ValueError as e:
                print(e)

        elif choice2 == "6":
            clear_console()
            break
        else:
            invalid_type()


def submenu_sorting():
    """
    SubMenu for Sorting files in folder
    """
    while True:
        clear_console()

        print("--------------------")
        print("Sort files in folder")
        print("--------------------")
        print()

        choice2 = input("Folder path (or 'exit / q'): ")

        if choice2.lower() in ["exit", 'q']:
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


def show_menu(addressbook, noteslist, items_per_page):
    while True:
        clear_console()
        print_menu_items(menu_main)

        choice1 = input("Where are you want to start: ")
        # AddressBook Menu
        if choice1 == "1":
            submenu_addressbook(addressbook, items_per_page)

        # SubMenu Notes
        elif choice1 == "2":
            submenu_notes(noteslist, items_per_page)

        # SubMenu Sorting Files
        elif choice1 == "3":
            submenu_sorting()

        # Close App
        elif choice1 == "4":
            clear_console()
            print('See you later!')
            break
        # Invalid command
        else:
            invalid_type()
