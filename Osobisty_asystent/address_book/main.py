from classes import *
from utilities import *
from sorting_module import main_sorting_folder
import pickle
import os

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
            if isinstance(raised_exception, ValueError) and str(raised_exception) == "class_email:setter-regex_format_error":
                print("Wrong email format!")
                return
            else:
                line_number = (lambda traceback: traceback.tb_lineno if not traceback.tb_next else traceback.tb_next.tb_lineno)(raised_exception.__traceback__)
                print(f"Unhandled exception >> Line:{line_number} Type:{type(raised_exception).__name__} Str:{str(raised_exception)}")
                return 
    return gracefull_error_handling

@input_error
def test_contacts(address_book: AddressBook):  
    """Function fills up addres book with random contacts for debugging purposes"""

    random_contacts = [
        {'name': 'adam wojcik', 'phone': '206947535', 'email': 'adam.wojcik@yahoo.com', 'birthday': '1981-3-2', 'address': 'sosnowiec ladna 57/10'},
        {'name': 'tomasz kowalczyk', 'phone': '521861174', 'email': 'tomasz.kowalczyk@outlook.com', 'birthday': '1966-3-3', 'address': 'sosnowiec sloneczna 57/10'},
        {'name': 'jan kowalczyk', 'phone': None, 'email': 'jan.kowalczyk@outlook.com', 'birthday': '1960-3-11', 'address': 'radom polna 57/10'},
        {'name': 'andrzej kowalski', 'phone': '065754408', 'email': None, 'birthday': '1983-11-21', 'address': 'warszawa ladna 57/10'},
        {'name': 'tomasz nowak', 'phone': '046952319', 'email': 'tomasz.nowak@yahoo.com', 'birthday': None, 'address': 'sosnowiec kolorowa 57/10'},
        {'name': 'adam kaminski', 'phone': '659435166', 'email': 'adam.kaminski@gmail.com', 'birthday': '1968-3-26', 'address': None},
        {'name': 'piotr nowak', 'phone': '678910629', 'email': 'piotr.nowak@yahoo.com', 'birthday': '1971-3-24', 'address': 'poznan 13/3'},
        {'name': 'adam kowalski', 'phone': '324844741', 'email': 'adam.kowalski@outlook.com', 'birthday': '1991-3-4', 'address': 'krakow 26/10'},
        {'name': 'piotr kaminski', 'phone': '453802562', 'email': 'adam.kaminski@yahoo.com', 'birthday': '1980-9-22', 'address': 'warszawa 76/18'},
        {'name': 'tomasz adamek', 'phone': '164015881', 'email': 'tomasz.kowalczyk@outlook.com', 'birthday': '2002-1-3', 'address': 'sosnowiec 74/10'},
        {'name': 'piotr kowalczyk', 'phone': '915881994', 'email': 'jan.kowalczyk@yahoo.com', 'birthday': '1964-3-23', 'address': 'sosnowiec 100/11'},
        {'name': 'andrzej nowak', 'phone': '529363681', 'email': 'andrzej.nowak@gmail.com', 'birthday': '1999-2-8', 'address': 'krakow 13/1'},
        {'name': 'sebastian kowalski', 'phone': '771463826', 'email': 'andrzej.kowalski@yahoo.com', 'birthday': '1966-12-22', 'address': 'warszawa 18/2'},
        {'name': 'adam kowalczyk', 'phone': '635549242', 'email': 'adam.kowalczyk@gmail.com', 'birthday': '1993-3-19', 'address': 'sosnowiec 25/12'},
        {'name': 'tomasz siekierka', 'phone': '623143519', 'email': 'tomasz.kowalczyk@gmail.com', 'birthday': '1977-12-6', 'address': 'sosnowiec 37/19'},
        {'name': 'jan kowalski', 'phone': '483958195', 'email': 'jan.kowalski@outlook.com', 'birthday': '1972-4-17', 'address': 'krakow 84/10'},
        {'name': 'leszek kowalski', 'phone': '039342693', 'email': 'jan.kowalski@outlook.com', 'birthday': '1981-5-3', 'address': 'poznan 97/17'},
        {'name': 'andrzej kaminski', 'phone': '718624235', 'email': 'andrzej.kaminski@yahoo.com', 'birthday': '1973-1-14', 'address': 'gdansk 42/6'},
        {'name': 'tomasz socha', 'phone': '052130035', 'email': 'tomasz.kowalczyk@gmail.com', 'birthday': '1964-8-14', 'address': 'krakow 17/6'},
        {'name': 'andrzej kowalczyk', 'phone': '087189332', 'email': 'andrzej.kowalczyk@outlook.com', 'birthday': '1967-3-27', 'address': 'gdansk 11/1'},
    ]

    for person in random_contacts:
        address_book.add_contact(person['name'])
        address_book.contacts[person['name']].add_phone(person['phone'])
        address_book.contacts[person['name']].add_email(person['email'])
        address_book.contacts[person['name']].add_birthday(person['birthday'])
        address_book.contacts[person['name']].add_address(person['address'])
    
