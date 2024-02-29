from collections import UserDict
<<<<<<< Updated upstream
# Bot - Syntax Conquerors
=======
import re
>>>>>>> Stashed changes

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

class Contact():
    def __init__(self, name, last_name):
        self.name = Name(name)
        self.last_name = Name(last_name)

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

address_book = AddressBook()
<<<<<<< Updated upstream
def changelog():
    """
    Need somewhere to keep up with the changes.
    """
    pass

def test_contacts():  
=======

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
>>>>>>> Stashed changes
    """Function fills up addres book with random contacts for debugging purposes"""

    random_contacts = [
        {'name': 'Zbyszek', 'last name': 'Kowalski', 'phone': '606505404', 'email': 'zbyszek.kowalski@gmail.com', 'birthday': '20 5 1990'},
<<<<<<< Updated upstream
        {'name': 'Rychu', 'last name': 'Nowak', 'phone': '546859652', 'email': 'rychu.nowak@gmail.com', 'birthday': '10 11 1995'}
=======
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
>>>>>>> Stashed changes
        ]
    
    for person in random_contacts: # add random contacts to
        address_book.add_contact(person['name'], person['last name'])
    
    for contact_name in address_book.contacts:
        print(f'Name: {address_book.contacts[contact_name].name.value}')
        print(f'Last Name: {address_book.contacts[contact_name].last_name.value}')
<<<<<<< Updated upstream

def main():
    test_contacts()    

=======

def end_program():
    print('Good bye')
    exit()

def unknown_command():
    print('Unknown command')    

def input_parser():
    """Functions runs in a while loop, takes input from user and returns apropiate functions
    """
    commands = {
    # 'create contact': create_contact,
    # 'add phone': add_phone,
    # 'change phone': change_phone_num,
    # 'show contact': show_contact,
    # 'delete phone': delete_phone,
    # 'add birthday' : set_birthday,
    # 'birthday': days_to_birthday,
    # 'show all': show_all,
    # 'find contact' : find_contact,
    'exit': end_program, 
}
    command = input('Input your command: ').lower()

    if command in commands:
        return commands[command]    
    else:
        return unknown_command

def main():
    test_contacts(address_book)
    while True:  
        function_to_execute = input_parser()
        function_to_execute()
 
>>>>>>> Stashed changes
if __name__ == '__main__':
    main()
