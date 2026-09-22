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

s = 1

while s != 0:
    print("\n-------AGENDA DE CONTACTOS-------")
    print("1- BÚSQUEDA")
    print("2- INSERCIÓN")
    print("3- ACTUALIZACIÓN")
    print("4- ELIMINACIÓN")
    print("5- SALIR")

    try:
        accion = int(input("SELECCIONA LA ACCIÓN QUE DESEAS HACER: "))
    except ValueError:
        print("Por favor, ingresa un número de opción válido.")
        continue

    match accion:

        case 1:
            busqueda = input("INGRESA EL NOMBRE A BUSCAR: ").strip()
            # Verifica dinámicamente si el nombre existe en las claves del diccionario
            if busqueda in agenda_contactos:
                print(f"Contacto encontrado -> {busqueda}: {agenda_contactos[busqueda]}")
            else:
                print("Contacto no encontrado.")

        case 2:
            nombre = input("INSERTA EL NOMBRE DEL NUEVO CONTACTO: ").strip()
            telefono = input("INSERTA EL NÚMERO DEL NUEVO CONTACTO: ").strip()
            
            # Asigna el teléfono usando el nombre directamente como clave
            agenda_contactos[nombre] = telefono
            print(f"¡Contacto '{nombre}' registrado con éxito!")

        case 3:
            nombre = input("INGRESA EL NOMBRE DEL CONTACTO A ACTUALIZAR: ").strip()
            if nombre in agenda_contactos:
                nuevo_telefono = input(f"INTRODUCE EL NUEVO NÚMERO PARA {nombre}: ").strip()
                agenda_contactos[nombre] = nuevo_telefono
                print(f"¡Contacto '{nombre}' actualizado correctamente!")
            else:
                print("El contacto especificado no existe.")

        case 4:
            nombre = input("INGRESA EL NOMBRE DEL CONTACTO A ELIMINAR: ").strip()
            if nombre in agenda_contactos:
                del agenda_contactos[nombre] 
                print(f"¡Contacto '{nombre}' eliminado correctamente!")
            else:
                print("El contacto especificado no existe.")

        case 5:
            print("------------------------------------")
            print("HAS SALIDO DE TU AGENDA DE CONTACTOS")
            print("------------------------------------")
            s = 0

        case _:
            print("Opción no válida. Intenta de nuevo.")

