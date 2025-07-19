from time import sleep
# EJERCICIO:
# Implementa los mecanismos de introducción y recuperación de elementos propios de las
# pilas (stacks - LIFO) y las colas (queue - FIFO) utilizando una estructura de array
# o lista (dependiendo de las posibilidades de tu lenguaje).

def diswaserh():
    dishes = []
    while len(dishes) < 5:
            dish = input()
            dishes.append(dish)
    print(dishes)
    while len(dishes) >= 5:
        cleaner = dishes.pop()
        print(cleaner)
    print("Todos los platos límpios, pila vacía")
    
def queue():
    queue = []
    while len(queue) < 5:
        action = input()
        queue.append(action)
    print(action)
    while len(queue) > 0:
        action_taken = queue[0]
        print(action_taken)
        sleep(0.2)
        queue.remove(action_taken)
        
    print("Todas las acciónes realizadas, cola vacía")
    
# DIFICULTAD EXTRA (opcional):
# - Utilizando la implementación de pila y cadenas de texto, simula el mecanismo adelante/atrás
#   de un navegador web. Crea un programa en el que puedas navegar a una página o indicarle
#   que te quieres desplazar adelante o atrás, mostrando en cada caso el nombre de la web.
#   Las palabras "adelante", "atrás" desencadenan esta acción, el resto se interpreta como
#   el nombre de una nueva web.

def brave():
   foward_stack = []
   back_stack = []
   current = input("Introduzca una pagina web.\n").strip().lower()
   while True:
       print(f"http://{current}")
       action = input("Nueva pagina o comandos 'adelante' o 'atras': 'X' para cerrar.\n").strip().lower()
       match action:
            case "x":
               break
            case "atras":
               if back_stack:
                   foward_stack.append(current)
                   current = back_stack.pop()
               else:
                   print("No se puede retroceder.")
            case "adelante":
                if foward_stack:
                    back_stack.append(current)
                    actual = foward_stack.pop()
                else:
                    print("No se puede avanzar.")
            case _:
                back_stack.append(current)
                current = action
                foward_stack.clear()

brave()                    

# - Utilizando la implementación de cola y cadenas de texto, simula el mecanismo de una
#   impresora compartida que recibe documentos y los imprime cuando así se le indica.
#   La palabra "imprimir" imprime un elemento de la cola, el resto de palabras se
#   interpretan como nombres de documentos.

def printer():
    queue_print = []
    while True:
        action = input("Quiere 'imprimir' archivo o crear nuevo archivo? pulsar 'X' para cerrar prógrama.\n").strip().lower()
        match action:
            case "imprimir":
                if (len(queue_print)) < 1:    
                    print("No hay archivos que imprimir")
                else:
                    printed = queue_print[0]
                    queue_print.pop(0)
                    print(f"Archivo {printed} Imprimiendose")
            case "x":
                break
            case _:
                queue_print.append(action)
        print(f"Archivos en cola: {len(queue_print)}")

printer()