# Listas
print("Vamos a crer una lista")
miLista = [1,8,4,2,5,6]

# Imprimir lista
print(f"La lista es: {miLista}")

# Añadir elemento a la lista
miLista.append(3)
print(f"La lista queda asi tras insertar el 3: {miLista}")

# Añadir elemento en una posicion concreta
miLista.insert(2, 10)
print(f"La lista queda asi tras insertar el 10 en la posicion 2: {miLista}")

# Eliminar un elemento de la lista
miLista.remove(2)
print(f"La lista tras eliminar el 2 es: {miLista}")

# Buscar un elemento en una posicion de la lista 
print(f"La elemento den la posicion 5 de la lista es: {miLista.index(5)}")

# Ordenar una lista
miLista.sort()
print(f"La lista ordenada es: {miLista}") 

# Invertir una lista
miLista.reverse()
print(f"La lista ordenada de forma inversa es: {miLista}")

# Comprobar si un elemento esta en la lista
print(f"¿Esta el numero 10 en la lista?: {10 in miLista}")

print("\n")

# Tuplas
print("Vamos a crear una tupla")
miTupla = (1,2,6,7,4,2,8)

print(f"El contenido de mi tupla es {miTupla}")

# añadir elemento a una tupla
miTupla += (5,)
print(f"El contenido de mi tupla tras añadir el 5 es: {miTupla}")

# convertir una tupla en una lista
miLista = list(miTupla)
print(f"El contenido de mi lista es: {miLista}")

# Convertir una lista en una tupla
miTupla = tuple(miLista)
print(f"El contenido de mi tupla es: {miTupla}")
# No se pueden añadir o eliminar elementos en una tupla

#ordenar tupla
miTupla = sorted(miTupla)
print(f"El contenido de mi tupla ordenada es: {miTupla}")

# Buscar un elemento en una tupla
print(f"El elemento 8 esta en la posicion {miTupla.index(8)}")

#Juntar dos tuplas
miTupla2 = (10,11,12)
miTupla += miTupla2
print(f"El contenido de mi tupla tras juntarla con otra es: {miTupla}")

print("\n")

# Conjuntos
print("Vamos a crear un conjunto")

# Crear un conjunto
miConjunto = set()
print(f"El contenido de mi conjunto es: {miConjunto}")
# Añadir elementos al conjunto
miConjunto.add(1)
miConjunto.add(2)
miConjunto.add(3)

print(f"El contenido de mi conjunto es: {miConjunto}")
# Eliminar un elemento del conjunto
miConjunto.discard(1)
print(f"El contenido de mi conjunto es: {miConjunto}")

# Comprobar si un elemento esta en el conjunto
print(f"¿Esta el numero 2 en el conjunto?: {2 in miConjunto}")

# Juntar conjuntos
miConjunto2 = {3,4,5}
miConjunto = miConjunto.union(miConjunto2)
print(f"El contenido de mi conjunto tras juntarlo con otro es: {miConjunto}")

# Diferencia entre conjuntos
miConjunto = {1,2,3,4,5}
miConjunto2 = {3,4,5,6,7}
miConjunto = miConjunto.difference(miConjunto2)
print(f"El contenido de mi conjunto tras hacer la diferencia con otro es: {miConjunto}")

# Interseccion entre conjuntos
miConjunto = {1,2,3,4,5}
miConjunto2 = {3,4,5,6,7}
miConjunto = miConjunto.intersection(miConjunto2)
print(f"El contenido de mi conjunto tras hacer la interseccion con otro es: {miConjunto}")

print("\n")

# Diccionarios
print("Vamos a crear un diccionario")

# Crear un diccionario
miDiccionario = {"Alemania":"Berlin", "Francia":"Paris", "España":"Madrid", "Italia":"Roma"}
print(f"El contenido de mi diccionario es: {miDiccionario}")

# Añadir un elemento al diccionario
miDiccionario["Portugal"] = "Lisboa"
print(f"El contenido de mi diccionario es: {miDiccionario}")

# Eliminar un elemento del diccionario
del miDiccionario["Portugal"]
print(f"El contenido de mi diccionario es: {miDiccionario}")

# Extra

agenda = {}

def showMenu():
    print("\nAgenda de Contactos")
    print("1. Buscar contacto")
    print("2. Insertar contacto")
    print("3. Actualizar contacto")
    print("4. Eliminar contacto")
    print("5. Mostrar todos los contactos")
    print("6. Salir")

def searchContact():
    nombre = input("Ingrese el nombre del contacto a buscar: ")
    if nombre in agenda:
        print(f"Nombre: {nombre}, Teléfono: {agenda[nombre]}")
    else:
        print(f"El contacto {nombre} no existe en la agenda.")

def addContact():
    nombre = input("Ingrese el nombre del contacto: ")
    telefono = input("Ingrese el número de teléfono: ")

    # Validar que el número de teléfono sea numérico y tenga la longitud deseada
    if telefono.isdigit() and len(telefono) <= 11:
        agenda[nombre] = telefono
        print(f"Contacto {nombre} insertado correctamente.")
    else:
        print("Número de teléfono no válido.")

def updateContact():
    nombre = input("Ingrese el nombre del contacto a actualizar: ")
    if nombre in agenda:
        nuevo_telefono = input("Ingrese el nuevo número de teléfono: ")

        # Validar que el número de teléfono sea numérico y tenga la longitud deseada
        if nuevo_telefono.isdigit() and len(nuevo_telefono) <= 11:
            agenda[nombre] = nuevo_telefono
            print(f"Contacto {nombre} actualizado correctamente.")
        else:
            print("Número de teléfono no válido.")
    else:
        print(f"El contacto {nombre} no existe en la agenda.")

def removeContact():
    nombre = input("Ingrese el nombre del contacto a eliminar: ")
    if nombre in agenda:
        del agenda[nombre]
        print(f"Contacto {nombre} eliminado correctamente.")
    else:
        print(f"El contacto {nombre} no existe en la agenda.")

def listContact():
    if agenda:
        print("\nLista de contactos:")
        for nombre, telefono in agenda.items():
            print(f"Nombre: {nombre}, Teléfono: {telefono}")
    else:
        print("La agenda está vacía.")

# Menú principal
while True:
    showMenu()
    opcion = input("Seleccione una opción (1-6): ")

    if opcion == "1":
        searchContact()
    elif opcion == "2":
        addContact()
    elif opcion == "3":
        updateContact()
    elif opcion == "4":
        removeContact()
    elif opcion == "5":
        listContact()
    elif opcion == "6":
        print("¡Hasta luego!")
        break
    else:
        print("Opción no válida. Por favor, seleccione una opción del 1 al 6.")