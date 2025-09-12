# pila
pila = []

# push
pila.append(1)
pila.append(2)
pila.append(3)

# pop
pila.pop()
print(pila)

# cola
cola = []

# enqueue
cola.append(1)
cola.append(2)
cola.append(3)

# dequeue
cola.pop(0)
print(cola)

# DIFICULTAD EXTRA


def webNavigation():
    stack = []

    while True:
        action = input("Añade una url o interactúa con palabras adelante/atras/salir: ")

        if action == "salir":
            print("Saliendo del navegador web.")
            break
        elif action == "adelante":
            continue
        elif action == "atras":
            if len(stack) > 0:
                stack.pop()
        else:
            stack.append(action)

        if len(stack) > 0:
            print("Has navegado a la web:", stack[-1])
        else:
            print("Estás en la página de inicio.")


webNavigation()


def sharedPrinted():
    queue = []

    while True:
        action = input("Añade un documento o selecciona imprimir/salir: ")

        if action == "salir":
            break
        elif action == "imprimir":
            if len(queue) > 0:
                print("Imprimiendo:", queue.pop(0))
        else:
            queue.append(action)
        print("Cola de impresión:", queue)


sharedPrinted()
