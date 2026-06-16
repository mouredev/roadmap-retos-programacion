from collections import deque


"""
Estructuras de datos
"""

print("LISTAS\n")

# Listas
fruits = ["orange", "apple", "pear", "banana", "kiwi", "apple", "banana"]
print("Lista original: ", fruits)

conteo = fruits.count("apple")
print("Veces que aparece 'apple': ", conteo)

indice_banana = fruits.index("banana")
print("Indice de banana: ", indice_banana)

otra_banana = fruits.index(
    "banana", 4
)  # Encuentra la siguiente banana, buscando desde la 4ta posicion
print("Buscar el indice siguiente de otra banana: ", otra_banana)

fruits.reverse()
print("Lista invertida: ", fruits)

fruits.append("grape")
print("'grape' añadida al final de la lista", fruits)

fruits.sort()
print("lista ordenada: ", fruits)

fruits.pop()
print("Eliminada la última fruta", fruits, "\n")

"""
Usar listas como pilas (último en entrar, primero en salir)
"""

print("LISTAS COMO PILAS\n")

stack = [6, 7, 2]
print("Stack original: ", stack)

stack.append(6)
stack.append(7)

print("Stack con 2 elementos añadidos: ", stack)

stack.pop()
print("Último elemento retirado, 7: ", stack)

stack.pop()
print("Ahora que el elemento es 6, es eliminado: ", stack, "\n")

"""
Listas como colas (primero en entrar, primero en salir)
"""
print("LISTAS COMO COLAS\n")

queue = deque([23, 7, 45, 76])
print("Cola original: ", queue)

queue.append(56)
print("Añadido el número 56: ", queue)

queue.popleft()
print("Eliminado el primero en la posicion: ", queue, "\n")

"""
Tuplas
"""

print("TUPLAS\n")

# Tuplas
t = 1232131, "Hola", 21424
print("Tupla estandar: ", t)

u = t, ("Hola", 342432, 564)
print("Tupla anidada: ", u)


tuple_with_mutable_objects = ([23, 34, 545], [324, 554, 676])
print("Tupla con objetos mutables", tuple_with_mutable_objects, "\n")

"""
Conjuntos
"""

# Conjunto vacío
group_a = set()

# Conjunto con valores
group_b = {"Ana", "Pedro", "Carlos", "Antonio"}


# Agregando valores con el método add
for i in range(5):
    group_a.add(i)


print("Grupo a: ", group_a)
print("Grupo b: ", group_b)

# Borrado de valores
group_a.pop()
print("número al azar eliminado: ", group_a)

# Ordenamiento
ascendente = sorted(group_b)
decendente = sorted(group_b, reverse=True)

print(ascendente)
print(decendente)

"""
Diccionarios
"""

# vacío
diccionario_1 = {}
print("Vacío: ", diccionario_1)

# Con elementos
diccionario_2 = {"Martín": {"Edad": 21}}

# Agregar datos
diccionario_1["Fruta"] = "Manzana"
diccionario_2["Sofía"] = {"Edad": 20}
diccionario_2["Felipe"] = {"Edad": 23}

print("Frutas: ", diccionario_1)
print("Nombres: ", diccionario_2)

# Actualización
diccionario_1.update({"Fruta": "Pera"})
print("Actualización de fruta: ", diccionario_1)

diccionario_2["Sofía"]["Edad"] = 19
print("Actualización edad Sofía: ", diccionario_2["Sofía"])

# Borrado
del diccionario_2["Martín"]
print("Martín borrado: ", diccionario_2)

# Ordenamiento
ordenado = sorted(diccionario_2.items())

print("Diccionario ordenado: ", ordenado, "\n")

# Agenda de contactos

print("Agenda", "\n")

contacts = {}


def searchContact():
    while True:
        try:
            tel = int(input("Escribe el número a Buscar: "))
            if tel in contacts:
                print("Encontrado: ", contacts[tel]["Nombre"])
                return
            if tel == 0:
                return
            else:
                print("No existe.\n0. volver al menu.")
        except ValueError:
            print("Debe ser numérico")


def addContact():
    while True:
        try:
            name = input("Escriba el nombre: ")
            tel = int(input("Escriba el número de teléfono: "))

            if len(str(tel)) <= 11 and len(str(tel)) > 2:
                contacts[tel] = {"Nombre": name}
                print(f"Se agregó {name} a su agenda\nRedirigiendo al menu...\n")
                return
            else:
                print("No es válido")
        except ValueError:
            print("Eso no es un número¡")


def updateContact():
    while True:
        try:
            option = int(
                input(
                    "Elige que quieres actualizar:\n1. Teléfono\n2. Nombre\n3. Regresar\n: "
                )
            )
            match option:
                case 1:
                    old = int(input("Escribe el número de teléfono: "))
                    if old in contacts:
                        new = int(input("Escribe el nuevo número: "))
                        if new in contacts:
                            print(f"El usuario {contacts[new]['Nombre']} ya existe")
                        elif new == old:
                            print("Es el mismo número")
                        else:
                            contacts[new] = contacts[old]
                            del contacts[old]
                            print("Actualizado")
                            return
                    else:
                        print("No existe")
                case 2:
                    number = int(input("Escribe el número: "))
                    if number in contacts:
                        name = input("Escribe el nuevo nombre: ")
                        contacts[number]["Nombre"] = name
                        print("Actualizado")
                        return
                    else:
                        print("No existe")
                case 3:
                    return
                case _:
                    print("Opción no valida")

        except ValueError:
            print("El valor debe ser numérico")


def deleteContact():
    while True:
        try:
            number = int(input("Escribe el numero\n 0. Salir\n: "))
            if number == 0:
                return

            if number in contacts:
                option = int(
                    input(
                        f"Seguro de que quieres eliminar a {contacts[number]}?\n1. Si\n2. No\n0. Regresar\n: "
                    )
                )
                match option:
                    case 1:
                        del contacts[number]
                        print("Contacto eliminado")
                        return
                    case 2:
                        print("Regresando...")
                        return
                    case 0:
                        print("Regresando...")
                        return
                    case _:
                        print("Opción no valida")
            else:
                print("No existe")
        except ValueError:
            print("No es un número")


def Agenda():

    while True:
        print(
            "1. Buscar contacto",
            "2. Añadir contacto",
            "3. Actualizar contacto",
            "4. Eliminar contacto",
            "5. Salir",
            sep="\n",
        )

        if contacts:
            print(contacts.items())
        else:
            print("No hay contactos")

        try:
            option = int(input(": "))
            match option:
                case 1:
                    searchContact()
                case 2:
                    addContact()
                case 3:
                    updateContact()
                case 4:
                    deleteContact()
                case 5:
                    break
        except ValueError:
            print("No valido, debe ser numérico")


Agenda()
