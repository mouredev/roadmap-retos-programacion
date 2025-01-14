'''
/*
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
 */
'''

### Pila/Stack (LIFO) 
## List in Python is a stack
stack = []
stack.append("1") # push
stack.append("2") # push
stack.append("3") # push
print(stack)
element = stack.pop() # pop
print(element)
print(stack)

### Cola/Queue (FIFO)
queue = []
#enqueue
queue.append("1") 
queue.append("2") 
queue.append("3") 
print(queue)
#dequeue
element = queue.pop(0)
print(element)
print(queue)

## EXTRA
### EXTRA 1

def web_navegation():
    
    stack = []

    while True:

        action = input(
            "Añade una url o interactúa con palabras adelante/atrás/salir: "
            )
        
        if action == 'salir':
            print('Saliendo del navegador web.')
            break 
        elif action == 'adelante': # El stack no podemos hacer
            pass
        elif action == "atrás":
            if len(stack) > 0:
                stack.pop()
        else:
            stack.append(action)
        
        if len(stack) > 0:
            print(f"Has navegado a la web: {stack[len(stack) - 1]}")
        else:
            print("Estás en la página de inicio.")

#web_navegation()

### EXTRA 2
def online_printer():
    queue = []

    while True:
        action = input("Añade documento o selecciona imprimir/salir: ")

        if action == "imprimir":
            if len(queue) > 0:
                print(f"Imprimiendo documento '{queue.pop(0)}'")
            else:
                print("No hay documento en cola.")
        elif action == "salir":
            print("Apagando la impresora LOL!!!")
            break
        else:
            queue.append(action)

        print(f"Cola de Impresora {queue}")

online_printer()