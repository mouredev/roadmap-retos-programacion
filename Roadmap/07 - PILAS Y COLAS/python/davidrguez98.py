""" /*
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
 */ """

#EJERCICIO

#Pila/Stack (LIFO - Last In First Out)

stack = []
stack.append("1") #Push
stack.append("2") #Push
stack.append("3") #Push
print(stack)

""" stack_item = stack[len(stack) -1] #Pop
del stack[len(stack) -1]
print(stack_item) """

print(stack.pop())

print(stack)

#Cola/Queue (FIFO - First In First Out)
""" 
queue = []
queue.append(1) #Enqueue
queue.append(2) #Enqueue
queue.append(3) #Enqueue
print(queue)

queue_item = queue[0] #Dequeue
del queue[0]
print(queue_item)

print(queue.pop(0)) #Dequeue

print(queue) """

#DIFICULTAD EXTRA

# Navegador

nav = []

nav.append("Web 1")
nav.append("Web 1/Web 2")
nav.append("Web 1/Web 2/Web 3")

position = 0 

def forward():
    nav[position]
    

def backward():
    nav[position]


while True:

    print("Actualmente estás en: ", nav[position])
    question = input("¿Qué quieres añadir una web, ir hacia adelante, ir hacia atrás o salir: ")

    if question.lower() == "adelante" or question.lower() == "ir hacia adelante":
        position += 1
        forward()
    elif question.lower() == "atrás" or question.lower() == "atras" or question.lower() == "ir hacia atrás" or question.lower() == "ir hacia atras":
        position -= 1
        backward()
    elif question.lower() == "añadir":
        nav.append(input("Añade la web:" ))
    elif question.lower() == "salir":
        break
    else:
        print("La opción seleccionada es incorrecta, elija adelante o atrás.")

# Impresora

queue_printer = []

def add_paper():
    queue_printer.append(input("Nombre del documento que quiere añadir a la cola para imprimir: "))

def print_paper():
    print("Se está imprimiendo: ", queue_printer.pop(0))

while True:
    quest = input("¿Quieres añadir un documento a la cola de impresión, imprimir o salir?: ")

    if quest.lower() == "añadir" or quest.lower() == "añadir un documento a la cola de impresión":
        add_paper()
        print("La cola de impresión es: ", queue_printer)
    elif quest.lower() == "imprimir":

        print_paper()
        print("La cola de impresión es: ", queue_printer)
    elif quest.lower() == "salir":
        break
    else:
        print("La opción seleccionada es incorrecta, elija añadir, imprimir o salir.")