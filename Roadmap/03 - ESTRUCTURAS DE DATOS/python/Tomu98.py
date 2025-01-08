""" Reto 03: Estructuras de datos """

# Listas
my_list: list = ["Tomu", "Pecas", "Jere"]
print(my_list)
my_list.append("Cris") # Inserción
print(my_list)
my_list.remove("Cris") # Eliminación
print(my_list)
print(my_list[1]) # Acceso
my_list[1] = "Pequitas" # Actualización
print(my_list)
my_list.sort() # Ordenación
print(my_list)

# Tuplas
my_tuple: tuple = ("Abel", "Tomu", "@Tomu98", "25")
print(my_tuple)
print(my_tuple[1]) # Acceso
print(my_tuple[2])
print(my_tuple[3])
my_tuple = tuple(sorted(my_tuple)) # Ordenación
print(my_tuple)
print(type(my_tuple))

# Sets
my_set: set = {"Abel", "Tomu", "@Tomu98", "25"}
print(my_set)
my_set.add("tomu@dev.py") # Inserción
my_set.add("tomu@dev.py")
print(my_set)
my_set.remove("Abel") # Eliminación
print(my_set)
my_set = set(sorted(my_set)) # No se puede ordenar
print(my_set)
print(type(my_set))

# Diccionarios
my_dict: dict = {"name":"Abel",
                 "alias":"Tomu",
                 "age":"25"
}
print(my_dict)
my_dict["email"] = "tomu@dev.py" # Inserción
print(my_dict)
del my_dict["email"] # Eliminación
print(my_dict)
print(my_dict["alias"]) # Acceso
my_dict["age"] = "26" # Actualización
print(my_dict)
my_dict = dict(sorted(my_dict.items())) # Ordenación
print(my_dict)
print(type(my_dict))



""" Reto extra """

def my_agenda():

    agenda = {}

    def insert_contact():
        phone = input("Introduce el teléfono del contacto: ")
        if phone.isdigit() and len(phone) > 0 and len(phone) <= 11:
            agenda[name] = phone
        else:
            print("Debes introducir un número de teléfono un máximo de 11 digitos")

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
                    print(f"El número de teléfono de {name} es {agenda[name]}.")
                else:
                    print(f"El contacto '{name}' no existe")
            case "2":
                name = input("Introduzca el nombre del contacto: ")
                insert_contact()
            case "3":
                name = input("Introduce el nombre del contacto a actualizar: ")
                if name in agenda:
                    insert_contact()
                else:
                    print(f"El contacto '{name}' no existe")
            case "4":
                name = input("Introduce el nombre del contacto a eliminar: ")
                if name in agenda:
                    del agenda[name]
                else:
                    print(f"El contacto '{name}' no existe")
            case "5":
                print("Saliendo de la agenda.")
                break
            case _:
                print("Opción no válida. Elige una opción del 1 al 5.")

my_agenda()
