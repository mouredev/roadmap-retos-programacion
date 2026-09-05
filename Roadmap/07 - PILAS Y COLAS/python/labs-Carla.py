"""
Pilas y Colas

Son de las estructuras de datos más importantes. 
Aparecen en navegadores, compiladores, servidores, algoritmos de búsqueda.

"""

""" Las Pilas son estructuras 
de datos que funcionan bajo
el principio LIFO

LAST IN FIRST OUT

en Python podemos usar listas para usar esta estructura
de datos

con la condición de que el primero
en salir sea el primero en entrar.

justo como en la navegación de páginas <atrás> <adelante>

"""

#ejemplo sencillo

stack = []

stack.append(1)
stack.append(2)

print(stack.pop()) 

stack.append(3)
stack.append(4)

print(stack)


"""Las colas son una estructura de datos que funcionan bajo el 
principio FIFO, justo como una fila en el banco
"""

queue = []

#encola

queue.append(1)
queue.append(2)
queue.append(3)

print(queue)

#desencola

del queue[0]
print(queue)

"""Extra"""

def web_navigation():

    stack = []

    while True:

        action = input(
            "Añade una url o interactúa con palabras adelante/atrás/salir: "
        )

        if action == "salir":
            print("\nSaliendo del navegador web.")
            break 
        elif action == "adelante":
            pass
        elif action == "atrás":
            stack.pop()
        else:
            stack.append(action)

            if len(stack) > 0:
                print("Has navegado a la web: {stack[len(stack)-1]}")
            else:
                print("Estás en la página anterior")          


#web_navigation()

def shared_printed():

    queue = []

    while True:
        action = input("Añade un documento o selecciona imprimir/salir: ")

        if action =="salir":
            break
        elif action == "imprimir":
            if(len(queue)>0):
                print(f"{queue.pop(0)}")
        else:
            queue.append(action)
        print(f"Cola de impresion: {queue}")


shared_printed()
        




