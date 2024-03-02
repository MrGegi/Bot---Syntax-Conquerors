from classes import AddressBook
import pickle
from utilities import *

address_book = AddressBook()

def add_phone():
    name = input("Enter the contact's name and surename: ")
    phone = input("Enter the phone number: ")
    if name in address_book.contacts:
        if address_book.contacts[name].phone.value:
            print(f"A phone number already exists for the contact {name}.")
        elif address_book.contacts[name].add_phone(phone):
            print(f"Phone number: {phone} added to contact {name}.")
        else:
            print("Failed to add phone number.")
    else:
        print("Contact not found.")

def change_phone_num():
    name = input("Enter the contact's name and surename: ")
    new_phone = input("Enter the new phone number: ")
    if name in address_book.contacts:
        if address_book.contacts[name].change_phone(new_phone):
            print(f"Phone number changed for {name}.")
        else:
            print("Failed to change phone number.")
    else:
        print("Contact not found.")

def delete_phone():
    name = input("Enter the contact's name and surename: ")
    if name in address_book.contacts:
        address_book.contacts[name].delete_phone()
        print(f"Phone number deleted for {name}.")
    else:
        print("Contact not found.")

def save_to_file():
    with open('bot_save.bin', "wb") as fh:
        pickle.dump(address_book, fh)
    print('File has been saved')

def end_program():
    save_to_file()
    print('Good bye')

def input_parser():
    """Function runs in a while loop, takes input from the user and executes appropriate functions."""
    commands = {
        'add phone': add_phone,
        'change phone': change_phone_num,
        'delete phone': delete_phone,
        'save': save_to_file,
        'exit': end_program
}
    command = input('Enter your command: ').lower()

    if command in commands:
        return commands[command]  
    else:
        return unknown_command
