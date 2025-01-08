'''EJERCICIO:
Implementa los mecanismos de introducción y recuperación de elementos propios de las
pilas (stacks - LIFO) y las colas (queue - FIFO) utilizando una estructura de array
o lista (dependiendo de las posibilidades de tu lenguaje).

DIFICULTAD EXTRA (opcional):
- Utilizando la implementación de pila y cadenas de texto, simula el mecanismo adelante/atrás
  de un navegador web. Crea un programa en el que puedas navegar a una página o indicarle
  que te quieres desplazar adelante o atrás, mostrando en cada caso el nombre de la web.
  Las palabras "adelante", "atrás" desencadenan esta acción, el resto se interpreta como
  el nombre de una nueva web.
- Utilizando la implementación de cola y cadenas de texto, simula el mecanismo de una
  impresora compartida que recibe documentos y los imprime cuando así se le indica.
  La palabra "imprimir" imprime un elemento de la cola, el resto de palabras se
  interpretan como nombres de documentos.'''

# Implementación de pilas y colas en Python
# Pilas/stack: LIFO (Last In, First Out)
pila = []
# push: añadir un elemento a la pila
pila.append(1)
pila.append(2)
pila.append(3)
pila.append(4)
pila.append(5)
print(pila)
# pop: eliminar un elemento de la pila
pila.pop() 
print(pila)
print(pila.pop()) # este método devuelve el elemento eliminado
print(pila)
print(pila.pop())
print(pila)

# Colas/queue: FIFO (First In, First Out)
cola = []
# enqueue: añadir un elemento a la cola
cola.append(1)
cola.append(2)
cola.append(3)
cola.append(4)
cola.append(5)
print(cola)
# dequeue: eliminar un elemento de la cola
cola.pop(0) # pop(0) elimina el primer elemento de la lista
print(cola)
print(cola.pop(0)) # este método devuelve el elemento eliminado
print(cola)

# EXTRA 
'''- Utilizando la implementación de pila y cadenas de texto, simula el mecanismo adelante/atrás
  de un navegador web. Crea un programa en el que puedas navegar a una página o indicarle
  que te quieres desplazar adelante o atrás, mostrando en cada caso el nombre de la web.
  Las palabras "adelante", "atrás" desencadenan esta acción, el resto se interpreta como
  el nombre de una nueva web.
- Utilizando la implementación de cola y cadenas de texto, simula el mecanismo de una
  impresora compartida que recibe documentos y los imprime cuando así se le indica.
  La palabra "imprimir" imprime un elemento de la cola, el resto de palabras se
  interpretan como nombres de documentos.'''

# Navegador web
def web_browser():
    stack = []

    while True:

        action = input(
            "Añade una url o interactúa con palabras adelante/atrás/salir: "
        )

        if action == "salir":
            print("Saliendo del navegador web.")
            break
        elif action == "adelante":
            pass
        elif action == "atrás" or action == "atras":
            if len(stack) > 0:
                stack.pop()
        else:
            stack.append(action)

        if len(stack) > 0:
            print(f"Has navegado a la web: {stack[len(stack) - 1]}.")
        else:
            print("Estás en la página de inicio.")

#web_browser()

# Impresora compartida
def printer():
    queue = []
    while True:
        action = input("Ingrese el nombre de un documento o 'imprimir'/'salir': ")
        if action == "salir":
            print("Saliendo de la impresora...")
            break
        elif action == "imprimir":
            if len(queue) > 0:
                print(f"Imprimiendo documento: {queue[0]}.")
                queue.pop(0)
            else:
                print("No hay documentos en la cola.")
        else:
            queue.append(action)
        print(f"Documentos en cola: {queue}")

printer()