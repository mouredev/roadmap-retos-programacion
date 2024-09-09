'''
Estructuras
'''

# Listas
my_list:list = ["Brais", "Pedro", "Mario", "Edu"]
print(my_list)
my_list.append("Javier")    # Inserción
print(my_list)
my_list.remove("Brais")     # Eliminación
print(my_list)
print(my_list[1])           # Acceso
my_list[1] = "José"
print(my_list)              # Actualización
my_list.sort()              # Ordenación
print(my_list)

# Tuplas - estructura inmutable
my_tuple:tuple = ("Mario", "Vidal", "mvidalb", "40")
print(my_tuple[1])              # Acceso
my_tuple = sorted(my_tuple)     # Devuelve una lista a partir de una tupla

# Sets - estructura desordenada, evita datos duplicados
my_set:set = {"Mario", "Vidal", "mvidalb", "40"}
my_set.add("abc@gmail.com")     # Inserción
my_set.add("abc@gmail.com")
print(my_set)
my_set.remove("Vidal")          # Eliminación
print(my_set)
sorted(my_set)                  # Devuelve una lista a partir de un set
print(my_set)

# Diccionario
my_dict:dict = {
    "name":"Mario", 
    "apellido":"Vidal", 
    "mote":"mvidalb", 
    "edad":"40"
    }
print(my_dict["name"])          # Acceso
del my_dict["apellido"]         # Eliminación
my_dict["mote"] = "garrulo"     # Inserción
sorted(my_dict.items())         # DEvuelve una lista


'''
Ejercicio extra
'''
def my_agenda():
    
    agenda = {}
    while True:

        print("\nAGENDA")
        print("1. Buscar contacto")
        print("2. Insertar contacto")
        print("3. Actualizar contacto")
        print("4. Eliminar contacto")
        print("5. Salir")

        option = input("\nSelecciona una opción: ")

        match option:
            case "1":
                name = input("Introduce el contacto a buscar: ")
                if name in agenda:
                    print(f"Contacto encontrado: \n{name} - {agenda[name]}")
                else:
                    print(f"El contacto {name} no existe.")
            case "2":
                name = input("\nIntroduce el contacto a guardar: ")
                phone = input("Introduce el número a guardar: ")
                if phone.isdigit() and len(phone) <= 11:
                    agenda[name] = phone
                    print("\nContacto guardado!")
                else:
                    print("Debes de introducir un número de teléfono con máximo 11 dígitos.")
            case "3":
                name = input("Introduce el contacto a actualizar: ")
                if name in agenda:
                    phone = input("\ntroduce el número del contacto: ")
                    if phone.isdigit() and len(phone) <= 11:
                        agenda[name] = phone
                        print("\nContacto actualizado!")
                else:
                    print("Debes de introducir un número de teléfono con máximo 11 dígitos.")
            case "4":
                name = input("Introduce el contacto a eliminar: ")
                if name in agenda:
                    del agenda[name]
                    print("Contacto eliminado.")
                else:
                    print(f"El contacto {name} no existe.")
            case "5":
                print("Saliendo de la agenda.")
                break
            case _:
                print("Opción no válida, elige una opción del 1 al 5.")

        
my_agenda()

