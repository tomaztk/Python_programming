contacts = {}

while True:
    print("\nContact Book")
    print("1. Add Contact")
    print("2. Update Contact")
    print("3. Search Contact")
    print("4. Exit")
    choice = input("Choose an option: ")
    
    if choice == '1':
        name = input("Enter name: ")
        phone = input("Enter phone: ")
        email = input("Enter email: ")
        contacts[name] = {'phone': phone, 'email': email}
        print("Contact added.")
    elif choice == '2':
        name = input("Enter name to update: ")
        if name in contacts:
            phone = input("Enter new phone: ")
            email = input("Enter new email: ")
            contacts[name] = {'phone': phone, 'email': email}
            print("Contact updated.")
        else:
            print("Contact not found.")
    elif choice == '3':
        print(contacts)
        name = input("Enter name to search: ")
        if name in contacts:
            print(f"Name: {name}")
            print(f"Phone: {contacts[name]['phone']}")
            print(f"Email: {contacts[name]['email']}")
        else:
            print("Contact not found.")
    elif choice == '4':
        break
    else:
        print("Invalid option.")