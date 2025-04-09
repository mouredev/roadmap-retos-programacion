""" #07 PILAS Y COLAS """

from collections import deque
from queue import Queue


# ------------- PILAS -------------

# Sin collections deque

pila = []
# Con append agregamos un elemento a la lista (PUSH)
pila.append("hola")
# con pop, eliminamos el ultimo elemento y este lo retorna (POP)
pila.pop()
# print(pila)
pila.append("hola")
# print(pila)
pila.append("mundo")
# print(pila)
pila.pop()
# print(pila)

# Con collections deque (recomendado)

pila = deque()
pila.append("Hola")
pila.append("como")
pila.append("estás")
# print(pila)
pila.pop()
# print(pila)

# ------------- COLAS -------------

# con collections deque

cola = deque()
cola.append("hola")
cola.append("mundo")
cola.append("como")
cola.append("estas")
# print(cola)
cola.popleft()
# print(cola)

# con queue Queue

# Agregar a la cola
cola = Queue()
cola.put("hola")
cola.put("como")
cola.put("estas")
# Quitar de la cola
# print(cola.get())


# ------------- EJERCICIO -------------

def acrossTheWeb():
    """ Funcion que muestra la ultima página en la que estamos
     al escribir adelante, quita esa ultima al escribir atras y
      agrega una nueva pagina al escribir cualquier otra cosa

        Ambos casos adelanta o atras, nos imprimie el ultimo
         valor o el que sigue """
    stack = deque(["home"])
    while True:
        command = str(input("Quieres ir adelante o atrás: "))
        if command.lower() == "adelante":
            print(stack[-1])
        elif command.lower() == "atras":
            stack.pop()
            if not stack:
                break
            print(stack[-1])
        else:
            stack.append(command)


acrossTheWeb()


def printingDocuments():
    """ Funcion que imprime un documento al escribir imprimir
     de lo contrario, lo que escribamos lo agrega como un nuevo
      documento a imprimir """
    docList = ["documento"]
    while True:
        # Mostramos el documento a imprimir
        print(f"Documento siguiente: {docList[0]}")
        command = str(input("$ "))
        if command.lower() == "imprimir":
            print(f"Documento impreso: {docList.pop(0)}")
            print(docList)
        else:
            print(f"Documento agregado a la cola: {command}")
            docList.append(command)
            print(docList)
        if not docList:
            break
    print("Sin documentos, adios.")


# printingDocuments()
