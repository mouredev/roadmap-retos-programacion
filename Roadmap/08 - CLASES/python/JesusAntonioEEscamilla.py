# #08 - Python -> Jesus Antonio Escamilla

"""
EJERCIÓ
"""
# Definición de la clase Persona
class Persona:
    # Inicializador con atributos nombre y edad
    def __init__(self, nombre, edad, ocupacion):
        self.nombre = nombre
        self.edad = edad
        self.ocupacion = ocupacion

    # Método para imprimir los atributos
    def imprimir_informacion(self):
        print(f"Nombre: {self.nombre}, Edad: {self.edad}, Ocupación: {self.ocupacion}")

# Crear una instancia de la clase Persona
persona1 = Persona("Jesus Antonio", 30, "Programador")

print("CLASES")
persona1.imprimir_informacion()



"""
EXTRA
"""
# Ejemplos de CLASES con Pilas y Colas
class Pila:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            return None

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)

    def print_stack(self):
        print(self.items)


class Cola:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)
        else:
            return None

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)

    def print_queue(self):
        print(self.items)


# Ejemplo de uso:
print("\nSTACK")
pila = Pila()
pila.push(1)
pila.push(2)
pila.push(3)
pila.print_stack()
pila.pop()
pila.print_stack()


print("\nQUEUE")
cola = Cola()
cola.enqueue("A")
cola.enqueue("B")
cola.enqueue("C")
cola.print_queue()
cola.dequeue()
cola.print_queue()
