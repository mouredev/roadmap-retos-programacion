### PILAS Y COLAS ###
# Implementa los mecanismos de introducción y recuperación de elementos propios de las
# pilas (stacks - LIFO) y las colas (queue - FIFO) utilizando una estructura de lista.

# PILAS - LIFO #

pila_list = ["Mario", "Olga", "Ana"]

# introduce un elemento al final de la pila
pila_list.append("Harold") 
print(pila_list)

# elimina el último elemento introducido y lo guarda en una variable
eliminado_pila = pila_list.pop()
print(eliminado_pila)

# PILAS USANDO EL MÓDULO COLLETIONS
from collections import deque # Módulo para manejar Pilas y Colas

pila = deque() # define la pila

# Agregar elementos a la pila
pila.append("ESDLA") 
pila.append("Harry Poter")
pila.append("La Torre Oscura")
pila.append("El Guardian Entre El Centeno")

eliminado = pila.pop() # Elimina el ultimo elemento en ser agregado y lo guarda en una variable

print(f"\"{eliminado}\" ha sido eliminado de la pila.")
print(pila)

# COLAS - FIFO #

cola_list = []

# Agregar elementos a la cola
cola_list.append(10)
cola_list.append(20)
cola_list.append(30)
cola_list.append(40)
print(cola_list)

# elimina el primer elemento introducido y lo guarda en una variable
eliminado_cola = cola_list.pop(0)

print(f"{eliminado_cola} ha sido eliminado de la cola")
print(cola_list)

# COLAS USANDO EL MÓDULO COLLETIONS

cola = deque() # define la cola

# Introducir elementos a la cola con el Método deque()
cola.append(10)
cola.append(20)
cola.append(30)
cola.append(40)
print(cola)

# Eliminar elemento y guardarlo en una variable
eliminado_cola = cola.popleft()
print(f"{eliminado_cola} fue eliminado de la cola")
print(cola)

### EXTRA ###
# Utilizando la implementación de pila y cadenas de texto, simula el mecanismo adelante/atrás
# de un navegador web. Crea un programa en el que puedas navegar a una página o indicarle
# que te quieres desplazar adelante o atrás, mostrando en cada caso el nombre de la web.
# Las palabras "adelante", "atrás" desencadenan esta acción, el resto se interpreta como
# el nombre de una nueva web.

web_pila = []
aux_pila = []
permanecer = True
menu = '''\nElije una opción:
# [i]ntroducir web
# [a]trás
# a[d]elante
# [s]alir
-> '''

def web():
    direccion = input("https://")
    web_pila.append(direccion)

def atras():
    if len(web_pila) < 1:
        pass
    else:
        borrado = web_pila.pop()
        aux_pila.append(borrado)

def adelante():
    if len(aux_pila) < 1:
        pass
    else:
        borrado = aux_pila.pop()
        web_pila.append(borrado)

while permanecer:
    opcion = input(menu)
    match opcion:
        case "i":
            web()
        case "a":
            atras()
        case "d":
            adelante()
        case "s":
            permanecer = False
        case _:
            print("Elije un opción valida")
    if len(web_pila) > 0:
        print(f"Estas en: {web_pila[-1]}")

print("Saliendo...")

'''Utilizando la implementación de cola y cadenas de texto, simula el mecanismo de una
 impresora compartida que recibe documentos y los imprime cuando así se le indica.
 La palabra "imprimir" imprime un elemento de la cola, el resto de palabras se
 interpretan como nombres de documentos.'''

cola_impresion = []
continuo = True

def entrada_doc(documento):
    cola_impresion.append(documento)
    print(f"El documento \"{documento}\" se ha agregado a la cola de impresión")

def imprimir():
    if len(cola_impresion) > 0:
        doc_salida = cola_impresion.pop(0)
        print(f"Se está imprimiendo el documento \"{doc_salida}\"")
    else:
        print("La cola de impresión está vacía.")

while continuo:
    entrada = input("Esperando entrada -> ")

    if entrada == "imprimir":
        imprimir()
    elif entrada == "salir":
        continuo = False
        print("Saliendo...")
    else:
        entrada_doc(entrada)