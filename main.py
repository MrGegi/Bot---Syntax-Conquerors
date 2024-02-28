from collections import UserDict
import re
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
        self.contacts[name + ' ' + last_name] = Contact(name, last_name)

class Contact():
    def __init__(self, name, last_name):
        self.name = Name(name)
        self.last_name = Name(last_name)

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

class Phone():
    pass

class Address():
    pass

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

class Notebook():
    pass
    
class Note():
    pass

class Tag():
    pass

def input_error():
    return

def changelog():
    """
    Need somewhere to keep up with the changes.
    """
    pass

def test_contacts(address_book: AddressBook):  
    """Function fills up addres book with random contacts for debugging purposes"""

    random_contacts = [
        {'name': 'Zbyszek', 'last name': 'Kowalski', 'phone': '606505404', 'email': 'zbyszek.kowalski@gmail.com', 'birthday': '20 5 1990'},
        {'name': 'Rychu', 'last name': 'Nowak', 'phone': '546859652', 'email': 'rychu.nowak@gmail.com', 'birthday': '10 11 1995'},
        {'name': 'Jan', 'last name': 'Wójcik', 'phone': '524835658', 'email': 'jan.wójcik@gmail.com', 'birthday': '5 9 1965'},
        {'name': 'Adam', 'last name': 'Kowalczyk', 'phone': '044175272', 'email': 'adam.kowalczyk@yahoo.com', 'birthday': '20 9 1985'},
        {'name': 'Tomasz', 'last name': 'Wójcik', 'phone': '523544638', 'email': 'tomasz.wójcik@yahoo.com', 'birthday': '3 8 1973'},
        {'name': 'Tomasz', 'last name': 'Kowalczyk', 'phone': '346595089', 'email': 'tomasz.kowalczyk@yahoo.com', 'birthday': '18 7 1978'},
        {'name': 'Andrzej', 'last name': 'Kowalski', 'phone': '270767747', 'email': 'andrzej.kowalski@yahoo.com', 'birthday': '6 8 1968'},
        {'name': 'Adam', 'last name': 'Nowak', 'phone': '587868953', 'email': 'adam.nowak@outlook.com', 'birthday': '1 7 1985'},
        {'name': 'Adam', 'last name': 'Kowalski', 'phone': '603277494', 'email': 'adam.kowalski@yahoo.com', 'birthday': '17 4 1961'},
        {'name': 'Tomasz', 'last name': 'Wójcik', 'phone': '114714793', 'email': 'tomasz.wójcik@outlook.com', 'birthday': '5 8 1985'},
        {'name': 'Andrzej', 'last name': 'Wójcik', 'phone': '819552896', 'email': 'andrzej.wójcik@outlook.com', 'birthday': '24 7 1964'},
        {'name': 'Andrzej', 'last name': 'Kamiński', 'phone': '497654652', 'email': 'andrzej.kamiński@gmail.com', 'birthday': '3 10 1982'},
        {'name': 'Adam', 'last name': 'Nowak', 'phone': '133258442', 'email': 'adam.nowak@outlook.com', 'birthday': '23 1 1980'},
        {'name': 'Tomasz', 'last name': 'Wójcik', 'phone': '313774876', 'email': 'tomasz.wójcik@yahoo.com', 'birthday': '1 1 1962'},
        {'name': 'Jan', 'last name': 'Wójcik', 'phone': '096489389', 'email': 'jan.wójcik@outlook.com', 'birthday': '4 4 1991'},
        {'name': 'Piotr', 'last name': 'Kamiński', 'phone': '809172250', 'email': 'piotr.kamiński@outlook.com', 'birthday': '25 8 1963'},
        {'name': 'Adam', 'last name': 'Nowak', 'phone': '491249850', 'email': 'adam.nowak@outlook.com', 'birthday': '16 5 1965'},
        {'name': 'Jan', 'last name': 'Kamiński', 'phone': '818690456', 'email': 'jan.kamiński@yahoo.com', 'birthday': '20 7 1995'},
        {'name': 'Jan', 'last name': 'Kowalski', 'phone': '441151946', 'email': 'jan.kowalski@gmail.com', 'birthday': '30 3 1986'},
        {'name': 'Piotr', 'last name': 'Kowalczyk', 'phone': '506499840', 'email': 'piotr.kowalczyk@outlook.com', 'birthday': '16 5 1962'}
        ]
    
    for person in random_contacts: # add random contacts to
        address_book.add_contact(person['name'], person['last name'])
    
    for contact_name in address_book.contacts:
        print(f'Name: {address_book.contacts[contact_name].name.value}')
        print(f'Last Name: {address_book.contacts[contact_name].last_name.value}')

def main():
    address_book = AddressBook()
    test_contacts(address_book)    

if __name__ == '__main__':
    main()
