"""
 * Implementa los mecanismos de introducción y recuperación de elementos propios de las
 * pilas (stacks - LIFO) y las colas (queue - FIFO) utilizando una estructura de array
 * o lista (dependiendo de las posibilidades de tu lenguaje).
"""

# Pila/Stack (LIFO)

stack = []

def push_stack(element):
    stack.append(element)

def pull_stack():
    return stack.pop()

print(stack)
push_stack(1)
print(stack)
push_stack(2)
print(stack)
print(f" Elemento sacado: {pull_stack()}")
print(stack)
push_stack(3)
print(stack)
push_stack(4)
print(stack)
print(f" Elemento sacado: {pull_stack()}")
print(stack)


# Cola/Queue (FIFO)

queue = []

def push_queue(element):
    queue.append(element)

def pull_queue():
    return queue.pop(0)


print("----------------------------")
print(queue)
push_queue(1)
print(queue)
push_queue(2)
print(queue)
print(f" Elemento sacado: {pull_queue()}")
print(queue)
push_queue(3)
print(queue)
push_queue(4)
print(queue)
print(f" Elemento sacado: {pull_queue()}")
print(queue)


"""
 * DIFICULTAD EXTRA (opcional):
 * - Utilizando la implementación de pila y cadenas de texto, simula el mecanismo adelante/atrás
 *   de un navegador web. Crea un programa en el que puedas navegar a una página o indicarle
 *   que te quieres desplazar adelante o atrás, mostrando en cada caso el nombre de la web.
 *   Las palabras "adelante", "atrás" desencadenan esta acción, el resto se interpreta como
 *   el nombre de una nueva web.
 * - Utilizando la implementación de cola y cadenas de texto, simula el mecanismo de una
 *   impresora compartida que recibe documentos y los imprime cuando así se le indica.
 *   La palabra "imprimir" imprime un elemento de la cola, el resto de palabras se
 *   interpretan como nombres de documentos.
"""

def web_browser():

    back = [] #Pila: almacena la web actual en la parte más alta y las de atras acontinuación
    forward = [] #Pila: Almacena las paginas a las que avanzar cuando vamos atras.
    salir = False

    while not salir:
        action = input("Introduce una web o una accion (adelante/atras/salir): ")

        if action == "salir":
            salir = True

        elif action == "adelante":
            if len(forward) > 0:    # Si hay paginas para avanzar(si hay elementos en forward)
                web = forward.pop() # Sacamos de forward y lo pasamos a back.
                back.append(web)
                print(f"Pagina actual: {back[-1]}") #Pagina actual el pico de la pila
            else:
                print(f"No hay mas paginas adelante")

        elif action == "atras":
            if len(back) > 1:       # Si hay mas de una web en back podremos usar atras.
                web = back.pop()    # Sacamos de back y pasamos el elemtno a forward, ya que son los elementos que podremos avanzar.
                forward.append(web) #
                print(f"Pagina actual: {back[-1]}") #Siempre se imprime el pico de back
            else:
                print("No hay más paginas atras")

        else:
            back.append(action) # Para añadir una nueva web se añade en back
            print(f"Pagina actual: {back[-1]}")
            forward.clear()     # En el caso de añadir una nueva web se descartan las que estaban
                                # preparadas para ir adelante (pila forward)
                                # Asi lo hace chrome.

web_browser()

def printer():

    printer_queue =[]
    salir = False
    while not salir:

        action = input("Introduce nombre de documento, o una acción(imprimir, salir): ")

        if action == "salir":
            salir = True

        elif action == "imprimir":
            if len(printer_queue) > 0:
                document = printer_queue.pop(0)
                print(f"Imprimiendo... {document}")
                print(printer_queue)
            else:
                print("Cola de impresion vacía")

        else:
            printer_queue.append(action)
            print(printer_queue)

printer()
