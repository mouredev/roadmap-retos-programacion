"""
EJERCICIO:
Implementa los mecanismos de introduccion y recuperacion de elementos
propios de las pilas (stacks - LIFO) y las colas (queue -FIFO) 
utilizando una estructura de array.

DIFICULTAD EXTRA (opcional):
- Utilizando la implementación de pila y cadenas de texto, simula el mecanismo adelante/atrás
de un navegador web. Crea un programa en el que puedas navegar a una página o indicarle
que te quieres desplazar adelante o atrás, mostrando en cada caso el nombre de la web.
Las palabras "adelante", "atras" desencadenan esta acción, el resto se interpreta como
el nombre de una nueva web.
- Utilizando la implementación de cola y cadenas de texto, simula el mecanismo de una
impresora compartida que recibe documentos y los imprime cuando así se le indica.
La palabra "imprimir" imprime un elemento de la cola, el resto de palabras se
interpretan como nombres de documentos.

by adra-dev.
"""


"""
Pilas:
    Una estructura de tipo pila es una lista en la que los elementos
    se añaden al final y se sacan del final; es decir, extraemos 
    siempre el elemento añadido más recientemente. A este tipo de 
    estructuras támbien se les denomina stack o LIFO (Last In, First
    Out).
"""

# Este codigo simula la accion de deshacer

# inicializamos la pila
acciones = [] 

# guardamos las acciones del usuario
acciones.append("escribir: 'h'")
acciones.append("escribir: 'o'")
acciones.append("escribir: 'y'")
acciones.append("negrita: 'hoy'")

# mostramos el contenido
print(acciones)

# deshacemos el ultimo cambio y ponemos en cursiva
print("sacamos:", acciones.pop())
acciones.append("cursiva: 'hoy'")

# mostramos estado final de la pila
print(acciones)


"""
Colas:
    Una cola es una lista en la que los elementos llegan por un lado 
    y salen por otro. Támbien se les denomina FIFO (First In, First
    Out), pues el primero elemento en llegar es el primero en salir.
"""

# Este codigo simula una cola de clientes en el supermercado

from collections import deque

# Iniciamos la cola
cola = deque()

# llegan 5 clientes a la cola 
for i in range(5):
    cliente = 'cliente ' + str(i+1)
    print('Llega', cliente)
    cola.append(cliente)
    print('Cola:', cola)


# salen todos los clientes de la cola 
while len(cola) > 0:
    print('Sale', cola.popleft())
    print('Qedan:', cola)


"""
Extra
"""


def web_browser():
    """
    En esta version del navegador, se asume que no se puede usar la 
    funcion forward sin antes haber utilizado la funcion backwards
    """
    
    pages = []

    last_page = ""

    def url():
       link = input("Introduce una pagina web: ")
       pages.append(link)
       print(f"Rdirigiendote a {link}") 
    

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

        print("")
        print("1. Navegar")
        print("2. Adelante")
        print("3. Atras")
        print("4. Historial")
        print("5. Salir")

        status = input("Que opcion deseas realizar?: ")

        match status:

            case "1":
                url()
            case "2":
                forward()
            case "3": 
                last_page = backwards()
            case "4": 
                print(pages)
            case "5":
                print("Cerrando del navegador.")
                break
            case _:
                print("Opcion no valida. Elige una opcion del 1 al 5")


web_browser()    


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
       
       print("")
       print("1. Enviar")
       print("2. Imprimir")
       print("3. Salir")
       
       status = input("Que opcion deseas realizar?: ")
       
       match status:

        case "1":
            send()
        case "2":
            if len(queue ) == 0:
                print("No hay documentos que imprimir.")
            else:
                printing()
        case "3":
            print("Cerrando la impresorsa.")
            break
        case _:
            print("Opcion no valida. Elige una opcion del 1 al 3")

printer()