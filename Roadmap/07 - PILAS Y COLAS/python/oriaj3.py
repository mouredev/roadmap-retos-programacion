"""	
06 - PILAS Y COLAS	
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

"""	
 * EJERCICIO:	
 * Entiende el concepto de recursividad creando una función recursiva que imprima	
 * números del 100 al 0.	
"""	
"""
EJERCICIO:
Implementa los mecanismos de introducción y recuperación de elementos propios de las
pilas (stacks - LIFO) y las colas (queue - FIFO) utilizando una estructura de array
o lista (dependiendo de las posibilidades de tu lenguaje).
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

#Implementación de colas sin clases con array
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

