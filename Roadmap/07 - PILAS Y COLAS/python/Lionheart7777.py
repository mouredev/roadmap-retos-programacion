"""
EJERCICIO
"""
# PILA/STACK/LIFO
"""

stack = []

#push
stack.append("1")
stack.append("2") 
stack.append("3")
print(stack)

#pop
stack_item = stack[len(stack)-1] 
del stack[len(stack)-1] # elimina el "3"

print(stack.pop()) # elimina el "2"

print(stack) # imprime ["1"]
"""

#Cola/Queue/ FIFO

queue = []

#push
queue.append(1)
queue.append(2) 
queue.append(3)

#dequeue
queue_item = queue[0] 
del queue[0] # elimina el #1
print(queue_item) 

print(queue.pop(0))# elimina el #2

print(queue) # imprime [3]




"""
EXTRA
"""

#WEB



def web_navigation():
    
    stack = []
    
    while True:
        
        action = input("Añade una url o interactúa con palabras adelante/atrás/salir:")

        if action == "salir":
            print("saliendo del navegador web")
            break
        elif action == "adelante" :
            pass
        elif action == "atrás" :
            if len(stack) > 0:
                stack.pop()
        else :
            stack.append(action)
        if len(stack) > 0:        
            print(f"Has navegado a la web : {stack[len(stack)-1]}")
        else:
            print("estás en la página de inicio")

#web_navigation()

def shared_printed():
    queue = []
    
    while True:
        action = input("añada un documento o seleccione imprimir/salir :")
        
        if action == "salir":
            break
        elif action == "imprimir":
            if len(queue) > 0:
                print(f"imprimiendo : {queue.pop(0)}")
        else:
            queue.append(action)
        
        print(f"Cola de Impresión:{queue}")
            
    
    
    
shared_printed()     