# USO CORRECTO
class Shape:
    def area(self):
        pass

class Rectangulo:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height
    
class Cuadrado(Rectangulo):
    def __init__(self, side):
        super().__init__(side, side)

def print_area(shape: Shape):
    print(f"Area: {shape.area()}")


rectangulo = Rectangulo(5, 10)
cuadrado = Cuadrado(10)

print_area(rectangulo)
print_area(cuadrado)


# USO INCORRECTO
class Square(Rectangulo):
    def __init__(self, width, height):
        if width != height:
            raise ValueError("Un cuadrado debe tener lados iguales.")
        super().__init__(width, height)

# Uso incorrecto del principio LSP
def print_area(shape: Shape):
    print(f"Área: {shape.area()}")

rectangle = Rectangulo(5, 10)
square = Square(7, 7)

print_area(rectangle)
print_area(square)

"""
El principio LSP establece que la subclase debe poder reemplazar a la superclase sin cambiar 
el comportamiento esperado del programa. En este caso, la subclase Square está introduciendo 
una restricción adicional que podría causar problemas en el código que espera que Square se 
comporte como un Rectangulo.
"""

"""
EXTRA
"""
class Vehiculo:
    def acelerar(self):
        raise NotImplementedError("Este método debe ser implementado por la subclase.")

    def frenar(self):
        raise NotImplementedError("Este método debe ser implementado por la subclase.")

class Coche(Vehiculo):
    def __init__(self, velocidad):
        self.velocidad = velocidad

    def acelerar(self):
        self.velocidad += 10
        return self.velocidad

    def frenar(self):
        self.velocidad -= 10
        return self.velocidad

class Bicicleta(Vehiculo):
    def __init__(self, velocidad):
        self.velocidad = velocidad

    def acelerar(self):
        self.velocidad += 2
        return self.velocidad

    def frenar(self):
        self.velocidad -= 2
        return self.velocidad

class Avion(Vehiculo):
    def __init__(self, velocidad):
        self.velocidad = velocidad

    def acelerar(self):
        self.velocidad += 50
        return self.velocidad

    def frenar(self):
        self.velocidad -= 50
        return self.velocidad


def test_vehiculo(vehiculo: Vehiculo):
    print(f"Velocidad inicial: {vehiculo.velocidad}")
    vehiculo.acelerar()
    print(f"Después de acelerar: {vehiculo.velocidad}")
    vehiculo.frenar()
    print(f"Después de frenar: {vehiculo.velocidad}")

# Crear instancias de cada tipo de vehículo
coche = Coche(50)
bicicleta = Bicicleta(10)
avion = Avion(200)

# Probar con diferentes vehículos
print("Coche")
test_vehiculo(coche) # Coche debe cumplir con el comportamiento esperado
print("Bicicleta")
test_vehiculo(bicicleta) # Bicicleta debe cumplir con el comportamiento esperado
print("Avion")
test_vehiculo(avion) # Avion debe cumplir con el comportamiento esperado
