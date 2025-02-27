""" 
EJERCICIO:
  Implementa los mecanismos de introducción y recuperación de elementos propios de las
  pilas (stacks - LIFO) y las colas (queue - FIFO) utilizando una estructura de array
  o lista (dependiendo de las posibilidades de tu lenguaje).
"""

# Pila/Stack (LIFO)
stack = []
stack.append("1") #Push
stack.append("2") #Push
stack.append("3") #Push
print(stack)

# Pop
stack_item = stack[len(stack) -1] 
del stack[len(stack) -1]
print(stack_item)

print(stack.pop()) # Devuelve el último elemento de la pila


# Cola/Queue (FIFO)
queue = []

# Enqueue/Encolar
queue.append(1)
queue.append(2) 
queue.append(3) 
print(queue)

# Dequeue/Desencolar
queue_item = queue[0]
del queue[0]
print(queue_item)

print(queue.pop(0)) # Devuelve el primer elemento de la cola


"""
DIFICULTAD EXTRA (opcional):
  - Utilizando la implementación de pila y cadenas de texto, simula el mecanismo adelante/atrás
    de un navegador web. Crea un programa en el que puedas navegar a una página o indicarle
    que te quieres desplazar adelante o atrás, mostrando en cada caso el nombre de la web.
    Las palabras "adelante", "atrás" desencadenan esta acción, el resto se interpreta como
    el nombre de una nueva web.
  - Utilizando la implementación de cola y cadenas de texto, simula el mecanismo de una
    impresora compartida que recibe documentos y los imprime cuando así se le indica.
    La palabra "imprimir" imprime un elemento de la cola, el resto de palabras se
    interpretan como nombres de documentos.
"""
print('\n\n\n--- EJERCICIO EXTRA ---\n')

# NAVEGADOR WEB
def web_browser():
    
    """
    En esta version del navegador, no se puede usar la 
    funcion adelante sin antes haber utilizado la funcion atras
    """
    
    pages = []

    last_page = ""

    def insert_web():
       link = input("Introduce una pagina web: ")
       pages.append(link)
       print(f"Redirigiendote a {link}") 
    

    def forward():
       if last_page == "":
           print("Te encuentras en la ultima pagina") 
       else:
           pages.append(last_page)
           print("Redirigiendote a ", pages[-1])


    def backwards():
        backwards = pages.pop()
        print(f"Ultima pagina: {backwards}")

        return backwards


    while True:

        print("\n\n GESTION DE PÁGINAS WEB\n")
        print("1. Introducir una pagina")
        print("2. Adelante")
        print("3. Atras")
        print("4. Historial")
        print("5. Salir")

        status = input("Que opcion deseas realizar?: ")

        match status:

            case "1":
                insert_web()
            case "2":
                forward()
            case "3": 
                last_page = backwards()
            case "4": 
                print(pages)
            case "5":
                print("Hasta pronto.")
                break
            case _:
                print("Opcion no valida. Elige una opcion del 1 al 5")

web_browser()    


# IMPRESORA
from collections import deque 

def printer():

   queue = deque() 

   def send():
        doc = input("Que documento deseas enviar? :")
        queue.append(doc)
        print(f"Cola: {queue}")


   def printing():
       print('Imprimiendo', queue.popleft())
       print('Qedan:', queue, 'documentos.')

   while True:
       
       print("\n\n GESTION DE DOCUMENTOS\n")
       print("1. Enviar")
       print("2. Imprimir")
       print("3. Salir")
       
       status = input("Que opcion deseas realizar?: ")
       
       match status:

        case "1":
            send()
        case "2":
            if len(queue) == 0:
                print("No hay documentos que imprimir.")
            else:
                printing()
        case "3":
            print("Cerrando la impresorsa.")
            break
        case _:
            print("Opcion no valida. Elige una opcion del 1 al 3")

printer()