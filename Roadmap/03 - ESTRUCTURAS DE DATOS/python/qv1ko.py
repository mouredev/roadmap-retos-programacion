contacts = {}
run = True

while run:

    option = input("Select one option:\n1) Search contact\n2) Create contact\n3) Update contact\n4) Delete contact\n0) Exit\n>> ")
    
    if option == "1":
        if len(contacts) > 0:
            name = input("Enter the name of the contact\n>> ")
            if name in contacts:
                phone = contacts[name]
                print(f"\n>> {name} - {phone}")
            else:
                print("\n>> Contact does not exist")
        else:
            print("\n>> You have no contacts")
    
    elif option == "2":
        name = input("Enter the name of the new contact\n>> ")
        while True:
            phone = input("Type the phone number of the new contact\n>> ")
            if phone.isdigit() and 9 <= len(phone) <= 11:
                break
            else:
                print("Phone number must be between 9 and 11 digits.")
        contacts[name] = phone
    
    elif option == "3":
        if len(contacts) > 0:
            name = input("Type the name of the contact to update\n>> ")
            if name in contacts:
                while True:
                    phone = input("Type the phone number\n>> ")
                    if phone.isdigit() and 9 <= len(phone) <= 11:
                        break
                    else:
                        print("Phone number must be between 9 and 11 digits.")
                contacts[name] = phone
                print(f"\n>> {name} - {phone}")
            else:
                print("\n>> Contact does not exist")
        else:
            print("\n>> You have no contacts")
    
    elif option == "4":
        name = input("Type the name of the contact to delete\n>> ")
        if name in contacts:
            del contacts[name]
            print(f"\n>> Contact {name} deleted.")
        else:
            print("\n>> Contact does not exist")
    
    elif option == "0":
        run = False
        print("Leaving...")
    
    else:
        print("\n>> Invalid option")
