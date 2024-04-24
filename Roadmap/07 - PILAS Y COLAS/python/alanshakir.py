"""
/*
 * EJERCICIO:
 * Implementa los mecanismos de introducción y recuperación de elementos propios de las
 * pilas (stacks - LIFO) y las colas (queue - FIFO) utilizando una estructura de array
 * o lista (dependiendo de las posibilidades de tu lenguaje).
 *
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
 */
"""

#Pilas 
my_list = [20, 50, 14, 83, 69, 74]

#my_list.remove(20)
my_list.insert(1, 25)
my_list.pop() #elimina el ultimo de la lista
my_list.append(18) #agrega al final de la lista

#Colas
my_list.append(18) #agrega al final de la lista
my_list.pop(1) #eliminar el elemento de la lista segun el indice
print (my_list)

#Extra
def web_navigation():
    user_stack = []
    while True:
        movimiento_user = input("¿Que movimiento desea realizar:? Seleccione un agregar url, adelante, atras, salir. ")
        if movimiento_user == "agregar":
            agregar_url = input("ingrese la url: ")
            user_stack.append(agregar_url)
            print(user_stack)
        elif movimiento_user == "adelante":
            if len(user_stack) > 0:
                print(user_stack[-1])
        elif movimiento_user == "atras":
            if len(user_stack) > 0:
                user_stack.pop()
                print(user_stack)
        else:
            print("Has salido de programa.!")
            break



web_navigation()
        
def printer():
    user_queue = []
    
    while True: 
        movimiento_user = input("¿Desea agregar documento, imprimir o salir:? ")
        if movimiento_user == "agregar":

            user_queue.append(input("nombre del documento: "))
        elif movimiento_user == "imprimir":
            while len(user_queue) > 0:
                print("Imprimiendo documento: ", user_queue.pop(0))
        else:
            print("Has salido de programa.!")
            break

printer()
