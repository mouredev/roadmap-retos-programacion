"""
 * EJERCICIO:
 * Implementa los mecanismos de introducción y recuperación de elementos propios de las
 * pilas (stacks - LIFO) y las colas (queue - FIFO) utilizando una estructura de array
 * o lista (dependiendo de las posibilidades de tu lenguaje).
"""


# Pilas
class Stack:

    def __init__(self, stack: list = []) -> None:
        self.stack = stack

    def __str__(self) -> str:
        return str(self.stack)

    def push(self, value) -> None:
        self.stack.append(value)

    def pop(self) -> None:
        self.stack.pop()


my_stack = Stack([1, 2, 3, 4, 5])
print(my_stack)

# Inserción
my_stack.push(6)
print(my_stack)

# Eliminación
my_stack.pop()
print(my_stack)

print("---------------------------------")


# Colas
class Queue:
    def __init__(self, queue: list = []) -> None:
        self._queue = queue

    def __str__(self) -> str:
        return str(self._queue)

    def queue(self, value) -> None:
        self._queue.append(value)

    def dequeue(self) -> None:
        self._queue.pop(0)


my_queue = Queue([1, 2, 3, 4, 5])
print(my_queue)

# Inserción
my_queue.queue(6)
print(my_queue)

# Eliminación
my_queue.dequeue()
print(my_queue)

# Ambas
my_queue.queue(7)
my_queue.dequeue()
my_queue.dequeue()
my_queue.dequeue()
my_queue.queue(8)
my_queue.dequeue()
my_queue.queue(9)
print(my_queue)


"""
 * DIFICULTAD EXTRA (opcional):
 * - Utilizando la implementación de pila y cadenas de texto, simula el mecanismo adelante/atrás
 *   de un navegador web. Crea un programa en el que puedas navegar a una página o indicarle
 *   que te quieres desplazar adelante o atrás, mostrando en cada caso el nombre de la web.
 *   Las palabras "adelante", "atras" desencadenan esta acción, el resto se interpreta como
 *   el nombre de una nueva web.
 * - Utilizando la implementación de cola y cadenas de texto, simula el mecanismo de una
 *   impresora compartida que recibe documentos y los imprime cuando así se le indica.
 *   La palabra "imprimir" imprime un elemento de la cola, el resto de palabras se
 *   interpretan como nombres de documentos.
"""

print("---------------------------------")


class Web(Stack):

    def __init__(self, stack: list[str] = []) -> None:
        super().__init__(stack)
        self.last_index_selection = 0

    def foward(self) -> str:
        if self.last_index_selection + 1 > len(self.stack) - 1:
            self.last_index_selection = 0
            return self.stack[self.last_index_selection]
        self.last_index_selection += 1
        return self.stack[self.last_index_selection]

    def back(self) -> str:
        if self.last_index_selection - 1 < 0:
            self.last_index_selection = len(self.stack) - 1
            return self.stack[self.last_index_selection]
        self.last_index_selection -= 1
        return self.stack[self.last_index_selection]


print("Web: 1", "Impresora: 2", sep="\n")
program = input("Qué programa quieres probar? ")
my_web = Web(['Index', 'About me', 'Education', 'Courses'])
print(my_web)

if program == "1":
    print(
        "------------ Web -------------",
        "Opciones:",
        "adelante -> siguiente página",
        "atras -> página anterior",
        "web -> todas las páginas",
        "exit -> salir",
        "cualquier string -> nueva página",
        sep="\n",
    )

while program == "1":
    option = input("Opción: ").lower()
    match option:
        case "adelante":
            print("Página actual: ", my_web.foward())
        case "atras":
            print("Página actual: ", my_web.back())
        case "web":
            print(my_web)
        case "exit":
            break
        case _:
            my_web.push(option)


print("---------------------------------")

if program == "2":
    print(
        "------------ Impresora -------------",
        "Opciones:",
        "imprimir -> imprime el siguiente documento",
        "all -> todas las impresiones pendientes",
        "exit -> salir",
        "cualquier string -> nuevo documento",
        sep="\n",
    )

documents = Queue(["Hoja de vida", "Trabajo literatura", "Carta presentación"])

while program == "2":
    option = input("Opción: ").lower()
    match option:
        case "imprimir":
            print("Imprimiendo: ", documents._queue[0])
            documents.dequeue()
        case "all":
            print(documents)
        case "exit":
            break
        case _:
            documents.queue(option)
