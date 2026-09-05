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

# PILA

stack: list[str] = []

stack.append("Comer la comida.")
stack.append("Preparar la comida.")
stack.append("Comprar los ingredientes para la comida.")

print("Pendientes actuales: ", stack )

print("Consultar primer pendiente: ", stack[0])
print("Consultar último pendiente agregado: ", stack[-1])

ultimo_pendiente = stack.pop()
print("Realizar: ", ultimo_pendiente)
print("Falta por realizar: ", stack)

ultimo_pendiente = stack.pop()
print("Realizar: ", ultimo_pendiente)
print("Falta por realizar: ", stack)

ultimo_pendiente = stack.pop()
print("Realizar: ", ultimo_pendiente)
print("Falta por realizar: ", stack)
print()

class EditorTexto:
    def __init__(self):
        self.contenido = ""
        self.pila_deshacer = []

    def escribir(self, nuevo_texto):
        self.pila_deshacer.append(self.contenido)
        self.contenido += nuevo_texto

    def deshacer(self):
        if self.pila_deshacer:
            self.contenido = self.pila_deshacer.pop()
        else:
            raise TypeError("No hay acciones por deshacer.")

editor = EditorTexto()
editor.escribir("Hello")
editor.escribir(",")
editor.escribir(" ")
editor.escribir("World")
editor.escribir("!")

print("Contenido: ", editor.contenido)

editor.deshacer()
print("Tras deshacer (Ctrl-Z): ", editor.contenido)

editor.deshacer()
print("Tras deshacer (Ctrl-Z): ", editor.contenido)

editor.escribir("\n")
editor.escribir("Hello, Python!")
print("Contenido: ", editor.contenido); print()

# COLA 
from collections import deque

cola_supermercado = deque()

cola_supermercado.append("Ana")
cola_supermercado.append("Roberto")
cola_supermercado.append("Sofía")

print("Fila de espera: ", list(cola_supermercado))

cliente_atendido = cola_supermercado.popleft()
print(f"Atendiendo a: {cliente_atendido}.")
print(f"Fila restante: ", list(cola_supermercado))
print(f"Siguiente de la fila...")

cliente_atendido = cola_supermercado.popleft()
print(f"Atendiendo a: {cliente_atendido}.")
print(f"Fila restante: ", list(cola_supermercado))
print(f"Siguiente de la fila...")

cliente_atendido = cola_supermercado.popleft()
print(f"Atendiendo a: {cliente_atendido}.")
print(f"Fila restante: ", list(cola_supermercado))
print(f"Siguiente de la fila...")
print()

from collections import deque
import time

class GestorImpresion:
    def __init__(self):
        self.cola_trabajos = deque()

    def enviar_documentos(self, nombre_documento):
        self.cola_trabajos.append(nombre_documento)
        print(f"Trabajo encolado:  '{nombre_documento}'")

    def procesar_siguiente(self):
        if self.cola_trabajos:
            documento = self.cola_trabajos.popleft()
            print("Imprimiendo: '{documento}'...\n¡Listo!")
        else:
            print("No hay trabajos pendientes de impresión.")

impresora = GestorImpresion()
impresora.enviar_documentos("Informe_Financiero.pdf")
impresora.enviar_documentos("Foto_vacaciones.jpg")
impresora.enviar_documentos("Receta.docx")

print(f"\nTrabajos en cola: {len(impresora.cola_trabajos)}")
impresora.procesar_siguiente()
impresora.procesar_siguiente()
impresora.procesar_siguiente()
impresora.procesar_siguiente()

