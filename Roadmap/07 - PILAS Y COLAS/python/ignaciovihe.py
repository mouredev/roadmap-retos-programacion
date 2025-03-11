"""
 * Implementa los mecanismos de introducción y recuperación de elementos propios de las
 * pilas (stacks - LIFO) y las colas (queue - FIFO) utilizando una estructura de array
 * o lista (dependiendo de las posibilidades de tu lenguaje).
"""

# Pila/Stack (LIFO)

stack = []

def push_stack(element):
    stack.append(element)

def pull_stack():
    return stack.pop()

print(stack)
push_stack(1)
print(stack)
push_stack(2)
print(stack)
print(f" Elemento sacado: {pull_stack()}")
print(stack)
push_stack(3)
print(stack)
push_stack(4)
print(stack)
print(f" Elemento sacado: {pull_stack()}")
print(stack)


# Cola/Queue (FIFO)

queue = []

def push_queue(element):
    queue.append(element)

def pull_queue():
    return queue.pop(0)


print("----------------------------")
print(queue)
push_queue(1)
print(queue)
push_queue(2)
print(queue)
print(f" Elemento sacado: {pull_queue()}")
print(queue)
push_queue(3)
print(queue)
push_queue(4)
print(queue)
print(f" Elemento sacado: {pull_queue()}")
print(queue)


"""
 * DIFICULTAD EXTRA (opcional):
 * - Utilizando la implementación de pila y cadenas de texto, simula el mecanismo adelante/atrás
 *   de un navegador web. Crea un programa en el que puedas navegar a una página o indicarle
 *   que te quieres desplazar adelante o atrás, mostrando en cada caso el nombre de la web.
 *   Las palabras "adelante", "atrás" desencadenan esta acción, el resto se interpreta como
 *   el nombre de una nueva web.
 * - Utilizando la implementación de cola y cadenas de texto, simula el mecanismo de una
 *   impresora compartida que recibe documentos y los imprime cuando así se le indica.
 *   La palabra "imprimir" imprime un elemento de la cola, el resto de palabras se
 *   interpretan como nombres de documentos.
"""

def web_browser():

    browse_history = []
    salir = False
    index = -1

    while not salir:
        action = input("Introduce una web o una accion (adelante/atras/salir): ")
        
        if action == "salir":
            salir = True

        elif action == "adelante":
            if (index + 1) >= len(browse_history):
                print("No hay mas paginas hacia adelante")
                print(browse_history)
            else:
                index += 1
                print(f"https:\\www.{browse_history[index]}")
                print(browse_history)

        elif action == "atras":
            if (index - 1) < 0:
                print("No hay mas paginas hacia atras")
                print(browse_history)
            else:
                index -= 1
                print(f"https:\\www.{browse_history[index]}")
                print(browse_history)

        else:
            del browse_history[index + 1 : len(browse_history)]
            browse_history.append(action)
            index += 1
            print(f"https:\\www.{action}")
            print(browse_history)

web_browser()
