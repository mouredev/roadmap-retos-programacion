"""
EJERCICIO:
 1. Muestra ejemplos de creación de todas las estructuras soportadas por defecto
    en tu lenguaje.
 2. Utiliza operaciones de inserción, borrado, actualización y ordenación.
 
 * DIFICULTAD EXTRA (opcional):
 3. Crea una agenda de contactos por terminal.
 *  Debes implementar funcionalidades de búsqueda, inserción, actualización
    y eliminación de contactos.
 *  Cada contacto debe tener un nombre y un número de teléfono.
 *  El programa solicita en primer lugar cuál es la operación que se quiere realizar,
    y a continuación los datos necesarios para llevarla a cabo.
 *  El programa no puede dejar introducir números de teléfono no numéricos y con más
    de 11 dígitos (o el número de dígitos que quieras).
 *  También se debe proponer una operación de finalización del programa.
"""

# Estructuras de datos basicas

# 1. List o listas

# Creation
fruits = ["apple", "pineaple", "banana", "cherry", "banana"]
print("List of fruits: ", fruits)

# Insercion
fruits.append("orange")    # agrego un elemento al final de la lista
fruits.insert(1, "kiwi")    # inserto un elemento en una posicion especifica de la lista
print("After insertion:", fruits)

# Deletion
fruits.remove("banana")    # elimina la primera ocurrencia que coincida con el elemento indicado
deleted_item = fruits.pop()    # elimina y devuelve el ultimo elemento de la lista
print("After deletion:", fruits)
print("Deleted item:", deleted_item)

# Update
fruits[0] = "green apple"   # Modifica un elemento de la lista por indice
print("After update:", fruits)

# Sorting and reverse
fruits.sort()   # Ordena los elementos de la lista en orden ascendente
print("Sorted list:", fruits)
fruits.reverse()
print("Reversed list:", fruits)

# 2. Tuples o tuplas

# Creation
coordinates = (15, 55)  
print("Original tuple:", coordinates)

# Access
print("First value:", coordinates[0])   # Devuelve un elemento de la tupla indicado por el indice

# "Update" via conversion to list
coordinates = list(coordinates)
coordinates[0] = 99
coordinates = tuple(coordinates)
print("Modified tuple:", coordinates)

# 3. Sets

# Creation
numbers = {1, 2, 3, 4}
print("Original set:", numbers)

# Insertion
numbers.add(5)
numbers.update([6, 7])              # Agrega multiples elementos
print("After insertion:", numbers)

# Deletion
numbers.remove(2)                   # Elimina un elemento pero genera un error si el indice no existe 
numbers.discard(10)                 # No genera error si el indice no existe
removed = numbers.pop()             # Elimina un elemento de manera arbitraria
print("After deletion:", numbers)
print("Popped element:", removed)

print("Sorted set:", sorted(numbers))  # Devuelve una lista ordenada, es temporal ya que no se puede ordenar un set

# Set operations
odds = {1, 3, 5}
evens = {2, 4, 6}
print("Union:", odds | evens)
print("Intersection:", odds & evens)

# 4. Dictionaries o Diccionarios

# Creation
person = {"name": "John", "age": 30}
print("Original dictionary:", person)

# Insertion
person["city"] = "New York"    # Agrega la llave y el valor indicado al diccionario
print("After insertion:", person)

# Deletion
del person["age"]   # Elimina tanto la llave indicada como el valor del diccionario
removed_city = person.pop("city")   # Elimina tanto la llave indicada como el valor del diccionario, y devuelve como resultado el valor asociado a la llave indicada
print("After deletion:", person)
print("Removed value:", removed_city)

# Update
person["name"] = "John Doe"    # Modifica el valor de la llave indicada por un valor especificado 
print("After update:", person)

# Sorting by keys
sorted_dict = dict(sorted(person.items()))  # Ordena el diccionario por llave en orden alfabetico ascendente
print("Sorted dictionary (by key):", sorted_dict)

# Other operations
print("Keys:", list(person.keys()))    # Genera una lista de las llaves del diccionario 
print("Values:", list(person.values()))    # Genera una lista de los valores de las llaves del diccionario 
print("Items:", list(person.items()))    # Genera una lista de tuplas, donde cada tupla contiene la llave con su respectivo valor      

# 5. Strings o cadenas de texto

# Creation
message = "Hello World"
print("Original string:", message)

# Access
print("First character:", message[0])   # Devuelve el primer caracter de la cadena de texto
print("Last character:", message[-1])   # Devuelve el ultimo caracter de la cadena de texto

# Update (esto crea una nueva cadena de texto)
message = message.replace("World", "Python")    # Remplaza una palabra de la cadena de texto(primer argumento) por una nueva palabra(segundo argumento)
print("After replacement:", message)

# Deletion by slice (Esto crea una nueva cadena de texto)
message = message[0:5]  # Extrae un segmento especifico de la cadena de texto y borra el resto
print("After slicing:", message)

# Sorting characters alphabetically
sorted_chars = ''.join(sorted("zebra"))    # Ordena de manera ascendente los caracteres de un string y los almacena en un nuevo string vacio 
print("Sorted string characters:", sorted_chars)

# String methods
text = "  Python is FUN  "
print("Lower:", text.lower())   # Devuelve la cadena de texto en minusculas
print("Upper:", text.upper())   # Devuelve la cadena de texto en mayusculas
print("Stripped:", text.strip())    # Elimina los espacion en blanco del inicio y el final de la cadena de texto
print("Split:", text.split())    # Devuelve una lista con cada palabra de la cadena de texto como elemento de la lista

