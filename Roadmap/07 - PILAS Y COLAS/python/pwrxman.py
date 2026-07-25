"""
 * EJERCICIO:
 * Implementa los mecanismos de introducción y recuperación de elementos propios de las
 * pilas (stacks - LIFO) y las colas (queue - FIFO) utilizando una estructura de array
 * o lista (dependiendo de las posibilidades de tu lenguaje).
 *
"""

# # PILAS  (STACKS)  LIFO

# agregar elemento a la pila o la cola
# def addelem(elem: str, stack: list):
#      print("añadir elemento")
#      stack.append(elem)

# # retirar elemento de la pila
# def pop(stack: list):
#     print("retirar elemento de la Pila")
#     if not stackempty(stack):
#         stack.pop()

# # validar si pila o cola vacia
def stackempty(stack: list) -> bool:
    if len(stack) == 0:
        print("Lista Vacia")
        return True
    else:
        return False


# # COLAS (QUEUES) FIFO

# # retirar elemento de la cola
# def dequeue(stack: list):
#     print("retirar elemento de la Cola")
#     if not stackempty(stack):
#         stack.pop(0)

# stack = list()
# queue = list()

# while True:
#     print("PILAS")
#     print("\t1 - Agregar elemento en pila")
#     print("\t2 - Eliminar elemento de pila")
#     print("\t3 - Mostrar pila\n")
#     print("COLAS")
#     print("\t4 - Agregar elemento en cola")
#     print("\t5 - Eliminar elemento de cola")
#     print("\t6 - Mostrar cola\n")
#     print("q - Terminar")

#     action= input("Que desea hacer? ")
#     match action:
#         case '1':
#             element=input("Cual es el elemento que desea añadir a la list? ")
#             addelem(element, stack)
#         case '2':
#             pop(stack)
#         case '3':
#             print(f"Pila -> {stack}")
#         case '4':
#             element=input("Cual es el elemento que desea añadir a la cola? ")
#             addelem(element, queue)
#         case '5':
#             dequeue(queue)
#         case '6': 
#             print(f"Cola -> {queue}")
#         case 'q':
#             print("Hasta la vista...")
#             break


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




# agregar elemento a la pila o la cola
def add_wj(web: str, stack: list):
    print(f"Has añadido un nuevo elemento {web}")
    stack.append(web)

# retirar elemento de la pila
def pop_web(stack: list):
    print("Regresando...")
    if not stackempty(stack):
        print(f"has navegado a la página {stack_web[len(stack_web)-2]}")
        stack.pop()



# COLAS (QUEUES) FIFO

# imprimir elemento de la cola
def job_queue(stack: list):
    print("imprimir job de la Cola")
    if not stackempty(stack):
        stack.pop(0)

stack_web = list()
print_queue = list()

while True:
    print("PILAS")
    print("\t1 - Agregar página web.")
    print("\t2 - Avanzar.?????")
    print("\t3 - Regresar.")
    print("\t4 - Mostrar páginas fr navegación.\n")

    print("COLAS")
    print("\t5 - Agregar job en cola")
    print("\t6 - Imprimir job de la cola")
    print("\t7 - Mostrar cola de impresion\n")
    print("q - Terminar")

    action= input("Que desea hacer? ")
    match action:
        case '1':
            element=input("Cual es la página a la que desea navegar? ")
            add_wj(element, stack_web)
        case '2':
            print("No se puede implementar con listas en python")
        case '3':
            pop_web(stack_web)
        case '4':
            print(f"Páginas -> {stack_web}")
        case '5':
            element=input("Cual es el job de impresión que desea añadir a la cola? ")
            add_wj(element, print_queue)
        case '6':
            job_queue(print_queue)
        case '7': 
            print(f"Cola -> {print_queue}")
        case 'q':
            print("Hasta la vista...")
            break
