def parse_input(user_input):
    cmd, *args = user_input.split()  
    cmd = cmd.strip().lower()  
    return cmd, args  

def input_error(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return "Give me name and phone please."
        except KeyError:
            return "Contact not found."
        except IndexError:
            return "Please provide the correct number of arguments."
    return wrapper

def add_contact_error(func):
    def wrapper(args, contacts):
        name = args[0]
        if name in contacts: 
            return f"Contact with the name '{name}' already exists."
        return func(args, contacts)
    return wrapper

# Функція для перевірки формату номера телефону
def validate_phone_number(phone):
    if len(phone) == 10 and phone.isdigit() and phone[0] == '0':
        return True
    else:
        return False
    

@input_error
@add_contact_error
def add_contact(args, contacts):
    name, phone = args
    if not validate_phone_number(phone):  # Перевіряємо номер телефону
        return "Please enter a phone number in the format: 0XXXXXXXXX (10 digits starting with 0)."
    contacts[name] = phone
    return "Contact added."

@input_error
def change_contact(args, contacts):
    name, new_phone = args
    if not validate_phone_number(new_phone):  # Перевіряємо новий номер телефону
        return "Please enter a phone number in the format: 0XXXXXXXXX (10 digits starting with 0)."
    if name in contacts:
        contacts[name] = new_phone
        return f"Contact '{name}' changed to new phone number '{new_phone}'."
    else:
        raise KeyError("Contact not found.")

def phone_error(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except KeyError:
            return "Contact not found."
        except IndexError:
            return "Please provide a name."
    return wrapper

@phone_error
def get_phone(args, contacts):
    name = args[0]
    if name in contacts:
        return f"Phone number for '{name}': {contacts[name]}"


def list_contacts(contacts):
    if contacts:
        return "\n".join(f"{name}: {phone}" for name, phone in contacts.items())
    else:
        return "No contacts found."

def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, args = parse_input(user_input)  # args - це список

        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "change":
            print(change_contact(args, contacts))
        elif command == "phone":
            print(get_phone(args, contacts))  # Викликаємо нову функцію
        elif command == "all":
            print(list_contacts(contacts))  # Викликаємо функцію для виводу всіх контактів
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()
