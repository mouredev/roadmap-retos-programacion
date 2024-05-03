"""
Estructuras
"""
# Listas

my_list = ["Angel", "Black", "Miguel"]
print(my_list)
my_list.append("Castor") # Insercion
print(my_list)
my_list.remove("Angel") # Eliminacion
print(my_list)
print(my_list[1]) # Acceso
my_list[1] = "Cuervo" # Actualizacion
print(my_list)
my_list.sort() # Ordenacion
print(my_list)
print(type(my_list))

# Tuplas
my_tuple: tuple = ("Angel", "Miguel", "@angelblack", "30")
print(my_tuple[1])  # Acceso
print(my_tuple[3])
my_tuple = tuple(sorted(my_tuple))  # Ordenacion
print(my_tuple)
print(type(my_tuple))

# Sets
my_set = {"Angel", "Miguel", "@angelblack", "30"}
print(my_set)
my_set.add("Angelblack@gmail.com")  # Insercion
my_set.add("Angelblack@gmail.com")
print(my_set)
my_set.remove("Miguel") # Eliminacion
print(my_set)
my_set = set(sorted(my_set)) # No se puede ordenar
print(my_set)
print(type(my_set))

# Diccionario
my_dict: dict = {
    "name":"Angel",
    "surname":"Miguel",
    "alias":"@angelblack",
    "age":"30"
}
my_dict["email"] = "Angelblack@gmail.com" # Insercion
print(my_dict)
del my_dict["surname"]  #Eliminacion
print(my_dict)
print(my_dict["name"])  # Acceso
my_dict["age"] = "31"  # Actualizacion
print(my_dict)
my_dict = dict(sorted(my_dict.items()))  # Ordenacion
print(my_dict)
print(type(my_dict))

"""
Extra
"""
def my_agenda():
    
    agenda = {}

    def insert_contact():
        phone = input("Introduce el telefono del contacto: ")
        if phone.isdigit() and len(phone) > 0 and len(phone) <= 11:
            agenda[name] = phone
        else:
            print("Debes introducir un numero de telefono con un maximo de 10 digitos ")



    while True:

        print("")
        print("1. Buscar contacto")
        print("2. Insertar contacto")
        print("3. Actualizar contacto")
        print("4. Eliminar contacto")
        print("5. Salir")

        option = input("\nSelecciona una opcion: ")

        match option:
            case "1":
                name = input("Introduce el nombre del contacto a buscar: ")
                if name in agenda:
                    print(f"El numero de telefono de {name} es {agenda[name]}.")
                else:
                    print(f"El contacto {name} no existe.")
            case "2":
                name = input("Introcude el nombre del contacto: ")
                insert_contact()
            case "3":
                name = input("Introduce el nombre del contacto a actualizar: ")
                if name in agenda:
                    insert_contact()
                else:
                    print(f"El contacto {name} no existe.")
            case "4":
                name = input("Introduce el nombre del contacto a eliminar: ")
                if name in agenda:
                    del agenda[name]
                else:
                    print(f"El contacto {name} no existe.")
            case "5":
                print("Saliendo de la agenda.")
                break
            case _:
                print("Opcion no valida. Elije una opcion del 1 al 5.")

my_agenda() 
