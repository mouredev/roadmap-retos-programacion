#  * EJERCICIO:
#  * Explora el concepto de clase y crea un ejemplo que implemente un inicializador,
#  * atributos y una función que los imprima (teniendo en cuenta las posibilidades
#  * de tu lenguaje).
#  * Una vez implementada, créala, establece sus parámetros, modifícalos e imprímelos
#  * utilizando su función.


class Programador:
    def __init__(self, nombre: str, lenguaje: list):
        self.nombre = nombre
        self.lenguaje = lenguaje

    def imprimir_info(self):
        print(f"Programador: {self.nombre}, Lenguaje: {self.lenguaje}")
    
    def __str__(self):
        return f"Programador: {self.nombre}, Lenguaje: {self.lenguaje}"


cristianfloyd = Programador("Cristian Floyd", ["Python"])
cristianfloyd.imprimir_info()
print(cristianfloyd)

cristianfloyd.lenguaje.append("JavaScript")
cristianfloyd.imprimir_info()
print(cristianfloyd)

cristianfloyd.nombre = "C. Floyd"
cristianfloyd.imprimir_info()

#  * DIFICULTAD EXTRA (opcional):
#  * Implementa dos clases que representen las estructuras de Pila y Cola (estudiadas
#  * en el ejercicio número 7 de la ruta de estudio)
#  * - Deben poder inicializarse y disponer de operaciones para añadir, eliminar,
#  *   retornar el número de elementos e imprimir todo su contenido.


class Pila:
    def __init__(self, elementos=[]) -> None:
        self.elementos = elementos

    def push(self, elemento) -> None:
        """Añade un elemento a la pila."""
        self.elementos.append(elemento)

    def pop(self):
        """Elimina y retorna el último elemento de la pila."""
        if self.count() == 0:
            return None
        return self.elementos.pop()

    def count(self) -> int:
        return len(self.elementos)

    def imprimir(self) -> None:
        print(f"Pila: {self.elementos}")

    def mostrar(self) -> None:
        for elemento in reversed(self.elementos):
            print(elemento)

    def __len__(self) -> int:
        return self.count()


pila = Pila()
pila.push("A")
pila.push("B")
pila.push("C")
pila.imprimir()
print(f"Cantidad de elementos en la pila: {pila.count()}")
pila.pop()
pila.imprimir()

print(len(pila))


class Cola:
    def __init__(self, elementos=[]) -> None:
        self.elementos = elementos

    def enqueue(self, elemento) -> None:
        """Añade un elemento a la cola."""
        self.elementos.append(elemento)

    def dequeue(self):
        """Elimina y retorna el primer elemento de la cola."""
        if self.count() == 0:
            return None
        return self.elementos.pop(0)

    def count(self) -> int:
        return len(self.elementos)

    def imprimir(self) -> None:
        print(f"Cola: {self.elementos}")

    def mostrar(self) -> None:
        for elemento in self.elementos:
            print(elemento)

    def __len__(self) -> int:
        return self.count()

cola = Cola([1, 2, 3])
cola.imprimir()
cola.enqueue(4)
cola.imprimir()
print(f"Cantidad de elementos en la cola: {cola.count()}")
cola.dequeue()
cola.imprimir()
print(len(cola))