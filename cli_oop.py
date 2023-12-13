from collections import UserDict


class Field:
    def __init__(self, value):
        self.value = value


    def __str__(self):
        return str(self.value)
    

class Name(Field):
    def __init__(self, name):
        self.value = name


class Phone(Field):
    def __init__(self, number):
        if len(str(number)) == 10 and number.isdigit():
            self.value = number
        else:
            raise ValueError("Phone number should have 10 digits")
        

class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []


    def add_phone(self, number):
        phone = Phone(number)
        self.phones.append(phone)


    def remove_phone(self, number):
        for phone in self.phones:
            if phone.value == number:
                self.phones.remove(phone)
        return f"No phone number {number} found for {self.name.value}."
    

    def edit_phone(self, old_number, new_number):
        for phone in self.phones:
            if phone.value == old_number:
                phone.value = new_number
        return f"No phone number {old_number} found for {self.name.value}."
    

    def find_phone(self, number):
        if number in [phone.value for phone in self.phones]:
            return number
        else:
            return f"No phone number found for {self.name}"
        

    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(phone.value for phone in self.phones)}"
    

class AddressBook(UserDict):
    def add_record(self, contact):
        self.data[contact.name.value] = contact


    def find(self, name):
        if name in self.data:
            contact = self.data[name]
            return contact
        else:
            return f'No phone number found for {name}.'
        

    def delete(self, name):
        if name in self.data:
            del self.data[name]



            
if __name__ == '__main__':
    book = AddressBook()

    john_record = Record("John")
    john_record.add_phone("1234567890")
    john_record.add_phone("5555555555")

    book.add_record(john_record)

    jane_record = Record("Jane")
    jane_record.add_phone("9876543210")
    book.add_record(jane_record)

    for name, record in book.data.items():
        print(record)

    john = book.find("John")
    print(john)

    john.edit_phone("1234567890", "1112223333")
    print(john)

    john.remove_phone("1112223333")
    print(john)

    found_phone = john.find_phone("5555555555")
    print(f"{john.name}: {found_phone}")

    jane = book.find("Jane")
    print(jane) 

    book.delete("Jane")

    jane = book.find("Jane")
    print(jane) 
    