"""
 * EJERCICIO:
 * Implementa los mecanismos de introducción y recuperación de elementos propios de las
 * pilas (stacks - LIFO) y las colas (queue - FIFO) utilizando una estructura de array
 * o lista (dependiendo de las posibilidades de tu lenguaje).
"""


# Implementación de una pila (stack):
class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if self.items:
            return self.items.pop()
        else:
            print("Pila vacía, no se puede extraer elementos.")

    def top_element(self):
        if self.items:
            return self.items[-1]
        else:
            print("Pila vacía.")


# Implementación de una cola (queue):
class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if self.items:
            return self.items.pop(0)
        else:
            print("Cola vacía, no se puede extraer elementos.")
            return None

    def front_element(self):
        if self.items:
            return self.items[0]
        else:
            print("Cola vacía.")
            return None


"""
 * DIFICULTAD EXTRA (opcional):
 * - Utilizando la implementación de pila y cadenas de texto, simula el mecanismo adelante/atrás
 *   de un navegador web. Crea un programa en el que puedas navegar a una página o indicarle
 *   que te quieres desplazar adelante o atrás, mostrando en cada caso el nombre de la web.
 *   Las palabras "adelante", "atras" desencadenan esta acción, el resto se interpreta como
 *   el nombre de una nueva web.
"""

class NavegadorWeb:
    def __init__(self):
        self.pila_atras = []  
        self.pila_adelante = []  
        self.pagina_actual = "PÁGINA DE INICIO"

    def visitar_pagina(self, nombre_pagina):
        print(f"Visitando la página: {nombre_pagina}")
        self.pila_atras.append(self.pagina_actual)
        self.pagina_actual = nombre_pagina
        self.pila_adelante = [] 

    def retroceder(self):
        if self.pila_atras:
            pagina_anterior = self.pila_atras.pop()
            self.pila_adelante.append(self.pagina_actual)
            self.pagina_actual = pagina_anterior
            print(f"Retrocediendo a la página: {pagina_anterior}")
        else:
            print("No hay páginas anteriores para retroceder.")

    def avanzar(self):
        if self.pila_adelante:
            pagina_siguiente = self.pila_adelante.pop()
            self.pila_atras.append(self.pagina_actual)
            self.pagina_actual = pagina_siguiente
            print(f"Avanzando a la página: {pagina_siguiente}")
        else:
            print("No hay páginas siguientes para avanzar.")


navegador = NavegadorWeb()
print("Visitando la página: PAGINA DE INICIO")
fin = 0

while fin < 5: # Vamos a dejar que se puedan realizar 5 acciones.

    input_usuario = input("Ingrese una acción (adelante/atras) o el nombre de una página: ").lower()

    if input_usuario == "adelante":
        navegador.avanzar()
        fin += 1
    elif input_usuario == "atras":
        navegador.retroceder()
        fin += 1
    else:
        navegador.visitar_pagina(input_usuario)
        fin += 1


"""
 * - Utilizando la implementación de cola y cadenas de texto, simula el mecanismo de una
 *   impresora compartida que recibe documentos y los imprime cuando así se le indica.
 *   La palabra "imprimir" imprime un elemento de la cola, el resto de palabras se
 *   interpretan como nombres de documentos.
"""


class Impresora:

    def __init__(self):
        self.documentos_cola = []

    def recibir_documento (self, documento):
        self.documentos_cola.append(documento)
        print(f"Se ha añadido el documento {documento} a la cola.")

    def imprimir(self):
        if self.documentos_cola:
            impreso = self.documentos_cola.pop(0)
            print(f"Se ha impreso el documento: {impreso}")
        else:
            print("No hay documentos pendientes por imprimir.")

impresora = Impresora()
fin = 0

while fin < 5: # Vamos a dejar que se puedan realizar 5 acciones.

    input_usuario = input("Ingrese 'imprimir' si desea imprimir, o indique el nombre del documento que quiera imprimir: ").lower()

    if input_usuario == "imprimir":
        impresora.imprimir()
        fin += 1
    else:
        impresora.recibir_documento(input_usuario)
        fin += 1