"""
6. Crea una agenda de contactos por terminal.
 *  Debes implementar funcionalidades de búsqueda, inserción, actualización
    y eliminación de contactos.
 *  Cada contacto debe tener un nombre y un número de teléfono.
 *  El programa solicita en primer lugar cuál es la operación que se quiere realizar,
    y a continuación los datos necesarios para llevarla a cabo.
 *  El programa no puede dejar introducir números de teléfono no numéricos y con más
    de 11 dígitos (o el número de dígitos que quieras).
 *  También se debe proponer una operación de finalización del programa.
"""

contactbook = {}

# ---------------------------------------------------------
# Esta función valida si un nombre ingresado es válido.
# Elimina los espacios y verifica que todos los caracteres
# restantes sean alfabéticos (letras). Retorna True o False.
# ---------------------------------------------------------

def valid_name(name):
    without_spaces = name.replace(" ", "")
    return without_spaces.isalpha() and len(without_spaces) > 0

# ---------------------------------------------------------
# Esta función permite agregar un nuevo contacto al diccionario.
# Verifica que el nombre no contenga caracteres inválidos y
# que no exista ya en la agenda, ignorando diferencias entre
# mayúsculas y minúsculas. También valida el número de teléfono.
# ---------------------------------------------------------

def add_contacts():
    name = input("Agrega el nombre del contacto: ")

    # Validación del nombre: debe contener solo letras y espacios.
    if not valid_name(name):
        print("\n❌ Error: El nombre del contacto solo debe contener letras y espacios")
        return

    # La funcion .strip() permite borrar los espacios ubicados antes y despues del nombre
    name_lower = name.strip().lower()

    # Verificación de existencia previa del contacto (sin importar mayúsculas)
    for name_saved in contactbook:
        if name_saved.lower() == name_lower:
            print("\n⚠️ El contacto ya existe! El guardado del nombre es sensible a mayusculas y minusculas.")
            return

    phone_number = input("Agrege el numero de telefono (Debe tener un maximo de 11 digitos): ")

    # Validación del número: debe contener solo dígitos y tener máximo 11 caracteres
    if not phone_number.isdigit() or len(phone_number) > 11:
        print("\n❌ Error: el numero de telefono solo debe contener numneros y un maximo de 11 digitos")
        return
    
    else:
        contactbook[name] = phone_number
        print(f"\n✅ El contacto {name} fue agregado!")

# ---------------------------------------------------------
# Esta función permite buscar un contacto por nombre.
# Si el nombre es válido y existe en la agenda, se muestra
# su número asociado.
# ---------------------------------------------------------

def search_contact():
    name = input("Agrega el contacto que deseas buscar: ")

    # Validación del nombre ingresado
    if not valid_name(name):
        print("\n❌ Error: El nombre del contacto solo debe contener letras y espacios")
        return

    # Búsqueda directa en el diccionario
    if name in contactbook:
        print(f"{name} : {contactbook[name]}")
    else:
        print("\n😅 El contacto no existe!")
        return
    
# ---------------------------------------------------------
# Esta función permite actualizar el número telefónico
# de un contacto existente.
# ---------------------------------------------------------  
    
def update_contact():
    name = input("Agrega el contacto que deseas actualizar: ")

    # Validación del nombre
    if not valid_name(name):
        print("\n❌ Error: El nombre del contacto solo debe contener letras y espacios")
        return
    
    # Verificación de existencia del contacto
    if name in contactbook:
        phone_number = input("Agrega el nuevo numero del contacto")
        contactbook[name] = phone_number
        print(f"\n✅ El contacto {name} ha sido actualizado!")
        return
    else:
        print("\n😅 El contacto no existe!")
        return
    
# ---------------------------------------------------------
# Esta función permite eliminar un contacto existente
# de la agenda, si este se encuentra registrado.
# ---------------------------------------------------------
    
def remove_contact():
    name = input("\nAgrega el contacto que deseas eliminar: ")

    # Validación del nombre
    if not valid_name(name):
        print("\n❌ Error: El nombre del contacto solo debe contener letras y espacios")
        return

    # Verificación de existencia y eliminación
    if name in contactbook:
        del contactbook[name]
        print(f"\n🔥 El contacto {name} ha sido eliminado!")
        return
    else:
        print("\n😅 El contacto no existe!")
        return

# ---------------------------------------------------------
# Esta función imprime todos los contactos registrados
# en la agenda. Si la agenda está vacía, informa al usuario.
# ---------------------------------------------------------

def show_contacts():

    if len(contactbook) == 0:
        print("\n⚠️ La agenda esta vacia, ingrese un contacto")
        return

    print("\n📋 Esta es la lista de contactos:")

    for name in contactbook:
        print(f"🔹{name} : {contactbook[name]}")

# ---------------------------------------------------------
# Menú principal del programa. Permite al usuario seleccionar
# una opción y repite el proceso hasta que elija salir.
# ---------------------------------------------------------

while True:
    print("\n📱 AGENDA DE CONTACTOS 📱\n"+
          "1. Agregar Contacto\n"+
          "2. Buscar Contacto\n"+
          "3. Actualizar Contacto\n"+
          "4. Borrar Contacto\n"+
          "5. Mostrar Contactos\n"
          "6. Salir")
    
    option = input("\n📌 Selecciona una opcion ( 1 - 6): ")

    # Validación de entrada: debe ser un número entre 1 y 6
    if not option.isdigit():
        print("⚠️ El menu solo acepta valores entre el 1 y el 6")
        continue

    option = int(option)

    if option < 1 or option > 6:
        print("⚠️ El menu solo acepta valores entre el 1 y el 6")
        continue


    if option == 1:
        add_contacts()
    elif option == 2:
        search_contact()
    elif option == 3:
        update_contact()
    elif option == 4:
        remove_contact()
    elif option == 5:
        show_contacts()
    elif option == 6:
        break