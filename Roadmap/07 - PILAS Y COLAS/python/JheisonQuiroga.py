from collections import deque

"""
Pilas y colas
Son estructuras de datos, se utilizan para almacenar y gestionar información

Pilas (Stacks):
Principio LIFO (Last in- First out) 
"""

# Ejemplo

stack = []

stack.append(1) # Push - Agregar un elemento
stack.append(2)
stack.append(3)
stack.append(4)
stack.append(5) # Ultimo en entrar
print(stack)

print(stack.pop()) # 5 POP - PRIMERO EN SALIR

"""
2. Colas - Queues
Principio FIFO (First in - first out)

push = Agregar elementos
pop = Eliminar elementos
top = Ver el elemento en la parte superior sin eliminarlo
is_empty = Comprobar si la lista está vacia
"""

first_queue = []

first_queue.append(1) # Agregando elementos
first_queue.append(2)
first_queue.append(3)
first_queue.append(4)
first_queue.append(5)
print(first_queue)

# Eliminando el primer elemento
print(first_queue.pop(0)) # 1

"""
2.1. Colas - Utilizando el módulo collections

enqueue = Agregar elementos
dequeue = Eliminar elementos
front = Ver el elemento en frente sin eliminarlo
is_empy = Comprobar si la cola está vacia
"""

queue = deque()

queue.append(1) # Agregar el elemento a la cola
queue.append(2)
queue.append(3)

print(queue) # deque([1, 2, 3])

#Eliminar el primer elemento
first_element_eliminated = queue.popleft()
print(first_element_eliminated) # 1
print(queue) # deque([2, 3])


"""
Extra
"""
lst = ["github.com", "roadmap-retos-programacion", "Roadmap", "07-pilasycolas"]
lst2 = []

def current_path_show():
    print("Ruta actual:")
    print("/".join(lst2))


def navigation_web():
    print("Esta es la ruta de la página")
    print("/".join(lst))
    lst2.append(lst.pop(0))
    print(lst2[0])

    while True:
        option = input("Quieres ir adelante/atras/salir: ").lower()

        while option not in ["adelante", "atras", "salir"]:
            option = input("Ingresa una opción valida adelante/atras/salir: ").lower()
        
        if option == "adelante":
            if len(lst2) == 4:
                print("Has llegado hasta el final de la ruta")
            else:
                lst2.append(lst.pop(0))
                current_path_show()
        elif option == "atras":
            if lst2:
                lst.insert(0, lst2.pop())
                current_path_show()
            else:
                print("Has llegado al inicio de la ruta")
        else:
            break


# Impresora
printer = []


def my_printer():
    global printer
    printer = []

    while True:

        print("""Operaciones disponibles:
            1. Agregar a la cola
            2. Imprimir
            3. Reiniciar cola
            4. Apagar impresora""")

        option = input("Que operación deseas realizar: ")

        if option == "1":
            element = input("Que deseas imprimir: ")
            print(push_elements(element))
        elif option == "2":
            print(prt_element())
        elif option == "3":
            print("Reiniciando cola...")
            printer = []
        elif option == "4":
            print("Apagando impresora...")
            return
        else:
            print("Ingrese una opción valida")


def show_elements():
    return "-".join(printer)

def push_elements(element):
    printer.append(element)
    return show_elements()

def prt_element():
    print(f"Imprimiendo: {printer.pop(0)}")
    return f"Elementos en cola: {show_elements()}"




my_printer()