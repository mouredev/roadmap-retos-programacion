"""#03 ESTRUCTURAS DE DATOS"""

# ----------------------- Listas -----------------------
# Estas se encierran por corchetes cuadrados []

import random

print("------ LISTAS ------\n")
lista = [1, 2, 3]
nuevaLista = list(range(3))  # List recibe un iterable para crear una lista
print(f"Lista original: {lista} | {nuevaLista}")
lista.append(4)  # agrega un item al final de la lista
print(f"Agregado \"4\" con append: {lista}")
# lista.extend(lista)
# agrega el 2do argumento en la posición indicada por el 1er argumento
lista.insert(1, 5)
print(f"Agregando \"5\" en índice \"1\" con insert: {lista}")
# Quita el valor de la lista (Si hay muchos iguales, quita el primero)
lista.remove(5)
print(f"Quitando \"5\" con remove: {lista}")
# Quita el último valor de la lista (como pilas) y regresa el valor quitado
elementoEliminado = lista.pop()
print(f"Quitando el último valor \"{elementoEliminado}\" con pop: {lista}")
# Regresa el indice donde se encuentra el argumento
print(f"Index de 2: {lista.index(2)}")
# Regresa el # de veces que el argumento se repite
print(f"Repet de 2: {lista.count(2)}")
lista.sort(reverse=True)
print(f"Lista invertida con sort: {lista}")
lista.reverse()
print(f"Lista invertida con reverse: {lista}")
lista.clear()  # Vacía la lista

"""
PILAS: Se usa list.append() para agregar un elemento a la lista y list.pop() para sacarlo
USA LIFO (last in, first out)

COLAS: Se usa list.append() igual, pero se usa list.popleft() para sacar el primero
USA FIFO (first in, first out)

La diferencia es que se requiere importar deque de collections para poder usarse como cola

Sacado de python.org ⬇️

from collections import deque

queue = deque(["Eric","John","Michael"])
queue.append("Terry") # Agrega a Terry
queue.append("Graham") # Agrega a Graham
queue.popleft() # Saca al primero en llegar (Eric)
queue.popleft() # Saca al segundo en llegar (John)
queue # Muestra la cola "deque(["Michael","Terry","Graham"])"
"""

"""
Comprensión de listas

Es como hacer un for y usando .append() para ir agregando el elemento en cada iteración

# Esto ⬇️
listaDeNumeros = []
for numero in range(10):
    listaDeNumeros.append(numero)

# Es equivalente a esto ⬇️
listaDeNumeros = [numero for numero in range(10)]
 """


""" La instrucción del hace lo mismo que la función pop, pero no devuelve ningún valor """


# ----------------------- Tuplas -----------------------
# Estas se encierran por paréntesis ()

print("\n------ TUPLAS ------\n")
tupla1 = (1, 2, 3)
tuplaNueva = tuple(range(3))  # tuple recibe un iterable para crear una tupla
# Al agregar datos separados con comas, tambien se crean las tuplas (empaquetado)
tupla2 = "hola", 1, "cien"
saludo, entero, numStr = tupla2  # Desempaquetado
nuevaTupla = tupla1, tupla2  # Podemos crear nuevas tuplas de otras tuplas existentes
# tupla1.append() # No se pueden modificar las tuplas
# tupla1.pop()
# Podemos hacer tuplas con listas
tuplaConListas = ([1, 2, 3], [4, 5, 6], [7, 8, 9])
print(nuevaTupla)


# ----------------------- Conjuntos -----------------------
# Se encierran por llaves {}
# Colección no ordeneda y sin elementos repetidos
# Se puede usar la funcion set() para crear un conjunto
# Se puede usar la comprension de conjuntos (identica a comprension de listas)

print("\n------ CONJUNTOS ------\n")
frutas = {"manzana", "naranja", "pera", "fresa", "platano"}
listaVerduras = ["zanahoria", "zanahoria", "tomate",
                 "cilantro", "tomate", "jalapeno"]
verdurasSinRepetir = set(listaVerduras)  # set recibe un iterable
# in indica si un elemento está en una lista o conjunto
print(frutas, verdurasSinRepetir, f"{listaVerduras[1] in verdurasSinRepetir}")


# ----------------------- Diccionarios -----------------------
# Estos se encierran por llaves {}
# Estos si o si deben llevar:
# - Una clave (Los que están con comillas dobles)
# - Un valor (Los que estan después de ":" y antes de ",")

