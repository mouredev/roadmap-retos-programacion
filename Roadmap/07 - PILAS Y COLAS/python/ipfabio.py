"""
Ejercicio
"""

# Pila/Stack (LIFO Last In First Out)

# Push
stack = []
stack.append(1)
stack.append(2)
stack.append(3)
print(stack)

# Pop
stack_item = stack[len(stack) - 1]
del stack[len(stack) - 1] # delete last item
print(stack_item)

print(stack.pop()) # delete last item

print(stack)

# Cola/Queue (FIFO First In First Out)
queue = []

# enqueue (encolar)
queue.append(1)
queue.append(2)
queue.append(3)

# dequeue (desencolar)
queue_item = queue[0]
del queue[0]

print(queue.pop(0))

print(queue)

"""
Extra
"""

# Opciones
def opciones():
    print("""1. Login\n2. Profile\n3. Atras\n4. Salir""")

# Web
def web_navigation():
    stack = [] # Inicialización pila vacía para rastrear navegación
    opciones() # Llamada función opciones
    while True:
        opcion = input("Ingresa la opcion: ") # Solicita al usuario la opción
        match opcion:
            case "1":
                stack.append("/Login/") # Agrega "/Login/" a la pila
            case "2":
                stack.append("/Login/Profile") # Agrega "/Login/Profile" a la pila
            case "3":
                if len(stack) > 0:
                    stack.pop() # Elimina el último elemento de la pila si no está vacía
            case "4":
                print("Saliendo del navegador.") # Imprime mensaje y sale del bucle
                break
            case _:
                print("Opcion no válida.") # Imprime mensaje si no recibe una opción válida
        
        if len(stack) > 0:
            print(stack[len(stack) - 1]) # Imprime el último elemento de la pila
        else:
            print(f"Esta en Home. Quiere salir? Presione 4.") # Mensaje cuando la pila está vacía


web_navigation()

def impresora_compartida():
    queue = [] # Inicializa cola vacía para documentos

    while True:

        action = input("Agrega un documento o selecciona imprimir/salir: ") # Solicita acción del usuario

        if action == "salir":
            break # Sale del bucle
        elif action == "imprimir":
            if len(queue) == 0:
                print(f"No hay elementos a imprimir.") # Informa si no hay documentos en cola

            if len(queue) > 0:
                elemento_0 = queue.pop(0) # Elimina y obtiene el documento
                print(f"Imprimiendo: {elemento_0}")
        else:
            queue.append(action) # Agrega el documento a cola
        
        print(f"Cola de impresión: {queue}") # Muestra el estado actual de cola



impresora_compartida()