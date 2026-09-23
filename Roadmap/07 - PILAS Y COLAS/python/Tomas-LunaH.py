
"""
Ejercicio

"""
#Pila/Stack (LIFO)

stack = []

#Push
stack.append(1)
stack.append(2)
stack.append(3)
print(stack)

#pop
stack_item = stack[len(stack)-1]
del stack[len(stack)-1]
print(stack_item)
print(stack.pop())
print(stack)

#Cola/Queue (FIFO)
queue = []

#enqueue
queue.append(1)
queue.append(2)
queue.append(3)
print(queue)

#dequeue
print(queue.pop(0))
queue_item = queue[0]
print(queue_item)
del queue[0]
print (queue)

"""
Extra

"""
action = 0
browser_back = []
browser_next = []
while action != 4:
    print(f"Sus pestanas abiertas {browser_back}")
    action= int(input("""Seleccione la accion a realizar
        1. nueva pagina
        2. adelante
        3. atras
        4. salir: """))
        
    if action == 1:
        page = input("\n Ingrese la url: ")
        browser_back.append(page)
        print(f"Usted esta situado en {browser_back[-1]}")

    elif action == 3:
        if len(browser_back) > 1:
            browser_item = browser_back.pop()
            browser_next.append(browser_item)
            print(f"Ha retorocedido a: {browser_back[-1]}")
        else :
            print("No puedes retroceder solo tienes una pestaña ")

    elif action == 2:
        if len(browser_next) > 1:
            browser_item = browser_next.pop()
            browser_back.append(browser_item)
            print(f"Se ha desplazado a : {browser_back[-1]}")
        else :
            print("No puedes avanzar solo tienes una pestaña ")


    elif action == 4:
        print("\n Ha salido del navegador")
    else :
        print("Esta no es una opcion valida seleccione una nueva")
    

def imprent():
    document = []
    while True:
        print_doc = input("Ingrese la accion o el nombre del documento: ").lower().strip()
        if print_doc == "off":
            break

        elif print_doc == "imprimir":
            if len(document) >= 1:
                doc_such = document.pop(0)
                print(f"El documento {doc_such} se ha impreso")
                print(f"La cola de impresion es la siguiente {document}")
            else:
                print("No tienes docuementos a impirmir")
        else:
            document.append(print_doc)
            print(f"La cola de impresion es la siguiente {document}")

imprent()