# pila
stack = []

stack.append(1)
stack.append(2)
stack.append(3)
stack.append(4)

print(stack)
print (stack.pop())
print(stack)

""""La pila ingresa varios valores pero al usar el pop siempre va a sacar el ultimo item (de la derecha)"""

queue = []

queue.append(1)
queue.append(2)
queue.append(3)
queue.append(4)

print(queue)
print(queue.pop(0))
print (queue)

"""la fila ingresa varios valores pero al usar el pop en el indice 0 siempre va a sacar el primer item (de la izquierda)"""

#Ejercicios dificultad Extra


def paginaweb():

    stack = []

    while True:

        accion = input("Añade una url o la accion que quieras: adelante/atras/salir")

        if accion == "salir":
            print ("saliendo de la web")
            break
        elif accion == "adelante":
            pass
        elif accion == "atras":
            if len(stack) > 0:
             stack.pop()
        else:
            stack.append(accion)

        if len(stack) > 0:

            print(f"estas en la web: {stack[len(stack)-1]}")   
           
        else:
            print("estas en el inicio") 
            


def impresora():

    queue = []

    while True:
        accion = input("porfavor indica el nombre del documento a agregar ola accion que quieres hacer: imprimir/salir " )

        if accion == "imprimir":

            if len(queue) > 0:
             print(f"El Documento {queue.pop(0)} ha sido impreso")
            else:
                print("no hay documentos para imprimir") 

        elif accion == "salir":
            print("saliendo de la impresora")
            break
         
        else:
            queue.append(accion)  
            print(f"documento {accion} agregado")

impresora()            