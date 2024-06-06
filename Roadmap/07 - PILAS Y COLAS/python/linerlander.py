"""
Ejercicio
"""

# Pilas/Stack (LIFO)

stack = []

# push
stack.append(1) 
stack.append(2) 
stack.append(3) 
print(stack)

# pop
stack_item = stack[len(stack) - 1]
del stack[len(stack) - 1]
print(stack_item)

print(stack.pop())

print(stack)

# Cola/Queue(FIFO)

# encolar
queue = []
queue.append(1)
queue.append(2)
queue.append(3)
print(queue)

# colar
queue_item = queue[0]
del queue[0]
print(queue_item)

print(queue.pop(0))

print(queue)

"""
Extra
"""

def web_navegation():
    stack = []

    while True:
        action = input("Añade una urla o interactúa con palabras adelante/atrás/salir: ")

        if action == "salir":
            print('Saliendo del navegador web.')
            break
        elif action == "adelante":
            pass
        elif action == "atrás":
            if len(stack) > 0:
                stack.pop()
        else:
            stack.append(action)
        if len(stack) > 0:
            print(f"Has navegado ala web {stack[len(stack) -1]}.")
        else:
            print('Estás en la página de inicio.')
#web_navegation()
            
def share_printed():
    queue = []

    while True:
        action = input("Añade una documento o seleciona imprimir/salir: ")

        if action == "salir":
            break
        elif action == "imprimir":
            if len(queue) > 0:
                print(f"Imprimiendo: {queue.pop(0)}")
            else:
                print('La cola de la impresión esta vacía')
                break
        else:
            queue.append(action)

        print(f'cola de impresión {queue}')

#share_printed()
