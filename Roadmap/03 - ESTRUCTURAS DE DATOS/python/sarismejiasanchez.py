# #03 ESTRUCTURAS DE DATOS

# Lists
"""
List: is a collection which is ordered and changeable(modifiable). 
Allows duplicate members.
"""
print("Lists\n")
# Crear una lista
fruits = list()
vegetables = []
print(type(fruits))
print(type(vegetables))

fruits = ['banana', 'orange', 'mango', 'lemon']                     # list of fruits
vegetables = ['Tomato', 'Potato', 'Cabbage','Onion', 'Carrot']      # list of vegetables
print(f"Fruits: {fruits}")
print(f"Vegetables: {vegetables}")

# Modifying Lists
# List is a mutable or modifiable ordered collection of items. Lets modify the fruit list.
fruits[1] = "watermelon"
print(f"Fruits: {fruits}")

# Adding Items to a List
# To add item to the end of an existing list we use the method append().
fruits.append("apple")
print(f"Fruits: {fruits}")

# Inserting Items into a List
"""
We can use insert() method to insert a single item at a specified index in a list. 
Note that other items are shifted to the right. 
The insert() methods takes two arguments:index and an item to insert.
"""
fruits.insert(2, 'pineapple') # insert pineapple between watermelon and mango
print(f"Fruits: {fruits}")

# Removing Items from a List
# The remove method removes a specified item from a list
fruits.remove("banana")
print(f"Fruits: {fruits}")

# Removing Items Using Pop
# The pop() method removes the specified index, (or the last item if index is not specified):
fruits.pop() # Remove de last item
print(f"Fruits: {fruits}")
fruits.pop(2) # Remove index 3 (lemon)
print(f"Fruits: {fruits}")

# Removing Items Using Del
"""
The del keyword removes the specified index and it can also be used to delete items within index range. 
It can also delete the list completely
"""
del fruits[0]
print(f"Fruits: {fruits}")
#del fruits
#print(fruits)       # This should give: NameError: name 'fruits' is not defined

# Clearing List Items
# The clear() method empties the list:
fruits.clear()
print(f"Fruits: {fruits}")      # []




# Tuples
"""
Tuple: is a collection which is ordered and unchangeable or unmodifiable(immutable). 
Allows duplicate members.
"""
print("\nTuples")

# Creating a Tuple
fruits = ()
vegetables = tuple()
print(type(fruits))
print(type(vegetables))

# Changing Tuples to Lists
fruits = ('banana', 'orange', 'mango', 'lemon')
fruits = list(fruits)
fruits[0] = 'apple'
fruits.append("watermelon")
print(f"Fruits List: {fruits}")     # ['apple', 'orange', 'mango', 'lemon']
fruits = tuple(fruits)
print(f"Fruits Tuple: {fruits}")     # ('apple', 'orange', 'mango', 'lemon')

# Joining Tuples
# We can join two or more tuples using + operator
fruits = ('banana', 'orange', 'mango', 'lemon')
vegetables = ('Tomato', 'Potato', 'Cabbage','Onion', 'Carrot')
fruits_and_vegetables = fruits + vegetables
print(f"Fruits and Vegetables: {fruits_and_vegetables}")

# Sorted
print(f"Fruits Ordenado: {sorted(fruits)}")

# Deleting Tuples
"""
It is not possible to remove a single item in a tuple 
but it is possible to delete the tuple itself using del.
"""
fruits = ('banana', 'orange', 'mango', 'lemon')
del fruits
#print(fruits) # NameError: name 'fruits' is not defined



# Sets
"""
Set: is a collection which is unordered, un-indexed and unmodifiable, but we can add new items to the set. 
Duplicate members are not allowed.
"""
print("\nSets")

# Creating a Set
fruits = set()
vegetables = {'tomato', 'potato', 'cabbage','onion', 'carrot'}
print(type(fruits))
print(type(vegetables))

# Adding Items to a Set
# Add one item using add()
vegetables.add("avocado")
print(f"Vegetables: {vegetables}")

"""
Add multiple items using update() The update() allows to add multiple items to a set. 
The update() takes a list argument.
"""
fruits.update(["mango", "banana", "watermelon"])
print(f"Fruits: {fruits}")

