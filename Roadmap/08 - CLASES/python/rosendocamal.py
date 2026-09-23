"""
 * EJERCICIO:
 * Explora el concepto de clase y crea un ejemplo que implemente un inicializador,
 * atributos y una función que los imprima (teniendo en cuenta las posibilidades
 * de tu lenguaje).
 * Una vez implementada, créala, establece sus parámetros, modifícalos e imprímelos
 * utilizando su función.
 *
 * DIFICULTAD EXTRA (opcional):
 * Implementa dos clases que representen las estructuras de Pila y Cola (estudiadas
 * en el ejercicio número 7 de la ruta de estudio)
 * - Deben poder inicializarse y disponer de operaciones para añadir, eliminar,
 *   retornar el número de elementos e imprimir todo su contenido.
"""

class UnaClase():
    def __init__(self, param: str):
        self.param = param

    def __str__(self):
        return "PARAMETER: %s" % self.param

instance_class: UnaClase = UnaClase("STRING")
print(instance_class)

# EXTRA - PILA
class Stack():
    def __init__(self) -> None:
        self.storage: list[any] = []

    def add(self, item: any) -> None:
        self.storage.append(item)

    def pop(self) -> any:
        item: any = self.storage.pop()
        return item

    def size(self) -> int:
        return len(self.storage)

    def __str__(self) -> str:
        text: str = ""

        last_index: int = self.storage.index(self.storage[-1]) + 1

        num_characters_last_index: int = len(str(last_index))

        for i, v in enumerate(self.storage):
            text += f"[{str(i).zfill(num_characters_last_index)}]" + f"{v}\n"

        return text

historial_navegacion: Stack = Stack()

historial_navegacion.add("The Website 1")
historial_navegacion.add("The Website 2")
historial_navegacion.add("The Website 3")
historial_navegacion.add("The Website 4")
historial_navegacion.add("The Website 5")
historial_navegacion.add("The Website 6")
historial_navegacion.add("The Website 7")
historial_navegacion.add("The Website 8")
historial_navegacion.add("The Website 9")
historial_navegacion.add("The Website 0")
historial_navegacion.add("The Website A")
print("="*10); print(historial_navegacion); print("="*10)

for i in range(0, historial_navegacion.size() - 1):
    pestaña_actual: any = historial_navegacion.pop()
    print("Cerrar pestaña actual:", pestaña_actual)
    print(historial_navegacion); print("Tamaño historial:", historial_navegacion.size())
else:
    print()

# EXTRA - COLA

from collections import deque

class Cola():
    def __init__(self) -> None:
        self.storage: deque = deque()

    def add(self, item: any) -> None:
        self.storage.append(item)

    def pop(self) -> any:
        item: any = self.storage.popleft()
        return item

    def size(self) -> int:
        return len(self.storage)

    def __str__(self) -> str:
        text: str = ""

        last_index: int = self.storage.index(self.storage[-1]) + 1

        num_characters_last_index: int = len(str(last_index))

        for i, v in enumerate(self.storage):
            text += f"[{str(i).zfill(num_characters_last_index)}]" + f"{v}\n"

        return text

impresora: Stack = Stack()
impresora.add("Document 1")
impresora.add("Document 2")
impresora.add("Document 3")
impresora.add("Document 4")
impresora.add("Document 5")
impresora.add("Document 6")
impresora.add("Document 7")
impresora.add("Document 8")
impresora.add("Document 9")
impresora.add("Document 0")
impresora.add("Document A")
print("="*10); print(impresora); print("="*10)

for i in range(0, impresora.size() - 1):
    pestaña_actual: any = impresora.pop()
    print("Imprimiendo:", pestaña_actual)
    print(impresora); print("Impresiones pendientes:", impresora.size())
else:
    print()