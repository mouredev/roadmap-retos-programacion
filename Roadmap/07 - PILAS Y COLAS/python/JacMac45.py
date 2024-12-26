# Pilas y colas

# Pila/Stack (LIFO/Ultimo en entrar, primero en salir)

stack = []

# Añadir elementos a la pila (push)
stack.append(1)
stack.append(2)
stack.append(3)

print(f'Items de la pila al apilar: {stack}')

# Eliminar el ultimo elemento de la pila
stack_item = stack[len(stack) - 1]
del stack[len(stack) - 1]
print(stack_item)
print(stack)

# Utilizamos el método pop para quitar el ultimo elemento que haya entrado " len()-1 ". Mas recomendable y eficiente
print(stack.pop())
print(stack)


# Cola/Queue (FIFO/Primero en entrar, primero en salir)

queue = []

# Insertar elementos a la cola (enqueue)
queue.append(1)
queue.append(2)
queue.append(3)

print(f'Items de la cola al apilar: {queue}')

# Eliminar el primer elemento de la cola
queue_item = queue[0]
del queue[0]
print(queue_item)
print(queue)

# Utilizamos el método pop para quitar el primer elemento que haya entrado " 0 ". Mas recomendable y eficiente
print(queue.pop(0))
print(queue)

# DIFICULTAD EXTRA 

# Navegador web con implementación de pila:

def web_navigation():
    navigator = []
    print("Panel de inicio de navegación")

    while True:
        action = input("Introduce una url o elige una de las opciones: adelante/atrás/salir: ").lower()
        if action == "salir":
            print("Saliendo del navegador web.")
            break
        elif action == "adelante":
            if len(navigator) > 0: 
                print(f"Has navegado a la web: {navigator[len(navigator) - 1]}")
                navigator.pop()
        elif action == "atrás":
            if len(navigator) > 0:
                print(f"Has navegado a la web: {navigator[len(navigator) - 1]}")
                navigator.pop()
        else:
            navigator.append(action)

        if len(navigator) > 0:
            print(f"Pagina web actual: {navigator[-1]}")
        else:
            print("Panel de inicio de navegación")        
            

web_navigation()

# DIFICULTAD EXTRA 2

# Impresora con implementación de cola:

def shared_printer():
    queue = []
    while True:
                
        action = input("Introduce el documento que deseas añadir o selecciona 'imprimir' para imprimir o 'salir' \n").lower()
        
        if action == "salir":
            break
        elif action == "imprimir":
            if len(queue) > 0:
                print(f"Imprimiendo el documento {queue.pop(0)}")
            else:
                print("No hay documentos en la cola de impresión.")
        else:
            queue.append(action)

        
        if len(queue) > 0: print(f"Cola de impresión: {queue}")
        else: print("No hay documentos en la cola de impresión.")
        

shared_printer()

