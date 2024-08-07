from enum import Enum

# @author Alberto Revel

"""
- Muestra ejemplos de creación de todas las estructuras soportadas por defecto en tu lenguaje.
"""

print("\n**** PART 1 - CREATING DATA STRUCTURES ****\n")


# PART 1.1 - Lists

print("\n** 1.1 - LISTS **\n")

list1 = []
list2 = list()
print(f"""There are two ways to create lists, that produces the same result
 - 'list1 = []' -> {list1}
 - 'list2 = list()' ->  {list2}\n""")

list1 = [1,2,True,'something',5,1]
list2 = list([1,2,True,'something',5,1])
print(f"""\nWe can initiate lists with some elements (that can have different types)
 - list1 = '[1,2,True,'something',5,1]' ->  {list1}
 - list2 = 'list([1,2,True,'something',5,1])' -> {list2}\n""")


# PART 1.2 - Sets

print("\n** 1.2 - SETS **\n")

set1 = {1,2,"3",True,1}
print("""Sets are created like lists but whitout duplicates (1 is equivalent to True)
 - 'set1 = {1,2,"3",True,1}' -> """ + f"{set1}\n")


# PART 1.3 - Tuples

print("\n** 1.3 - TUPLES **\n")

tuple1 = (1,2,"3",True,1)
print("""Tuples are inmutables lists
 - 'tuple1 = (1,2,"3",True,1)' -> """ + f"{tuple1}\n")


# PART 1.4 - Matrixes

print("\n** 1.4 - MATRIXES **\n")

matrix1 = [['X','O',' '], ['X','O',' '], ['O','X','X ']]
print(f"""A matrix is a list containing other lists
 - 'matrix1 = [['X','O',' '], ['X','O',' '], ['O','X','X ']]'
      -> {matrix1}\n""")


# PART 1.5 - Dictionaries

print("\n** 1.5 - DICTIONARIES **\n")

dictionary1 = {"name": "Alberto", "surname": "Revel", "birthYear": 1992}
print("""A dictionary contains key-value pairs
 - "dictionary1 = {'name': 'Alberto', 'surname': 'Revel', 'brithYear': 1992}'
      -> """+f"{dictionary1}\n")

dictionary2 = dict(name = "Alberto", surname = "Revel", birthYear = 1992)
print("""There's other way to create a dictionary
 - "dictionary2 = dict(name = "Alberto", surname = "Revel", birthYear = 1992)
      -> """+f"{dictionary2}\n")

"""
- Utiliza operaciones de inserción, borrado, actualización y ordenación.
"""


print("\n**** PART 2 - OPERATING WITH DATA STRUCTURES ****\n")


# PART 2.1 - List

print("\n** 2.1 - LIST **\n")
list3 = [5,2,-1,10,0]
print(f"Being the initial list : {list3}")
list3.append(2)
print(f" - We add the element '2' at the end with append(): {list3}")
list3.extend([5,9,1])
print(f" - We add the elements '[5,9,1]' at the end with extend() : {list3}")
list3.insert(2,4)
print(f" - We add the element '4' at the position 2 with insert(): {list3}")
list3+=[8,11]
print(f" - We add the elements '[8,11]' at the end through concatenation: {list3}")
list3.remove(2)
print(f" - We remove the first element '2' with remove() : {list3}")
list3.pop()
print(f" - We remove the last element with pop(): {list3}")
list3.pop(5)
print(f" - We remove the element at position 5 with pop(): {list3}")
list3.sort(reverse=True)
print(f" - We sort the list in reverse order with sort(reverse=): {list3}")
list3.clear()
print(f" - We remove all the elements with clear() : {list3}")

# PART 2.2 - Set

