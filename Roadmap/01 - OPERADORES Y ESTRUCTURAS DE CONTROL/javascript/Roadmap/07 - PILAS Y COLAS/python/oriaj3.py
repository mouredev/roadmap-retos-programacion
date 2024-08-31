"""	
07 - PILAS Y COLAS	
Autor de la solución: Oriaj3	
Teoría:	
Las pilas y las colas son estructuras de datos que permiten almacenar y recuperar elementos.

Las pilas (stacks) son estructuras de datos que siguen el principio LIFO (Last In, First Out), es decir, 
el último elemento que se introduce es el primero en salir. Las pilas se utilizan en multitud de aplicaciones, 
como la gestión de llamadas a funciones, la evaluación de expresiones matemáticas, la gestión de memoria, etc.

Las colas (queues) son estructuras de datos que siguen el principio FIFO (First In, First Out), es decir,
el primer elemento que se introduce es el primero en salir. Las colas se utilizan en multitud de aplicaciones,
como la gestión de tareas, la gestión de recursos compartidos, la impresión de documentos, etc.
"""	

# EJERCICIO BÁSICO:
"""
EJERCICIO:
Implementa los mecanismos de introducción y recuperación de elementos propios de las
pilas (stacks - LIFO) y las colas (queue - FIFO) utilizando una estructura de array
o lista (dependiendo de las posibilidades de tu lenguaje).
"""

# Implementación de pilas sin usar clases con listas 
lista = []
tope_lista = 0    
def l_apilar(elemento: int):
    global lista, tope_lista
    lista.append(elemento)
    tope_lista = len(lista)

def l_desapilar()-> int:
    global lista, tope_lista
    if lista_is_vacia() == False:
        tope_lista -= 1
        return lista.pop()
    else:
        return None
    
def l_mostrar_pila():
    global lista, tope_lista
    print(lista)

def lista_is_vacia()-> bool:
    global lista, tope_lista
    return tope_lista == 0


#Prueba, mete 10 elementos en la pila, los muestra y los saca y los muestra
for i in range(10):
    l_apilar(i)

l_mostrar_pila()

for i in range(5):
    print(l_desapilar())

l_mostrar_pila()

#Implementación de colas sin clases con listas
cola = []

def l_encolar(numero: int):
    global cola
    cola.append(numero)
    
def l_is_vacia():
    global cola
    return len(cola) == 0

def l_desencolar() -> int:
    global cola
    if(l_is_vacia() == False):
        return cola.pop(0)
    else:
        return None
    
def mostrar_cola():   
    global cola
    print(cola)

#Prueba, mete 10 elementos en la cola, los muestra y los saca y los muestra
    
for i in range(10):
    l_encolar(i)

mostrar_cola()

for i in range(5):
    print(l_desencolar())

mostrar_cola()


# EJERCICIO EXTRA NAVEGADOR WEB
"""
- Utilizando la implementación de pila y cadenas de texto, simula el mecanismo adelante/atrás
de un navegador web. Crea un programa en el que puedas navegar a una página o indicarle
que te quieres desplazar adelante o atrás, mostrando en cada caso el nombre de la web.
Las palabras "adelante", "atras" desencadenan esta acción, el resto se interpreta como
el nombre de una nueva web.
"""

#Al ser una pila, cuando se añade un elemento se añade al final, y cuando se saca se saca del final
def     w_new(elemento: str)-> str:
    global lista_web
    lista_web.append(elemento)
    return str(elemento)
    
def w_atras()-> str:
    global lista_web
    aux = lista_web.pop()
    if len(lista_web) > 0:
        lista_web.insert(0, aux)
        #Devuelve el último elemento de la lista
        return lista_web[-1]
    else:
        return "No hay más webs"

def w_siguiente()-> str:
    global lista_web
    if len(lista_web) > 0:
        #copia el primer elemento de la lista
        aux = lista_web.pop(0)
        lista_web.append(aux)
        actual = lista_web[-1]
        return actual
    else:
        return "No hay más webs" 

lista_web = ["www.google.com", "www.youtube.com", "www.facebook.com"]
#Instrucciones
print("Introduce una web o 'salir' para terminar, 'atras' para retroceder y 'adelante' para avanzar en el historial de navegación.")

while True:
    print(f"Historial de navegación:")
    for url in lista_web:
        print(url, end=" - ")
    
    print()
    print()

    web = input("Introduce una web: ")
    if (web == "atras"):
        print(f"Has navegado a {w_atras()}")
    elif (web == "adelante"):
        print(f"Has navegado a {w_siguiente()}")
    elif (web.startswith("www.")):
        print(f"Has navegado a {w_new(web)}")
    elif (web == "salir"):
        break
    else:
        print("No es una web válida")


# EJERCICIO EXTRA IMPRESORA
"""
- Utilizando la implementación de cola y cadenas de texto, simula el mecanismo de una
impresora compartida que recibe documentos y los imprime cuando así se le indica.
La palabra "imprimir" imprime un elemento de la cola, el resto de palabras se
interpretan como nombres de documentos.
"""

#Al ser una cola, cuando se añade un elemento se añade al final, y cuando se saca se saca del principio
lista_impresion = ["Documento1", "Documento2", "Documento3", "Documento4", "Documento5"]

def imprimir()-> str:
    print(f"Imprimiendo {lista_impresion.pop(0)}")

def nuevo_documento(nombre: str)-> str:
    lista_impresion.append(nombre)
    return nombre

print("Introduce un documento o 'salir' para terminar, 'imprimir' para imprimir un documento.")

while True:
    print(f"Documentos en la cola de impresión:")
    for doc in lista_impresion:
        print(doc, end=" - ")
    
    print()
    print()

    doc = input("Introduce un documento: ")
    if (doc == "imprimir"):
        imprimir()
    elif (doc == "salir"):
        break
    else:
        print(f"Has añadido el documento {nuevo_documento(doc)}")
