'''
PILAS Y COLAS
'''

#Pilas/Stack (LIFO) Last In First Out

stack = []

#push
stack.append(1) 
stack.append(2) 
stack.append(3) 
print(stack)

#pop
stack_item = stack[len(stack) - 1]
del stack[len(stack) - 1] #borra elemento del stack
print(stack_item)

print(stack.pop()) #también muestra el último añadido

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

print


'''
EXTRA
'''
'''
* - Utilizando la implementación de pila y cadenas de texto, simula el mecanismo adelante/atrás
 *   de un navegador web. Crea un programa en el que puedas navegar a una página o indicarle
 *   que te quieres desplazar adelante o atrás, mostrando en cada caso el nombre de la web.
 *   Las palabras "adelante", "atrás" desencadenan esta acción, el resto se interpreta como
 *   el nombre de una nueva web.
 * - Utilizando la implementación de cola y cadenas de texto, simula el mecanismo de una
 *   impresora compartida que recibe documentos y los imprime cuando así se le indica.
 *   La palabra "imprimir" imprime un elemento de la cola, el resto de palabras se
 *   interpretan como nombres de documentos.
'''

# Navegador web

pila = []
ans = "0"
cont=0
while True:
    
    if ans != "adelante" and ans != "atras" and cont!=1:
        cont=1
        at=len(pila)-1
    else: 
        cont=1
        at=at

    ans = input("adelante/atras: ")


    if ans == "adelante":
        at=at+1
    elif ans == "atras": #ok
        at=at-1  
    elif ans == "end":
        break
    else:
        pila.append(ans)
        at=len(pila)-1

    pos = pila[at]
    print(f"\n Dirección actual: {pos}")
    print(" ")   



# Impresora

cola = []

while True:

    doc = input("\nIMP: ")

    if doc == "imprimir" and cola:
        print(f"\nImprimiendo {cola.pop(0)}")
    elif doc == "imprimir" and not cola:
        print("\nNo hay elementos en la cola")
    elif doc == "end":
        break
    else:
        cola.append(doc)
    
    print(cola)


    '''
    EL SUYO

    # Web


def web_navigation():

    stack = []

    while True:

        action = input(
            "Añade una url o interactúa con palabras adelante/atrás/salir: "
        )

        if action == "salir":
            print("Saliendo del navegador web.")
            break
        elif action == "adelante":
            pass
        elif action == "atrás":
            if len(stack) > 0:
                stack.pop()
        else:
            stack.append(action)

        if len(stack) > 0:
            print(f"Has navegado a la web: {stack[len(stack) - 1]}.")
        else:
            print("Estás en la página de inicio.")


web_navigation()


def shared_printed():

    queue = []

    while True:

        action = input("Añade un documento o selecciona imprimir/salir: ")

        if action == "salir":
            break
        elif action == "imprimir":
            if len(queue) > 0:
                print(f"Imprimiendo: {queue.pop(0)}")
        else:
            queue.append(action)

        print(f"Cola de impresión: {queue}")


shared_printed()

    '''
