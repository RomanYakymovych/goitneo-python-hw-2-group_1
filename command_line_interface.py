class TelNumberError(Exception):
    pass


class ContactNameError(Exception):
    pass


def input_error(func):
    def inner(*args, **kwargs):
        try:
            if 'add_contact' in func.__name__:
                name, phone = args[0]
                if not phone.isdigit():
                    raise TelNumberError("Telephone number should be a number")
                if not name.isalpha():
                    raise ContactNameError("Name should not be a number")
            return func(*args, **kwargs)
        except ValueError:
            return "Please provide a name and phone number."
        except TelNumberError as e:
            return f"Exception occurred: {e}"
        except ContactNameError as e:
            return f"Exception occurred: {e}"
    return inner


def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args


@input_error
def add_contact(args, contacts):
    name, phone = args
    contacts[name] = phone
    return f'Contact {name} with phone number: {phone} added.'

@input_error
def show_phone(args, contacts):
    name = args[0][0]
    if name in contacts:
        return f'Name: {name}, Phone Number: {contacts[name]}'
    else:
        return f'No phone number found for {name}.'
 
  
def show_all(contacts):
    if not contacts:
        return 'No contacts found.'
    text = "{:.<15}{:<10}\n".format('Name', 'Phone Number')
    for name, phone in contacts.items():
        text += "{:.<15}{:<10}\n".format(name, phone)
    return text
 
  
def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "phone":
            print(show_phone(args, contacts))
        elif command == "all":
            print(show_all(contacts))
        else:
            print("""Invalid command. Available commands: hello, add, phone, all, close, exit""")

if __name__ == "__main__":
    main()