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
    def __init__(self, name, phone=None, address=None, email=None, birthday=None):
        self.name = Name(name)
        self.phone = Phone(phone)
        self.address = Address(address)
        self.email = Email(email)
        self.birthday = Birthday(birthday)
        
    def add_phone(self, phone):
        try:
            self.phone = Phone(phone)
            # print(self.phone)
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
        
    def add_email(self, email):
        self.email = Email(email)

    def remove_email(self, email=None):
        self.email = Email(email)
        
    def add_address(self, address):
        self.address = Address(address)

    def remove_address(self, address = None):
        self.address = Address(address)
    
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
            return None

class Field:
    def __init__(self, input_value = None):
        self.internal_value = None
        self.value = input_value

    @property
    def value(self):
        return self.internal_value
    
    @value.setter
    def value(self, input_value):
        self.internal_value = input_value

class Name(Field):
    @Field.value.setter
    def value (self, name):
        if not name:
            raise ValueError("class_Name-def_value:name_cannot_be_empty")       
        self.internal_value = name.lower()

class Phone(Field):
    @Field.value.setter
    def value(self, number):
        if number:
            number = number.strip()
            if not number.isdigit() or len(number) != 9:
                raise ValueError("Number must be 9 digits long and contain digits only.")
            self.internal_value = number[0:3]+'-'+number[3:6]+'-'+number[6:]

class Address(Field):
    @Field.value.setter
    def value(self, address: str):
        self.internal_value = address

class Email(Field): 
    @Field.value.setter
    def value(self, email):
        if email:
            """Check email format"""
            patern_email = r"^([A-Za-z0-9]+ |[A-Za-z0-9][A-Za-z0-9\.\_]+[A-Za-z0-9])@([A-Za-z0-9]+|[A-Za-z0-9\_\-]+[A-Za-z0-9])\.([a-z]{,3}|[a-z]{3}\.[a-z]{2})$"
            result = re.findall(patern_email,email)
            if result == []:
                # print('Wrong mail format!')
                raise ValueError("class_email:setter-regex_format_error")
        self.internal_value = email

class Birthday(Field):
    @Field.value.setter
    def value(self, input_value: str):
        self.internal_value = input_value

class Notebook(UserDict):
    num_of_notes = 0

    def add_note(self, note, tags):
        try:
            Notebook.num_of_notes += 1
            while True:
                if Notebook.num_of_notes in self.data.keys():
                    Notebook.num_of_notes += 1
                else:
                    break
            self.num_of_note = Notebook.num_of_notes
            self.data[self.num_of_note] = [Note(note).internal_value, Tags(tags).internal_value]
            return True
        
        except ValueError as e:
            print(e)
            return False
        
    def show_notes(self):
        all_notes = ''
        for num_of_note, note_and_tags in self.data.items():
            note = note_and_tags[0]
            tags = note_and_tags[1]
            str_tags = ''
            for tag in tags:
                str_tags += f'{tag}; '
            all_notes += f'Number of note: {str(num_of_note):<2} Note: {str(note)} Tags: {str_tags}\n'
        return all_notes
    
    def search_note_by_tags(self, searched_tags):
        searched_tags = Tags(searched_tags).internal_value
        finded_notes = ''
        for num_of_note, note_and_tags in self.data.items():
            note = note_and_tags[0]
            tags = note_and_tags[1]
            
            if searched_tags <= tags:
                str_tags = ''
                for tag in tags:
                    str_tags += f'{tag}; '
                finded_notes += f'Number of note: {str(num_of_note):<2} Note: {str(note)} Tags: {str_tags}\n'
                
        if finded_notes == '':
            return f'Notes not find'
        else:
            return finded_notes
    
    def edit_note(self, num_of_note):
        if num_of_note not in str(self.data.keys()):
            print('Number of note doesn\'t exists')
            return False
        else:
            try:
                note = input('Enter new note text: ')
                tags = input("Enter new tags: ")
                self.data[int(num_of_note)] = [Note(note).internal_value, Tags(tags).internal_value]
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

class Tags(Field):
    @Field.value.setter
    def value(self, tags:str):
        tags = tags.lower()
        tags = re.split(r'[^0-9a-z]', tags)
        tags = set(filter(lambda tag: tag.isalnum(), tags))
        self.internal_value = tags