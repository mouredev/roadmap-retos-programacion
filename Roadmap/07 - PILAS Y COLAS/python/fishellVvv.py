# ejercicio pila/stack (LIFO)
stack = []
# push
stack.append(1)
stack.append(2)
stack.append(3)
print(stack)
# pop
stack.pop()
print(stack)

# ejercicio cola/Queue (FIFO)
queue = []
# enqueue
queue.append(1)
queue.append(2)
queue.append(3)
print(queue)
# dequeue
queue.pop(0)
print(queue)

# EXTRA

# web_pila
def web_navigation():
    stack = []
    stack.append("fishellVvv.com")
    position = 0

    print(f"https://{stack[0]}/", end="")
    while True:
        action = input("\nAñade una url o interactúa con palabras adelante/atrás/salir: ")
        if action == "salir":
            print("Saliendo del navegador web.")
            break
        elif action == "adelante":
            if position < len(stack) - 1:
                position += 1
        elif action == "atrás":
            if position > 0:
                position -= 1
        else:
            for i in range(position, len(stack) - 1):
                stack.pop()
            stack.append(action)
            position += 1

        print("https://", end="")
        for i in range(position + 1):
            print(f"{stack[i]}/", end="")

web_navigation()

# impresora_cola
def shared_printer():
    queue = []

    while True:
        action = input("\nAñade un documento o selecciona imprimir/salir: ")
        if action == "salir":
            print("Saliendo de la impresora.")
            break
        elif action == "imprimir":
            if len(queue) > 0:
                print(f"Imprimiendo: {queue.pop(0)}")
        else:
            queue.append(action)

        print("Cola de impresión:")
        for i in range(len(queue)):
            print(f"- {queue[i]}")

shared_printer()