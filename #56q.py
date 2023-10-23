#56q


address_book = {}


def add_contact(name, phone_number, email):
    if name not in address_book:
        address_book[name] = {'Phone': phone_number, 'Email': email}
        print(f"Added {name} to the address book.")
    else:
        print(f"{name} is already in the address book. Use 'update_contact' to modify their details.")


def update_contact(name, phone_number, email):
    if name in address_book:
        address_book[name]['Phone'] = phone_number
        address_book[name]['Email'] = email
        print(f"Updated {name}'s contact information.")
    else:
        print(f"{name} is not in the address book. Use 'add_contact' to create a new entry.")


def view_contact(name):
    if name in address_book:
        contact = address_book[name]
        print(f"Name: {name}")
        print(f"Phone: {contact['Phone']}")
        print(f"Email: {contact['Email']}")
    else:
        print(f"{name} is not in the address book.")


def list_contacts():
    print("Address Book:")
    for name, contact in address_book.items():
        print(f"Name: {name}, Phone: {contact['Phone']}, Email: {contact['Email']}")


while True:
    print("\nAddress Book Menu:")
    print("1. Add Contact")
    print("2. Update Contact")
    print("3. View Contact")
    print("4. List All Contacts")
    print("5. Quit")

    choice = input("Enter your choice (1/2/3/4/5): ")

    if choice == '1':
        name = input("Enter the name: ")
        phone_number = input("Enter the phone number: ")
        email = input("Enter the email: ")
        add_contact(name, phone_number, email)
    elif choice == '2':
        name = input("Enter the name to update: ")
        phone_number = input("Enter the updated phone number: ")
        email = input("Enter the updated email: ")
        update_contact(name, phone_number, email)
    elif choice == '3':
        name = input("Enter the name to view: ")
        view_contact(name)
    elif choice == '4':
        list_contacts()
    elif choice == '5':
        break
    else:
        print("Invalid choice. Please select a valid option.")
