# Listas
my_list = ["Brais", "Bl4ck", "Wolfy", "Visionos"]
print(my_list)
my_list.append("Castor")  # Inserción
print(my_list)
my_list.remove("Brais")  # Eliminación
print(my_list)
print(my_list[1])  # Acceso
my_list[1] = "Cuervillo"  # Actualización
print(my_list)
my_list.sort()  # Ordenación
print(my_list)
print(type(my_list))

# Tuplas
my_tuple: tuple = ("Brais", "Moure", "@mouredev", "36")
print(my_tuple[1])  # Acceso
print(my_tuple[3])
my_tuple = tuple(sorted(my_tuple))  # Ordenación
print(my_tuple)
print(type(my_tuple))

# Set

# Diccionario
my_dict: dict = {
    "name": "Brais",
    "surname": "Moure",
    "alias": "@mouredev",
    "age": "36"
}
my_dict["email"] = "mouredev@gmail.com"  # Inserción
print(my_dict)
del my_dict["surname"]  # Eliminación
print(my_dict)
print(my_dict["name"])  # Acceso
my_dict["age"] = "37"  # Actualización
print(my_dict)
my_dict = dict(sorted(my_dict.items()))  # Ordenación
print(my_dict)
print(type(my_dict))

"""
EXTRA
"""

# AGENDA DE CONTACTOS 

agenda_contactos: dict = {
    "Mónica": "75310006",
    "Neslin": "57366046"
}

def nombre_contacto():
    nombre = input("INGRESE EL NOMBRE DEL CONTACTO: ")
    return nombre

def telefono_contacto():
    telefono = input("INTRODUCE EL NÚMERO DE TELÉFONO: ")
    if telefono.isdigit() and len(telefono) > 0 and len(telefono) == 8:
        agenda_contactos[nombre] = telefono
    else:
        print("DEBES INTRODUCIR UN NÚMERO DE TELÉFONO DE 8 DÍGITOS")




while True:

    print("\n-------AGENDA DE CONTACTOS-------")
    print("1- BÚSQUEDA")
    print("2- INSERCIÓN")
    print("3- ACTUALIZACIÓN")
    print("4- ELIMINACIÓN")
    print("5- SALIR")

    accion = input("\nSelecciona una opción: ")

    match accion:

        case "1":
            nombre = nombre_contacto()
            if nombre in agenda_contactos:
                print(f"El número de Teléfono de {nombre} es: {agenda_contactos[nombre]}")
            else:
                print("El contacto que ingresaste no existe")

            
        case "2":
            nombre = nombre_contacto()
            telefono_contacto()
            print("--CONTACTO AÑADIDO CORRRECTAMENTE--")
         
        case "3":
            nombre = nombre_contacto()
            if nombre in agenda_contactos:
             telefono_contacto()
             print("--TELÉFONO ACTUALIZADO CORRRECTAMENTE--")
            else:
                print("El contacto que ingresaste no existe.")
        case "4":
            nombre = nombre_contacto()
            if nombre in agenda_contactos:
                del agenda_contactos[nombre]
                print("--CONTACTO ELIMINADO CORRRECTAMENTE--")
            else:
                print("El contacto que ingresaste no existe.")
        case "5":
            print("------------SALIENDO DE LA AGENDA------------")
            break
        case _:
            print("Opción no válida. Elige una del 1 al 5")



            
            