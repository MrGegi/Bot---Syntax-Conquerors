import pickle
from classes import AddressBook

def load_from_file():
    try:
        with open('bot_save.bin',"rb") as fh:
            address_book = pickle.load(fh)
            print('The adress_book has been loaded from file')
    except FileNotFoundError:
        print("File with address_book doesn't exist yet! Creating new Addressbook")
        return AddressBook()
    return address_book