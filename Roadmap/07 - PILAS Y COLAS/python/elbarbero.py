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
 *   Las palabras "adelante", "atrás" desencadenan esta acción, el resto se interpreta como
 *   el nombre de una nueva web.
 * - Utilizando la implementación de cola y cadenas de texto, simula el mecanismo de una
 *   impresora compartida que recibe documentos y los imprime cuando así se le indica.
 *   La palabra "imprimir" imprime un elemento de la cola, el resto de palabras se
 *   interpretan como nombres de documentos.
 """

from collections import deque

def navigationWeb():
    webs = ["https://es.wikipedia.org/wiki/Wikipedia:Portada", "https://es.wikipedia.org/wiki/Gran_Premio_de_Abu_Dabi", "https://es.wikipedia.org/wiki/Lewis_Hamilton", "https://es.wikipedia.org/wiki/Fernando_Alonso", "https://es.wikipedia.org/wiki/Asturias"]
    index = len(webs)-1
    print(f"Estás en la web {webs[index]}")
    action = input("Introduce acción: ")
    if action.lower() == "adelante":
        index += 1
    elif action.lower() == "atras":
        index -= 1
    else:
        print("Comando incorrecto")
        
    if index > 0 and index <= len(webs)-1:
        new_url = webs[index]
        print(f"Estás en la web {new_url}")
    else:
        print("Has llegado al limite")

def printer():
    docs = deque(["mi_Doc.docx", "mi_Doc_FINAL.docx", "mi_Doc_ELBUENO.docx", "mi_Doc_BUENO_FINAL.pdf"])
    action = input("Introduce acción: ")
    if action.lower() == "imprimir":
        print(f"Estás imprimiendo el documento {docs.popleft()}")
    else:
        print("Comando incorrecto")

if __name__ == "__main__":

    # LIFO
    stack = [5, 6, 14, 52]
    stack.append(9)
    print(f"LIFO in list {stack}-> {stack.pop()}")

    # FIFO
    queue = deque([5, 6, 14, 52])
    queue.append(9)
    print(f"FIFO in list {queue} -> {queue.popleft()}")
    
    # Navegador web
    navigationWeb()
        
    # Impresion documentos
    printer()

