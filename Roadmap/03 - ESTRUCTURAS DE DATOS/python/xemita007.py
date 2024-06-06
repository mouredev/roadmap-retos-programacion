@ -1,232 +0,0 @@
# Ejercicio 03 Estructuras de Datos

###Listas

miLista = list()  ## se convierte a lsita cualquier variable
miOtraLista = []  ##se declara con el corchete

print(len(miOtraLista))  ## cuenta elementos de la lsita

miLista = [5, 8, 7, 4, 5, 8, 7, 9]  ## inserción de datos

miLista

# Operación de ordenación
print("Operaciones de ordenación")

miLista.reverse()
print(miLista)

miLista.sort()
print(miLista)

# Operación de inserción
print("Operaciones de inserción")

miLista.append(20)  # Lo añade al final
miLista.insert(0, 25)  # Lo añade donde espesifiquemos en este caso el primero

print(miLista)


# Operación de actualización
print("Operaciones de actualización")

miLista[0] = 1  # modificamos el elemento primero por un 0
print(miLista)


# Operación de busqueda
print("Operaciones de busqueda")
elementos = miLista.__len__()
elemento1 = miLista[0]
print(miLista)
elementoUltimo = miLista[-1]
print("Cantidad de elementos de la lista... ", elementos)
print("Primer elemento de la lista... ", elemento1)
print("Ultimo elemento de la lista... ", elementoUltimo)
print("Cuantas veces aparece el numero 8: ", miLista.count(8))
print("En que indice se encuentra el numero 8: ", miLista.index(8))
print("Quiero ver desde el indice 0 al 4", miLista[0:5])

# Operación de borrado
print("Operaciones de borrado")
miLista.pop(0)  # Borrado por indice
miLista.remove(20)  # Borrado por valor
del miLista[-1]
print(miLista)
miLista.clear()
print("Despues del clear mi lista es: ", miLista)

### Tuplas
myTuple = tuple()
myTuple = ("Antonio", "Juan", "Pepe", "Cristian")

print(len(myTuple))  ## cuenta elementos de la lsita
print(myTuple.__len__())

# Operación de inserción
print("Operaciones de inserción")

myTuple = ("Antonio", "Juan", "Pepe", "Cristian")

cadena = "Chema"
myTuple = myTuple + (cadena,)


print(myTuple)

# Operación de ordenación
print("Operaciones de ordenación")
myTuple = tuple(sorted(myTuple))
print(myTuple)


# Operación de actualización
print("Operaciones de actualización")
myTuple = list(myTuple)
myTuple[0] = "Jose"
myTuple.insert(0, "Primero")
myTuple = tuple(myTuple)
print(myTuple)

# Operación de busqueda
print("Operaciones de busqueda")

print(myTuple[0])
print(myTuple[-1])
print(myTuple[0:2])

print(myTuple.index("Chema"))

# Operación de borrado
print("Operaciones de borrado")


# Sets

mySet = set()


print("Operaciones de inserción")

mySet = {"chema", "jose", "rodolfo", "juan", "moure"}
mySet.add("carlos")
mySet.add("carlos")  # no duplica los datos
print(mySet)

print("Operaciones de ordenación en set no tiene sentido")


print("Operaciones de actualización en set no tiene sentido ")


print("Operaciones de busqueda en set no tiene sentido")


print("Operaciones de borrado")

mySet.pop()  # elimina al azar por que no se ordena no tiene sentido
mySet.remove("jose")
print(mySet)


# Diccionarios
myDict = dict()
myDict = {}
print("Operaciones de insert")

myDict = {"Nombre": "Chema", "Apellido": "Galvez", "Correo": "xemita_007@hotmail.com"}
print(myDict)

myDict = {
    "Nombre": "Chema",
    "Apellido": "Galvez",
    "Correo": "xemita_007@hotmail.com",
    "Lenguajes": {"java", "Python", "Kotlin"},
}

myDict["Calle"] = "calle murillo 5"
print(myDict)


print("Operaciones de ordenación")
myDict = dict(sorted(myDict.items()))  # ordenar por clave
print(myDict)

print("Operaciones de actualización")

myDict["Nombre"] = "Jose Manuel"

print(myDict["Nombre"])

print("Operaciones de busqueda")

print("nombre del diccionario es: ", myDict["Nombre"])


print("Operaciones de borrado")

myDict.popitem()  # elimina el ultimo elemento del diccionario
print(myDict)
del myDict["Correo"]
print(myDict)

##DIFICULTA EXTRA
agendaList = list()

while True:
    print(
        "Bienvenido a la agenda que desea realizar: 1:inserción,2:actualización,3:busqueda, 4:eliminación, 5:Listar y 6:Salir"
    )
    consola = int(input())
    print(consola)
    if consola == 1:
        contacto = {"nombre": "", "Telefono": ""}
        contacto["nombre"] = input("Inserter el nombre: ")
        contacto["Telefono"] = input("Inserter el telefono: ")
        if contacto["Telefono"].__len__() <= 11 and contacto["Telefono"].isdigit():
            agendaList.append(contacto)
        else:
            print("Error Introducir solo digitos maximo 11")

    elif consola == 2:
        print("Actualizar")
        contactoA = input("nombre que desea actualizar: ")
        if contacto["nombre"] == contactoA:
            contacto["nombre"] = input("nombre nuevo: ")
            contacto["Telefono"] = input("Telefono nuevo: ")
            if contacto["Telefono"].__len__() <= 11 and contacto["Telefono"].isdigit():
                agendaList.append(contacto)
            else:
                print("Error Introducir solo digitos maximo 11")
        else:
            print("el conctacto no se encuentra")

    elif consola == 3:
        print("Busqueda")
        contactoB = input("nombre que desea buscar: ")
        if contacto["nombre"] == contactoB:
            print("Encontrado: ", contacto["nombre"], contacto["Telefono"])

        else:
            print("Contacto no encontrado intentelo de nuevo")
    elif consola == 4:
        print("Eliminación")
        contactoE = input("nombre que desea Eliminar: ")
        if contacto["nombre"] == contactoE:
            del contacto["nombre"], contacto["Telefono1"]
        else:
            print("Contacto no encontrado intentelo de nuevo")
    elif consola == 5:
        for contacto in agendaList:
            print(f"Nombre: {contacto['nombre']}, Teléfono: {contacto['Telefono']}")
    elif consola == 6:
        print("Salir")
        break
    else:
        print("por favor selecciones una de las opciones")


print("se imprime la lista: ")
print(agendaList)