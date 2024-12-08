"""
 * Estruturas de datos
"""

# Lista

my_list = [1, 1, 2, 3, 5, 6]
print(my_list)
print(type(my_list))

my_list.insert(4, 4)  # Inserción
print(my_list)

my_list.remove(6)  # Borrado
print(my_list)

my_list[0] = 0  # Actualización
print(my_list)

my_list.sort(reverse=True)  # Ordenación descendente
print(my_list)

# Tupla

my_tuple = (1, 2, 3, 4, 5)
print(my_tuple)
print(type(my_tuple))

# Set

my_set = {1, 2, 3, 4, 5}
print(my_set)
print(type(my_set))

my_set.add(6)  # Inserción
print(my_set)

my_set.remove(6)  # Borrado
print(my_set)

# Diccionario

my_dict = {
    "Month": "April",
    "Day": "Monday",
    "Year": 2024
}
print(my_dict)
print(type(my_dict))

my_dict["Century"] = "XXI"  # Inserción
print(my_dict)

del my_dict["Century"]  # Borrado
print(my_dict)

my_dict["Month"] = "August"  # Actualización
print(my_dict)

my_dict = dict(sorted(my_dict.items()))  # Ordenación
print(my_dict)

"""
 * Extra
"""

def menu():
    print("=====================================")
    print("WELCOME TO THE CONTACTS AGENDA")
    print("1. Search contact")
    print("2. Insert contact")
    print("3. Update contact")
    print("4. Delete contact")
    print("5. Exit")
    print("=====================================")

menu()

def contacts_agenda():

    agenda = {}

    def validate_phone_number(phone):
        return phone.isdigit() and len(phone) == 10

    while True:
        option = input("Choose an option: ")

        match option:
            case "1":
                name = input("Enter the name to search: ")
                if name in agenda:
                    print(f"The phone number of {name} is {agenda[name]}")
                else:
                    print("Contact not found")
            case "2":
                name = input("Enter the name to insert: ")
                phone = input("Enter the phone: ")
                if validate_phone_number(phone):
                    agenda[name] = phone
                    print("Contact inserted")
                else:
                    print("Invalid phone number")
            case "3":
                name = input("Enter the name to update the phone: ")
                if name in agenda:
                    phone = input("Enter the new phone: ")
                    if validate_phone_number(phone):
                        agenda[name] = phone
                        print("Contact updated")
                    else:
                        print("Invalid phone number")
                else:
                    print("Contact not found")
            case "4":
                name = input("Enter the name to delete: ")
                if name in agenda:
                    del agenda[name]
                    print("Contact deleted")
                else:
                    print("Contact not found")
            case "5":
                print("Exiting...")
                break
            case _:
                print("Invalid option... Retry")

contacts_agenda()