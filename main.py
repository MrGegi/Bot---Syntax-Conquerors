from collections import UserDict
# Bot - Syntax Conquerors

# OPERATIONS = {
#     'accepted_commands':accepted_commands,
#     'hello': hello,
#     'create_contact': create_contact,
#     'add_phone': add_phone,
#     'change_phone_num': change_phone_num,
#     'show_contact': show_contact,
#     'delete_phone': delete_phone,
#     'set_birthday' : set_birthday,
#     'days_to_birthday': days_to_birthday,
#     'iterator': iterator,
#     'show_all': show_all,
#     'find_contact' : find_contact,
#     'good_bye': end_program, 
#     'close': end_program, 
#     'exit': end_program, 
#     '.': end_program, 
# }

class AddressBook(UserDict):
    def __init__(self):
        self.contacts = {}

    def add_contact(self, name, last_name):
        address_book.contacts[name + ' ' + last_name] = Contact(name, last_name)
        
    def add_phone(self, name, last_name, number):
        if name + ' ' + last_name in self.contacts:
            self.contacts[name + ' ' + last_name].add_phone(number)
            
class Contact():
    def __init__(self, name, last_name):
        self.name = Name(name)
        self.last_name = Name(last_name)
        self.phones = []
    
    def add_phone(self, number):
        self.phones.append(Phone(number))

class Field(): # Mega parent
    """
    Można się teraz odnieść do settera za pomocą @Field.value.setter.
    Należy tylko do klasy dziedziczącej (child) w nawiasie nazwę klasy przekazującej (parent).
    Np. class Name(Field):
    """
    def __init__(self, input_value = None):
        self.value = input_value

    @property # makes life so much easier
    def value(self):
        return self.internal_value
    
    @value.setter # Można się odwwołaać do tego settera w swojej klasie za pomocą @Field.value.setter i zrobić overide.
    def value(self, input_value):
        self.internal_value = input_value

class Name():
    pass

class Phone(Field):
    @Field.value.setter
    def value(self, number):
        if not number.strip().isdigit():
            raise ValueError("Numer telefonu musi składać się tylko z cyfr.")
        self.internal_value = number

class Address():
    pass

class Email():
    pass

class Birthday():
    pass

class Notebook():
    pass
    
class Note():
    pass

class Tag():
    pass

def changelog():
    """
    Need somewhere to keep up with the changes.
    """
    pass

def test_contacts():  
    """Function fills up addres book with random contacts for debugging purposes"""

    random_contacts = [
        {'name': 'Zbyszek', 'last name': 'Kowalski', 'phone': '606505404', 'email': 'zbyszek.kowalski@gmail.com', 'birthday': '20 5 1990'},
        {'name': 'Rychu', 'last name': 'Nowak', 'phone': '546859652', 'email': 'rychu.nowak@gmail.com', 'birthday': '10 11 1995'}
        ]
    
    for person in random_contacts: # add random contacts to
        address_book.add_contact(person['name'], person['last name'])
        address_book.add_phone(person['name'], person['last name'], person['phone'])

    for contact_name, contact in address_book.contacts.items():
        print(f'Name: {contact.name.value}')
        print(f'Last Name: {contact.last_name.value}')
        print('Phone numbers:')
        for phone in contact.phones:
            print(f' - {phone.value}')

def main():
    test_contacts()    

if __name__ == '__main__':
    main()
