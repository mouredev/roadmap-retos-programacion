"""
Structures of Data - Python
"""

# Lists

my_list: list = ["GTA", "LOL", "FIFA", "PES", "AOE", "COD"]
print(my_list)

my_list.append("CS")  # Insertion
my_list.append("TFT")

my_list.remove("FIFA")  # Deletion

my_list[1] = "Valorant"  # Update

my_list.sort()  # Sorting

print(my_list)
print(type(my_list))

# Tuples

my_tuple: tuple = ("GTA", "LOL", "FIFA", "PES", "AOE", "COD")
print(my_tuple)

print(my_tuple[1])  # Access
print(my_tuple[3])

# Tuples are immutable: insertion, deletion and update require converting to a list, modifying it, and converting back.
# Insertion
temp = list(my_tuple)
temp.append("CS")
my_tuple = tuple(temp)

# Deletion
temp = list(my_tuple)
temp.remove("FIFA")
my_tuple = tuple(temp)

# Update
temp = list(my_tuple)
temp[1] = "Valorant"
my_tuple = tuple(temp)

my_tuple = tuple(sorted(my_tuple))  # Sorting

print(my_tuple)
print(type(my_tuple))

# Sets

my_set: set = {"GTA", "LOL", "FIFA", "PES", "AOE", "COD"}
print(my_set)

my_set.add("CS")  # Insertion
my_set.add("TFT")
my_set.add("CS")  # Insertion (duplicate, will not be added)

my_set.remove("FIFA")  # Deletion

my_set.update({"Valorant", "TFT"})  # Update (adding new elements)

my_set = set(sorted(my_set))  # Sorting, but sets are unordered, so this will return a sorted list of the set elements.
print(my_set)
print(type(my_set))

# Dictionary

my_dict: dict = {
    "game1": "GTA",
    "game2": "LOL",
    "game3": "FIFA",
    "game4": "PES",
    "game5": "AOE",
    "game6": "COD"
}

my_personal_dict: dict = {
    "name": "Sergio",
    "alias": "elhdrond",
    "age": 35,
    "email": "myemail@domain.com",
    "hobbies": ["gaming", "programming", "reading"]
}
print(my_dict)
print(my_personal_dict)

print(my_dict["game2"])  # Access
print(my_dict["game4"])
print(my_personal_dict["hobbies"][1])  # Access

# Dictionary is mutable, so we can perform insertion, deletion, or update directly.

my_dict["game7"] = "CS"  # Insertion
del my_dict["game3"]  # Deletion
my_dict["game2"] = "Valorant"  # Update

my_personal_dict["married"] = True  # Insertion
my_personal_dict["hobbies"].append("traveling")  # Insertion in a list inside the dictionary
my_personal_dict["age"] = 36  # Update
del my_personal_dict["email"]  # Deletion

my_dict = dict(sorted(my_dict.items()))  # Sorting by keys
my_personal_dict = dict(sorted(my_personal_dict.items()))  # Sorting by keys

print(my_dict)
print(my_personal_dict)
print(type(my_dict))


"""
Extra Exercise
"""

def my_agenda():

    agenda = {}

    def add_contact(name, phone):
        agenda[name] = phone

    def search_contact(name):
        return agenda.get(name, "Contact not found.")

    def update_contact(name, phone):
        if name in agenda:
            agenda[name] = phone
        else:
            return "Contact not found."

    def delete_contact(name):
        if name in agenda:
            del agenda[name]
        else:
            return "Contact not found."

    def show_all_contacts():
        return agenda

    def order_contacts():
        return dict(sorted(agenda.items()))

    def check_phone_number(phone):
        return phone.isdigit() and len(phone) > 0 and len(phone) <= 11

    def main_menu():
        print("\n--- AGENDA ---")
        print("1. Search contact")
        print("2. Add contact")
        print("3. Update contact")
        print("4. Delete contact")
        print("5. Show all contacts")
        print("6. Order contacts")
        print("0. Exit")

    while True:
        # MENU
        main_menu()
        choice = input("\nEnter your choice: ")
        match choice:
            case '1':
                name = input("Enter the name to search: ")
                result = search_contact(name)
                print(result)
            case '2':
                name = input("Enter a name: ")           
                phone = input(f"Enter the phone number for {name}: ")
                if check_phone_number(phone):
                    add_contact(name, phone)
                else:
                    print("Invalid phone number. Please enter a valid phone number.")
            case '3':
                name = input("Enter the name to update: ")
                phone = input(f"Enter the new phone number for {name}: ")
                if check_phone_number(phone):
                    result = update_contact(name, phone)
                    print(result)
                else:
                    print("Invalid phone number. Please enter a valid phone number.")
            case '4':
                name = input("Enter the name to delete: ")
                result = delete_contact(name)
                print(result)
            case '5':
                print("\n--- All Contacts ---")
                for name, phone in show_all_contacts().items():
                    print(f"{name}: {phone}")
            case '6':
                agenda = order_contacts()
                print("Contacts ordered by name.")
            case '0':
                print("Exiting the agenda.")
                break
            case _:
                print("Invalid option. Please try again.")

my_agenda()