print("\n** 2.2 - SET **\n")
set2 = {5,2,-1,10,0}
print(f"Being the initial set : {set2}")
set2.add(3)
print(f" - We add the element '3' with add() : {set2}")
set2.add(3)
print(f" - We add the element '3' with add() (nothing happens because duplicates aren't possible in a set) : {set2}")
set2.update([5,9,1])
print(f" - We add the elements '[5,9,1]' with update() : {set2}")
set2.remove(2)
print(f" - We remove the element '2' with remove() : {set2}")
set2.discard(2)
print(f" - We remove the element '2' with discard() if present : {set2}")
set2.discard(3)
print(f" - We remove the element '3' with discard() if present : {set2}")
set2.pop()
print(f" - We remove an arbitrary element with pop() : {set2}")
set2.intersection_update({1,2,3,4,5,8,9,11})
print(" - We keep only the elements contained in set and in '{1,2,3,4,5,8,9,11}' with intersection_update(): "+f"{set2}")
set2.difference_update({1,2,8,6,10})
print(" - We remove the elements contained in '{1,2,8,6,10}' with difference_update(): "+f"{set2}")
set2.symmetric_difference_update({1,2,8,9,10})
print(" - We keep only the elements contained in set or in '{1,2,8,9,10}' but not both with symmetric_difference_update(): "+f"{set2}")
set2.clear()
print(f" - We remove all the elements with clear() : {set2}")

# PART 2.3 - Tuple

print("\n** 2.3 - TUPLE **\n")
tuple2 = (5,2,-1,10,0)
print(f"Being the initial tuple : {tuple2}")
tuple2+=(3,)
print(f" - We add the element '3' using the addition operator : {tuple2}")
tuple2+=(8,2)
print(f" - We add the elements '(8,2)' using the addition operator : {tuple2}")
tuple2 = tuple(sorted(tuple2))
print(f" - We sort the tuple by converting it to a list and then converting it to a tuple again : {tuple2}")


# PART 2.4 - Matrix

print("\n** 2.4 - Matrix **\n")
matrix2 = [['X','O','X'], ['X','O',' '], ['O','X','X ']]
print(f"Being the initial matrix : {matrix2}")
matrix2.append(['O','O','X'])
print(f" - We add the elements '['O','O','X']' with append() : {matrix2}")
matrix2.pop()
print(f" - We remove elements at the end with pop() : {matrix2}")
matrix2.sort()
print(f" - We sort matrixes with sort() : {matrix2}")
print("PS: As a matrix is a list of lists, all list operations are allowed")


# PART 2.5 - Dictionaries

print("\n** 2.5 - DICTIONARIES **\n")

