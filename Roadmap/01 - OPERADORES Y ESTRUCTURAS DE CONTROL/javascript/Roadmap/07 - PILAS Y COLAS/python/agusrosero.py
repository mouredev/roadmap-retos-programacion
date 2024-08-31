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
 *   Las palabras "adelante", "atras" desencadenan esta acción, el resto se interpreta como
 *   el nombre de una nueva web.
 * - Utilizando la implementación de cola y cadenas de texto, simula el mecanismo de una
 *   impresora compartida que recibe documentos y los imprime cuando así se le indica.
 *   La palabra "imprimir" imprime un elemento de la cola, el resto de palabras se
 *   interpretan como nombres de documentos.
 */
"""
from collections import deque


# PILAS
pila = []

# Agregar un elemento al tope de la pila.


def push(elemento):
    pila.append(elemento)
    return pila


push(1)
push(2)
push(3)
print(pila)

# Eliminar un elemento del tope de la pila.


def eliminar():
    pila.pop()
    return pila


eliminar()
eliminar()
print(pila)

# Mostrar el tope de la pila.


def top():
    return pila[-1]


print(top())

# Mostrar el tamanio de la pila.


def tamanio():
    return len(pila)


print(tamanio())

# COLAS
cola = deque()

# Agregar un elemento al final de la cola.
cola.append(1)
cola.append(2)
cola.append(3)
print(cola)

# Eliminar un elemento del final de la cola.
cola.popleft()
print(cola)

# Mostrar el primer elemento de la cola.
print(cola[0])

# Mostrar el tamanio de la cola.
print(len(cola))

# DIFICULTAD EXTRA:


class NavegadorWeb:
    def __init__(self):
        self.pila_atras = []
        self.pila_adelante = []
        self.pagina_actual = ""

    def navegar(self, direccion):
        if direccion.lower() == "atras" and self.pila_atras:
            self.pila_adelante.append(self.pagina_actual)
            self.pagina_actual = self.pila_atras.pop()
        elif direccion.lower() == "adelante" and self.pila_adelante:
            self.pila_atras.append(self.pagina_actual)
            self.pagina_actual = self.pila_adelante.pop()
        else:
            self.pila_atras.append(self.pagina_actual)
            self.pagina_actual = direccion

    def mostrar_pagina(self):
        print(f'Pagina actual: {self.pagina_actual}')


navegador = NavegadorWeb()
navegador.navegar("www.google.com")
navegador.navegar("www.youtube.com")
navegador.navegar("www.instagram.com")
navegador.navegar("atras")
navegador.mostrar_pagina()
navegador.navegar("adelante")
navegador.mostrar_pagina()


class Impresora:
    def __init__(self):
        self.cola_impresion = deque()

    def agregar_doc(self, doc):
        self.cola_impresion.append(doc)

    def imprimir(self):
        if self.cola_impresion:
            print(f"Imprimiendo: {self.cola_impresion.popleft()}")
        else:
            print("No hay documentos para imprimir")


impresora = Impresora()
impresora.agregar_doc("Documento 1")
impresora.agregar_doc("Documento 2")
impresora.agregar_doc("Documento 3")
impresora.imprimir()
impresora.imprimir()
