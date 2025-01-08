"""
 * EJERCICIO:
 * Implementa los mecanismos de introducción y recuperación de elementos propios de las
 * pilas (stacks - LIFO) y las colas (queue - FIFO) utilizando una estructura de array
 * o lista (dependiendo de las posibilidades de tu lenguaje).
 *
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

# Stack - LIFO

stack = []

# Add item
stack.append(1)
stack.append(2)
stack.append(3)
stack.append(4)
print(stack)  # [1, 2, 3, 4]

# Remove item
removed_item = stack[-1]
del stack[-1]
print(stack)  # [1, 2, 3]
print(removed_item)  # 4

print(stack.pop())  # 3
print(stack)  # [1, 2]


# Queue - FIFO

queue = []

# Add item
queue.append(1)
queue.append(2)
queue.append(3)
queue.append(4)

# Remove item
removed_item = queue[0]
del queue[0]
print(queue)  # [2, 3, 4]
print(removed_item)  # 1

print(queue.pop(0))  # 2
print(queue)  # [3, 4]

removed_item = queue[0]
queue = queue[1:]
print(queue)  # [4]
print(removed_item)  # 3


"""
 * DIFICULTAD EXTRA (opcional):
 * - Utilizando la implementación de pila y cadenas de texto, simula el mecanismo adelante/atrás
 *   de un navegador web. Crea un programa en el que puedas navegar a una página o indicarle
 *   que te quieres desplazar adelante o atrás, mostrando en cada caso el nombre de la web.
 *   Las palabras "adelante", "atrás" desencadenan esta acción, el resto se interpreta como
 *   el nombre de una nueva web.
"""


history = []
pointer = -1


def web_navigation():
    def show_menu():
        print("\nType one of the following:")
        print(" - The web page you want to visit")
        print(" - Back (to go to the previous page)")
        print(" - Next (to go to the next page)")
        print(" - Exit")

    show_menu()

    global pointer

    action: str = input("Where do you want to go?\n> ")

    if action and action.strip().lower() == "exit":
        return

    elif action and action.strip().lower() == "next":
        if pointer != len(history) - 1:
            pointer += 1
        print("\nYou are in:", history[pointer])

    elif action and action.strip().lower() == "back":
        pointer -= 1
        if pointer < 0:
            pointer = -1
            print("\nYou are in home page")
        else:
            print("\nYou are in:", history[pointer])

    elif action:
        history.append(action)
        pointer = len(history) - 1
        print("\nYou are in:", history[pointer])

    web_navigation()


web_navigation()


"""
 * DIFICULTAD EXTRA (opcional):
 * - Utilizando la implementación de cola y cadenas de texto, simula el mecanismo de una
 *   impresora compartida que recibe documentos y los imprime cuando así se le indica.
 *   La palabra "imprimir" imprime un elemento de la cola, el resto de palabras se
 *   interpretan como nombres de documentos.
"""


printer_queue = []


def printer():
    def show_menu():
        print("\nPrinter options:")
        print(" - Type a document name to add it to the queue")
        print(" - Type 'print' to print the first item")
        print(" - Exit")

    def show_queue():
        print("\nPrinter Queue:")

        if len(printer_queue) > 0:
            for doc in printer_queue:
                print(f" - {doc}")
        else:
            print("The Queue is empty.")

    show_menu()

    action: str = input("What do you want to do?\n> ")

    if action and action.strip().lower() == "exit":
        return

    elif action and action.strip().lower() == "print":
        if len(printer_queue) > 0:
            printing_doc = printer_queue.pop(0)
            print("Printing:", printing_doc)
        else:
            print("There are no documents to print.")

    elif action:
        printer_queue.append(action)

    show_queue()
    printer()


printer()
