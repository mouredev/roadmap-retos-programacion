#Pila (LIFO)

stack = []
stack.append("1")
stack.append("2")
stack.append("3")
print(stack)            #Inicializamos la pila

stack.pop()             #Sacar un item de la pila (el último que se añadió)
print(stack)

#Cola (FIFO)

queue = []
queue.append("1")
queue.append("2")
queue.append("3")
print(queue)            #Iniciar la cola

queue.pop(0)         #Sacar un item de la cola (el primero que se añadió)
print(queue)


#EJERCICIO EXTRA

def web_navegation():

    stack = []

    while True:

        action = input("Añade una url o interactúa con palabras adelante/atras/salir: ")

        match action:
            case "adelante":
                #Como la página web no es una pila, entonces no hay operacion de adelante
                pass
            case "atras":
                if(len(stack) > 0):
                    stack.pop()
                else:
                    print("Añade una URL para poder navegar")
            case "salir":
                print("Hasta la próxima")
                break
            case _:
                stack.append(action)

        if len(stack) > 0:
            print("Estas en la web " + stack[len(stack)-1])
        else:
            print("Estas en la página de inicio")

web_navegation()


def printer():

    queue = []

    while True:

        action = input("Añade un documento o interactúa con palabras imprimir/salir: ")

        match action:
            case "imprimir":
                if len(queue) > 0:
                    print(f"Imprimiendo: {queue.pop(0)}")
                else:
                    print("No hay documentos en la impresora")
            case "salir":
                print("Hasta la próxima")
                break
            case _:
                queue.append(action)
                print("Documento añadido")

printer()