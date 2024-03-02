from classes import *
import pickle
from utilities import *

address_book = load_from_file()
LOGO = """
@@@ @@@ @@@  @@@ @@@ @@@  @@@ @@@ @@@  @@@  @@@ @@@ @@@  @@@ @@@ @@@  @@@ @@@ @@@  @@@     @@@  @@@ @@@ @@@ 
@@@     @@@  @@@          @@@          @@@  @@@              @@@      @@@     @@@  @@@ @   @@@      @@@     
@@@ @@@ @@@  @@@ @@@ @@@  @@@ @@@ @@@  @@@  @@@ @@@ @@@      @@@      @@@ @@@ @@@  @@@ @@@ @@@      @@@     
@@@     @@@          @@@          @@@  @@@          @@@      @@@      @@@     @@@  @@@   @ @@@      @@@     
@@@     @@@  @@@ @@@ @@@  @@@ @@@ @@@  @@@  @@@ @@@ @@@      @@@      @@@     @@@  @@@     @@@      @@@     

                                                                                    by Syntax Conquerors
"""

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
            print(f"Unhandled exception >> Line:{line_number} Type:{type(raised_exception).__name__} Str:{str(raised_exception)}")
            return 
    return gracefull_error_handling

def test_contacts(address_book: AddressBook):  
    """Function fills up addres book with random contacts for debugging purposes"""

    random_contacts = [
        # {'name': 'NAME', 'phone': 'PHONE', 'email': 'EMAIL', 'birthday': 'BIRTHDAY', "address": "ADDRESS"},
        {'name': 'zbyszek kowalski', 'phone': '606505404', 'email': 'zbyszek.kowalski@gmail.com', 'birthday': '1990-5-20'},
        {'name': 'rychu nowak', 'phone': '546859652', 'email': 'rychu.nowak@gmail.com', 'birthday': None},
        {'name': 'adam nowak', 'phone': None, 'email': 'adam.nowak@outlook.com', 'birthday': '1973-1-26'},
        {'name': 'andrzej nowak', 'phone': '998114469', 'email': None, 'birthday': '1993-4-2'},
        # {'name': 'adam kowalski', 'phone': '550483921', 'email': 'adam.kowalski@outlook.com', 'birthday': '1966-3-3'},
        # {'name': 'jan kamiński', 'phone': '222035333', 'email': 'jan.kamiński@yahoo.com', 'birthday': '1981-5-3'},
        # {'name': 'tomasz kamiński', 'phone': '070003125', 'email': 'tomasz.kamiński@outlook.com', 'birthday': '1991-7-16'},
        # {'name': 'jan wójcik', 'phone': '821817242', 'email': 'jan.wójcik@outlook.com', 'birthday': '1990-3-19'},
        # {'name': 'jan kowalczyk', 'phone': '949533885', 'email': 'jan.kowalczyk@yahoo.com', 'birthday': '1994-7-24'},
        # {'name': 'piotr kowalczyk', 'phone': '860425088', 'email': 'piotr.kowalczyk@outlook.com', 'birthday': '1994-10-22'},
        # {'name': 'adam kowalski', 'phone': '929106345', 'email': 'adam.kowalski@outlook.com', 'birthday': '1997-5-3'},
        # {'name': 'tomasz kamiński', 'phone': '425074571', 'email': 'tomasz.kamiński@gmail.com', 'birthday': '1997-3-21'},
        # {'name': 'jan nowak', 'phone': '433071736', 'email': 'jan.nowak@yahoo.com', 'birthday': '1965-7-16'},
        # {'name': 'tomasz kowalczyk', 'phone': '172823343', 'email': 'tomasz.kowalczyk@outlook.com', 'birthday': '1965-6-26'},
        # {'name': 'adam kowalski', 'phone': '445123820', 'email': 'adam.kowalski@gmail.com', 'birthday': '1974-6-25'},
        # {'name': 'adam kowalczyk', 'phone': '129125052', 'email': 'adam.kowalczyk@yahoo.com', 'birthday': '1987-5-10'},
        # {'name': 'andrzej wójcik', 'phone': '981967451', 'email': 'andrzej.wójcik@yahoo.com', 'birthday': '1992-1-5'},
        # {'name': 'andrzej kowalski', 'phone': '336976595', 'email': 'andrzej.kowalski@outlook.com', 'birthday': '1966-12-13'},
        # {'name': 'tomasz kowalczyk', 'phone': '172712416', 'email': 'tomasz.kowalczyk@yahoo.com', 'birthday': '1991-5-26'},
        # {'name': 'adam kowalczyk', 'phone': '358341124', 'email': 'adam.kowalczyk@outlook.com', 'birthday': '1966-5-18'},
        ]

    for person in random_contacts:
        address_book.add_contact(person['name'])
        address_book.contacts[person['name']].add_phone(person['phone'])
        address_book.contacts[person['name']].add_email(person['email'])
        address_book.contacts[person['name']].add_birthday(person['birthday'])

    # for contact_name in address_book.contacts:
    #     print(f'Name: {address_book.contacts[contact_name].name.value}', end="  ")
    #     print(f'Phone: {address_book.contacts[contact_name].phone.value}', end="  ")
    #     print(f'Email: {address_book.contacts[contact_name].email.value}', end="  ")
    #     print(f'Birthday: {address_book.contacts[contact_name].birthday.value}')
      

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

