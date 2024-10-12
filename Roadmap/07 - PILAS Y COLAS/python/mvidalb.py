'''
Ejercicio
'''
 # Pila/Stack (LIFO - Last In First Out)

stack = []
# push
stack.append("1")
stack.append("2")
stack.append("3")
print(stack)
# pop
stack_item = stack[len(stack) - 1]
#del stack[len(stack) - 1]

print(stack.pop())      #["a","b","c"].pop() --> "c"

print(stack_item)
print(stack)

# Cola/Queue (FIFO - First In First Out)
queue = []
# enqueue
queue.append(1)
queue.append(2)
queue.append(3)
# dequeue
print(queue.pop(0))     #["a","b","c"].pop(0) --> "a"


'''
Ejercicio extra
'''

# Web
def web_navigation():
    
    stack = []
    
    while True:
        action = input("Añade una url o interactúa con palabra adelante/atrás/salir: ")
        if action == "salir":
            print("Saliendo del navegador web.")
            break
        elif action == "adelante":
            pass
        elif action == "atrás":
            if len(stack) > 0:
                stack.pop() 
        else:
            stack.append(action)

        print(stack)
        if len(stack) > 0:
            print(f"Has navegado a la web: {stack[len(stack) - 1]}")
        else:
            print("Estás en la página de inicio.")

web_navigation()


# Shared printer
def shared_printer():
    queue=[]

    while True:
        action = input("Añade un documento o selecciona imprimir/salir: ")
        if action == "salir":
            break
        elif action == "imprimir":
            if len(queue) > 0:
                impreso = queue.pop(0)   # Elimina el primer elemento que entro en la cola (1º en la lista)
                print(f"Archivo impreso: {impreso}")
            else:
                print("No hay nada en la cola de impresión")
        else:
            queue.append(action)

        print(f"Cola de impresión: {queue}")

shared_printer()
