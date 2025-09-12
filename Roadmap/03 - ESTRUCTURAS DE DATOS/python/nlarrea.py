"""
 * EJERCICIO:
 * - Muestra ejemplos de creación de todas las estructuras soportadas por defecto en tu lenguaje.
 * - Utiliza operaciones de inserción, borrado, actualización y ordenación.
 *
 * DIFICULTAD EXTRA (opcional):
 * Crea una agenda de contactos por terminal.
 * - Debes implementar funcionalidades de búsqueda, inserción, actualización y eliminación de contactos.
 * - Cada contacto debe tener un nombre y un número de teléfono.
 * - El programa solicita en primer lugar cuál es la operación que se quiere realizar, y a continuación
 *   los datos necesarios para llevarla a cabo.
 * - El programa no puede dejar introducir números de teléfono no numéricos y con más de 11 dígitos.
 *   (o el número de dígitos que quieras)
 * - También se debe proponer una operación de finalización del programa.
"""

# LISTS

from audioop import reverse


fruits = ["apple", "orange", "pear", "banana"]

# Insert new items

fruits.append("melon")
fruits.insert(2, "strawberry")
print(fruits)
# ['apple', 'orange', 'strawberry', 'pear', 'banana', 'melon']

fruits = ["apple", "orange", "pear", "banana"]
fruits.extend(["melon", "strawberry"])  # add multiple items at the end
print(fruits)  # ['apple', 'orange', 'pear', 'banana', 'melon', 'strawberry']

# Remove items from list

fruits.pop(2)  # removes by index -> IndexError if item not found
fruits.remove("melon")  # removes by value -> ValueError if item not found
print(fruits)  # ['apple', 'orange', 'banana', 'strawberry']

# Update the list

# Negative indexes -> from back to front
fruits[-1] = "banana"
print(fruits)  # ['apple', 'orange', 'banana', 'banana']

# Positive indexes -> from front to back
fruits[2] = "pear"
print(fruits)  # ['apple', 'orange', 'pear', 'banana']

# Order lists

# Ascending order -> without modifying the original
asc_fruits = sorted(fruits)
print(asc_fruits)  # ['apple', 'banana', 'orange', 'pear']
print(fruits)  # ['apple', 'orange', 'pear', 'banana']

# Ascending order -> modifying the original
fruits.sort()
print(fruits)  # ['apple', 'banana', 'orange', 'pear']

# Descending order -> without modifying the original
des_fruits = list(reversed(fruits))
print(des_fruits)  # ['pear', 'orange', 'banana', 'apple']
print(fruits)  # ['apple', 'banana', 'orange', 'pear']

# Descending order -> modifying the original
fruits.reverse()
print(fruits)  # ['pear', 'orange', 'banana', 'apple']

# SETS -> remove duplicates

fruit_set = {"apple", "orange", "pear", "banana", "banana"}
print(fruit_set)
# {'pear', 'orange', 'banana', 'apple'} -> it also modifies the order

# Insert new items

fruit_set.add("melon")
print(fruit_set)  # {'pear', 'melon', 'banana', 'orange', 'apple'}

# Remove one item

fruit_set.remove("pear")  # if item not found -> KeyError
print(fruit_set)  # {'melon', 'apple', 'banana', 'orange'}

fruit_set.discard("orange")  # if item not found -> nothing happens
print(fruit_set)

# Remove all

fruit_set.clear()
print(fruit_set)  # set()

# DICTIONARIES

person = {"name": "Naia", "age": 25}

# Insert new data

person["country"] = "Spain"
print(person)
# {'name': 'Naia', 'age': 25, 'country': 'Spain'}

# Update data

person["age"] = 26
print(person)
# {'name': 'Naia', 'age': 26, 'country': 'Spain'}

# Remove data

# .pop() -> receives a key and returns the removed value
person.pop("country")  # if key not found -> KeyError
print(person)
# {'name': 'Naia', 'age': 26}

person.pop("country", "Not country found")
# default value given -> no error raising, returns default
print(person)
# {'name': 'Naia', 'age': 26}


"""
/* DIFICULTAD EXTRA (opcional):
 * Crea una agenda de contactos por terminal.
 * - Debes implementar funcionalidades de búsqueda, inserción, actualización y eliminación de contactos.
 * - Cada contacto debe tener un nombre y un número de teléfono.
 * - El programa solicita en primer lugar cuál es la operación que se quiere realizar, y a continuación
 *   los datos necesarios para llevarla a cabo.
 * - El programa no puede dejar introducir números de teléfono no numéricos y con más de 11 dígitos.
 *   (o el número de dígitos que quieras)
 * - También se debe proponer una operación de finalización del programa.
 */
"""

