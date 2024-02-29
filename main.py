from collections import UserDict
import re
import pickle

class AddressBook(UserDict):
    def __init__(self):
        self.contacts = {}

    def add_contact(self, name, last_name):
        self.contacts[name + ' ' + last_name] = Contact(name, last_name)

class Contact():
    def __init__(self, name, last_name):
        self.name = Name(name)
        self.last_name = Name(last_name)
        self.address = ''
        self.note = ''
        
    def add_phone(self, phone):
        self.phone = Phone(phone)
        
    def delete_phone(self):
        self.phone = None   

    def change_phone(self, new_phone):
        self.phone = Phone(new_phone)
        
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

class Field:
    """
    Można się teraz odnieść do settera za pomocą @Field.value.setter.
    Należy tylko do klasy dziedziczącej (child) w nawiasie nazwę klasy przekazującej (parent).
    Np. class Name(Field):
    """
    def __init__(self, input_value = None):
        self.value = input_value

    @property
    def value(self):
        return self.internal_value
    """
    Dzieki @property można używać dodatkowych funkcj dekoratora klasy takich jak .setter ponizej.
    """
    
    @value.setter
    def value(self, input_value):
        self.internal_value = input_value
    """
    Można się odwwołaać do tego settera w swojej klasie za pomocą @Field.value.setter i zrobić overide.
    """

class Name(Field):
    """
    Przykład jak można użyć dekoratora @property do wprowadzenia warunków do settera dla Name.
    """
    @Field.value.setter
    def value (self, name):
        if not name:
            raise ValueError("class_Name-def_value:name_cannot_be_empty")
        """
        Ta wiadomość idzie do @input_error Jeśli funkcja handler używa tego settera do wysłania wartości do obiektu.
        """
        self.internal_value = name

class Phone(Field):
    @Field.value.setter
    def value(self, number):
        if not number.strip().isdigit():
            raise ValueError("Numer telefonu musi składać się tylko z cyfr.")
        if len(number) != 9:
            raise ValueError("Numer telefonu musi składać się z 9 cyfr.")
        self.internal_value = number

class Address(Field):
    @Field.value.setter
    def value(self, address: str):
        self.internal_value = address

class Email(Field):
    
    def __init__(self, email=''):
       self.__name = None
       self.email = email

    @property
    def email(self):
        return self.__name
    
    @email.setter
    def email(self, email):
        
        """Sprawdzenie czy format maila jest prawidłowy"""

        patern_email = r"^([A-Za-z0-9]+ |[A-Za-z0-9][A-Za-z0-9\.\_]+[A-Za-z0-9])@([A-Za-z0-9]+|[A-Za-z0-9\_\-]+[A-Za-z0-9])\.([a-z]{,3}|[a-z]{3}\.[a-z]{2})$"
        result = re.findall(patern_email,email)

        if result != []:
            end_text = 'Adress mail has correct format.'
            self.__name  = email
        else:
            end_text = "Wrong mail format!"
        print(end_text)
        # print(result)
        return

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
        {'name': 'Zbyszek', 'last name': 'Kowalski', 'phone': '606505404', 'email': 'zbyszek.kowalski@gmail.com', 'birthday': '20 5 1990'},
        {'name': 'Rychu', 'last name': 'Nowak', 'phone': '546859652', 'email': 'rychu.nowak@gmail.com', 'birthday': '10 11 1995'},
        #{'name': 'Jan', 'last name': 'Wójcik', 'phone': '524835658', 'email': 'jan.wójcik@gmail.com', 'birthday': '5 9 1965'},
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
        address_book.add_contact(person['name'], person['last name'])
        address_book.contacts[person['name'] + ' ' + person['last name']].add_phone(person['phone'])
    
    for contact_name in address_book.contacts:
        print(f'Name: {address_book.contacts[contact_name].name.value}')
        print(f'Last Name: {address_book.contacts[contact_name].last_name.value}')
        print(f'Phone: {address_book.contacts[contact_name].phone.value}')

def save_to_file():
    with open('bot_save.txt', "wb") as fh:
        pickle.dump(address_book, fh)
        print('File saved')

def end_program():
    print('Good bye')
    save_to_file()
    exit()

def unknown_command():
    print('Unknown command')

def input_parser():
    """Functions runs in a while loop, takes input from user and returns apropiate functions
    """
    commands = {
    # 'add contact': add_contact,
    # 'add note': add_note,
    # 'add phone': add_phone,
    # 'change phone': change_phone_num,
    # 'show contact': show_contact,
    # 'delete phone': delete_phone,
    # 'add birthday' : set_birthday,
    # 'birthday': days_to_birthday,
    # 'show all': show_all,
    # 'find contact' : find_contact,
    'save': save_to_file,
    'exit': end_program, 
}
    command = input('Enter your command: ').lower()

    if command in commands:
        return commands[command]  
    else:
        return unknown_command

def main():
    test_contacts(address_book)
    while True:  
        function_to_execute = input_parser()
        try:
            function_to_execute()
        except:
            continue
 
if __name__ == '__main__':
    main()
