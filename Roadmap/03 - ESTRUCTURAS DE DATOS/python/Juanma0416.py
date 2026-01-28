
"""
Estructuras
"""

# Listas
my_list: list = ["Loyle", "Tyrone", "Marifroes", "Wesley"] # Lista 
print(my_list)
my_list.append("Barbatuqes")  # Insertar elemento al final de la lista
my_list.append("Barbatuqes")  # Insertar elemento al final de la lista
print(my_list)
my_list.remove("Loyle")  # Eliminar un elemento en especifico de la lista
print(my_list)
print(my_list[1])  #  Imprimir un elemento en especifico de la lista en este caso es de la posición 1
my_list[1] = "Tomoko"  # Actualización de un elemento en especifico de la lista en este caso es de la posición 1
print(my_list)
my_list.sort()  # Ordenación de la lista en orden alfabético ascendente
print(my_list)
print(type(my_list))  # Impresión del tipo de dato de la lista

# Tuplas
my_tuple: tuple = ("juancho", "mancho", "@juancho", "28")  # Tupla, la diferencia entre una lista y una tupla 
# es que la tupla es inmutable, es decir, no se puede modificar
print(my_tuple[1])  # Aquí imprimimos el elemento en la posición 1 de la tupla
print(my_tuple[3])  # Aquí imprimimos el elemento en la posición 3 de la tupla
my_tuple = tuple(sorted(my_tuple))  # Aquí lo que hacemos es ordenar la tupla en orden alfabético ascendente y 
# convertirla en una tupla, osea que se pierde la inmutabilidad de la tupla ya que al hacer sorted() 
# se crea una lista ordenada y luego se convierte en una tupla con tuple()
print(my_tuple)
print(type(my_tuple))  # Impresión del tipo de dato de la tupla

# Sets
my_set: set = {"juancho", "mancho", "@juancho", "28"}  # Set, es para almacenar elementos únicos, es decir, no permite duplicados
print(my_set)
my_set.add("loyle@gmail.com")  # Inserción, si se intenta insertar un elemento que ya existe, no se inserta
my_set.add("loyle@gmail.com")
print(my_set)
my_set.remove("juancho")  # Eliminación, si se intenta eliminar un elemento que no existe, se lanza un error
print(my_set)
my_set = set(sorted(my_set))  # Ordenación, se 
print(my_set)
print(type(my_set))  # Impresión del tipo de dato del set

# Diccionario
my_dict: dict = {
    "name": "Juancho",
    "surname": "Mancho",
    "alias": "@juancho",
    "age": "28"
}  # Diccionario, es para almacenar pares clave-valor, es decir, cada valor tiene una clave asociada
my_dict["email"] = "loyle@gmail.com"  # Aquí insertamos un nuevo par clave-valor 
print(my_dict)
del my_dict["surname"]  # Aquí eliminamos un par clave-valor
print(my_dict)
print(my_dict["name"])  # Aquí accedemos a un valor mediante su clave
my_dict["age"] = "28"  # Aquí actualizamos un valor mediante su clave
print(my_dict)
my_dict = dict(sorted(my_dict.items()))  # Ordenación, se ordena el diccionario en orden alfabético ascendente
print(my_dict)
print(type(my_dict))  # Impresión del tipo de dato del diccionario

"""
Extra
"""


def my_agenda(): # Procedemos con la creación de una agenda para practicar con los diccionarios

    agenda = {} # Creamos un diccionario vacío

    def insert_contact(): # Procedemos con la creación de una función para insertar contactos
        phone = input("Introduce el teléfono del contacto: ") # Pedimos el teléfono del contacto
        if phone.isdigit() and len(phone) > 0 and len(phone) <= 11: # Validamos que el teléfono sea un número y que tenga entre 1 y 11 dígitos
            agenda[name] = phone # Insertamos el contacto en el diccionario
        else:
            print(
                "Debes introducir un número de teléfono un máximo de 11 dígitos.") # Mensaje de error

    while True: # Procedemos con la creación de un bucle infinito para mostrar el menú y que se rompa cuando el usuario elija la opción 5

        print("") # Salto de línea
        print("1. Buscar contacto") # Opción 1
        print("2. Insertar contacto") # Opción 2
        print("3. Actualizar contacto") # Opción 3
        print("4. Eliminar contacto") # Opción 4
        print("5. Salir") # Opción 5

        option = input("\nSelecciona una opción: ") # Pedimos al usuario que elija una opción

        match option: # Procedemos con la creación de un match para que el usuario elija una opción
            case "1":
                name = input("Introduce el nombre del contacto a buscar: ") # Pedimos el nombre del contacto a buscar
                if name in agenda: # Validamos que el contacto exista
                    print(
                        f"El número de teléfono de {name} es {agenda[name]}.") # Mostramos el número de teléfono del contacto
                else:
                    print(f"El contacto {name} no existe.") # Mensaje de error
            case "2":
                name = input("Introduce el nombre del contacto: ") # Pedimos el nombre del contacto
                insert_contact() # Insertamos el contacto
            case "3":
                name = input("Introduce el nombre del contacto a actualizar: ") # Pedimos el nombre del contacto a actualizar
                if name in agenda: # Validamos que el contacto exista
                    insert_contact() # Insertamos el contacto
                else:
                    print(f"El contacto {name} no existe.") # Mensaje de error
            case "4":
                name = input("Introduce el nombre del contacto a a eliminar: ") # Pedimos el nombre del contacto a eliminar
                if name in agenda: # Validamos que el contacto exista
                    del agenda[name] # Eliminamos el contacto
                else:
                    print(f"El contacto {name} no existe.") # Mensaje de error
            case "5": # Opción 5
                print("Saliendo de la agenda.") # Mensaje de despedida
                break
            case _:
                print("Opción no válida. Elige una opción del 1 al 5.") # Mensaje de error


my_agenda() # Llamamos a la función
