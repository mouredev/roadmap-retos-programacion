# --- DATA STRUCTURES ---

# --- LISTS ---
print("\n LISTS: Ordered mutable collectio that allows duplicate elements")

my_list = [0, 1, 2, 3, 4, 5]

# INSERT
print("\n\t INSERT")

my_list.append(6) # Insert value at the end of a list
print(f"\t Insert using .append(): {my_list}")

my_list.insert(0, -1) # .insert(position, value)
print(f"\t Insert using .insert(): {my_list}")

# DELETE
print("\n\t DELETE")
my_list.remove(-1) # Specify value to be deleted
print(f"\t Deleting using .remove(): {my_list}")

my_list.pop(0) # Specify index of the value to be deleted. If not, it removes the las element
print(f"\t Deleting using .pop(): {my_list}")

del my_list[0] # Deletes the element at the specified index
print(f"\t Deleting using del: {my_list}")

# UPDATE
print("\n\t UPDATE")

my_list[0] = 1 # Change the value of the position specified with the new one
print(f"\t Update using indexation: {my_list}")

# ORDER
print("\n\t ORDER")

my_list.sort(reverse=True) # Ascending default, if reverse TRUE descending
print(f"\t Ordering using .sort(): {my_list}")

sorted(my_list) # Returns a new sorted list
print(f"\t Ordering using sorted: {my_list}")





# --- TUPLES ---
print("\n TUPLES: Ordered, inmutable collection that allows duplicate elements")

my_tuple = (1, 2, 3, 4, 5, 6)

# INSERT, DELETE, UPDATE
print("\n\t INSERT, DELETE, UPDATE")

print(f"\t Tuples are inmutable so we cannot insert, update or delete data!")

# ORDER
print("\n\t ORDER")

sorted(my_tuple) # Returns a new sorted list from a tuple
print(f"\t Ordering using sorted: {my_tuple} and type: {type(my_tuple)}")





# --- SETS ---
print("\n SETS: Unordered, mutable collection with no duplcate elements")

my_set = {1, 2, 3, 4, 5, 6}

# INSERT
print("\n\t INSERT")

my_set.add(7) # Adds an element to the set
print(f"\t Insert using .add(): {my_set}")

my_set.update([8, 9, 10, 10]) # Adds several elements to the set
print(f"\t Insert using .update(): {my_set}")

# DELETE
print("\n\t DELETE")

my_set.remove(10) # Removes a specific element (raises an error if the element is not found)
print(f"\t Deleting using .remove(): {my_set}")

my_set.discard(9) # Removes a specific element (Do not raise an error if the element is not found)
print(f"\t Deleting using .discard(): {my_set}")

my_set.pop() # Removes and returns an arbitrary element
print(f"\t Deleting using .pop(): {my_set}")

my_set.clear() # Removes all elements from the set
print(f"\t Deleting using .clear(): {my_set}")

# UPDATE
print("\n\t UPDATE")

print("\t Sets are unorderes, so elements cannot be updated directly. We must remove the old element and add the new one")

# ORDER
print("\n\t ORDER")

print("\t Sets do not have order, so ordering is not applicable")





# --- DICTIONARIES ---
print("\n DICTIONARIES: Unorderes, mutable collection of key-value pairs")

my_dict = {
    "name" : "Jesus",
    "surname" : "Adraz",
    "age" : 28,
    "email" : "adrazj96@gmail.com"
}

# INSERT
print("\n\t INSERT")

my_dict["phone_number"] = "+584140270337" # Adds a new key-value par or updates the value if the key already exists
print(f"\t Insert using [key]: {my_dict}")

# DELETE
print("\n\t DELETE")

my_dict.pop("email") # Removes and returns the value associated with the key
print(f"\t Deleting using .pop(): {my_dict}")

del my_dict["phone_number"] # Deletes the key-value pair
print(f"\t Deleting using del: {my_dict}")

my_dict.clear() # Removes all key-value pairs from the dictionary
print(f"\t Deleting using .clear(): {my_dict}")

# UPDATE
print("\n\t UPDATE")

my_dict["email"] = "adrazj96@gmail.com"
print(f"\t Update using [key]: {my_dict}")

my_dict.update({
    "name" : "Jesus",
    "surname" : "Adraz",
    "age" : 28,
})
print(f"\t Update using .update(): {my_dict}")

# ORDER
print("\n\t ORDER")

my_dict_2 = dict(sorted(my_dict.items(), reverse=False)) # We need to create a new dictionary variable to sort it
print(f"\t Order using sorted: {my_dict_2}")





# --- STRINGS ---
print("\n STRINGS: Inmutable sequence of characters")

my_string = "Jesus"

# INSERT, DELETE, UPDATE
print("\n\t INSERT, DELETE, UPDATE")
print(f"\t Strings are immutable, so elements cannot be inserted, updated, or deleted after creation. We can create a new string with the desired changes.")

# ORDER
print("\n\t ORDER")
print(f"\t Strings are inherently ordered by their character sequence.")

my_string_2 = ''.join(sorted(my_string))
print(f"\t Order using sorted: {my_string_2}")

"""
 * DIFICULTAD EXTRA (opcional):
 * Crea una agenda de contactos por terminal.
 * - Debes implementar funcionalidades de búsqueda, inserción, actualización y eliminación de contactos.
 * - Cada contacto debe tener un nombre y un número de teléfono.
 * - El programa solicita en primer lugar cuál es la operación que se quiere realizar, y a continuación
 *   los datos necesarios para llevarla a cabo.
 * - El programa no puede dejar introducir números de teléfono no númericos y con más de 11 dígitos.
 *   (o el número de dígitos que quieras)
 * - También se debe proponer una operación de finalización del programa.
 */
"""

def my_agenda():

    print("\n")

    agenda = {}

    while True:

        print("1. Search contact")
        print("2. Add contact")
        print("3. Update contact")
        print("4. Delete contact")
        print("5. Exit")

        option = input("Choose an option: ")

        match option:
            # Search contact
            case "1" :
                name = input("Enter the name you want to search for: ")

                if name in agenda:
                    print(f"The phone number of {name} is: {agenda[name]}")
                else:
                    print(f"The name {name} was not found!")
            
            # Add contact
            case "2" :
                name = input("Enter the name: ")
                phone_number = input("Enter the phone number: ")

                if phone_number.isdigit() and len(phone_number) > 0 and len(phone_number) <= 11:
                    agenda[name] = phone_number
                else:
                    print("You must enter a valid phone number less or equal than 11 digits")
            
            # Update contact
            case "3" :
                name = input("Enter the contact name to be updated: ")

                if name in agenda:
                    phone_number = input("Enter the new phone number: ")

                    if phone_number.isdigit() and len(phone_number) > 0 and len(phone_number) <= 0:
                        agenda[name] = phone_number
                else:
                    print(f"The contact {name} was not found")
            
            # Delete contact
            case "4" :
                name = input("Enter the contact name to be deleted: ")

                if name in agenda:
                    del agenda[name]
                else:
                    print(f"The contact {name} was not found!")
            
            # Close agenda
            case "5" :
                print("Closing agenda!")
                break
            
            # Invalid option
            case "" :
                print("Option not valid. Please, choose an option from 1 to 5")

my_agenda()