"""
Estrutura de datos
"""

# Listas
my_list = []    # Constructor
my_other_list = list()  # Constructor
my_list.append("manzana")   # Inserción
my_list.extend(["pera","uva"])  # Inserción
print(my_list)
del my_list[1]  # Borrado
print(my_list)
my_list.remove("uva")   # Borrado
print(my_list)
my_list[0] = "lechuga"  # Actualización
print(my_list)
my_list.extend(["tomate","queso","mortadela","mayonesa"])
print(my_list)
my_list.sort()  # Ordenación
print(my_list)

# Tuplas
my_tuple = ()   # Constructor
my_other_tuple = tuple()    # Constructor
my_thrith_tuple = 10, 2, 1  # Constructor
my_fourth_tuple = ("Lunes", "Miercoles", "Viernes")  # Constructor
print(type(my_thrith_tuple))
print(my_thrith_tuple[2])   # Acceso
my_thrith_tuple = tuple(sorted(my_thrith_tuple))    # Ordenación
print(my_thrith_tuple)
print(type(my_thrith_tuple))

# Conjuntos/Sets
my_set = set() # Constructor
my_other_set = {1,"Ottawa","Roma"}  # Constructor
print(my_other_set)
my_other_set.add("Madrid")  # Inserción
print(my_other_set)
my_other_set.remove(1)  # Borrado
print(my_other_set)
my_other_set = set(sorted(my_other_set))    # No se puede ordenar por definición
print(my_other_set)
print(type(my_other_set))

# Diccionarios
my_dict = dict()
my_other_dict = {}
my_thrith_dict = {
    "english":"hello world!",
    "español":"¡Hola mundo!"
}
print(my_thrith_dict)
my_thrith_dict["Deutsch"] = "Hallo Welt"   # Inserción
print(my_thrith_dict)
my_thrith_dict["Deutsch"] = "Hallo Welt!"   # Actualización
print(my_thrith_dict)
del my_thrith_dict["Deutsch"]   # Actualización
print(my_thrith_dict)
my_thrith_dict = dict(sorted(my_thrith_dict.items())) # Ordenación
print(my_thrith_dict)
print(type(my_thrith_dict))


"""
Ejercicio Extra
"""

contact_list = {}

def find_contact(name: str, contact_list: dict) -> list:
    if name in contact_list:
        print(f"El numero de telefono de {name} es {contact_list[name]}")
    else:
        print(f"No existe el contacto {name}")
    return contact_list

def insert_contact(name: str, contact_list: dict):
    if name not in contact_list:
        number = input("Ingrese el número: ")
        if number.isdigit() and len(number) > 0 and len(number) < 11:
            contact_list[name] = number
            print(f"Contacto: {name}: {number} agregado")
        else:
            print("Numero invalido. \nDebes introducir un numero de telefono con un maximo de 11 dígitos")
    else:
        print("El contacto ya existe")
    return contact_list


def refresh_contact(name: str, contact_list: dict):
    if name in contact_list:
        number = input("Ingrese el nuevo número: ")
        if number.isdigit() and len(number) > 0 and len(number) < 11:
            contact_list[name] = number
            print(f"Contacto: {name}: {number} actualizado")
        else:
            print("Numero invalido. \nDebes introducir un numero de telefono con un maximo de 11 dígitos")
    else:
        print("El contacto no existe")
    return contact_list

def del_contact(name: str, contact_list: dict):
    if name in contact_list:
        del contact_list[name]
        print(f"Contacto: {name} eliminado")
    else:
        print("El contacto no existe")
    return contact_list

def show_menu():
    print("*"*20)
    print("AGENDA DE CONTACTOS.")
    print("Operaciones:")
    print("1. Buscar contacto.")
    print("2. Insertar contacto.")
    print("3. Actualizar contacto")
    print("4. Borrar contacto")
    print("5. Salir")

def my_agenda(action=0):
    contact_list = {}
    
    while True:
        show_menu()
        action = input("Opción: ") 
        match action:
            case "1":
                contact_list = find_contact(
                    input("Ingrese el nombre del contacto: "),
                    contact_list=contact_list
                )
            case "2": 
                contact_list = insert_contact(
                    input("Ingrese el nombre del contacto: "),
                    contact_list=contact_list
                )
            case "3": 
                contact_list = refresh_contact(
                    input("Ingrese el nombre del contacto: "),
                    contact_list=contact_list
                )
            case "4": 
                contact_list = del_contact(
                    input("Ingrese el nombre del contacto: "),
                    contact_list=contact_list
                )
            case "5": 
                print("Saliendo...")
                break
            case _:
                print("Valor invalido, ingrese una opción del 1 al 5")
        input("\n\nPulse enter para continuar")

my_agenda()