def add_contact():    
    name = input("Enter the contact's name and surname: ").lower()
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
    name = input("Enter the contact's name and surname you'd like to delete: ").lower()
    if name in address_book.contacts:
        address_book.contacts.pop(name)
        print(f'Contact {name} deleted.')
    else:
        print(f'There is no contact {name}')

def add_phone():
    name = input("Enter the contact's name and surname: ").lower()
    if not name in address_book.contacts:
        print(f'There is no contact {name}')
        return
    phone = input("Enter phone number: ")
    try:
        address_book.contacts[name].add_phone(phone)
        if address_book.contacts[name].phone.value:
            print(f"{phone} was added to contact {name}.")
    except:
        return

def change_phone_num():
    name = input("Enter the contact's name and surename: ").lower()
    if not name in address_book.contacts:
        print(f'There is no contact {name}')
        return
    if not address_book.contacts[name].phone.value:
        print(f"Contact {name} doesnt have a phone number yet. However we can proceed.")
    new_phone = input("Enter the new phone number: ")
    try:
        address_book.contacts[name].add_phone(new_phone)
        if address_book.contacts[name].phone.value == new_phone[0:3] + '-' + new_phone[3:6] + '-' + new_phone[6:]:
            print(f"Number was changed for contact {name}.")
    except:
        return

def delete_phone():
    name = input("Enter the contact's name and surename: ").lower()
    if name in address_book.contacts:
        address_book.contacts[name].delete_phone()
        print(f"Phone number deleted for {name}.")
    else:
        print("Contact not found.")

def add_email():
    name = input("Enter the contact's name and surname: ").lower()
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
    name = input("Enter the contact's name and surname: ").lower()
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
    name = input("Enter the contact's name and surname: ").lower()
    if not name in address_book.contacts:
        print(f'There is no contact {name}')
        return
    address_book.contacts[name].remove_email()
    print(f'Email deleted')

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
    width = 123
    print("\n+" + "-" * width + "+")
    print('|{:^30}|{:^30}|{:^30}|{:^30}|'.format("NAME", "BIRTHDAY", "DAYS TO BIRTHDAY", "UPCOMING"))
    print("+" + "-" * width + "+")
    
    for contact_name in address_book.contacts:
        contact = address_book.contacts[contact_name]
        if contact.birthday.value and contact.days_to_birthday < 31:
            format_value = lambda x: x if x is not None else "---"
            print('|{:^30}'.format(format_value(contact.name.value.title())), end="")
            print('|{:^30}'.format(format_value(contact.birthday.value)), end="")
            print('|{:^30}'.format(format_value(contact.days_to_birthday)), end="")

            days_to_birthday = contact.days_to_birthday
            
            if contact.birthday.value:
                birthday_date = datetime.strptime(contact.birthday.value, "%Y-%m-%d")
                today = datetime.today()
                next_birthday = datetime(today.year, birthday_date.month, birthday_date.day)
                
                if today > next_birthday:
                    next_birthday = datetime(today.year + 1, birthday_date.month, birthday_date.day)
                
                days_from_beginning_of_week = (today.weekday() - 7) % 7
                
                if days_to_birthday == 0:
                    print('|{:^30}|'.format("Today"), end="\n")
                elif days_to_birthday == 1:
                    print('|{:^30}|'.format("Tomorrow"), end="\n")
                elif days_to_birthday < 7 - days_from_beginning_of_week:
                    print('|{:^30}|'.format("This week"), end="\n")
                elif days_to_birthday < 14 - days_from_beginning_of_week:
                    print('|{:^30}|'.format("Next week"), end="\n")
                elif next_birthday.month == today.month:
                    print('|{:^30}|'.format("This month"), end="\n")
                elif (today.month + 1) % 12 == next_birthday.month % 12:
                    print('|{:^30}|'.format("Next month"), end="\n")
                else:
                    print('|{:^30}|'.format("---"), end="\n")
            else:
                print('|{:^30}|'.format("---"), end="\n")
            
    print("+" + "-" * width + "+\n")

def add_address():
    name = input("Enter the contact's name and surname: ").lower()
    if not name in address_book.contacts:
        print(f'There is no contact {name}')
        return
    city = input("City: ")
    street = input("Street: ")
    number = input("House and flat number: ")
    address = city + ' ' + street + ' ' + number
    try:
        address_book.contacts[name].add_address(address.title())
        if address_book.contacts[name].address.value:
            print(f"{address} was added to contact {name}.")
    except:
        return
    
