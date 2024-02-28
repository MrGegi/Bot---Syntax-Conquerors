from collections import UserDict
from datetime import datetime
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
        self.name = name
        self.last_name = last_name

class Field: # Mega parent
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

class Phone():
    pass

class Address():
    pass

class Email():
    pass

class Birthday:
    def __init__(self, birthday):
        self.birthday = date(int(year_of_birth), int(month_of_birth), int(day_of_birth))

    def wishing(self, name):
        today = date.today()
        current_year = today.year

        age = current_year - self.birthday.year

        next_birthday = date(current_year, self.birthday.month, self.birthday.day)

        if next_birthday < today:
            next_birthday = date(current_year + 1, self.birthday.month, self.birthday.day)

        time_delta = next_birthday - today

        if today == self.birthday:
            return f"{name}, wszystkiego najlepszego z okazji {age} urodzin!"
        else:
            return f"Twoje urodziny są za {time_delta.days} dni."


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

def documentation():
    """Function Description
    Lets keep documenation up to date.
    """
    my_code = 0 # remember to comment important parts of your code
    return 'good luck and have fun'


def main():
    print('')
    

if __name__ == '__main__':
    main()