# Removing Items from a Set
"""
We can remove an item from a set using remove() method. 
If the item is not found remove() method will raise errors, 
so it is good to check if the item exist in the given set. 
However, discard() method doesn't raise any errors.
"""
vegetables.remove("cabbage")
print(f"Vegetables: {vegetables}")

# vegetables.remove("potatoes") # KeyError: 'potatoes'
# print(f"Vegetables: {vegetables}")

vegetables.discard("potatoes")
print(f"Vegetables: {vegetables}")

# Clearing Items in a Set
# If we want to clear or empty the set we use clear method.
fruits.clear()
print(f"Fruits: {fruits}")  # Fruits: set()

# Deleting a Set
# If we want to delete the set itself we use del operator.
del fruits
# print(f"Fruits: {fruits}")  # NameError: name 'fruits' is not defined

# Converting List to Set
fruits = ['banana', 'orange', 'mango', 'lemon','orange', 'banana']
print(f"Fruits: {fruits}") 
fruits = set(fruits) # {'mango', 'lemon', 'banana', 'orange'}
print(f"Fruits: {fruits}") 


# Dictionaries
"""
Dictionary: is a collection which is unordered, changeable(modifiable) and indexed. 
No duplicate members.
"""
print("\nDictionaries")

# Creating a Dictionary
person = {}
print(type(person))
person = {
    'first_name':'Sara',
    'last_name':'Mejia',
    'age':31,
    'country':'Colombia',
    'skills':['PL/SQL', 'Oracle Apex', 'Python'],
    'address':{
        'street':'Medellin',
        'zipcode':'050001'
    }
    }
print(type(person))
print(person)

# Adding Items to a Dictionary
person['job_title'] = 'Especialista en Programación Aplicada'
print(f"job_title: {person['job_title']}")
person['skills'].append('RPA')
print(f"skills: {person['skills']}")
print(person)

# Modifying Items in a Dictionary
person['first_name'] = 'Maria'
print(f"first_name: {person['first_name']}")

# Removing Key and Value Pairs from a Dictionary
"""
pop(key): removes the item with the specified key name:
popitem(): removes the last item
del: removes an item with specified key name
"""
person.pop('age')
print(person)

person.popitem()
print(person)

del person['country']
print(person)

# Clearing a Dictionary
person.clear()
print(f"Person: {person}") # Person: {}

# Deleting a Dictionary
del person
# print(f"Person: {person}") # NameError: name 'person' is not defined


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

def my_agenda():

    agenda = {}

    """
    Cada contacto debe tener un nombre y un número de teléfono.
    """
    def insert_contact():
        phone = input("Introduce el teléfono del contacto: ")
        """
        El programa no puede dejar introducir números de teléfono no númericos y con más de 11 dígitos.
        (o el número de dígitos que quieras)
        """
        if phone.isdigit() and len(phone) > 0 and len(phone) <= 11:
            agenda[name] = phone
        else:
            print(
                "Debes introducir un número de teléfono un máximo de 11 dígitos.")

    while True:
        """
        Debes implementar funcionalidades de búsqueda, inserción, actualización y eliminación de contactos.
        """
        print("")
        print("1. Buscar contacto")
        print("2. Insertar contacto")
        print("3. Actualizar contacto")
        print("4. Eliminar contacto")
        print("5. Salir") # También se debe proponer una operación de finalización del programa.

        """
        El programa solicita en primer lugar cuál es la operación que se quiere realizar, 
        y a continuación los datos necesarios para llevarla a cabo.
        """
        option = input("\nSelecciona una opción: ")

        match option:
            case "1":
                name = input("Introduce el nombre del contacto a buscar: ")
                if name in agenda:
                    print(
                        f"El número de teléfono de {name} es {agenda[name]}.")
                else:
                    print(f"El contacto {name} no existe.")
            case "2":
                name = input("Introduce el nombre del contacto: ")
                insert_contact()
            case "3":
                name = input("Introduce el nombre del contacto a actualizar: ")
                if name in agenda:
                    insert_contact()
                else:
                    print(f"El contacto {name} no existe.")
            case "4":
                name = input("Introduce el nombre del contacto a a eliminar: ")
                if name in agenda:
                    del agenda[name]
                    print(f"Se eliminó el contacto {name}.")
                else:
                    print(f"El contacto {name} no existe.")
            case "5":
                print("Saliendo de la agenda.")
                break
            case _:
                print("Opción no válida. Elige una opción del 1 al 5.")

my_agenda()
