'''
EJERCICIO:
Implementa los mecanismos de introducción y recuperación de elementos propios de las
pilas (stacks - LIFO) y las colas (queue - FIFO) utilizando una estructura de array
o lista (dependiendo de las posibilidades de tu lenguaje).

DIFICULTAD EXTRA (opcional):

Utilizando la implementación de pila y cadenas de texto, simula el mecanismo adelante/atrás
de un navegador web. Crea un programa en el que puedas navegar a una página o indicarle que te quieres desplazar adelante o atrás, mostrando en cada caso el nombre de la web.
Las palabras "adelante", "atrás" desencadenan esta acción, el resto se interpreta como el nombre de una nueva web.
Utilizando la implementación de cola y cadenas de texto, simula el mecanismo de una impresora compartida que recibe documentos y los imprime cuando así se le indica.
La palabra "imprimir" imprime un elemento de la cola, el resto de palabras se interpretan como nombres de documentos.
'''

def lifo():
    lista = []
    action = ""
    while action != "S":
        action = input("Introduce la acción que quieres realizar (I: para insertar, E: para extraer, S: para salir) ")
        action = action.upper()
        if action == "I":
            nuevo = input("Introduce el parametro que quieres insertar ")
            lista.append(nuevo)
        elif action == "E":
            print(lista[-1])
            lista.pop()
        else:
            print("no se ha introducido una letra valida")
    print(f'lista final: {lista}')

lifo()

def fifo():
    lista = []
    action = ""
    while action != "S":
        action = input("Introduce la acción que quieres realizar (I: para insertar, E: para extraer, S: para salir )")
        action = action.upper()
        if action == "I":
            nuevo = input("Introduce el parametro que quieres insertar ")
            lista.append(nuevo)
        elif action == "E":
            print(lista[0])
            lista.pop(0)
        else:
            print("no se ha introducido una letra valida")
    print(f'lista final: {lista}')

fifo()