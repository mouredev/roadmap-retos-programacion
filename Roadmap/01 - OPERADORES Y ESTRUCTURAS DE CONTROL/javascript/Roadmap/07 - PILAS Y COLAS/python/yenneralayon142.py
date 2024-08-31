"""
PILAS Y COLAS
"""
#PILA / STACK (LIFO)
list_one = []
#PUSH (Agregar)
list_one.append(1)
list_one.append(2)
list_one.append(3)
print(list_one)

#POP (Eliminar)
#del list_one(len(list_one - 1))  Hacerlo manualmente
print(list_one.pop())
print(list_one)

#COLA/QUEUE(FIFO)
list_two= []
# enqueue
list_two.append(1)
list_two.append(2)
list_two.append(3)
print(list_two)
# dequeue
print(list_two.pop(0))
print(list_two)


"""
Extra
"""

#Navegador web

def navigation():

    list_three = []

    while True:
        action = input(
            "Añade una url o interactua con palabras adelante/atrás/salir"
        )
        if action == "salir":
            print("saliendo del navegador web")
            break
        elif action == "adelante":
            pass
        elif action == "atrás":
            if len(list_three) > 0:
                list_three.pop()
        else:
            list_three.append(action)

        if len(list_three) > 0:
            print(f"Has navegado a la web {list_three[len(list_three) - 1]}.")
        else:
            print("Estas en la pagina de inicio")

navigation()


#Impresora

def printed():

    queue = []
    while True:
        action = input("Añade un documento o selecciona imprimir/salir: ")
        if action == "salir":
            break
        elif action == "imprimir":
            if len(queue) > 0:
                print(f"Imprimiendo {queue.pop(0)}.")
        else:
            queue.append(action)

        print(f"Cola de impresión:{queue}")
printed()

