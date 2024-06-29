"""
Estrutura de datos
"""

# Listas
my_list = []
my_other_list = list()

# Tuplas
my_tuple = ()
my_other_tuple = tuple()
my_thrith_tuple = 10, 2, 1

# Conjuntos
my_set = set()
my_other_set = {1,"Canada","Roma"}

# Diccionarios
my_dict = dict()
my_other_dict = {}
my_thrith_dict = {"hello":"world","hi":"comunity"}

"""
Operaciones
"""

# Inserción
my_list.append("manzana")
my_list.extend(["pera","uva"])
print(my_list)

# Borrado
del my_list[1]
print(my_list)
my_list.remove("uva")
print(my_list)


# Actualización
my_list[0] = "lechuga"
print(my_list)


# Ordenación
my_list.extend(["tomate","queso","mortadela","mayonesa"])
print(my_list)
my_list.sort()
print(my_list)

"""
Ejercicio Extra
"""

contact_list = {}

def find_contact(name: str) -> list:
    if name in contact_list:
        print(f"Contacto: {name}")
        print(f"Numero: {contact_list.get(name)}")
    else:
        print("No existe el contacto")

def insert_contact(name: str):
    if name not in contact_list:
        number = input("Ingrese el número: ")
        contact_list[name] = number
        print(f"Contacto: {name}:{number} agregado")
    else:
        print("El contacto ya existe")

def refresh_contact(name: str):
    if name in contact_list:
        number = input("Ingrese el nuevo número: ")
        contact_list[name] = number
        print(f"Contacto: {name}:{number} actualizado")
    else:
        print("El contacto no existe")

def del_contact(name):
    if name in contact_list:
        del contact_list[name]
        print(f"Contacto: {name} eliminado")
    else:
        print("El contacto no existe")

def show_menu():
    print("*"*20)
    print("AGENDA DE CONTACTOS.")
    print("Operaciones:")
    print("1. Buscar contacto.")
    print("2. Insertar contacto.")
    print("3. Actualizar contacto")
    print("4. Borrar contacto")
    print("5. Salir")

def select_action(action: int):
    match action:
        case 1:
            find_contact(input("Ingrese el nombre del contacto: "))
        case 2: 
            insert_contact(input("Ingrese el nombre del contacto: "))
        case 3: 
            refresh_contact(input("Ingrese el nombre del contacto: "))
        case 4: 
            del_contact(input("Ingrese el nombre del contacto: "))
        case 5: 
            print("Saliendo...")


def menu(action=0):
    while action != 5:
        show_menu()
        print("Ingrese el número de la acción.")
        try:
            action = int(input("Opción: "))  
        except:
            print("Valor invalido....")
            input("Presiona cualquier boton para continuar")
            continue
        else:
            select_action(action)
            if action == 5:
                break
            input("Presiona cualquier boton para continuar")
            if action not in range(1,6):
                print("Valor invalido....")
                input("Presiona cualquier boton para continuar")


menu()