print("\n------ DICCIONARIOS ------\n")
diccionario = {"1erValor": 1,
               "2doValor": 2,
               "3erValor": 3}
# dict crea diccionarios desde secuencias de pares clave-valor ("Clave": Valor)
nuevoDiccionario = dict(
    [("Nombre", "Allan"), ("Apellido", "Salazar"), ("Edad", 29)])

print(diccionario)
print(nuevoDiccionario, end="\n\n")

# Interaccion con diccionarios
# items() nos devuelve cada item clave-valor como tupla
for item in diccionario.items():
    print(item)

# si ponemos dos variables, la primera guarda la clave y la segunda el valor
for c, v in diccionario.items():
    print(c, v)

# enumerate() develve cada item indice-valor como tupla
for item in enumerate(diccionario):
    print(item)

# si ponemos dos variables, la primera guarda el indice y la segunda el valor
for i, v in enumerate(diccionario):
    print(i, v)

# ----------------------- EJERCICIO -----------------------

# Creamos la agenda en base a una lista de diccionarios
agenda = [{"id": 1,
          "Nombre": "Allan",
           "Numero": 10123456789}]

# Buscando un usuario


def buscarUsuario(nombreUsuario):
    for usuario in agenda:
        if nombreUsuario in usuario["Nombre"]:
            return usuario
    return "Usuario no encontrado"

# Agregando un usuario


def agregarUsuario():
    nombreNuevoUsuario = str(input("Ingresa el nombre: "))
    numeroNuevoUsuario = "0"
    # Verificamos que el usuario ingrese un numero correcto
    while len(numeroNuevoUsuario) != 11:
        numeroNuevoUsuario = str(input("Ingresa el numero: "))
        if len(numeroNuevoUsuario) != 11:
            print("Debes ingresar un numero correcto.")
        else:
            agenda.append({"id": random.randint(1, 100),
                           "Nombre": nombreNuevoUsuario,
                           "Numero": numeroNuevoUsuario})
            print("Usuario agregado")
    return agenda

# Actualizando un usuario


def actualizarUsuario(nombreUsuario):
    # Verificamos que el usuario exista
    usuarioEncontrado = buscarUsuario(nombreUsuario)
    if usuarioEncontrado != "Usuario no encontrado":
        nuevoNombreUsuario = str(input("Ingresa el nuevo nombre: "))
        usuarioEncontrado["Nombre"] = nuevoNombreUsuario
        # Conseguimos la ubicacion del usuario encontrado y reemplazamos el nombre
        for indice, usuario in enumerate(agenda):
            if usuario["Nombre"] == usuarioEncontrado["Nombre"]:
                agenda[indice] = usuarioEncontrado
        print("Usuario actualizado")
    else:
        print(usuarioEncontrado)
    return agenda

# Borrando un usuario


def borrarUsuario(nombreUsuario):
    # Verificamos que el usuario exista
    usuarioEncontrado = buscarUsuario(nombreUsuario)
    if usuarioEncontrado != "Usuario no encontrado":
        # Borramos al usuario encontrado
        agenda.remove(usuarioEncontrado)
        print("Usuario borrado")
    else:
        print(usuarioEncontrado)
    return agenda

# Mostrando la agenda completa


def mostrarAgenda():
    if len(agenda) != 0:  # Verificamos si la agenda no está vacía
        print("Listado de usuarios")
        # Mostramos la agenda
        for usuario in agenda:
            print(usuario)
    else:
        print("Agenda sin usuarios")

# Main


while True:
    print("\n------ EJERCICIO ------\n")
    print("- Bienvenido a la agenda\n ¿Qué deseas hacer con tus contactos?")
    print("1. Buscar\n2. Agregar\n3. Actualizar\n4. Eliminar\n5. Mostrar\nSalir. Cierra el programa")
    opcion = input("$ ")
    if opcion.lower() == "salir":
        break
    opcion = int(opcion)
    if opcion == 1:
        nombreUsuario = input("Ingresa el usuario a buscar: ")
        print(buscarUsuario(nombreUsuario))
    elif opcion == 2:
        agenda = agregarUsuario()
    elif opcion == 3:
        nombreUsuario = input("Ingresa el usuario a actualizar: ")
        agenda = actualizarUsuario(nombreUsuario)
    elif opcion == 4:
        nombreUsuario = input("Ingresa el usuario a borrar: ")
        agenda = borrarUsuario(nombreUsuario)
    elif opcion == 5:
        mostrarAgenda()
    else:
        print("Selecciona una opción válida")

print("Hasta luego")
