import sys
"""
* EJERCICIO:
Muestra ejemplos de creación de todas las estructuras soportadas por defecto en tu lenguaje.
Utiliza operaciones de inserción, borrado, actualización y ordenación.
"""


# **** LIST ****
def data_structure_list():
    ordinal_numbers = ['Second', 'Fourth', 'First']  # Create a list
    ordinal_numbers.remove('Fourth')  # Remove an element from the list
    ordinal_numbers.append('Third')  # Append/add an element to the list
    ordinal_numbers.sort()  # Sort the list
    first_element = ordinal_numbers[0]  # Accessing an element within
    ordinal_numbers.clear()  # Clear the list


# **** TUPLE ****
def data_structure_tuple():
    users_category = (1, 2, 'Trial', 'Freemium', 'Premium', 'Pro')  # Create a tuple
    category_slice = users_category[2:]  # Slicing the tuple
    non_users_category = (-1, -2, 'ex member', 'non member')  # Create a second tuple
    all_categories = users_category + non_users_category  # Concatenation of two tuples
    is_premium_in_categories = 'Premium' in all_categories  # Verification that the element 'Premium' is in tuple
    premium_element_count = all_categories.count('Premium')  # Count how many times 'Premium' is in the tuple


# **** DICTIONARIES ****
def data_structure_dictionaries():
    players_stats = {'Jordan': 32292, 'Bryant': 33643, 'James': 46675}  # Create a dictionary
    bryant_points = players_stats['Bryant']  # Accessing the value in the key 'Bryant'
    players_stats['James'] = 46676  # Updating the value of the key 'James'
    players_stats['Kareem'] = 38387  # Adding a new value in the dictionary
    del players_stats['Jordan']  # Removing the element 'Jordan' from the dictionary
    is_jordan_in_stats = 'Jordan' in players_stats  # Checking if the element 'Jordan' is in the dictionary
    dictionary_keys = list(players_stats.keys())  # Getting the keys of the dictionary
    dictionary_values = list(players_stats.values())  # Getting the values of the dictionary
    soccer_stats = {'Messi': 821, 'Ronaldo': 873}  # Create a second dictionary
    players_stats.update(soccer_stats)  # Merge the 'Soccer_stats' into the players stats
    players_stats.clear()  # Clearing the players_stats dictionary


# **** SETS ****
def data_structure_sets():
    students_set = {'Brandon', 'Cavero', 'Brandon', 'Andres'}  # Creating a set
    students_set.add('Moure')  # Adding the element 'Moure' to students_set
    students_set.remove('Cavero')  # Remove the element 'Cavero' from the student_set
    is_andres_in_students = 'Andres' in students_set
    second_students_sets = {'Brandon', 'Kobe', 'Jordan'}  # Create a second set of elements
    union_students_sets = students_set | second_students_sets  # Union of both sets
    intersection_students_sets = students_set & second_students_sets  # Intersection of both sets
    difference_students_sets = students_set - second_students_sets  # Difference of both sets
    symmetric_students_sets = students_set ^ second_students_sets  # Symmetric difference of both sets
    students_set.clear()  # Clearing the students_set

"""
DIFICULTAD EXTRA (opcional) Crea una agenda de contactos por terminal:
- Debes implementar funcionalidades de búsqueda, inserción, actualización y eliminación de contactos.
- Cada contacto debe tener un nombre y un número de teléfono.
- El programa solicita en primer lugar cuál es la operación que se quiere realizar, y a continuación los datos  necesarios para llevarla a cabo.
- El programa no puede dejar introducir números de teléfono no númericos y con más de 11 dígitos (o el número de dígitos que quieras).
- También se debe proponer una operación de finalización del programa. 
"""


def display_menu():
    print('**** MENU ****\n'
          '1. Search contact\n'
          '2. Insert contact\n'
          '3. Update contact\n'
          '4. Remove contact\n'
          '5. Close\n')
    option = input('Select an option: ')
    try:
        option = int(option)
    except ValueError:
        print('Input an integer value between 1 and 5')
        display_menu()

    if 0 < int(option) <= 5:
        if int(option) == 1:
            search_contact()
        elif int(option) == 2:
            insert_contact()
        elif int(option) == 3:
            update_contact()
        elif int(option) == 4:
            remove_contact()
        elif int(option) == 5:
            sys.exit()
    else:
        print('Select a correct option between 1 and 5\n')
        display_menu()


def search_contact():
    print('**** SEARCH CONTACT ****')
    name = input('Input the name of the contact: ')
    if agenda.get(name) is not None:
        print(f'{name}', ':', agenda.get(name))
        display_menu()
    else:
        print(f'No contact with name {name} was found')
        display_menu()


def phone_number_input(name):
    phone_number = input('Phone number: ')
    if phone_number.isnumeric() and len(phone_number) <= 11:
        agenda[name] = int(phone_number)
        print(f'Contact {name} was successfully saved with phone number {phone_number}')
        display_menu()
    else:
        print('Phone number must be a number with less than 11 digits, please try again')
        phone_number_input(name)


def insert_contact():
    print('**** INSERT CONTACT ****')
    name = input('Name of the contact: ')
    phone_number_input(name)


def update_contact():
    print('**** UPDATE CONTACT ****')
    name = input('Enter the contact name to update: ')
    if name in agenda:
        phone_number_input(name)
    else:
        print('Contact was not found, try again')
        update_contact()


def remove_contact():
    print('**** REMOVE CONTACT ****')
    name = input('Enter the contact name to remove: ')
    if name in agenda:
        del agenda[name]
        print(f'Contact {name} was successfully removed from the agenda')
        display_menu()
    else:
        print('Contact was not found, try again')
        remove_contact()


agenda = dict()
display_menu()
