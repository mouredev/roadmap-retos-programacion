# Pila/Stack (LIFO)

stack = []
stack.append("1")
stack.append("2")
stack.append("3")
last_item = stack[len(stack) - 1]
print(stack)
print(last_item)

# pop
del stack[len(stack) - 1]
print(stack , "\n")

# Cola/Queue (FIFO)

queue = []

# enqueue
queue.append(1)
queue.append(2)
queue.append(3)

print(queue)

# dequeue
print(queue.pop(0))

print(queue)

# Ejercicios extra

# Web

def web_navegator():
    stack = []
    
    while True:
        action = input("Inserta una url o navega con adelante/atras/salir: ").lower()
        if action == "salir":
            print("Saliendo..")
            break
        elif action == "adelante":
            pass
        elif action == "atras":
            if len(stack) > 0:
                stack.pop()
        else:
            stack.append(action)
        
        if len(stack) > 0:
            print(stack[len(stack) - 1])
        else:
            print("Estas en el index")

# web_navegator()

# Impreso
def imprimir_elemento():
    queue = []
    while True:
        printer = input("Inserte el documento o la palabra imprimir/salir: ").lower()
        if printer == "salir":
            print("Saliendo..")
            break
        elif printer != "imprimir":
            queue.append(printer)
        else:
            if len(queue) > 0:
                print(f"Imprimiendo el documento: {queue.pop()}")
        
        print(f"Cola de impresion {queue}")

imprimir_elemento()