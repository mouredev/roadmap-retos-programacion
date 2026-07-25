'''
ESTRUCTURAS DE DATOS
'''

# LISTAS

my_ice_cream = ["coconut", "vanilla", "chocolate", "oreo"]
print(my_ice_cream)
my_ice_cream.append("cookies and cream")
my_ice_cream.append("cookies and cream") # INSERCIÓN
print(my_ice_cream)
my_ice_cream.remove("coconut") # ELIMINACIÓN
print(my_ice_cream)
print(my_ice_cream[1]) # ACCESO
my_ice_cream[1] = "strawberry" # ACTUALIZACIÓN
print(my_ice_cream)
my_ice_cream.sort() # ORDENACIÓN
print(my_ice_cream)
print(type(my_ice_cream))

# TUPLAS

my_tupla = ("Yahir", "yah1r404", "Sulu", "22")
print(my_tupla[1])
print(my_tupla[3])
my_tupla = tuple(sorted(my_tupla))
print(my_tupla)
print(type(my_tupla))

# SETS

my_set = {"Yahir", "yah1r404", "Sulu", "22"}
print(my_set)
my_set.add("yah1r.sulu18@gmail.com")
my_set.add("yah1r.sulu18@gmail.com") # INSERCIÓN
print(my_set)
my_set.remove("Sulu") # ELIMINACIÓN
print(my_set)
my_set = set(sorted(my_set))
print(my_set)
print(type(my_set))

# DICCIONARIO

my_dict : dict = {
    "name" : "Yahir",
    "username" : "yah1r404",
    "surname" : "Sulu",
    "age" : "22"
}
my_dict["email"] = "yah1r.sulu18@gmail.com" # INSERCIÓN
print(my_dict)
del my_dict["surname"] # ELIMINACIÓN
print(my_dict["name"]) # ACCESO
my_dict["age"] = "23" # ACTUALIZACIÓN
print(my_dict)
my_dict = dict(sorted(my_dict.items())) # ORDENACIÓN
print(my_dict)
print(type(my_dict))

'''
TAREA EXTRA
'''

def my_agenda():

    agenda = {}

    while True:

        print("")
        print("1. BUSCAR CONTACTO")
        print("2. INSERTAR CONTACTO")
        print("3. ACTUALIZAR CONTACTO")
        print("4. ELIMINAR CONTACTO")
        print("5. SALIR")

        option = input("\nSelecciona una opción: ")
    
        match option:
            case "1":
                name = input("Introduce el nombre del contacto: ")
                if name in agenda:
                    print(f"El número de teléfono de {name} es {agenda[name]}.")
                else:
                    print(f"El usuario {name} no existe.")
            case "2":
                name = input("Escribe el nombre del contacto: ")
                phone = input("Escribe el número telefónico del contacto: ")
                if phone.isdigit() and len(phone) > 0 and len(phone) <= 11:
                    agenda[name] = phone
                else:
                    print("Debes introducir un número de teléfono con un máximo de 11 dígitos.")
            case "3":
                name = input("Introduce el nombre del contacto a actualizar: ")
                if name in agenda:
                    phone = input("Escribe el nuevo número telefónico del contacto: ")   
                    if phone.isdigit() and len(phone) > 0 and len(phone) <= 11:
                        agenda[name] = phone
                    else:
                        print("Debes introducir un número de teléfono con un máximo de 11 dígitos.")                    
                else:
                    print(f"El usuario {name} no existe.")
            case "4":
                name = input("Introduce el nombre del contacto a eliminar: ")
                if name in agenda:
                    del agenda[name]
                else:
                    print(f"El usuario {name} no existe.")

            case "5":
                print("Cerrando la agenda")
                break
            case _:
                print("Opción no válida. Elige un número del 1 al 5")









my_agenda()