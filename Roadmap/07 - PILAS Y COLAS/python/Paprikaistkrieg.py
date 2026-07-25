#pilas y colas



#Pilas (stack LIFO - Last In, First Out)

"""
las pilas y colas son estructuras de datos fundamentales en la programación
que permiten almacenar y gestionar colecciones de elementos de manera eficiente.
Una pila (stack) es una estructura de datos que sigue el principio LIFO (Last In, First Out),
 lo que significa que el último elemento en ser añadido a la pila es el primero en ser removido. 
 Las operaciones principales en una pila son:

 "push" (añadir un elemento a la cima de la pila) y

"pop" (remover el elemento de la cima de la pila). 

Las pilas son útiles para tareas como la gestión de llamadas a funciones,
la evaluación de expresiones y la navegación por el historial.

Las pilas se pueden implementar utilizando listas, ya que a nivel conceptual,
una lista permite añadir y eliminar elementos de un extremo de manera eficiente.
Sin embargo, para aplicaciones que requieren un rendimiento óptimo,
es recomendable utilizar la biblioteca collections, 
que proporciona una estructura de datos especializada llamada deque (double-ended queue).
Deque permite añadir y eliminar elementos de ambos extremos de manera eficiente,
lo que la hace ideal para implementar pilas y colas.
Aquí tienes un ejemplo básico de cómo implementar una pila utilizando una lista en Python:
"""

from inspect import stack

from operator import truediv

from argparse import Action


stack = []  # Creamos una pila vacía
#para añadir elementos a la pila, utilizamos el método append() 

#PUSH

stack.append(1)  # Añadimos el elemento 1 a la pila
stack.append(2)  # Añadimos el elemento 2 a la pila
stack.append(3)  # Añadimos el elemento 3 a la pila

print(stack)  # Imprimimos la pila actual

#POP

# Para eliminar elementos de la pila, utilizamos el método pop(remover el elemento de la cima de la pila)
stack_item = stack[len(stack)-1]  # Obtenemos el elemento de la cima de la pila 
del stack[len(stack)-1] # Removemos el elemento de la cima de la pila que en esencia es lo que hace pop
elemento = stack.pop()  # Removemos el elemento de la cima de la pila
print(elemento)  # Imprimimos el elemento removido
print(stack)  # Imprimimos la pila actual después de la operación pop

#lo que se entiende por lista es internamente una pila, ya que el último elemento añadido es el primero en ser removido.



#Cola / queue ( FIFO - First In, First Out)

"""
Una cola (queue), por otro lado, sigue el principio FIFO (First In, First Out), 
lo que significa que el primer elemento en ser añadido a la cola es el primero en ser removido. 
Las operaciones principales en una cola son:

"enqueue" (añadir un elemento al final de la cola) y 

"dequeue" (remover el elemento del frente de la cola). 

Las colas son útiles para tareas como la gestión de tareas en sistemas operativos,
la impresión de trabajos y la simulación de procesos.
Las pilas y colas se pueden implementar utilizando listas o la biblioteca collections,
que proporciona estructuras de datos especializadas como deque (double-ended queue) para colas.
"""

queue = []  # Creamos una cola vacía
#para añadir elementos a la cola, utilizamos el método append()

#ENQUEUE (encolar) 
queue.append(1)  # Añadimos el elemento 1 a la cola
queue.append(2)  # Añadimos el elemento 2 a la cola
queue.append(3)  # Añadimos el elemento 3 a la cola

print(queue)  # Imprimimos la cola actual

#DEQUEUE (desencolar)

# Para eliminar elementos de la cola, utilizamos el método pop(0) (remover el elemento del frente de la cola)

queue_item = queue[0]  # Obtenemos el elemento del frente de la cola
del queue[0]  # Removemos el elemento del frente de la cola

#tambien 
queue_item = queue.pop(0)  # Removemos el elemento del frente de la cola

print(queue_item)  # Imprimimos el elemento removido
print(queue)  # Imprimimos la cola actual después de la operación dequeue

#lo que se entiende por lista es internamente una cola, ya que el primer elemento añadido es el primero en ser removido.
#Sin embargo, para aplicaciones que requieren un rendimiento óptimo, es recomendable utilizar la biblioteca collections,
#que proporciona una estructura de datos especializada llamada deque (double-ended queue).


#XTRAJ

def web_navigation():
    stack = []

    while True:
        action = input("añade una url o interactua con palabras como adelante, atras o salir: ")
       
        if action == "salir":
            print("saliendo del navegador Web.")
            break
        elif action == "adelante":
            pass
        elif action == "atras":
            if len(stack) > 0:
                stack.pop()
                if stack:
                    print(f"Navegando hacia atrás: {stack[-1]}")
                else:
                    print("Estas en la pagina de inicio.")
            else:
                print("Estas en la pagina de inicio.")
        else:
            stack.append(action)
        if len(stack) > 0:
            print(f"Has navegado a la Web: {stack[-1]}")
        
 
web_navigation()

def impresora():
    queue = []

    while True:
        action = input("Añade un documento o selecciona imprimir/salir:")
        if action == "salir":
            print("Saliendo de la impresora.")
            break
        elif action == "imprimir":
            pass
            if len(queue) > 0:
                print(f"Imprimiendo documento: {queue.pop(0)}")
            else:
                print("No hay documentos en la cola para imprimir.")
        else:
            queue.append(action)
            print(f"Documento añadido a la cola: {queue}")

impresora()
