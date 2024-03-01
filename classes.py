from collections import UserDict
import re
from datetime import datetime

class AddressBook(UserDict):
    def __init__(self):
        self.contacts = {}
        self.notebook = Notebook()

    def add_contact(self, name):
        self.contacts[name] = Contact(name)

class Contact():
    def __init__(self, name):
        self.name = Name(name)
        self.address = ''
        self.birthday = ''
        
    def add_phone(self, phone):
        try:
            self.phone = Phone(phone)
            print(self.phone)
            return True
        except ValueError as e:
            print(e)
            return False
        
    def delete_phone(self):
        self.phone = None   

    def change_phone(self, new_phone):
        try:
            self.phone = Phone(new_phone)
            return True
        except ValueError as e:
            print(e)
            return False
        
    def add_address(self, address):
        self.address = Address(address).value

    def remove_address(self):
        self.address = ''

    def change_address(self, address):
        self.address = Address(address).value
    
    def add_birthday(self, birthday):
        self.birthday = Birthday(birthday)

    @property
    def days_to_birthday(self):
        if self.birthday.value:
            today = datetime.today()
            birthday_date = datetime.strptime(self.birthday.value, "%Y-%m-%d")
            upcoming_birthday_date = datetime(today.year, birthday_date.month, birthday_date.day)
            if today > upcoming_birthday_date:
                upcoming_birthday_date = datetime(today.year + 1, birthday_date.month, birthday_date.day)
            delta = upcoming_birthday_date - today
            return delta.days
        else:
            print("it doesnt see any value")
            return None

class Field:
    """
    Można się teraz odnieść do settera za pomocą @Field.value.setter.
    Należy tylko do klasy dziedziczącej (child) w nawiasie nazwę klasy przekazującej (parent).
    Np. class Name(Field):
    """
    def __init__(self, input_value = None):
        self.internal_value = None
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
            raise ValueError("Number can contain digits only.")
        if len(number) != 9:
            raise ValueError("Number must be 9 digits long.")
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

class Birthday(Field):
    @Field.value.setter
    def value(self, input_value: str):
        if input_value and not datetime.strptime(input_value, "%Y-%m-%d"):
            raise ValueError("Wrong date format. Expected YYYY-MM-DD.")
        self.internal_value = input_value

class Notebook(UserDict):
    num_of_notes = 0

    def add_note(self, note):
        try:
            Notebook.num_of_notes += 1
            self.num_of_note = Notebook.num_of_notes
            self.data[self.num_of_note] = Note(note).internal_value
            return True
        
        except ValueError as e:
            print(e)
            return False
        
    def show_notes(self):
        all_notes = ''
        for num_of_note, note in self.data.items():
            all_notes += f'Number of note: {str(num_of_note):<2} Note: {str(note)}\n'
        return all_notes
    
    def edit_note(self, num_of_note):
        if num_of_note not in str(self.data.keys()):
            print('Number of note doesn\'t exists')
            return False
        else:
            try:
                note = input('Enter new note text: ')
                self.data[self.num_of_note] = Note(note).internal_value
                return True
            
            except ValueError as e:
                print(e)
                return False
            
    def remove_note(self, num_of_note):
        if num_of_note == 'all':
            self.data.clear()
            return True
    
        elif num_of_note not in str(self.data.keys()):
            print('Number of note doesn\'t exists')
            return False
        else:
            self.data.pop(int(num_of_note))
            return True

    def remove_all_notes(self):
        self.note = ''

    def change_notebook(self, note):
        self.note = Notebook(note).value
    
class Note(Field):
    @Field.value.setter
    
    def value(self, note):
        if note == '':
            raise ValueError("Note must include any characters")
        self.internal_value = note