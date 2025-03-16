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

### Pilas 

stack = [] # Se apilan elementos (LIFO: Last In, First Out)

stack.append(1)
stack.append(2)
stack.append(3)
stack.append(4)
print(stack)
stack_item = stack[len(stack) - 1]
del stack[len(stack) - 1]
print(stack_item)
stack.pop(1)
print(stack)

### Colas

queue = [] # Se crean colas de elementos (FIFO: First In, First Out)
queue.append(1)
queue.append(2)
queue.append(3)
queue.append(4)

queue_item = queue[0]
del queue[0]
print(queue)
queue.pop(0)
print(queue)

### Extra

def web_navi():
    
    stack = []

    while True:

        action = input(
            "Inserte una url o continue con adelante/atras/salir: ")
        
        
        if action == "salir":
            break
        elif action == "adelante":
            pass
        elif action == "atrás":
            if len(stack) > 0:
                stack.pop()  
        else:
            stack.append(action) 

        if len(stack) > 0:
            print(f"Has navegado a la web ,{stack[len(stack)-1]}")
        else:
            print("Estas en la pagina de inicio")
            

web_navi()

def online_printed():
    queue = []

    while True:
        
        action = input("Añada un elemeno o seleccione Imprimir/Salir")

        if action == "Salir":
            break
        elif action == "Imprimir":
            if len(queue) > 0:
                print(f"Imprimiendo: {queue.pop(0)}")
        else:
            queue.append(action)

        print(f"Cola de impresion: {queue}")
    
online_printed()

