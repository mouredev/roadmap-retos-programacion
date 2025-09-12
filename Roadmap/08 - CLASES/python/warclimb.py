""" * EJERCICIO:
 * Explora el concepto de clase y crea un ejemplo que implemente un inicializador,
 * atributos y una función que los imprima (teniendo en cuenta las posibilidades
 * de tu lenguaje).
 * Una vez implementada, créala, establece sus parámetros, modifícalos e imprímelos
 * utilizando su función.
"""

class Vehiculo():
    def __init__(self, marca, modelo, año):
        self._marca = marca
        self._modelo = modelo
        self._año = año

    # getters y setters
    @property
    def marca(self):
        return self._marca
    
    @marca.setter
    def marca(self, marca):
        self._marca = marca
    
    @property
    def modelo(self):
        return self._modelo

    @modelo.setter
    def modelo(self, modelo):
        self._modelo = modelo
    
    @property
    def año(self):
        return self._año
    
    @año.setter
    def año(self, año):
        self._año = año

# Creo un vehículo
coche = Vehiculo("Ford", "Fiesta", 2010)

# muestra atributos del coche
print(f"Caracteristicas del vehículo:")
for attr, value in coche.__dict__.items():
    print(f"{value}")

"""
 * DIFICULTAD EXTRA (opcional):
 * Implementa dos clases que representen las estructuras de Pila y Cola (estudiadas
 * en el ejercicio número 7 de la ruta de estudio)
 * - Deben poder inicializarse y disponer de operaciones para añadir, eliminar,
 *   retornar el número de elementos e imprimir todo su contenido."""

class Pila:
    def __init__(self):
        self.items = []

    def esta_vacia(self):
        return self.items == []

    def agregar(self, item):
        self.items.append(item)

    def eliminar(self):
        return self.items.pop()

    def num_elementos(self):
        return len(self.items)

    def imprimir(self):
        print("Elementos en la pila:")
        for item in self.items:
            print(item)

# Ejemplo de uso con cola
class Cola:
    def __init__(self):
        self.items = []

    def esta_vacia(self):
        return self.items == []

    def agregar(self, item):
        self.items.insert(0, item)

    def eliminar(self):
        return self.items.pop()

    def num_elementos(self):
        return len(self.items)

    def imprimir(self):
        print("Elementos en la cola:")
        for item in self.items:
            print(item)


# testeo

if __name__ == "__main__":
    pila = Pila()
    pila.agregar("Queso")
    pila.agregar("Pan")
    pila.agregar("Leche")
    pila.agregar("Huevos")
    pila.imprimir()
    print(f"La pila tiene {pila.num_elementos()} elementos.")
    print(f"Eliminamos el elemento {pila.eliminar()}.")
    print(f"La pila tiene {pila.num_elementos()} elementos.")
    pila.imprimir()

    cola = Cola()
    cola.agregar("Libros")
    cola.agregar("Cuadernos")
    cola.agregar("Lápices")
    cola.agregar("Borradores")
    cola.imprimir()
    print(f"La cola tiene {cola.num_elementos()} elementos.")
    print(f"Eliminamos el elemento {cola.eliminar()}.")
    print(f"La cola tiene {cola.num_elementos()} elementos.")
    cola.imprimir()