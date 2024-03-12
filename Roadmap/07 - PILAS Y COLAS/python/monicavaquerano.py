# 07 PILAS Y COLAS
# Monica Vaquerano
# https://monicavaquerano.dev

"""
EJERCICIO:
Implementa los mecanismos de introducción y recuperación de elementos propios de las
pilas (stacks - LIFO) y las colas (queue - FIFO) utilizando una estructura de array
o lista (dependiendo de las posibilidades de tu lenguaje).
"""
import os, time


print("07 PILAS Y COLAS\n")

# Pilas (Stacks):
# Una pila es una estructura de datos en la que el último elemento añadido es el primero en ser eliminado (LIFO - Last In, First Out).
# Puedes implementar una pila fácilmente en Python utilizando una lista.
print("* Pilas (Stacks)")
print("- LIFO - Last In, First Out")
stack = []
print("Pila (stack) inicial =>", stack)
stack.append(1)
stack.append(2)
stack.append(3)
print(f"Pila (stack) después de varios appends: stack.append(x) => {stack}")
popped = stack.pop()
print(f"Último elemento de la pila (stack) eliminado: stack.pop() => {popped}")
print(f"Pila (stack) después de eliminar el último elemento => {stack}\n")

# Colas (Queues):
# Una cola es una estructura de datos en la que el primer elemento añadido es el primero en ser eliminado (FIFO - First In, First Out).
# Para implementar una cola en Python, puedes utilizar la biblioteca collections que proporciona la clase deque.
print("* Colas (Queues)")
print("- FIFO - First In, First Out")
queue = []
print("Cola (queue) inicial =>", queue)
queue.append("a")
queue.append("b")
queue.append("c")
print(f"Cola (queue) después de varios appends: queue.append(x) => {queue}")
popFirst = queue.pop(0)
print(f"Último elemento de la cola (queue) eliminado: queue.pop(0) => {popFirst}")
print(f"Cola (queue) después de eliminar el primer elemento => {queue}\n")

"""
DIFICULTAD EXTRA (opcional):
- Utilizando la implementación de pila y cadenas de texto, simula el mecanismo adelante/atrás
de un navegador web. Crea un programa en el que puedas navegar a una página o indicarle
que te quieres desplazar adelante o atrás, mostrando en cada caso el nombre de la web.
Las palabras "adelante", "atrás" desencadenan esta acción, el resto se interpreta como
el nombre de una nueva web.
"""

history = ["test1.com", "test2.com", "test3.com", "test4.com"]
lasts = []


def web_navigation():
    while True:
        os.system("clear")
        print("--- Web navigation ---")

        numb = len(history) - 1

        if numb < 0:
            print("\nHome Page\n")
        else:
            print("\n", "https://", history[numb], "\n")

        choice = input("1. Ir a...\n2. Atrás\n3. Avanzar\n4. Salir\n> ").strip()

        if choice == "1":
            web = input("Enter web page: > ").strip().lower()
            history.append(web)
        elif choice == "2":
            if numb >= 0:
                last = history.pop()
                lasts.append(last)
        elif choice == "3":
            if lasts:
                history.append(lasts.pop())
            else:
                print("\nYou reached the last page\n")
                time.sleep(1)
        elif choice == "4":
            break


"""
- Utilizando la implementación de cola y cadenas de texto, simula el mecanismo de una
impresora compartida que recibe documentos y los imprime cuando así se le indica.
La palabra "imprimir" imprime un elemento de la cola, el resto de palabras se
interpretan como nombres de documentos.
"""
cola = ["doc1", "doc2", "doc3", "doc4"]


def shared_printer():
    while True:
        os.system("clear")
        print("--- Impresora Compartida ---")
        choice = (
            input("\n1. Imprimir\n2. Añadir\n3. Ver Cola\n4. Salir\n> ").strip().lower()
        )
        if choice == "1" or choice == "imprimir":
            os.system("clear")
            print("--- Documento Impreso ---\n")
            if cola:
                firstDoc = cola.pop(0)

                print(f"\t{firstDoc}")
            else:
                print("No hay documentos en la cola")
            time.sleep(2)
        elif choice == "2" or choice == "añadir":
            os.system("clear")
            print("--- Añadir Documento ---\n")
            document = input("Añadir documento: > ").strip().lower()
            cola.append(document)
            print("\nDocumento añadido")
            time.sleep(1)
        elif choice == "3" or choice == "ver":
            os.system("clear")
            print("--- Cola de documentos ---\n")
            if cola:
                print(
                    f"Próximo a imprimir: {cola[0]}\nSiguientes: {', '.join(cola[1:])}\n",
                )
            else:
                print("No hay documentos en la cola")
            time.sleep(4)
        elif choice == "4" or choice == "salir":
            break


while True:
    print("DIFICULTAD EXTRA (opcional)")
    choice = input(
        "Escoge la función:\n1. Web Navigation (pila)\n2. Shared Printer (cola)\n3. Exit\n> "
    )
    if choice == "1":
        web_navigation()
    elif choice == "2":
        shared_printer()
    elif choice == "3":
        break
