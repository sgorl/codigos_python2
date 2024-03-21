contacts = {}

def add_contact(name, phone):
    contacts[name] = phone
    print(f"Contact {name} added successfully.")

def remove_contact(name):
    if name in contacts:
        del contacts[name]
        print(f"Contact {name} removed successfully.")
    else:
        print(f"Contact {name} not found.")

def edit_contact(name, new_phone):
    if name in contacts:
        contacts[name] = new_phone
        print(f"Contact {name} edited successfully.")
    else:
        print(f"Contact {name} not found.")

def search_contact(name):
    if name in contacts:
        print(f"Contact found: {name}, {contacts[name]}")
    else:
        print(f"Contact {name} not found.")

def show_all_contacts():
    if contacts:
        print("All Contacts:")
        for name, phone in contacts.items():
            print(f"{name}: {phone}")
    else:
        print("No contacts found.")
