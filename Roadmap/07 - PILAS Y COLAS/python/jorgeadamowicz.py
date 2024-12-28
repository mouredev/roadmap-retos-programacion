## Pilas Y Colas

# pilas (stacks - LIFO)

my_stack = [] #creo una lista

#push
my_stack.append(1) #apilo, el primer elemento
my_stack.append(2) #apilo, el segundo elemento
my_stack.append(3) #apilo, el tercer elemento

print(my_stack)

#pop
my_stack_item = my_stack[len(my_stack)-1] #recupero el ultimo elemento en mi lista(my_stack)
#del my_stack[len(my_stack)-1] # borra el último elemento de mi lista
del my_stack[-1] #tambien se puede eliminar el elemento a travez de su indice

print(my_stack_item)
print(my_stack)

#desapilando un elemento a travez del método ".pop()"
my_pop_item = my_stack.pop()

print(my_pop_item)
print(my_stack)


# Colas (Queues - FIFO)
my_queue = []

#enqueue
my_queue.append(1) 
my_queue.append(2) 
my_queue.append(3) 

print(my_queue)

#dequeue

print(my_queue.pop(0)) # indicar el indice "0", que es el mas viejo de la lista. 
del my_queue[0] #tambien lo podemos hacer como en el caso de pila pero esta vez asignanos el indice "0"

"""
Extra
"""

def web_navigator():
    
    stack_web = []
    stack_foward = []
    
    while True:
        action = input("Añade una ruta, o selecciona atras, adelante o salir: \n")
        
        if action == "salir":
            print("Saliendo de la aplicación")
            break
        elif action == "adelante":
            if stack_foward: # equiva a -> len(stack_foward)>0
                siguiente_pagina = stack_foward.pop()# recupera la pagina hacia adelante
                stack_web.append(siguiente_pagina) # la añade al historial
                
            else:
                print("No hay paginas para avanzar.")
                 
        elif action == "atras":
            if stack_web: # equivale a -> len(stack_web)> 0:
                ultima_pagina = stack_web.pop() #retira la pagina actual y la asigna a stack_foward
                stack_foward.append(ultima_pagina)
                if stack_web: 
                    print(f"te envuentras en el sitio: {stack_web[-1]}\n")
                else: 
                    print("Te encuentras en la pagina principal. el historial de navegacion se encuentra vacio.")
                
            else:
                print("Te encuentras en la pagina principal. el historial de navegacion se encuentra vacio.")
            
        else:
            stack_web.append(action)
            stack_foward.clear()
            
        print(f"Historial de navegación: {stack_web}")
        print(f"pagina hacia adelante: {stack_foward}\n")
        
web_navigator()
    
    
"""
Nota: se implementó un pila temporal, para recuperar el valor alojado en ".pop" y tener la opción de hacer
un paso "adelante". cuando el usuario ingresa una nueva url la pila temporal se reinicia.
"""
    
def shared_printer():
    
    cola_impresion = []
    while True:
        action = input("Añade un documento a la cola, selecciona imprimir o salir: \n")
        
        if action == "salir":
            break
        elif action == "imprimir":
            if len(cola_impresion) > 0:
                print(f" Imprimiendo el documento: {cola_impresion.pop(0)}\n")
            else:
                print("la cola de impresión esta vacia. no hay documentos por imprimir.")
        else:
            cola_impresion.append(action)
        print(f"documentos en cola de impresion:\n {cola_impresion}")    
shared_printer()