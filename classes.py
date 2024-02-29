from collections import UserDict
import re
import pickle

class AddressBook(UserDict):
    def __init__(self):
        self.contacts = {}

    def add_contact(self, name):
        self.contacts[name] = Contact(name)

class Contact():
    def __init__(self, name):
        self.name = Name(name)
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
