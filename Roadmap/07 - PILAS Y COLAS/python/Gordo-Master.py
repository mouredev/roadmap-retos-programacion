"""
Pilas y Colas
"""


### Pilas / Stack (LIFO) ###

pila = list()


# Push

pila.append("python")
pila.append("C++")
pila.append("C#")
pila.append("PHP")
pila.append("Java")

print(pila)


# Pop

pila_item = pila[len(pila)-1]
print(pila_item)
del pila[len(pila)-1]
print(pila)

print(pila.pop())
print(pila)


### Cola / Queue (FIFO) ###

cola = list()


# enqueue

cola.append("Casa")
cola.append("Casita")
cola.append("Rancho")
cola.append("Palacio")

print(cola)


# dequeue

cola_item = cola[0]
print(cola_item)
del cola[0]
print(cola)

print(cola.pop(0))
print(cola)


# Metodo con deque de collections, mas optimo

from collections import deque

cola2 = deque()

cola2.append("Agua")
cola2.append("Fuego")
cola2.append("Tierra")
cola2.append("Aire")

print(cola2)
print(cola2.popleft())
print(cola2)
print(cola2.popleft())
print(cola2)



"""
Ejercicio Extra
"""


def navigator():
    historial = []
    historial_ad = []
    while True:
        action = input(
            "Coloca una url o elige una de las opciónes: adelante/atrás/salir: "
        ).lower()
        if action == "adelante":
            if len(historial_ad) > 0:
                historial.append(historial_ad.pop())
        elif action == "atrás":
            if len(historial) > 0:
                historial_ad.append(historial.pop())
        elif action == "salir":
            print("Saliendo del programa...")
            break
        else: 
            historial.append(action)
            historial_ad = []

        if len(historial) > 0:
            print(f"Pagina web actual: {historial[-1]}")
        else:
            print("Panel de inicio de navegación")


navigator()



def impresora(action: str ="", cola: list = []):
    
    while True:
        action = input(
            "Ingrese 'imprimir', el nombre del documento o 'salir': "
        )
        if action == "imprimir":
            if len(cola) > 0:
                print(f"Imprimiendo documento: {cola.pop(0)}....")
        elif action == "salir":
            print("Saliendo del programa...")
            break
        else :
            cola.append(action)
            print(f"Documento: {action} agregado a la cola")
        
        if len(cola) > 0:
            print(f"Cola de impresión: {cola}")
        else:
            print("No hay documentos en cola...")


impresora()