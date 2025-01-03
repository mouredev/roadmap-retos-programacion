###################################
# Dev: rianojnicolas              #
###################################

from collections import deque

# EJERCICIO:

## Listas como Pilas - LIFO (last in first out)
def stackMethod(stack, action, element=None):
    """
    Inputs:
        stack: lista de elementos
        action: accion a realizar "push"/"pop"/"peek"
        element: elemento a insertar/eliminar/devolver ultimo elemento
    Outputs:    
        stack: lista de elementos
    """
    if action == "push":
        stack.append(element)
        return stack
    elif action == "pop":
        stack.pop()
        return stack
    elif action == "peek":
        return stack[len(stack)-1]

print("Prueba del metodo stack-LIFO")
myStack = [1,2,3,4,5]
print(stackMethod(myStack, "push", 6))
print(stackMethod(myStack, "pop"))
print(stackMethod(myStack, "peek"))

## Listas como Colas - FIFO (first in first out)

def queueMethod(queue, action, element=None):
    """
    Inputs:
        queue: lista de elementos
        action: accion a realizar "enqueue"/"dequeue"/"queue"
        element: elemento a insertar/eliminar/devolver primer elemento
    Outputs:    
        queue: lista de elementos
    """
    if action == "enqueue":
        queue.append(element)
        return queue
    elif action == "dequeue":
        queue.popleft()
        return queue
    elif action == "peek":
        return queue[0]

print("Prueba del metodo queue-FIFO")
myQueue = deque([1,2,3,4,5])
print(queueMethod(myQueue, "enqueue", 6))
print(queueMethod(myQueue, "dequeue"))
print(queueMethod(myQueue, "peek"))


# DIFICULTAD EXTRA

# Web - LIFO
def webNavigation():
    """
    Funcion que simula el navegador web 
    y realiza las acciones de ingreso de url, 
    adelante, atras y salida
    
    inputs: -
    outputs:
        print(url)
    """

    print("""

            Hola, soy el navegador web y
            Estas en la pagina principal
            
        """)
    stack = []

    while True:
        
        accion = input("Ingresa una accion (adelante/atras/salir): ")

        if accion == "adelante":
            url = input("Ingresa una url: ")
            stack = stackMethod(stack, "push", url)
        elif accion == "atras":
            if len(stack) > 0:
                stack = stackMethod(stack, "pop")
            else:
                pass
        elif accion == "salir":
            print("Saliendo del navegador")
            break
        else:
            print("Accion incorrecta")
            print("Opciones: adelante/atras/salir")
            pass
        
        if len(stack) == 0:
            print("Estas en la pagina principal")
            pass
        elif len(stack) > 0:
            print(stackMethod(stack, "peek"))


webNavigation()


# Impresora Compartida - FIFO
def printerShared():
    """
    Funcion que simula la impresora compartida
    y realiza las acciones de ingreso de documento, 
    impresion y salida
    
    inputs: -
    outputs:
        print(document)
    """

    print("""

            Hola, soy la impresora compartida
            
        """)

    queue = deque()

    while True:

        accion = input("Ingresa una accion (agregar/imprimir/salir): ")

        if accion == "agregar":
            document = input("Ingresa un documento: ")
            queue = queueMethod(queue, "enqueue", document)
        elif accion == "imprimir":
            if len(queue) > 0:
                print("Imprimiendo documento - " + queueMethod(queue, "peek"))
                document = queueMethod(queue, "dequeue")
            else:
                print("No hay documentos en la impresora")
                pass
        elif accion == "salir":
            print("Saliendo de la impresora")
            break
        else:
            print("Accion incorrecta")
            print("Opciones: imprimir/salir")
            pass


printerShared()