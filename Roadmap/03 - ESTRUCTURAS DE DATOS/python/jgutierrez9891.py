"""
Estructuras de datos
"""

# Listas

ciudades = ["Bogotá", "Cali", "Medellín", "Cartagena", "Santa Marta", "Bucaramanga"]

#Agregar elemento al final
ciudades.append('Pereira')
print(ciudades)

# Remover elemento
ciudades.remove('Cali')
print(ciudades)

# Insertar elemento en una posición dada
ciudades.insert(3, "Montería")
print(ciudades)

# Eliminar elemento en una posicióno dada
ciudades.pop(5)
print(ciudades)

# Ordenar elementos
ciudades.sort()
print(ciudades)

# Actualizar elemento
ciudades[1] = "Cartagena de Indias"
print(ciudades)

#Tuplas

animales_salvajes = "pájaro", "león", "ratón", "pez", "murciélago", "liebre"

# Las tuplas son inmutables: no se puede agregar, modificar o eliminar elementos

# Seleccionar elemento
print(animales_salvajes[2])

# Anidar otra tupla
animales = "perro", animales_salvajes
print(animales)

# Diccionarios

telefonos = {'Jose': 34973904, 'Andrea': 4343240, 'Eduardo': 38105735, 'Luisa': 44340904}

# Seleccionar elemento
print (telefonos['Andrea'])

# Añadir elemento
telefonos['Alberto'] = 31735540
print (telefonos)

# Eliminar elemento
del telefonos['Eduardo']
print (telefonos)

# Ordenar elementos
print (dict (sorted(telefonos.items())))

# Actualizar elemento
telefonos['Andrea'] = 1234567
print (telefonos)


"""
Extra
"""

contactos = {'Jose': 34973904, 'Andrea': 4343240, 'Eduardo': 38105735, 'Luisa': 44340904}

def consultar_contacto():
    nombre = input(f"Ingrese el nombre del contacto que desea buscar:\n")
    if nombre in contactos.keys():
        print (f"El teléfono de {nombre} es {contactos[nombre]}")
        print(contactos)
    else:
        print("El nombre ingresado no se encuentra en los contactos")
    

def agregar_contacto():
    nombre = input(f"Ingrese el nombre del contacto que desea agregar:\n")
    telefono = input(f'Ingrese el teléfono del contacto\n')
    if telefono.isdigit() and len(telefono) <= 11:
        contactos[nombre] = int(telefono)
        print (f"El contacto {nombre} ha sido agregado a su lista")
        print(contactos)
    else:
        print("El teléfono ingresado no es válido. Debe ser un valor numérico de máximo 11 dígitos")

def actualizar_contacto():
    nombre = input(f"Ingrese el nombre del contacto que desea actualizar:\n")
    if nombre in contactos.keys():
        telefono = input(f'Ingrese el nuevo teléfono del contacto\n')
        if telefono.isdigit() and len(telefono) <= 11:
            contactos[nombre] = int(telefono)
            print (f"El teléfono de {nombre} ha sido actualizado a {telefono}")
            print(contactos)
        else:
            print("El teléfono ingresado no es válido. Debe ser un valor numérico de máximo 11 dígitos")
    else:
        print("El nombre ingresado no se encuentra en los contactos")
    

def eliminar_contacto():
    nombre = input(f"Ingrese el nombre del contacto que desea eliminar:\n")
    if nombre in contactos.keys():
        del contactos[nombre]
        print (f"El contacto {nombre} ha sido eliminado")
        print(contactos)
    else:
        print("El nombre ingresado no se encuentra en los contactos")
    

def admin_contactos():
    accion = 0
    while True:
        accion = input("Ingresa la acción a realizar:\n"
                    "1: buscar contacto\n"
                    "2: agregar contacto\n"
                    "3: actualizar contacto\n"
                    "4: eliminar contacto\n"
                    "5: Terminar programa\n")

        match accion:
            case "1":
                consultar_contacto()
            case "2":
                agregar_contacto()
            case "3":
                actualizar_contacto()
            case "4":
                eliminar_contacto()
            case "5":
                print("Gracias por utilizar la lista de contactos")
                break
            case _:
                print("No ha ingresado una opción válida.")


admin_contactos()

