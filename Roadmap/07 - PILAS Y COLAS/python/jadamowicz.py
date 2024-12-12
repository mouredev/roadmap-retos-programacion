from icecream import ic
## Pilas Y Colas

# pilas (stacks - LIFO)

my_stack = [] #creo una lista

#push
my_stack.append(1) #apilo, el primer elemento
my_stack.append(2) #apilo, el segundo elemento
my_stack.append(3) #apilo, el tercer elemento

print(my_stack)
ic(my_stack)

#pop
my_stack_item = my_stack[len(my_stack)-1] #recupero el ultimo elemento en mi lista(my_stack)
#del my_stack[len(my_stack)-1] # borra el último elemento de mi lista
del my_stack[-1] #tambien se puede eliminar el elemento a travez de su indice

print(my_stack_item)
ic(my_stack_item)

print(my_stack)
ic(my_stack)

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