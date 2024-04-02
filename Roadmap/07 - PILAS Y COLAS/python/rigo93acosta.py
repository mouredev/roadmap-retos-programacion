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

### EXTRA
