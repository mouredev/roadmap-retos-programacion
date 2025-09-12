# Sets
print("SETS")
my_set = {4, 3, 1, 2}
print(my_set)

# Insert
my_set.add(5)
print(my_set)

# Deleted
my_set.remove(1)
print(my_set)

# Can't sort by default, need to cast to list to be sorted and cast again to set
print(set(sorted(my_set)))

# Lists
print("LISTS")
my_list = [1, 2, 3, 4]
print(my_list)

# Insert
my_list.append(5)
print(my_list)
my_list.insert(0, 6)
print(my_list)

# Read
print(my_list[2])

# Update
my_list[2] = 9
print(my_list)

# Delete
my_list.remove(3)
print(my_list)

# Sort
my_list.sort()
print(my_list)

# Tuples
print("TUPLES")
my_tuple = (4, 2, 3, 1)
print(my_tuple)

# Read
print(my_tuple[1])

# Can't sort by default, need to cast to list to be sorted and cast again to set
print(tuple(sorted(my_tuple)))

# Dicts / hashmaps
print("DICTS")
my_dict = {"one": 1, "two": 2, "three": 3, "four": 4}
print(my_dict)

# Insert
my_dict["five"] = 5
print(my_dict)

# Read
print(my_dict["five"])
print(my_dict.get("five"))

# Update
my_dict["five"] = 55
print(my_dict)

# Delete
my_dict.pop("two")
print(my_dict)

# Sort by key (keys must be same type)
print(dict(sorted(my_dict.items())))

# Sort by value (values must be same type)
print(dict(sorted(my_dict.items(), key=lambda x: x[1])))


# EXTRA
def agenda():
    agenda = {}

    def show_menu():
        print("(1) Insert contact")
        print("(2) Search contact")
        print("(3) Update contact")
        print("(4) Remove contact")
        print("(5) Close program")

    def is_valid_phone(phone: str) -> bool:
        return phone.isdigit() and len(phone) > 0 and len(phone) <= 11

    def ask_for_name():
        return input("Contact name: ")

    def ask_for_phone():
        phone = input("Contact phone: ")
        if not is_valid_phone(phone):
            print("Invalid phone number.")
            return
        return phone

    def insert_contact():
        name = ask_for_name()
        if name in agenda:
            print("Contact already exists. Choose update option.")
            return

        phone = ask_for_phone()
        if phone is None:
            return  # invalid phone

        agenda[name] = phone
        print("Contact saved.")

    def search_contact():
        name = ask_for_name()
        if name in agenda:
            print(f"Contact {name}. Phone: {agenda[name]}")
        else:
            print("Contact not found.")

    def update_contact():
        name = ask_for_name()
        if name not in agenda:
            print("Contact not found.")
            return

        phone = ask_for_phone()
        if phone is None:
            return  # invalid phone

        agenda[name] = phone
        print("Contact updated.")

    def remove_contact():
        name = ask_for_name()
        if name not in agenda:
            print("Contact not found.")
            return

        agenda.pop(name)
        print("Contact removed.")

    while True:
        show_menu()
        option = input("Select an option: ")
        if option == '1':
            insert_contact()
        elif option == '2':
            search_contact()
        elif option == '3':
            update_contact()
        elif option == '4':
            remove_contact()
        elif option == '5':
            print("Exiting...")
            break
        else:
            print("Choose a correct option.")


agenda()
