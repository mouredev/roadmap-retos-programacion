'''Creación de pilas y colas'''
# PILAS /STACKS

# Pilas son estructuras de datos que siguen el principio LIFO 
# (Last In, First Out), es decir, el último elemento en entrar es el
# primero en salir. 

pila = [1, 2, 3, 4, 5]
pila.append(6)
pila.append(7)
print('Pila original: ', pila)

# Eliminar el último elemento agregado a la pila
pila_elemento = pila[len(pila) - 1]
# len(pila) - 1 es el índice del último elemento en la pila
del pila[len(pila) - 1] # Elimina el último elemento de la pila
print(pila_elemento) # Imprime el último elemento eliminado
print(pila)# Imprime la pila actualizada sin el último elemento

print(pila.pop()) # Elimina el último elemento de la pila y lo imprime
print(pila) # Imprime la pila actualizada sin el último elemento



# COLAS / QUEUES
queue = [2, 4, 6, 8, 10]

#Añadir
queue.append(12)
queue.append(14)
queue.append(16)

print('Cola original: ', queue)

# Eliminar el primer elemento agregado a la cola
# Dequeue

queue_elemento = queue[0]
del queue[0]
print(queue_elemento)

print(queue.pop(0))
print(queue)

# Las pilas sirven para almacenar elementos en un orden específico y
# las colas para almacenar elementos en un orden específico.
# Las pilas siguen el principio LIFO y las colas el principio FIFO


# DIFICULTAD EXTRA
def navegar():
    total = []
    
    while True:
        action =input("Selecciona una opción:\n1. Agregar nueva url\n2. Adelante\n3. Atrás\n4. Salir\n")
        
        match action:
            case "1": 
                url =input(input("Ingresar la url: "))
                total.append(url)
            case "2":
                print("Adelante")
            case "3":
                print("Atrás")
                del total[len(total) -1]
            case "4":
                break
            case _:
                print("Opción no válida")
        
        if (len(total) > 0):
            print(f"Has navegado a la web: {total[len(total) -1]}.")
        
        else: 
            print("No hay nada")

def impresion():
    total = []
    while True:
        action = input("Selecciona una opción:\n1. Agregar documento\n2. Imprimir\n3. Salir\n")
        
        match action:
            case "1":
                documento = input("Ingresar el documento: ")
                total.append(documento)
            case "2":
                if len(total) > 0:
                    print(f"Imprimiendo {total[0]}")
                    del total[0]
                else:
                    print("No hay documentos")
                print("")
            case "3":
                break
            case _:
                print("Opción no válida")
            
                