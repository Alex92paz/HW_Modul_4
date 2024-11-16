def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

def add_contact(args, contacts):
    name, phone = args
    contacts[name] = phone
    return "Contact added."

def change_username_phone(args, contacts):
    name, phone = args
    if name in contacts:
        contacts[name] = phone
    return "Contact updated."

def find_phone(args,contacts):
    name = args[0]
    if name in contacts:
        return f"{name}'s phone number is {contacts[name]}."
    else:
        return "Contact not found."  

def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        try:
            user_input = input("Enter a command: ")
            command, *args = parse_input(user_input)

            if command in ["close", "exit"]:
                print("Good bye!")
                break

            elif command == "hello":
                print("How can I help you?")

            elif command == "add":
                print(add_contact(args, contacts))

            elif command == "change":
                print(change_username_phone(args, contacts))

            elif command == "find":
                print(find_phone(args, contacts))

            elif command == "all":
                print(contacts)

            else:
                print("Invalid command.")

        except ValueError:
            print("not enough values to unpack (expected 2, got 0)")
            continue

if __name__ == "__main__":
    main()
