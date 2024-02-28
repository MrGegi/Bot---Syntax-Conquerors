from collections import UserDict
# Bot - Syntax Conquerors



class AddressBook(UserDict):
    def __init__(self):
        self.contacts = {}

    def add_contact(self, name, last_name):
        address_book.contacts[name + ' ' + last_name] = Contact(name, last_name)

class Contact():
    def __init__(self, name, last_name):
        self.name = Name(name)
        self.last_name = Name(last_name)
        self.address = ''
        self.note = ''

    def add_address(self, address):
        self.address = Address(address).value

    def remove_address(self):
        self.address = ''

    def change_address(self, address):
        self.address = Address(address).value


    def add_notebook(self, note):
        self.note = Notebook(note).value

    def remove_notebook(self):
        self.note = ''

    def change_notebook(self, note):
        self.note = Notebook(note).value

class Field: # Parent
    """
    Można się teraz odnieść do settera za pomocą @Field.value.setter.
    Należy tylko do klasy dziedziczącej (child) w nawiasie nazwę klasy przekazującej (parent).
    Np. class Name(Field):
    """
    def __init__(self, input_value = None):
        self.value = input_value

    @property # # Dzieki temu możesz używać dodatkowych funkcj dekoratora klasy takich jak .setter ponizej. Dlatego - makes life so much easier :)
    def value(self):
        return self.internal_value
    
    @value.setter # Można się odwwołaać do tego settera w swojej klasie za pomocą @Field.value.setter i zrobić overide.
    def value(self, input_value):
        self.internal_value = input_value

class Name(Field): # Przykład jak można użyć dekoratora @property do wprowadzenia warunków do settera dla Name.
    
    @Field.value.setter
    def value (self, name):
        if not name:
            raise ValueError("class_Name-def_value:name_cannot_be_empty") # Ta wiadomość idzie do @input_error Jeśli funkcja handler używa tego gettera do wysłania wartości do obiektu.
        self.internal_value = name

class Phone():
    pass

class Address(Field):
    @Field.value.setter
    def value(self, address: str):
        self.internal_value = address

class Email():
    pass

class Birthday():
    pass

class Notebook(Field):
    @Field.value.setter
    def value(self, note: str):
        self.internal_value = note
    
class Note():
    pass

class Tag():
    pass

def accepted_commands(command, contacts):
    commands = (list(OPERATIONS.keys()))
    message = ''
    for command in commands:
        message += f'"{command}" '  
    return f"Accepted commands: {message}"









address_book = AddressBook()
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
    
    for contact_name in address_book.contacts:
        print(f'Name: {address_book.contacts[contact_name].name.value}')
        print(f'Last Name: {address_book.contacts[contact_name].last_name.value}')

def end_program(command, address_book):
    print('Good bye')
    exit()

OPERATIONS = {
    'accepted_commands':accepted_commands,
    # 'hello': hello,
    # 'create_contact': create_contact,
    # 'add_phone': add_phone,
    # 'change_phone_num': change_phone_num,
    # 'show_contact': show_contact,
    # 'delete_phone': delete_phone,
    # 'set_birthday' : set_birthday,
    # 'days_to_birthday': days_to_birthday,
    # 'iterator': iterator,
    # 'show_all': show_all,
    # 'find_contact' : find_contact,
    'good_bye': end_program, 
    'close': end_program, 
    'exit': end_program, 
    '.': end_program, 
}

def handler_command(base_command=None, command=None, address_book = address_book):
    return OPERATIONS[base_command](command, address_book)

def main():
    test_contacts()   
    print(accepted_commands(OPERATIONS, address_book))
    while True:
        command = input('Write your command: ').lower().strip().split()
        try:
            base_command = command[0]
        except IndexError('Error, main(), not writted command'):
            continue

        handler = handler_command(base_command, command, address_book)
        if isinstance(handler, str): # jeżeli chcemy wyświetlić wynik działania funkcji, których wynik działania funkcji powinien być w str (np. show_contact)
            print(handler)
        else: # wywołanie funkcji, które nie wyświetlają output (np. add_phone)
            handler
 

if __name__ == '__main__':
    main()

