"""
* EJERCICIO:
 * Implementa los mecanismos de introducción y recuperación de elementos propios de las
 * pilas (stacks - LIFO) y las colas (queue - FIFO) utilizando una estructura de array
 * o lista (dependiendo de las posibilidades de tu lenguaje).
 *
 * DIFICULTAD EXTRA (opcional):
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

# Pilas/Stacks (LIFO Last In First Out)

stack = []

#Añadir elementos a la pila
stack.append("a")
stack.append("b")
stack.append("c")

print(stack)

#Eliminar el último elemento de la pila
stack_item = stack.pop(len(stack) - 1 )

print(stack_item)
print(stack)


# Cola/Queue (FIFO First In First Out)

queue = []

#Añadir elementos a la cola
queue.append(1)
queue.append(2)
queue.append(3)

print(queue)

#Eliminar el primer elemento de la cola
queue_item = queue.pop(0)

print(queue_item)
print(queue)


#----EXTRA----

#Navegador web con implementación de pila

def web():
    url = ["www.google.es", "www.amazon.es", "www.youtube.es"]

    while True:
        action = input("Añade una URL o navega escribiendo adelante/atrás/salir: ").lower()

        match action:
            case "salir":
                print("Saliendo de la web. Hasta luego.")
                break

            case "adelante":
                web = input("Introduzca la dirección: ")
                url.append(web)
                print(f"Se encuentra en: {web}")

            case "atrás":
                try:
                    elemento = url.pop()
                    print(f"Se encuentra en: {elemento}")
                except IndexError:
                    print("No hay elementos en la lista de URLs.")

            case _:
                url.append(action)
                print(f"Añadida la URL {action}")
                print(url)


web()


#Impresora compartida con implementación de cola

def printer():

    printing_queue= []
    papel = ["hoja 1", "hoja 2", "hoja 3", "hoja 4", "hoja 5"]
    tinta = 100
    
    while True:
        action = input("Escriba imprimir para añadir un documento, o explore las diferentes funciones con cola/estado/papel/tinta/salir: ").lower()
        
        match action:
            
            case "salir":
                print("Saliendo del programa de impresión, hasta pronto.")
                break
            
            case "cola":
                print(printing_queue)
        
            case "estado":
                if papel > 0 and tinta:
                    print("La impresora está lista para la impresión")
                else:
                    if not papel:
                        print("No hay suficiente papel para imprimir. Cargue papel e inténtelo de nuevo.")
                    elif tinta <= 0:
                        print("No hay suficiente tinta para imprimir. Rellene el depósito e inténtelo de nuevo.")
                break
                        
            case "papel":
                print(f"Quedan {len(papel)} hojas disponibles para imprimir.")
            
            case "tinta":
                tinta = len(papel) * 20
                print(f"El nivel de tinta está en {tinta}%.")
            
            case "imprimir":
                try:
                    if len(papel) > 0 and tinta > 0:
                        document = printing_queue.pop(0)
                        papel.pop()
                        print(f"Imprimiendo... {document}")
                    else: 
                        print("No hay suficiente papel o tinta para realizar la impresión.")
                except IndexError:
                    print("La cola de impresión está vacía. Añada documentos con 'imprimir'.")
                    
            case _:
                printing_queue.append(action)
                print(f"Se añadió el documento {action}")
                
printer()