contact_list: list[dict] = []


def print_menu():
    print("\nWhat do you want to do?")
    print("1. Add contact")
    print("2. Find contact")
    print("3. Update contact")
    print("4. Remove contact")
    print("5. View contact list")
    print("6. Exit")


def print_contact_data(
    name: str, number: str, print_message: bool = True
) -> None:
    if print_message:
        print("\nHere is the contact data:")

    print(f" - Name: {name}")
    print(f" - Phone: {number}")


def print_contact_list() -> None:
    if len(contact_list) == 0:
        print("\nThere are not contacts yet.")
        return

    print("\nThese are the stored contacts:")
    for contact in contact_list:
        print_contact_data(**contact, print_message=False)
        print()


def check_correct_phone(number: str) -> bool:
    if len(number) > 11:
        print("\nThe phone number must be less than 11 characters length.")
    elif not number.isdigit():
        print("\nThe phone number must be a number.")
    else:
        return True

    return False


def add_contact(name, number) -> bool:
    is_correct_phone = check_correct_phone(number)

    if not is_correct_phone:
        return False

    if find_contact_by_name(name):
        print("\nThe introduced name already exists.")
        return False

    contact_list.append({"name": name, "number": number})
    print("\nThe new contact has been created.")
    print_contact_data(name, number)
    return True


def find_contact_by_name(name_to_find) -> dict | None:
    try:
        return [
            contact
            for contact in contact_list
            if contact.get("name") == name_to_find
        ][0]
    except IndexError:
        return None


def find_contact_index(name, number) -> int | None:
    try:
        return contact_list.index({"name": name, "number": number})
    except ValueError:
        return None


def update_contact(old_data, new_data) -> bool:
    contact_index = find_contact_index(**old_data)

    if contact_index is None:
        print("\nThe contact doesn't exist.")
        return False

    contact_list[contact_index] = {**new_data}
    print_contact_data(**new_data)
    return True


def remove_contact(name, number) -> bool:
    contact_index = find_contact_index(name, number)

    if contact_index is None:
        print("\nThe contact doesn't exist.")
        return False

    removed_contact = contact_list.pop(contact_index)
    print("\nContact removed successfully.")
    print("This is the removed data:")
    print_contact_data(**removed_contact, print_message=False)
    return True


def run():
    print_menu()
    option = input("Select your option (1-6): ")

    if option == "1":
        # ADD CONTACT

        new_name = input("\nEnter the new name:\n> ")

        contact = find_contact_by_name(new_name)
        if contact:
            print("\nThe contact already exists. Use another name instead.")
            run()

        new_number = input("Enter the new phone number:\n> ")

        add_contact(new_name, new_number)
        run()

    elif option == "2":
        # FIND CONTACT

        name = input("\nEnter the name to find:\n> ")

        contact = find_contact_by_name(name)
        if not contact:
            print("\nNo contact has been found.")
        else:
            print_contact_data(**contact)

        run()

    elif option == "3":
        # UPDATE CONTACT

        old_name = input("\nEnter the name of the contact to update:\n> ")

        contact = find_contact_by_name(old_name)
        if not contact:
            print("\nThe contact doesn't exist.")

        new_data = {**contact}
        print("\nWhat do you want to update?")
        print("1. Contact name")
        print("2. Contact phone number")
        modifier = input("Select (1-2): ")

        if modifier == "1":
            new_data["name"] = input("\nEnter the new name:\n> ")
            update_contact(contact, new_data)
        elif modifier == "2":
            new_number = input("\nEnter the new number:\n> ")

            is_correct_number = check_correct_phone(new_number)
            if not is_correct_number:
                run()

            new_data["number"] = new_number
            update_contact(contact, new_data)
        else:
            print("\nNot a correct option.")

        run()

    elif option == "4":
        # REMOVE CONTACT

        c_name = input("\nEnter the name of the contact to remove:\n> ")

        contact = find_contact_by_name(c_name)
        if not contact:
            print("\nThe contact doesn't exist.")
            run()

        remove_contact(**contact)
        run()

    elif option == "5":
        # VIEW CONTACT LIST

        print_contact_list()
        run()

    elif option == "6":
        # EXIT

        return

    else:
        print("\nOption not allowed.")
        run()


run()
