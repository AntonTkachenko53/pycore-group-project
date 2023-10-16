import os
from sorting_files.Sorting import Sorting
from AddressBook import AddressBook
from NotesList import NotesList

"""
PythonCore 17 group №6 personal assistant project
"""

class ConsoleManager:
    @staticmethod
    def clear_console():
        if os.name == 'nt':  # Windows
            os.system('cls')
        else:  # MacOS и Linux
            os.system('clear')


def invalid_type():
    ConsoleManager.clear_console()
    print("Invalid choice. try again.")

menu_main = ["*** Menu ***", "1. AddressBook", "2. Notes", "3. Sorting Files", "4. Exit"]
menu_addressbook = ["*** AddressBook Menu ***", "1. Find", "2. Add", "3. Edit", "4. Delete", "5. Show All", "6. Exit"]
menu_single_contact = ["*** Edit Contact Menu ***", "1. Name", "2. Phone", "3. Email", "4. Address", "5. Birthday", "6. Edit all contact", "7. Exit"]
menu_noteslist = ["*** NotesList Menu ***", "1. Find", "2. Add", "3. Edit", "4. Delete", "5. Show All", "6. Exit"]
menu_single_note = ["*** Edit Contact Menu ***", "1. Title", "2. Content", "3. Tags", "4. Edit all", "5. Exit"]

def print_menu_items(list):
    for item in list:
        print(item)



while True:
    ConsoleManager.clear_console()
    print("------------------")
    print_menu_items(menu_main)
    print("------------------")

    choice1 = input("Where are you want to start: ")

    if choice1 == "1":
        ConsoleManager.clear_console()
        while True:
            ConsoleManager.clear_console()
            print("------------------")
            print_menu_items(menu_addressbook)
            print("------------------")

            choice2 = input("Choose an item: ")

            if choice2 == "1":
                ConsoleManager.clear_console()
                command = input("Enter info: ")
                print(f"Contact with info: {command}")
                print()
                input('Press enter to continue')
            elif choice2 == "2":
                ConsoleManager.clear_console()
                print('Add Contact.')
                print('Example: name phone email address birthday')
                command = input("Enter info: ")
                print(f"You wrote: {command}")
                print()
                input('Press enter to continue')
            elif choice2 == "3":
                ConsoleManager.clear_console()

                while True:
                    ConsoleManager.clear_console()
                    print("------------------")
                    print_menu_items(menu_single_contact)
                    print("------------------")

                    choice3 = input("Choose an item: ")

                    if choice3 == "1":
                        ConsoleManager.clear_console()
                        command = input("Enter name: ")
                        print(f"New name: {command}")
                        print()
                        input('Press enter to continue')
                    elif choice3 == "2":
                        ConsoleManager.clear_console()
                        command = input("Enter phone: ")
                        print(f"New phone: {command}")
                        print()
                        input('Press enter to continue')
                    elif choice3 == "3":
                        ConsoleManager.clear_console()
                        command = input("Enter email: ")
                        print(f"New email: {command}")
                        print()
                        input('Press enter to continue')
                    elif choice3 == "4":
                        ConsoleManager.clear_console()
                        command = input("Enter address: ")
                        print(f"New address: {command}")
                        print()
                        input('Press enter to continue')
                    elif choice3 == "5":
                        ConsoleManager.clear_console()
                        command = input("Enter birthday: ")
                        print(f"New birthday: {command}")
                        print()
                        input('Press enter to continue')
                    elif choice3 == "6":
                        ConsoleManager.clear_console()
                        print('Add Contact.')
                        print('Example: name phone email address birthday')
                        command = input("Enter info: ")
                        print(f"You wrote: {command}")
                        print()
                        input('Press enter to continue')
                    elif choice3 == "7":
                        ConsoleManager.clear_console()
                        break
                    else:
                        invalid_type()

            elif choice2 == "4":
                ConsoleManager.clear_console()
                command = input("Delete contact: ")
                print(f"{command} deleted")
                print()
                input('Press enter to continue')
            elif choice2 == "5":
                ConsoleManager.clear_console()
                print(f"Contacts List")
                print()
                input('Press enter to continue')
            elif choice2 == "6":
                ConsoleManager.clear_console()
                break
            else:
                invalid_type()

    elif choice1 == "2":
        ConsoleManager.clear_console()
        while True:
            ConsoleManager.clear_console()
            print("------------------")
            print_menu_items(menu_noteslist)
            print("------------------")

            choice2 = input("Choice item: ")

            if choice2 == "1":
                ConsoleManager.clear_console()
                command = input("Enter Title: ")
                print(f"Note with title: {command}")
                print()
                input('Press enter to continue')
            elif choice2 == "2":
                ConsoleManager.clear_console()
                print('Edit whole Note')
                print('Example: title;content;#tag1,#tag2')
                command = input("Enter info: ")
                print(f"You wrote: {command}")
                print()
                input('Press enter to continue')
            elif choice2 == "3":
                ConsoleManager.clear_console()

                while True:
                    ConsoleManager.clear_console()
                    print("------------------")
                    print_menu_items(menu_single_note)
                    print("------------------")

                    choice3 = input("Choose an item: ")

                    if choice3 == "1":
                        ConsoleManager.clear_console()
                        command = input("Enter title: ")
                        print(f"New title: {command}")
                        print()
                        input('Press enter to continue')
                    elif choice3 == "2":
                        ConsoleManager.clear_console()
                        command = input("Enter content: ")
                        print(f"New content: {command}")
                        print()
                        input('Press enter to continue')
                    elif choice3 == "3":
                        ConsoleManager.clear_console()
                        command = input("Enter tags: ")
                        print(f"New tags: {command}")
                        print()
                        input('Press enter to continue')
                    elif choice3 == "4":
                        ConsoleManager.clear_console()
                        print('Edit whole Note')
                        print('Example: title;content;#tag1,#tag2')
                        command = input("Enter info: ")
                        print(f"You wrote: {command}")
                        print()
                        input('Press enter to continue')
                    elif choice3 == "5":
                        ConsoleManager.clear_console()
                        break
                    else:
                        invalid_type()

            elif choice2 == "4":
                ConsoleManager.clear_console()
                command = input("Delete note: ")
                print(f"{command} deleted")
                print()
                input('Press enter to continue')
            elif choice2 == "5":
                ConsoleManager.clear_console()
                print(f"Notes List")
                print()
                input('Press enter to continue')
            elif choice2 == "6":
                ConsoleManager.clear_console()
                break
            else:
                invalid_type()

    elif choice1 == "3":
        ConsoleManager.clear_console()
        while True:
            ConsoleManager.clear_console()
            print("------------------")
            print("Sort files in folder")
            print("------------------")

            choice2 = input("Folder path (or 'exit'): ")

            if choice2 == "exit":
                ConsoleManager.clear_console()
                break
            else:
                ConsoleManager.clear_console()
                sorting = Sorting(choice2)
                sorting.sort()
                print('Finish')
                break

    elif choice1 == "4":
        ConsoleManager.clear_console()
        print('See you later!')
        break
    else:
        invalid_type()