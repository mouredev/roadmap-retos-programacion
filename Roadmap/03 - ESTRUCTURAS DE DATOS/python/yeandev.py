"""
Respuesta al ejercicio 03
/*
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
 */
"""

# Listas -  Estructuras de datos ordenadas y mutables

my_list: list = ["Yean", "Zerek", "Thony", "Kenys"]
print(my_list)
my_list.append("Troy") # inserción
print(my_list)
my_list.remove("Thony") # eliminación
print(my_list)
print(my_list[2])
my_list[2] = "Kylian" # actualización
print(my_list)
my_list.sort() # ordenación
print(my_list)
print(type(my_list))

#Tuplas - Estructuras de datos ordenadas pero inmutables

my_tuple: tuple = ("Yean", "Fierro", "YeanGit", "24")
print(my_tuple[2]) # acceso
print(my_tuple[3])
my_tuple = tuple(sorted(my_tuple)) # ordenación
print(type(my_tuple))
print(my_tuple)

# Sets - Estructuras de datos no ordenadas con elementos únicos

my_set: set = {"Yean", "Fierro", "YeanGit", "24"}
print(my_set)
my_set.add("yeanfierro@outlook.cl") # inserción
my_set.add("yeanfierro@outlook.cl")
my_set.remove("Fierro") # eliminación
print(my_set)
my_set = set(sorted(my_set)) # no se puede ordenar
print(my_set)
print(type(my_set))

# Diccionario - Estructuras de datos con claves y valores

my_dict: dict = {
    "name": "Yean",
    "surname": "Fierro",
    "alias": "YeanGit",
    "age": "24"
}
my_dict["email"] = "yeanfierro@outlook.cl" # inserción
print(my_dict)
del my_dict["surname"] # eliminación
print(my_dict)
print(my_dict["name"]) # acceso
my_dict["age"] = 25 # actualización
print(my_dict)
my_dict = dict(sorted(my_dict.items())) # ordenación
print(my_dict)
print(type(my_dict))

"""
Extra
"""

def my_agenda():

    agenda = {}

    def insert_contact():
        phone = input("Introduce el télefono de contacto: ")
        if phone.isdigit() and len(phone) > 0 and len(phone) <= 11:
            agenda[name] = phone
        else:
            print("Introduce un número de télefono con un máximo de 11 dígitos.")

    while True:
        print("")
        print("1. Buscar contacto")
        print("2. Insertar contacto")
        print("3. Actualizar contacto")
        print("4. Eliminar contacto")
        print("0. Salir")

        option = input("\nSelecciona una opción:")

        match option:
            case "1":
                name = input("Introduce el nombre del contacto a buscar: ").lower()
                if name in agenda:
                    print(f"El número de télefono de {name} es {agenda[name]}")
                else:
                    print(f"El contacto {name} no existe en la agenda.")
            case "2":
                name = input("Introduce el nombre del contacto: ").lower()
                insert_contact()
            case "3":
                name = input("Introduce el nombre del contacto a actualizar: ").lower()
                if name in agenda:
                    insert_contact()
                else:
                    print(f"El contacto {name} no existe en la agenda.")
            case "4":
                name = input("Introduce el nombre del contacto a eliminar: ").lower()
                if name in agenda:
                    del agenda[name]
                else:
                    print(f"El contacto {name} no existe en la agenda.")
                pass
            case "0":
                print("Saliendo.")
                break
            case _:
                print("Opción no válida. Elige una opción del 1 al 5.")

my_agenda()