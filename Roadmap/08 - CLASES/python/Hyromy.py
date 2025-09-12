# definicion de la clase "Car"
class Car:

    # constructor de la clase
    def __init__(self, color, marca, modelo): # self hace referencia a si mismo
        
        # declaracion e inicializacion de atributos
        self.color = color
        self.marca = marca
        self.modelo = modelo

    def imprimir(self): # metodo "imprimir"
        print(f"Soy un {self.marca} modelo {self.modelo} de color {self.color}")

# crear instancias de "Car" (crear objetos "Car")
coche_1 = Car("blanco", "HotWheels", "Terreneitor")
coche_2 = Car("azul", "Transformer", "willy")

# ejecutar el metodo "imprimir" en ambos objetos
coche_1.imprimir()
coche_2.imprimir()

# modificar coche_1
coche_1.color = "naranja"
coche_1.modelo = None

# comprobar cambios
coche_1.imprimir()



"""
 ---- DIFICULTAD EXTRA ----
"""

class Pila:
    def __init__(self, *items):
        self.content = []

        for item in items:
            self.content.append(item)

    def show(self):
        pila = "|"
        
        for value in self.content:
            pila += f"{value}|"

        print(pila)

    def add(self, item):
        self.content.insert(0, item)

    def pop(self):
        if len(self.content) == 0:
            print("No hay elementos por remover")
        else:
            self.content.pop(0)

    def len(self) -> int:
        return len(self.content)

class Cola:
    def __init__(self, *items):
        self.content = []

        for item in items:
            self.content.append(item)

    def show(self):
        cola = "-"
        
        for value in self.content:
            cola += f"{value}-"

        print(cola)

    def add(self, item):
        self.content.append(item)

    def pop(self):
        if len(self.content) == 0:
            print("No hay elementos por remover")
        else:
            self.content.pop(0)

    def len(self) -> int:
        return len(self.content)

pila = Pila("A")
for i in range(5, 10):
    pila.add(i)
pila.show()

pila.pop()
pila.pop()
pila.show()



cola = Cola("B")
for i in range(5, 10):
    cola.add(i)
cola.show()

cola.pop()
cola.pop()
cola.show()

print(cola.len())
cola.pop()
print(cola.len())