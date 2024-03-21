def main():
    while True:
        print("\nContact Agenda System")
        print("1. Add Contact")
        print("2. Remove Contact")
        print("3. Edit Contact")
        print("4. Search Contact")
        print("5. Show All Contacts")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            name = input("Enter name: ")
            phone = input("Enter phone number: ")
            agenda.add_contact(name, phone)
        elif choice == '2':
            name = input("Enter name to remove: ")
            agenda.remove_contact(name)
        elif choice == '3':
            name = input("Enter name to edit: ")
            new_phone = input("Enter new phone number: ")
            agenda.edit_contact(name, new_phone)
        elif choice == '4':
            name = input("Enter name to search: ")
            agenda.search_contact(name)
        elif choice == '5':
            agenda.show_all_contacts()
        elif choice == '6':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please enter a valid option.")

if _name_ == "_main_":
    main()