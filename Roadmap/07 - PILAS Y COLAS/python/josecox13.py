''' 
Ejercicio 7
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
# Pila / Stack (LIFO)
stack = [0,1,2,3]
stack.append(4) # push
stack_item = stack[-1] # pop
del stack[-1]

print(stack_item)
print(stack)

# También se puede hacer con el método pop de las listas
print(stack.pop())
print(stack)

# Cola / Queue (FIFO)

queue = [0,1,2,3]
queue.append(4) # enqueue
queue.append(5) # enqueue

print(queue.pop(0)) # dequeue
print(queue)

#De forma manual
queue_item = queue[0]
del queue[0]
print(queue_item)
print(queue)

#Extra navegador web
def navegador_web():
    stack = []
    paginas_atras = []
    while True:
        action = input('Introduce una URL o interactúa con las palabras adelante/atrás/salir: ')
        if action == "salir":
            break
        elif action == "adelante":
            if len(paginas_atras) > 0:
                stack.append(paginas_atras[-1])
                paginas_atras.pop()
            else:
                print('No hay páginas para mostrar')
        elif action == "atrás":
            if len(stack) > 0:
                paginas_atras.append(stack[-1])
                stack.pop()
        else:
            stack.append(action)
            paginas_atras = []
        if len(stack) == 0:
            print('No hay páginas para mostrar')
        else:  
            print(f'Estas en la web {stack[-1]}')
navegador_web()

# Impresora compartida
def impresora_compartida():
    queue = []
    while True:
        action = input('Introduce un documento para imprimir o interactúa con la palabra imprimir/salir: ')
        if action == 'salir':
            break
        elif action == 'imprimir':
            if len(queue) > 0:
                print(f'Imprimiendo {queue[0]}')
                queue.pop(0)
        else:
            queue.append(action)
        print(f'Cola de impresion: {queue}')
