'''
ejercicio
'''
# pila/stack (LIFO)
stack = []

stack.append('1')
stack.append('2')
stack.append('3')
print(stack)

#pop
stack_item = stack[len(stack)- 1 ]
del stack[len(stack)- 1 ]
print(stack_item)
print(stack.pop())
print(stack)

# cola/queue (FIFO)
queue = []
queue.append(1)
queue.append(2)
queue.append(3)

del queue[0]
print(queue)
# dequeue
print(queue.pop(0))

print(queue)

'''
extra
'''

web_pages = [
    'google',
    'facebook',
    # 'youtube',
    # 'temu',
    # 'x',
    # 'threads',
    # 'gmail',
    # 'outlook'
    ]

def navigator():
    cursor=0
    action= ''
    while True:
        while action == '':
            print(f"Usted esta en {web_pages[cursor]}")
            print(f"sus pestañas disponibles son {web_pages}")
            action = input("Ejecute alguna accion (salir, adelante, atras)")
        if action == "salir":
            break
        if action == "adelante":
            if cursor < len(web_pages) - 1:
                cursor += 1
            else:
                new_page = input("No hay más páginas. ¿Desea agregar una nueva? (si/no): ").strip().lower()
                if new_page == 'si':
                    new_url = input("Ingrese el nombre de la nueva página: ")
                    web_pages.append(new_url) 
                    cursor += 1  
                else:
                    print("No se ha agregado ninguna página nueva.")
        if action == "atras":
            cursor -= 1   
        action=''
# navigator()

def shared_printer():
    queue = [] 
    while True:
       
        action = input(" Añade un documento o seleciona imprimir/salir : ")

        if action == "salir":
            break
        elif action == "imprimir":
            if len(queue) > 0:
                print(f"imprimiendo... {queue[0]}")
                queue.pop(0)
            else:
                print("No hay documentos disponibles para impresion")
        else:
            queue.append(action)
        print(f"Cola de impresion: {queue}")
shared_printer()