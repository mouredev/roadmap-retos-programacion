# Listas
from os import name


my_list:list = ["Brais", "Bl4ck", "Wolfy", "Visionos"]
print(my_list)
my_list.append("Castor") # Inserción
my_list.append("Castor")
print(my_list)
my_list.remove("Brais") # Eliminación
print(my_list)
print(my_list[1]) # Acceso
my_list[1] = "Cuervillo" # Actualización
print(my_list)
print(type(my_list))


# Tuplas
my_tuple:tuple = ("Brais", "Mouredev", "@mouredev", "36")
print(my_tuple[1]) # Acceso
print(my_tuple[3])
my_tuple = tuple(sorted(my_tuple)) # Ordenación
print(my_tuple)
print(type(my_tuple))

# Sets
my_sets:set = {"Brais", "Moure", "@mouredev", "36"}
print(my_sets)
my_sets.add("mouredev@gmail.com") # Insercción
my_sets.add("mouredev@gmail.com") # No se puede insertar duplicados
print(my_sets)
my_sets.remove("Moure") # Eliminación
print(my_sets)
my_sets = set(sorted(my_sets)) # No se puede ordenar
print(my_sets)
print(type(my_sets)) 

# Diccionario
my_dict:dict = {
    "name": "Brais",
    "surname": "Moure",
    "alias": "@mouredev",
    "edad": "36"
}
my_dict ["email"] = "mouredev@gmail.com" # Insercción
print(my_dict)
del my_dict ["surname"] # Eliminación
print(my_dict)
print(my_dict["name"]) # Acceso
my_dict["edad"] = "37" # Actualización
print(my_dict)
my_dict = dict(sorted(my_dict.items())) # Ordenación
print(my_dict)
print(type(my_dict))

"""
Extras
"""

agenda = {
}
def insertar_contacto(name):
    phone = input("Introduce un nro de telefono: ")
    if phone.isdigit() and len(phone) > 0 and len(phone) <= 11:
        agenda[name] = phone
    else: 
        print("Debes introducir un numero de teléfono un máximo de 11 dígitos.")

def my_agenda():
    
    
    while True:
        
        print("\n1. Buscar un contacto.")
        print("2. Insertar un contacto.")
        print("3. Actualizar un contacto.")
        print("4. Eliminar un contacto.")
        print("5. Salir.")
        
        option = input("\nIngresar una opcion: ")
        
        match option:
            case "1":
                name = input("\nIntroduce el nombre del contacto a buscar: ")
                if name in agenda:
                    print(f"El numero de teléfono de {name} es {agenda[name]}.")
                else: 
                    print(f"El contacto {name} no existe.")
            case "2":
                name = input("Introduce un nombre: ")
                insertar_contacto(name)
                pass
            case "3":
                name = input("Que contacto quieres actualizar?: ")
                if name in agenda:
                    insertar_contacto(name)
                else:
                    print(f"El contacto {name} no existe.")
                pass
            case "4":
                name = input("Que contacto deseas eliminar?: ")
                if name in agenda:
                    del agenda[name]
                    print("Su contacto ha sido eliminado con exito!")
                else: 
                    print(f"El contacto {name} no existe.")
                pass
            case "5":
                print("Saliendo de la agenda")
                break
            case _:
                print("Opcion no valida. Seleccione una opcion del 1 al 5")
                pass
my_agenda()
