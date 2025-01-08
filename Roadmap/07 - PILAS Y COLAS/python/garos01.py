# Implementación de una pila (stack) utilizando una lista
def crear_pila():
    return []


def pila_esta_vacia(pila):
    return len(pila) == 0


def apilar(pila, elemento):
    pila.append(elemento)


def desapilar(pila):
    if not pila_esta_vacia(pila):
        return pila.pop()
    else:
        print("La pila está vacía.")


# Implementación de una cola (queue) utilizando una lista
def crear_cola():
    return []


def cola_esta_vacia(cola):
    return len(cola) == 0


def encolar(cola, elemento):
    cola.insert(0, elemento)


def desencolar(cola):
    if not cola_esta_vacia(cola):
        return cola.pop()
    else:
        print("La cola está vacía.")


# Ejemplo de uso
pila = crear_pila()
apilar(pila, 1)
apilar(pila, 2)
apilar(pila, 3)

print("Elementos de la pila:")
while not pila_esta_vacia(pila):
    print(desapilar(pila))

cola = crear_cola()
encolar(cola, 1)
encolar(cola, 2)
encolar(cola, 3)

print("\nElementos de la cola:")
while not cola_esta_vacia(cola):
    print(desencolar(cola))


# Ejercicio extra

from collections import deque


def simular_impresora():
    cola_documentos = deque()

    while True:
        comando = input("Ingrese un comando ('imprimir' o el nombre de un documento): ")

        if comando == "imprimir":
            if cola_documentos:
                documento_a_imprimir = cola_documentos.popleft()
                print(f"Imprimir documento: {documento_a_imprimir}")
            else:
                print("No hay documentos para imprimir.")
        else:
            cola_documentos.append(comando)
            print(f"Añadir documento a la cola: {comando}")


simular_impresora()
