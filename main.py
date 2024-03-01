from classes import *
import pickle

address_book = AddressBook()

def input_error(func):
    """
    Use as decorator @input_error before function to gracefully handle raised exceptions.
    By default, if the raised error is unknown it will gracefully return last __traceback__ line number, exception type and it's string.
    """
    def gracefull_error_handling(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as raised_exception:
            line_number = (lambda traceback: traceback.tb_lineno if not traceback.tb_next else traceback.tb_next.tb_lineno)(raised_exception.__traceback__)
            return f"Unhandled exception >> Line:{line_number} Type:{type(raised_exception).__name__} Str:{str(raised_exception)}"
    return gracefull_error_handling

def test_contacts(address_book: AddressBook):  
    """Function fills up addres book with random contacts for debugging purposes"""

    random_contacts = [
        {'name': 'Zbyszek Kowalski', 'phone': '606505404', 'email': 'zbyszek.kowalski@gmail.com', 'birthday': '1990-5-20'},
        {'name': 'Rychu Nowak', 'phone': '546859652', 'email': 'rychu.nowak@gmail.com', 'birthday': '1995-3-26'},
        # {'name': 'Jan', 'last name': 'Wójcik', 'phone': '524835658', 'email': 'jan.wójcik@gmail.com', 'birthday': '5 9 1965'},
        # {'name': 'Adam', 'last name': 'Kowalczyk', 'phone': '044175272', 'email': 'adam.kowalczyk@yahoo.com', 'birthday': '20 9 1985'},
        # {'name': 'Tomasz', 'last name': 'Wójcik', 'phone': '523544638', 'email': 'tomasz.wójcik@yahoo.com', 'birthday': '3 8 1973'},
        # {'name': 'Tomasz', 'last name': 'Kowalczyk', 'phone': '346595089', 'email': 'tomasz.kowalczyk@yahoo.com', 'birthday': '18 7 1978'},
        # {'name': 'Andrzej', 'last name': 'Kowalski', 'phone': '270767747', 'email': 'andrzej.kowalski@yahoo.com', 'birthday': '6 8 1968'},
        # {'name': 'Adam', 'last name': 'Nowak', 'phone': '587868953', 'email': 'adam.nowak@outlook.com', 'birthday': '1 7 1985'},
        # {'name': 'Adam', 'last name': 'Kowalski', 'phone': '603277494', 'email': 'adam.kowalski@yahoo.com', 'birthday': '17 4 1961'},
        # {'name': 'Tomasz', 'last name': 'Wójcik', 'phone': '114714793', 'email': 'tomasz.wójcik@outlook.com', 'birthday': '5 8 1985'},
        # {'name': 'Andrzej', 'last name': 'Wójcik', 'phone': '819552896', 'email': 'andrzej.wójcik@outlook.com', 'birthday': '24 7 1964'},
        # {'name': 'Andrzej', 'last name': 'Kamiński', 'phone': '497654652', 'email': 'andrzej.kamiński@gmail.com', 'birthday': '3 10 1982'},
        # {'name': 'Adam', 'last name': 'Nowak', 'phone': '133258442', 'email': 'adam.nowak@outlook.com', 'birthday': '23 1 1980'},
        # {'name': 'Tomasz', 'last name': 'Wójcik', 'phone': '313774876', 'email': 'tomasz.wójcik@yahoo.com', 'birthday': '1 1 1962'},
        # {'name': 'Jan', 'last name': 'Wójcik', 'phone': '096489389', 'email': 'jan.wójcik@outlook.com', 'birthday': '4 4 1991'},
        # {'name': 'Piotr', 'last name': 'Kamiński', 'phone': '809172250', 'email': 'piotr.kamiński@outlook.com', 'birthday': '25 8 1963'},
        # {'name': 'Adam', 'last name': 'Nowak', 'phone': '491249850', 'email': 'adam.nowak@outlook.com', 'birthday': '16 5 1965'},
        # {'name': 'Jan', 'last name': 'Kamiński', 'phone': '818690456', 'email': 'jan.kamiński@yahoo.com', 'birthday': '20 7 1995'},
        # {'name': 'Jan', 'last name': 'Kowalski', 'phone': '441151946', 'email': 'jan.kowalski@gmail.com', 'birthday': '30 3 1986'},
        # {'name': 'Piotr', 'last name': 'Kowalczyk', 'phone': '506499840', 'email': 'piotr.kowalczyk@outlook.com', 'birthday': '16 5 1962'}
        ]
    
    for person in random_contacts:
        address_book.add_contact(person['name'])
        address_book.contacts[person['name']].add_phone(person['phone'])
        # address_book.contacts[person['name']].add_birthday(person['birthday'])
    
    for contact_name in address_book.contacts:
        print(f'Name: {address_book.contacts[contact_name].name.value}')
        print(f'Name: {address_book.contacts[contact_name].phone.value}')
      

def add_phone():
    name = input("Enter the contact's name and surename: ")
    phone = input("Enter the phone number: ")
    if name in address_book.contacts:
        if address_book.contacts[name].phone:
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

def find_contact():
    name = input("Enter the contact's name and surename: ")
    if name in address_book.contacts:
        contact = address_book.contacts[name]
        print(f"Name: {contact.name.value}")
        if contact.phone:
            print(f"Phone: {contact.phone.value}")
        else:
            print("No phone number added")
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


def load_from_file():
    try:
        with open('bot_save.bin',"rb") as fh:
            address_book = pickle.load(fh)
            print('The adress_book has been loaded from file')
    except FileNotFoundError:
        print("File with address_book doesn't exist yet!")
    return address_book

def end_program():
    save_to_file()
    print('Good bye')

def add_contact():    
    name = input("Enter the contact's name and surname: ")
    if name in address_book.contacts:
        print("A contact with this name already exists.")
    else:
        try:
            address_book.contacts[name] = Contact(name)
        except Exception as e:
            print(e)
        if name in address_book.contacts:
                print(f"Contact {name} was added.")

def delete_contact():
    name = input("Enter the contact's name and surname you'd like to delete: ")
    if name in address_book.contacts:
        address_book.contacts.pop(name)
        print(f'Contact {name} deleted.')
    else:
        print(f'There is no contact {name}')

def unknown_command():
    print('Unknown command')

def days_to_birthday():
    for contact_name in address_book.contacts:
        countdown = address_book.contacts[contact_name].days_to_birthday
        print(f"{address_book.contacts[contact_name].name.value} was born on {address_book.contacts[contact_name].birthday.value}. {countdown}days left till his birthday.")
    return

def add_note():
    note = input("Enter the text of note: ")
    address_book.notebook.add_note(note)
    # tag = input("Enter tags")

def show_notes():
    print('bbb')
    address_book.notebook.show_notes()


def input_parser():
    """Functions runs in a while loop, takes input from user and returns apropiate functions
    """
    commands = {
    'add contact': add_contact,
    'delete contact': delete_contact,
    'add note': add_note,
    'show notes':show_notes,
    'add phone': add_phone,
    'change phone': change_phone_num,
    # 'show contact': show_contact,
    'delete phone': delete_phone,
    # 'add birthday' : set_birthday,
    'birthday': days_to_birthday,
    # 'show all': show_all,
    'find contact' : find_contact,
    'save': save_to_file,
    'exit': end_program, 
}
    command = input('Enter your command: ').lower()

    if command in commands:
        return commands[command]  
    else:
        return unknown_command

def main():
    address_book = load_from_file()
    test_contacts(address_book)
    while True:
        function_to_execute = input_parser()
        try:
            if function_to_execute == end_program:
                end_program()
                break
            else:
                function_to_execute()
        except:
            continue
           
 
if __name__ == '__main__':
    main()