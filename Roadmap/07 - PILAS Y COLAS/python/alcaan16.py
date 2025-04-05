"""
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
 */"""

# Pila/Stack (LIFO)

stack = [] #creamos

# push
stack.append(1)
stack.append(2)
stack.append(3)
print(stack) #imprime la lista 

# pop
stack_item = stack[len(stack) - 1] #ultimo elemento de la lista (3)
del stack[len(stack) - 1] #eliminamos la ultima posicion de la lista (3)
print(stack_item) #ultimo elemento lista (3)

print(stack.pop()) #elimina el ultimo elemento (2)

print(stack) #ahora solo queda un elemento (1)

# Cola/Queue (FIFO)

queue = [] #creamos la lista

# enqueue
queue.append(1) 
queue.append(2)
queue.append(3)

print(queue) #imprime la lista

# dequeue
queue_item = queue[0] #primer elemento de la lista (1)
del queue[0] #elimina el primer elemento (1)
print(queue_item) #primer elemento de la lista 

print(queue.pop(0)) #imprime y elimina el ultimo elemento 

print(queue) #imprime el elemeto que queda

# EJERCICIO

def navegador():
    historial = []
    flag = 0

    def mostrar(flag:int):
        if len(historial) > 1:
            print(historial[flag])
        else:
            print("no hay elemento a mostrar")

    while True:
        action = []
        action = input("introduce una accion:  ")
        if action == "adelante":
            action = 0
            flag = -1
            mostrar (flag)
            
        if action == "atras":
            action = 0
            flag = -2
            mostrar (flag)
    
        if action == "mostrar":
            action = 0
            if len(historial) != 0:
                print(historial[flag])
            else:
                print("no hay nada que mostrar")
        if action == "salir":
            action = 0
            print (historial)
            break
        elif action !=0 :
            flag = -1
            historial.append(action)
            print(f"la url {action} a sido añadida")
        print (historial)

navegador()

def impresora():
    cola=[]
    while True:
        print(cola)
        option=input("introduce una palabra o escribe imprimir para imprimir la ultima palabra ")
        if option == "salir":
            print("saliendo")
            break
        if option == "imprimir":
            if len(cola) == 0:
                print("no hay nada que imprimir")
            else:
                print(f"la palabra {cola[0]} se a impreso")
                cola.pop(0)
                print(cola)
        else:
            cola.append(option)
            print(cola)
impresora()