dictionary3 = {"name": "Alberto", "surname": "Revel", "birthYear": 1992}
print(f"Being the initial dictionary : {dictionary3}")
dictionary3.update({"town" : "Barcelona"})
print(f" - We add elements from another dictionary with update() : {dictionary3}")
dictionary3["hairColor"]="brown"
print(f" - We add elements by assigning a value to a inexistent key with 'dictionary3['hairColour']= 'brown'' : {dictionary3}")
dictionary3 = dict(sorted(dictionary3.items()))
print(f" - We sort the items by its keys sorting the items with 'dict(sorted(dictionary3.items()))' : {dictionary3}")
dictionary3.pop("town")
print(f" - We remove the element by its key with pop() : {dictionary3}")
dictionary3.popitem()
print(f" - We remove a random element with popitem() : {dictionary3}")
dictionary3.clear()
print(f" - We remove all the elements with clear() : {dictionary3}")
print("\n\n")




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
"""

my_contact_book = {}
min_digits = 1
max_digits = 11


# Main Menu

def main_program():
     print("\n--> Welcome to the contacts book v3 <--")
     selected_op = 1
     while selected_op > 0:
          selected_op = query_user_input()
          perform_operation(selected_op)
     print("\n--> Ending program, See you soon! <--\n")


def query_user_input():
      selected_op = -1
      try:
            selected_op =  int(input("""\nPlease, try an operation by typying the operation number:
                  - 0: Exit
                  - 1: Search a contact
                  - 2: Add a contact
                  - 3: Update a contact
                  - 4: Delete a contact\n"""))
      except ValueError:
            print("Please, select a valid option")
            selected_op = query_user_input()
      return selected_op

def query_contact_name():
     contact_name = str(input("\nPlease, enter the name of the contact: "))

     try:
        validate_name(contact_name)
     except Exception as e:
        print("ERROR" + str(e))

     return contact_name

def query_contact_number():
     contact_number = str(input("\nPlease, enter the number of the contact: "))

     try:
        contact_number = convert_str_to_int(contact_number)
        validate_number(contact_number)
        return contact_number
     except Exception as e:
        print(e.args)

def perform_operation(selected_op):
     match selected_op:
          case Operations.SEARCH.value:
               search_operation()
          case Operations.ADDITION.value:
               add_operation()
          case Operations.UPDATE.value:
               update_operation()
          case Operations.DELETION.value:
               delete_operation()


def search_operation():
     contact_name = query_contact_name()
     contact_number = search_contact(contact_name)

     if contact_number != None and len(str(contact_number)) > 0:
          print(f"\nContact found -> {contact_name}: {contact_number}")
     else:
          print(f"\nThere's no contact in address book with name: {contact_name}")

     print("\n")

def add_operation():
     contact_name = query_contact_name()
     contact_number = query_contact_number()

     try:
          add_contact(contact_name, contact_number)
     except ContactAlreadyExistsException as e:
          print("Contact cannot be added" + str(e))
     else:
          print("\nContact added\n")

def update_operation():
     contact_name = query_contact_name()
     contact_number = query_contact_number()

     update_contact(contact_name, contact_number)

     print("\nContact updated\n")

def delete_operation():
     contact_name = query_contact_name()
     try:
        delete_contact(contact_name)
        print("\nContact deleted\n")
     except:
         print("\nContact not found, it cannot be deleted\n")

# Menu operations

def search_contact(name):
     return find_contact(name)

def add_contact(name, number):
     validate_contact_addition(name, number)
     set_contact(name, number)


def update_contact(name, number):
     old_contact = find_contact(name)
     if old_contact != None:
          set_contact(name, number)
     else:
          raise ContactNotFoundException


# Contact Operations
def set_contact(name, number):
      my_contact_book[name] = number

def find_contact(name):
      return my_contact_book[name] if name in my_contact_book else None

def delete_contact(name):
      return my_contact_book.pop(name)

# Validations
def validate_contact_addition(name, number):
     if name in my_contact_book:
            raise ContactAlreadyExistsException
     validate_number(number)
     validate_name(name)

def validate_number(number):
      if not(isinstance(number,int)):
            raise NumberNoDigitCharsException
      elif len(str(number)) < min_digits or len(str(number)) > max_digits:
            raise NumberExtensionException
      else:
            pass

def validate_name(name):

      if not(isinstance(name,str)):
            raise NumberNoDigitCharsException
      elif len(name.strip()) == 0:
            raise NameCannotBeVoid

# Utils
def convert_str_to_int(str_from):
     try:
        return int(str_from)
     except:
        return str_from

# Enums
class Operations(Enum):
     EXIT = 0
     SEARCH = 1
     ADDITION = 2
     UPDATE = 3
     DELETION = 4


# Exceptions
class ContactAlreadyExistsException(Exception):
    "The contact already exists, update the contact instead adding it again"
    pass

class ContactNotFoundException(Exception):
    "The contact doesn't exist"
    pass

class NumberNoDigitCharsException(Exception):
    "Phone number can only contain digits"
    pass

class NumberExtensionException(Exception):
    f"Phone number length has to be between {min_digits} and {max_digits} digits"
    pass

class NameFormatError(Exception):
    f"Contact name has no valid type, please check introduced characters"
    pass

class NameCannotBeVoid(Exception):
    f"Contact name cannot be empty"
    pass


main_program()
