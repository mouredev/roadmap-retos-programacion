"""
Ejercicio
"""

# Pila/Stack (LIFO)

stack = []

# push 
stack.append(1) # push
stack.append(2) # push
stack.append(3) # push
print(stack) 

# pop
stack_item = stack[len(stack) - 1]
del stack[len(stack) - 1]
print(stack_item)

print(stack.pop()) 

print(stack)

# Cola/Queue (FIFO)

queue = []

# enqueue
queue.append(1)
queue.append(2)
queue.append(3)

print(queue)

#dequeue
queue_item = queue[0]
del queue[0]
print(queue_item)

print(queue.pop(0))

print(queue)
"""
Extra
"""

# Web

def web_navegation():
    
    stack = []

    while True:

        action = input(
            "Añade una URL o iteractua con las palabras adelante/atras/salir:"
        )

        if action == "salir":
            print("Saliendo del navegador")
            break
        elif action == "adelante":
            pass
        elif action == "atras":
            if len(stack) > 0:
                stack.pop()
        else:
            stack.append(action)

        
        if len(stack) > 0:
            print("has navegado a la web: {stack[len(stack) - 1]}")
        else:
            print("Estas en la pagina de inicio.")

web_navegation()

def shared_printed():

    queue = []

    while True:
        action = input("Añade un documentos o selecciona imprimir/salir: ")

        if action == "salir":
            break
        elif action == "imprimir":
            if len(queue) > 0:
                print(f"Imprimiendo: {queue.pop(0)}")
        else:
            queue.append(action)

        print(f"Cola de impresión: {queue}")
    
shared_printed()