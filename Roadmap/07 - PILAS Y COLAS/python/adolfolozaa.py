'''
EJERCICIO:
 * Implementa los mecanismos de introducción y recuperación de elementos propios de las pilas (stacks - LIFO) y las colas (queue - FIFO) utilizando una estructura de array
 o lista (dependiendo de las posibilidades de tu lenguaje).
 *
 * DIFICULTAD EXTRA (opcional):
 * - Utilizando la implementación de pila y cadenas de texto, simula el mecanismo adelante/atrás de un navegador web. Crea un programa en el que puedas navegar a una página o indicarle que te quieres desplazar adelante o atrás, mostrando en cada caso el nombre de la web.
 *   Las palabras "adelante", "atrás" desencadenan esta acción, el resto se interpreta como el nombre de una nueva web.
 * - Utilizando la implementación de cola y cadenas de texto, simula el mecanismo de una impresora compartida que recibe documentos y los imprime cuando así se le indica.
 *   La palabra "imprimir" imprime un elemento de la cola, el resto de palabras se interpretan como nombres de documentos.'''

# Pila(stack) (LIFO).   LA LISTA ES UNA PILA
print('---------------------')
print('Pila(stack) (LIFO)')
stack = []
stack.append('1')  # push
stack.append('2') # push
stack.append('3') # push
print(stack)

#Pop
stack_item = stack[len(stack) - 1] # peek
print(stack_item)
del stack[len(stack) - 1] # pop
print(stack)

# una mejor opcion de desapilar
stack.append('3') # push

print(stack)
print(stack.pop())  # pop hace la funcion de desapilar (peek y pop)
print(stack)


# COLAS (QUEUE) (FIFO)
print('---------------------')
print('COLAS (QUEUE) (FIFO)')
queue = []
queue.append('1') # enqueue
queue.append('2') # enqueue
queue.append('3') # enqueue

print(queue)
print(queue.pop(0)) # dequeue  Se usa pop(0) para desencolar
print(queue)

'''
DIFICULTAD EXTRA (opcional):
 * - Utilizando la implementación de pila y cadenas de texto, simula el mecanismo adelante/atrás
 *   de un navegador web. Crea un programa en el que puedas navegar a una página o indicarle
 *   que te quieres desplazar adelante o atrás, mostrando en cada caso el nombre de la web.
 *   Las palabras "adelante", "atrás" desencadenan esta acción, el resto se interpreta como
 *   el nombre de una nueva web.
 * - Utilizando la implementación de cola y cadenas de texto, simula el mecanismo de una
 *   impresora compartida que recibe documentos y los imprime cuando así se le indica.
 *   La palabra "imprimir" imprime un elemento de la cola, el resto de palabras se
 *   interpretan como nombres de documentos.'''

# DIFICULTAD EXTRA (opcional):

def navegacion():
    stack = []
    while True:


        action = input('Ingrese la accion deseada: ')
        if action == 'salir':
            print(' Usted ha salido del navegador')
            break
        elif action == 'adelante':
            print('pagina bonita')

        elif action == 'atras':
            if len(stack) == 0:
                print('No hay paginas para atras')
            else:
                print(stack.pop())
        else:
            stack.append(action)
            print(stack)

        
'''
print('---------------------')
print('Navegador web')
print('adelante, atrás o nombre de la web')
print('---------------------')
navegacion()'''


def impresora():
    queue = []
    while True:
        action = input('Ingrese la accion deseada (anadir/imprimir/salir): ')
        if action == 'salir':
            print('Usted ha salido de la impresora')
            break
        elif action == 'imprimir':
            if len(queue) == 0:
                print('No hay documentos para imprimir')
            else:
                print(queue.pop(0))
        else:
            queue.append(action)
            print(queue)

impresora()
