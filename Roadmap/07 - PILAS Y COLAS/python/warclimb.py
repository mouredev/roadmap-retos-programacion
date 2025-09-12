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
 *   Las palabras "adelante", "atras" desencadenan esta acción, el resto se interpreta como
 *   el nombre de una nueva web.
 * - Utilizando la implementación de cola y cadenas de texto, simula el mecanismo de una
 *   impresora compartida que recibe documentos y los imprime cuando así se le indica.
 *   La palabra "imprimir" imprime un elemento de la cola, el resto de palabras se
 *   interpretan como nombres de documentos.
 """
 from collections import deque

# Implementamos las pilas y colas
# impelemntacion como pila
pila = []
pila.append("fuego") # añadimos fuego a la pila
pila.pop("fuego") # sacamos fuego de la pila

# implementacion como cola
cola = []

def enqueue(element):
    cola.append(element)

def dequeue():
    if len(cola) > 0:
        return cola.pop(0)
    else:
        return None

# añadimos a la cola:
enqueue("fuego")  # añadimos fuego a la cola
dequeue()  # sacamos fuego de la cola

# Extra: Simulamos el mecanismo adelante/atrás de un navegador web
