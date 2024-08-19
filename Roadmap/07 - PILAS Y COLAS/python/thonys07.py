'''

EJERCICIO:
 * Implementa los mecanismos de introducción y recuperación de elementos propios de las
 * pilas (stacks - LIFO) y las colas (queue - FIFO) utilizando una estructura de array
 * o lista (dependiendo de las posibilidades de tu lenguaje).
 *



'''
pila = []
def insertar(elemento):
    pila.append(elemento)
    print(pila)
def extraer():
    pila.pop()
    print(pila)
insertar(1)
insertar(2)
insertar(3)
insertar(4)
insertar(5)
extraer()
print(pila)
queue = []
def enqueue(elemento):
    queue.append(elemento)
    print(queue)
def dequeue():
    queue.pop(0)
    print(queue)
enqueue(1)
enqueue(2)
enqueue(3)
enqueue(4)
enqueue(5)
dequeue()
print(queue)

#EXTRAAAAA
"""
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
def navegacion():
    page = ""
    stack=[]
 
    while True:
        navegar = input("Indique la URL a la que desea navegar, adelante, atras o salir: ")
        if navegar == "adelante":
           if len(stack) == 0:
               print("No hay historial adelante")
           else:
               page = stack.pop()
               print(f"Navegando hacia {page}")
        elif navegar == "atras":
            if len(stack)==0:
               print("No hay historial atrás")
            else:
             stack.append(page)
             page = stack.pop()
             print(f"Navegando hacia {page}")          
        elif navegar == "salir":
            break
        else:
            stack.append(page)
            page=navegar
            print(f"Navegando hacia {page}")

def imprimir():
    stack=[]
 
    while True:
        imprimir = input("Indique i para imprimir, s para salir, o el ")
        if imprimir == "i" | "I":
           if len(stack) == 0:
               print("No hay historial para imprimir. ")
           else:
               imprimiendo = stack.pop(0)
               print(f"Imprimiendo: {imprimiendo}")
        elif imprimir == "s" | "S":
            break
            
        else:
            stack.append(imprimir)
        
        print(f"lista de impresion: {stack}")


navegacion()
imprimir()



