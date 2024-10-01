"""
Listas
"""

nums = [1,2,3,4]

# borrado
nums.pop(0) # por índice
nums.remove(2) # por valor
nums.clear() # eliminar todos los elementos de la lista

# inserción
nums.append(5)
nums.insert(1, 10) # por índice
nums.extend([1,5]) # extender de otra lista

# actualización
nums[0] = 11 # por indice

# ordenación
nums.sort()

"""
Tuplas
"""

numsTuple = (10,2,13,42,5)

# obtener valores
numsTuple[0] # 1

# ordenación
sorted(numsTuple)

"""
Set
"""

numsSet = {1,3,5,6}

# borrado
numsSet.pop() # primer elemento
numsSet.remove(3) # por valor
numsSet.clear() # eliminar todos los elementos
numsSet.discard(5) # eliminar si existe en el set

# inserción
numsSet.add(7)

# actualización
numsSet.update({20,30})

"""
Diccionario
"""

person = {'name': 'michael', 'last_name': 'bay'}

# inserción
person['age'] = 30

# borrado
person.pop('last_name')
del person['age']

# actualización
person['name'] = "gabriel"

"""
Opcional
"""

contactos = []
print("****AGENDA****")
while True :
    print("1. Buscar contactos (por nombre)")
    print("2. Crear contacto")
    print("3. Actualizar contacto")
    print("4. Eliminar contacto")
    print("5. Salir")

    opcion = int(input("Eliga su operación: "))

    if opcion == 1:
        nombre = input("Ingrese el nombre del contacto: ")
        contactosEncontrados = []
        for contacto in contactos:
            if contacto['nombre'] == nombre:
                contactosEncontrados.append(contacto)

        if len(contactosEncontrados) == 0:
            print(f"No hay contactos con el nombre {nombre}")
        else:
            print(f"El número de {nombre} es {contactosEncontrados[0]['télefono']}")
    elif opcion == 2:
        nombre = input("Ingrese el nombre del contacto: ")
        tlf = input("Ingrese el número de télefono: ")
        if not tlf.isdigit():
            print("El número de télefono debe ser numérico!!")
            continue
        if len(tlf) != 11:
            print("El número de télefono debe tener 11 digitos!!")
            continue

        contactos.append({'nombre': nombre, 'télefono': tlf})
        print("Contacto agregado!")
    elif opcion == 3:
        nombre = input("Ingrese el nombre del contacto que quiere actualizar: ")
        contactosEncontrados = []
        for contacto in contactos:
            if contacto['nombre'] == nombre:
                contactosEncontrados.append(contacto)

        if len(contactosEncontrados) == 0:
            print(f"No hay contactos con el nombre {nombre}")
        else:
            tlf = input("Ingrese el nuevo número de télefono: ")
            if not tlf.isdigit():
                print("El número de télefono debe ser numérico!!")
                continue
            if len(tlf) != 11:
                print("El número de télefono debe tener 11 digitos!!")
                continue
            contactos[contactos.index(contactosEncontrados[0])]['télefono'] = tlf
            print("Contacto acutalizado!")
            continue
    elif opcion == 4:
        nombre = input("Ingrese el nombre del contacto que quiere eliminar: ")
        contactosEncontrados = []
        for contacto in contactos:
            if contacto['nombre'] == nombre:
                contactosEncontrados.append(contacto)
        if len(contactosEncontrados) == 0:
            print(f"No hay contactos con el nombre {nombre}")
        else:
            contactos.pop(contactos.index(contactosEncontrados[0]))
            print("Contacto eliminado!")
            continue
    elif opcion == 5:
        break



