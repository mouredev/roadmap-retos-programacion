# Listas
lista: list = ["Uno", "Dos", "Tres", "Cuatro"] # Creación
print(lista) # Impresión
lista.append("Cinco")  # Inserción 
print(lista) 
lista.insert(1, "One") # Inserción en la posición 1
print(lista)
lista.remove("Uno") # Eliminación 
print(lista)
print(lista[1]) # Acceso al elemento en la posición 1
lista[1] = "Three" # Actualización del elemento en la posición 1
print(lista[-1]) # Acceso al último elemento
print(lista)
lista.sort() # Ordenación de la lista
print(lista)
print(type(lista)) # Tipo de la variable

# Tuplas
tupla = ("Marcos", "Lumanet", "@lumanet", "42") # Creación
print(tupla[1]) # Acceso al elemento en la posición 1
print(tupla[2]) # Acceso al elemento en la posición 3
print(tupla[-1]) # Acceso al último elemento
print(tupla[-2]) # Acceso al penúltimo elemento
tupla = tuple(sorted(tupla)) # Ordenación de la tupla
print(tupla) 
print(type(tupla)) # Tipo de la variable

# Sets
mi_set = {"Marcos", "Lumanet", "@lumanet", "42"} # Creación
print(mi_set) 
mi_set.add("miemail@gmail.com") # Inserción
mi_set.add("miemail@gmail.com") # Inserción duplicada (no se añade)
print(mi_set)
mi_set.remove("@lumanet") # Eliminación
print(mi_set)
mi_set = set(sorted(mi_set)) # Ordenación (no se puede ordenar)
print(mi_set)
print(type(mi_set)) # Tipo de la variable

# Diccionario
my_dict: dict = {
    "nombre": "Marcos",
    "apellido": "Lumanet",
    "alias": "@lumanet",
    "edad": "41"
} # Creación
print(my_dict)
my_dict["email"] = "miemail@gmail.com" # Inserción
print(my_dict)
del my_dict["apellido"] # Eliminación 
print(my_dict)
print(my_dict["nombre"]) # Acceso al valor de la clave "nombre"
my_dict["edad"] = "42" # Actualización del valor de la clave "edad"
print(my_dict)
my_dict = dict(sorted(my_dict.items())) # Ordenación del diccionario por clave 
print(my_dict)
print(type(my_dict)) # Tipo de la variable

"""
Crea una contacto de contactos por terminal.
- Debes implementar funcionalidades de búsqueda, inserción, actualización y eliminación de contactos.
- Cada contacto debe tener un nombre y un número de teléfono.
- El programa solicita en primer lugar cuál es la operación que se quiere realizar, y a continuación
  los datos necesarios para llevarla a cabo.
- El programa no puede dejar introducir números de teléfono no numéricos y con más de 11 dígitos.
  (o el número de dígitos que quieras)
- También se debe proponer una operación de finalización del programa.
"""

def contactos():

    contacto = {} # Creación del diccionario de contactos

    def insert_contact(): # Función para insertar un contacto
        telefono = input("Introduce el teléfono del contacto: ")
        if telefono.isdigit() and len(telefono) > 5 and len(telefono) <= 11: # Validación del número de teléfono
            contacto[nombre] = telefono # Inserción o actualización del contacto en el diccionario de contactos
        else:
            print("Debes introducir un número de teléfono entre 5 y 11 dígitos.")

    while True:
        print("")
        print("1. Buscar contacto")
        print("2. Nuevo contacto")
        print("3. Actualizar contacto")
        print("4. Eliminar contacto")
        print("5. Salir")

        option = input("\nSelecciona una opción: ")

        match option:
            case "1":
                nombre = input("Introduce el nombre del contacto a buscar: ")
                if nombre in contacto: # Búsqueda del contacto en el diccionario de contactos 
                    print(f"El número de teléfono de {nombre} es {contacto[nombre]}.")
                else:
                    print(f"El contacto {nombre} no existe.")
            case "2":
                nombre = input("Introduce el nombre del contacto: ")
                insert_contact() # Llamada a la función para insertar un contacto
            case "3":
                nombre = input("Introduce el nombre del contacto que deseas actualizar: ")
                if nombre in contacto: # Búsqueda del contacto en el diccionario de contactos
                    insert_contact() # Llamada a la función para actualizar el teléfono del contacto
                else:
                    print(f"El contacto {nombre} no existe.")
            case "4":
                nombre = input("Introduce el nombre del contacto que deseas eliminar: ")
                if nombre in contacto:
                    del contacto[nombre] # Eliminación del contacto en el diccionario de contactos
                else:
                    print(f"El contacto {nombre} no existe.")
            case "5":
                print("Saliendo de contactos.")
                break
            case _: # Opción no válida
                print("Opción no válida. Elige una opción del 1 al 5.")

contactos()
