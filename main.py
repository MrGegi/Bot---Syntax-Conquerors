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

def main():
    test_contacts()    

if __name__ == '__main__':
    main()
