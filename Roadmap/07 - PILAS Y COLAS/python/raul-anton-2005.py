def add_stack(stack, value):
    stack.append(value)
    return stack

def remove_stack(stack):
    if stack:
        stack.pop()
        return stack
    else:
        return None

def add_queue(queue, value):
    queue.append(value)
    return queue

def remove_queue(queue):
    if queue:
        queue.pop(0)
        return queue
    else:
        return None

stack = []
queue = []

# Añadiendo elementos a la pila
add_stack(stack, 1)
add_stack(stack, 2)
add_stack(stack, 3)

# Eliminando elementos de la pila
print("Estado final de la pila:", remove_stack(stack))

# Añadiendo elementos a la cola
add_queue(queue, 1)
add_queue(queue, 2)
add_queue(queue, 3)

# Eliminando elementos de la cola
print("Estado final de la cola:", remove_queue(queue))

def browser():
    pages = ["Google", "Facebook", "Twitter", "Instagram", "LinkedIn", "YouTube", "GitHub"]
    history = []
    forward_history = []
    current_page = None
    while True:
        print("\n--- Navegador Web ---")
        print("Página actual:", current_page)
        print("Historial:", history)
        print("Historial hacia adelante:", forward_history)
        print("Páginas disponibles:", pages)
        action = input("Introduce 'adelante' o 'atrás' para navegar, o directamente una web: ")
        
        if action == "atrás":
            if history:
                add_stack(forward_history, current_page)
                current_page = history[-1]
                remove_stack(history)
                print("Navegando a:", current_page)
            else:
                print("No hay historial disponible.")
        elif action == "adelante":
            if forward_history:
                add_stack(history, current_page)
                current_page = forward_history[-1]
                remove_stack(forward_history)
                print("Navegando a:", current_page)
            else:
                print("No hay páginas disponibles.")
        elif action in pages:
            if current_page:
                add_stack(history, current_page)
            current_page = action
        elif action == "salir":
            print("Saliendo del navegador.")
            break
        else:
            print("Acción invalida.")

def printer():
    queue = []
    while True:
        print("\n--- Impresora ---")
        print("Cola de impresión:", queue)
        action = input("Introduce 'imprimir' para imprimir el primer documento, o un nombre de documento para añadir a la cola: ")
        
        if action == "imprimir":
            if queue:
                remove_queue(queue)
                print("Imprimiendo documento...")
            else:
                print("No hay documentos en la cola.")
        elif action == "salir":
            print("Saliendo de la impresora.")
            break
        else:
            add_queue(queue, action)
            print(f"Documento '{action}' añadido a la cola.")

browser()
printer()
