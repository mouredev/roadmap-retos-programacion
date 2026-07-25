#  * EJERCICIO:
#  * Implementa los mecanismos de introducción y recuperación de elementos propios de las
#  * pilas (stacks - LIFO) y las colas (queue - FIFO) utilizando una estructura de array
#  * o lista (dependiendo de las posibilidades de tu lenguaje).
#  *
#  * DIFICULTAD EXTRA (opcional):
#  * - Utilizando la implementación de pila y cadenas de texto, simula el mecanismo adelante/atrás
#  *   de un navegador web. Crea un programa en el que puedas navegar a una página o indicarle
#  *   que te quieres desplazar adelante o atrás, mostrando en cada caso el nombre de la web.
#  *   Las palabras "adelante", "atrás" desencadenan esta acción, el resto se interpreta como
#  *   el nombre de una nueva web.
#  * - Utilizando la implementación de cola y cadenas de texto, simula el mecanismo de una
#  *   impresora compartida que recibe documentos y los imprime cuando así se le indica.
#  *   La palabra "imprimir" imprime un elemento de la cola, el resto de palabras se
#  *   interpretan como nombres de documentos.

from collections import deque

# Estructura LIFO

stack = [10,20,30]
stack.append(40)
print(stack)
stack.pop()
print(stack)

# Estructura FIFO

queue = deque([10,20,30])
queue.append(40)
print(queue)
queue.popleft()
print(queue)

# DIFICULTAD EXTRA:

def navegador():
    pila_adelante = ['youtube.com','google.com','twitch.com','amazon.com','x.com']
    pila_atras = []
    pagina_actual = 'Inicio'
    
    print(f'Estas en {pagina_actual}')
    
    while True:
        entrada = input('Ingresa una URL, "atras", "adelante" o "salir": ').strip().lower()
        
        if entrada == 'salir':
            print('Estas saliendo del navegador')
            break
        elif entrada == 'adelante':
            if pila_adelante:
                pila_atras.append(pagina_actual)
                pagina_actual = pila_adelante.pop()
                print(f'Estas en {pagina_actual}')
            else:
                print('No hay mas paginas adelantes.')
        elif entrada == 'atras':
                if pila_atras:
                    pila_adelante.append(pagina_actual)
                    pagina_actual = pila_atras.pop()
                    print(f'Estas en {pagina_actual}')
                else:
                    print('No hay mas paginas atras.')
        else:
            pila_atras.append(pagina_actual)
            pagina_actual = entrada
            pila_adelante.clear()
            print(f'Estas en {pagina_actual}')


def impresora():
    cola = deque([])
    
    while True:
        entrada = input('Indique una accion a seguir:\nEscriba el nombre del documento para añadirlo a la cola.\nEscriba "imprimir" para dar paso al primer documento en la cola.\nEscriba "salir" para salir de la impresora.\n').strip().lower()
        if entrada == 'imprimir':
            if cola:
                print (cola[0])
                cola.popleft()
            else:
                print('No hay nada en cola para imprimir')
        elif entrada == 'salir':
            break         
        elif entrada != 'imprimir':
            print(f'El documento {entrada} ha sido ha añadido a la cola de impresion')
            cola.append(entrada)
