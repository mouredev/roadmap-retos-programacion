""" /*
 * EJERCICIO:
 * Implementa los mecanismos de introducción y recuperación de elementos propios de las
 * pilas (stacks - LIFO) y las colas (queue - FIFO) utilizando una estructura de array
 * o lista (dependiendo de las posibilidades de tu lenguaje).
 *

 */"""
 
""" Stacks - LIFO """
stack = []
# Insert element (end)
stack.append(1)
stack.append(2)
stack.append(3)
stack.append(4)
print(f'Stack: {stack}')

# Remove element (last)
stack.pop()
stack.pop()
print(f'Stack: {stack}')

""" Queues - FIFO """
queue = []
# Insert element (first)
queue.insert(0,1)
queue.insert(0,2)
queue.insert(0,3)
print(f'Queue: {queue}')

# Remove element(last)
queue.pop()
queue.pop()
print(f'Queue: {queue}')

""" * DIFICULTAD EXTRA (opcional):
 * - Utilizando la implementación de pila y cadenas de texto, simula el mecanismo adelante/atrás
 *   de un navegador web. Crea un programa en el que puedas navegar a una página o indicarle
 *   que te quieres desplazar adelante o atrás, mostrando en cada caso el nombre de la web.
 *   Las palabras "adelante", "atras" desencadenan esta acción, el resto se interpreta como
 *   el nombre de una nueva web.
 * - Utilizando la implementación de cola y cadenas de texto, simula el mecanismo de una
 *   impresora compartida que recibe documentos y los imprime cuando así se le indica.
 *   La palabra "imprimir" imprime un elemento de la cola, el resto de palabras se
 *   interpretan como nombres de documentos.
"""
def website():
    page = []
    history = []
    print(f'''
    Ingrese donde desea desplazarse:
    * nueva web
    * adelante
    * atras
    * salir
    ''')
    option = input()
    while option != 'salir':
        if option == "adelante":
            if len(history) != 0:
                page.append(history[0])
                print(f"Ahora se encuentra en la pagina {history.pop(0)}")
            else:
                print("Ya se encuentra en la ultima pagina visitada")
        elif option == 'atras':
            if len(page) == 0:
                print("Error. Se encuentra en la primer pagina del sitio web")
            else:
                print(f"Se encuentra en la pagina: {history.append(page.pop())}")
        elif option == 'nueva web':
            web = input("Ingrese nombre nueva pagina web: ")
            page.append(web)
        print(f'''
        Ingrese donde desea desplazarse:
        * nueva web
        * adelante
        * atras
        * salir
        ''')
        option = input()

def printer():
    queue = []
    option = input("Ingrese 'imprimir' si desea imprimir un documento, de lo contrario, indique nuevo documento para agregar a la cola de impresion. Si desea salir del programa indique 'salir': ")

    while option != 'salir':
        if option == 'imprimir':
            if len(queue) == 0:
                print("No hay documentos en la cola de impresion")
            else:
                printer = queue.pop()
                print(f"Se imprimio el documento {printer}")
        else:
            queue.insert(0,option)
            print(f"Se agrega el documento {option} a la cola de impresion")
        option = input("Ingrese 'imprimir' si desea imprimir un documento, de lo contrario, indique nuevo documento para agregar a la cola de impresion. Si desea salir del programa indique 'salir': ")
website()
printer()
    