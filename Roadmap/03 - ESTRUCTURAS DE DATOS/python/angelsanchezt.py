"""
 * EJERCICIO: ESTRUCTURAS DE DATOS
 * - Muestra ejemplos de creación de todas las estructuras soportadas por defecto en tu lenguaje.
 * - Utiliza operaciones de inserción, borrado, actualización y ordenación.
 *
"""
print("EJERCICIO: ESTRUCTURAS DE DATOS")

"""
Listas
"""
print("LISTAS")
my_list: list = ["Nueva York", "Tokio", "Londres", "París", "Shanghai"]
print(my_list)

# Inserción: Adicionar un item al fian de la lista
my_list.append("Beijing") 
my_list.append("Moscú")
print(f"La lista despues de insertar las ciudades de Beijin y Moscú: {my_list}")

# Eliminar un item de la lista
my_list.remove("Tokio")
print(f"La lista despues de eliminar la ciudad Tokio: {my_list}")

# Actualización de un item de la lista
my_list[3] = "Dubai"
print(f"La lista despues de actualizar la posición 3: {my_list}")

# Ordenacion
my_list.sort()
print(f"La lista ordenada es: {my_list}") 

# Buscar el valor de una posición de la lista
print(f"El elemento 'Nueva York' esta en la posición: {my_list.index('Nueva York')}")

# Invertir la lista:
my_list.reverse()
print(f"la Lista ordenada de forma inversa es: {my_list}")

# Imprimir el tipo de objeto de la list
print(f"El tipo de la lista es: {type(my_list)}")
print("\n")

"""
Tuplas
"""
print("Tupla")
# Definición de una tupla
my_tuple: tuple = ("manzana", "plátano", "naranja", "fresa", "uva")

# Imprimir la tupla
print(my_tuple)

print(my_tuple[1])  # Acceso

print(my_tuple[3])

my_tuple = tuple(sorted(my_tuple))  # Ordenación
print(my_tuple)

print(type(my_tuple))
print("\n")

"""
Sets
"""
print("SETS")
# Definición de un set
my_set: set = {"Nueva York", "Tokio", "Londres", "París", "Shanghai"}

# Imprimir el set
print(my_set)

my_set.add("Moscú")  # Inserción
my_set.add("Moscú")
print(my_set)
my_set.remove("Shanghai")  # Eliminación
print(my_set)

my_set = set(sorted(my_set))  # No se puede ordenar
print(my_set)

print(type(my_set))

# Diccionario
# Definición de un diccionario
my_dict: dict = {
    "nombre": "Juan",
    "apellido" : "Casas",
    "edad": 30,
    "ciudad": "Madrid",
    "profesión": "Ingeniero"
}

# Imprimir el diccionario
print(my_dict)

my_dict["email"] = "juan.casas@gmail.com"  # Inserción
print(my_dict)

del my_dict["apellido"]  # Eliminación
print(my_dict)

print(my_dict["nombre"])  # Acceso

my_dict["edad"] = 36  # Actualización
print(my_dict)

my_dict = dict(sorted(my_dict.items()))  # Ordenación
print(my_dict)

print(type(my_dict))


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

    def insert_contact():
        phone = input("Introduce el teléfono del contacto: ")
        if phone.isdigit() and len(phone) > 0 and len(phone) <= 11:
            agenda[name] = phone
        else:
            print(
                "Debes introducir un número de teléfono un máximo de 11 dígitos.")

    while True:

        print("")
        print("1. Buscar contacto")
        print("2. Insertar contacto")
        print("3. Actualizar contacto")
        print("4. Eliminar contacto")
        print("5. Salir")

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
                else:
                    print(f"El contacto {name} no existe.")
            case "5":
                print("Saliendo de la agenda.")
                break
            case _:
                print("Opción no válida. Elige una opción del 1 al 5.")


my_agenda()