def change_address():
    name = input("Enter the contact's name and surname: ").lower()
    if not name in address_book.contacts:
        print(f'There is no contact {name}')
        return
    if not address_book.contacts[name].address.value:
        print(f"Contact {name} doesnt have a email yet. However we can proceed.")
    city = input("City: ")
    street = input("Street: ")
    number = input("House and flat number: ")
    address = city + ' ' + street + ' ' + number
    try:
        address_book.contacts[name].add_address(address.title())
        if address_book.contacts[name].address.value == address.title():
            print(f"{address} was changed for contact {name}.")
    except:
        return
    
def delete_address():
    name = input("Enter the contact's name and surname: ").lower()
    if not name in address_book.contacts:
        print(f'There is no contact {name}')
        return
    address_book.contacts[name].remove_address()
    print(f'Address deleted')

def add_note():
    note = input("Enter the note text: ")
    tags = input("Enter tags: ")
    address_book.notebook.add_note(note, tags)

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

def show_notes():
    print('List of notes: \n', address_book.notebook.show_notes())

def search_note_by_tags():
    searched_tags = input("Enter tags: ")
    print(address_book.notebook.search_note_by_tags(searched_tags))

def show_all():
    width = 154
    print("\n+" + "-" * width + "+")
    print('|{:^30}|{:^30}|{:^30}|{:^30}|{:^30}|'.format("NAME", "PHONE", "EMAIL", "BIRTHDAY", "ADDRESS"))
    print("+" + "-" * width + "+")
    for contact_name in address_book.contacts:
        contact = address_book.contacts[contact_name]
        format_value = lambda x: x if x is not None else "---"
        print('|{:^30}'.format(format_value(contact.name.value.title())), end="")
        print('|{:^30}'.format(format_value(contact.phone.value)), end="")
        print('|{:^30}'.format(format_value(contact.email.value)), end="")
        print('|{:^30}'.format(format_value(contact.birthday.value)), end="")
        print('|{:^30}|'.format(format_value(contact.address.value)), end="\n")
    print("+" + "-" * width + "+\n")

def find_contact():
    contact_name = input("Enter the contact's name and surename: ")
    if contact_name in address_book.contacts:
        width = 154
        print("\n+" + "-" * width + "+")
        print('|{:^30}|{:^30}|{:^30}|{:^30}|{:^30}|'.format("NAME", "PHONE", "EMAIL", "BIRTHDAY", "ADDRESS"))
        print("+" + "-" * width + "+")
        contact = address_book.contacts[contact_name]
        format_value = lambda x: x if x is not None else "---"
        print('|{:^30}'.format(format_value(contact.name.value.title())), end="")
        print('|{:^30}'.format(format_value(contact.phone.value)), end="")
        print('|{:^30}'.format(format_value(contact.email.value)), end="")
        print('|{:^30}'.format(format_value(contact.birthday.value)), end="")
        print('|{:^30}|'.format(format_value(contact.address.value)), end="\n")
        print("+" + "-" * width + "+\n")
    else:
        print("Contact not found.")

def sort_folder():
    current_path = os.getcwd()
    path_to_folder = input(" Enter path to folder that should be sorted: ")
    main_sorting_folder(path_to_folder)
    os.chdir(current_path)

def save_to_file():
    with open('bot_save.bin', "wb") as fh:
        pickle.dump(address_book, fh)
    print('File has been saved')

def end_program():
    save_to_file()
    print('Goodbye')

def accepted_commands(commands):
    for command in commands.keys():
        print(f"   {command}")

def unknown_command(commands: dict):
    print("\nUnknown command! Please choose one from the list provided below:\n")
    for command in commands.keys():
        print(f"   {command}")

def input_parser():
    """Functions runs in a while loop, takes input from user and returns apropiate functions
    """
    commands = {
    'add contact': add_contact,
    'delete contact': delete_contact,
    'add phone': add_phone,
    'change phone': change_phone_num,
    'delete phone': delete_phone,
    'add email': add_email,
    'change email': change_email,
    'delete email': delete_email,
    'add birthday' : set_birthday,
    'birthday': days_to_birthday,
    'add address': add_address,
    'change address': change_address,
    'delete address': delete_address,
    'add note': add_note,
    'edit note': edit_note,
    'remove note': remove_note,
    'show notes':show_notes,
    'search note': search_note_by_tags,
    'show all': show_all,
    'find contact' : find_contact,
    'sort folder': sort_folder,
    'save': save_to_file,
    'exit': end_program,
    'help': accepted_commands, 
}   
    command = input('\nEnter your command: ').lower()
    if command == 'help':
        return accepted_commands(commands)
    elif command in commands:
        return commands[command]  
    else:
        return unknown_command(commands)

def main():
    print(LOGO)
    print('Type "help" to get a command list.')
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