def find_contact():
    contact_name = input("Enter the contact's name and surename: ")
    if contact_name in address_book.contacts:
        print(f'Name: {address_book.contacts[contact_name].name.value}', end="  ")
        print(f'Phone: {address_book.contacts[contact_name].phone.value}', end="  ")
        print(f'Birthday: {address_book.contacts[contact_name].birthday.value}', end="  ")
        print(f'Email: {address_book.contacts[contact_name].email.value}')
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

def set_birthday():
    name = input("Enter the contact's name and surename: ").lower()
    if name in address_book.contacts:
        if not address_book.contacts[name].birthday.value:
            while True:
                year = input("Enter the contact's year of birth: ")
                month = input("Enter the contact's month of birth: ")
                day = input("Enter the contact's day of birth: ")
                try:
                    year = int(year)
                    month = int(month)
                    day = int(day)
                    date = datetime(year, month, day)
                    birthday_to_add = date.strftime('%Y-%m-%d')
                    break
                except ValueError:
                    print("Invalid data. Please enter a valid date.")
            address_book.contacts[name].add_birthday(birthday_to_add)
            print(f"Birthday date ({birthday_to_add}) added to contact {name}")
        else:
            print(f"Contact {name} already has birthday date set to {address_book.contacts[name].birthday.value}.")
    else:
        print("Contact not found.")

def days_to_birthday():
    for contact_name in address_book.contacts:
        countdown = address_book.contacts[contact_name].days_to_birthday
        print(f"{address_book.contacts[contact_name].name.value} was born on {address_book.contacts[contact_name].birthday.value}. {countdown}days left till his birthday.")
    return

def show_all():
    width = 154
    print("\n+" + "-" * width + "+")
    print('|{:^30}|{:^30}|{:^30}|{:^30}|{:^30}|'.format("NAME", "PHONE", "EMAIL", "BIRHDAY", "ADDRESS"))
    print("+" + "-" * width + "+")
    for contact_name in address_book.contacts:
        contact = address_book.contacts[contact_name]
        format_value = lambda x: x if x is not None else "---"
        print('|{:^30}'.format(format_value(contact.name.value)), end="")
        print('|{:^30}'.format(format_value(contact.phone.value)), end="")
        print('|{:^30}'.format(format_value(contact.email.value)), end="")
        print('|{:^30}'.format(format_value(contact.birthday.value)), end="")
        print('|{:^30}|'.format(format_value(contact.address.value)), end="\n")
    print("+" + "-" * width + "+\n")

def add_email():
    name = input("Enter the contact's name and surname: ")
    if not name in address_book.contacts:
        print(f'There is no contact {name}')
        return
    email = input("Enter the email: ")
    try:
        address_book.contacts[name].add_email(email)
        if address_book.contacts[name].email.value:
            print(f"{email} was added to contact {name}.")
    except:
        return
    
def change_email():
    name = input("Enter the contact's name and surname: ")
    if not name in address_book.contacts:
        print(f'There is no contact {name}')
        return
    if not address_book.contacts[name].email.value:
        print(f"Contact {name} doesnt have a email yet. However we can proceed.")
    email = input("Enter the email: ")
    try:
        address_book.contacts[name].add_email(email)
        if address_book.contacts[name].email.value == email:
            print(f"{email} was changed for contact {name}.")
    except:
        return
    
def delete_email():
    name = input("Enter the contact's name and surname: ")
    if not name in address_book.contacts:
        print(f'There is no contact {name}')
        return
    address_book.contacts[name].remove_email()
    print(f'Email deleted')


def add_note():
    note = input("Enter the note text: ")
    address_book.notebook.add_note(note)
    # tag = input("Enter tags")

def show_notes():
    print('List of notes: \n', address_book.notebook.show_notes())

def edit_note():
    if not address_book.notebook.data:
        print('Notebook is empty')
    else:
        show_notes()
        num_of_note = input('Enter number of note: ')
        address_book.notebook.edit_note(num_of_note)

def remove_note():
    if not address_book.notebook.data:
        print('Notebook is empty')
    else:
        show_notes()
        num_of_note = input('Enter number of note or write "all" to remove all notes: ')
        address_book.notebook.remove_note(num_of_note)


def input_parser():
    """Functions runs in a while loop, takes input from user and returns apropiate functions
    """
    commands = {
    'add contact': add_contact,
    'delete contact': delete_contact,
    'add note': add_note,
    'show notes':show_notes,
    'edit note': edit_note,
    'remove note': remove_note,
    'add phone': add_phone,
    'change phone': change_phone_num,
    'delete phone': delete_phone,
    'add birthday' : set_birthday,
    'birthday': days_to_birthday,
    'add email': add_email,
    'change email': change_email,
    'delete email': delete_email,
    'show all': show_all,
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
    print(LOGO)
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