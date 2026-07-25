#### SOLID PRINCIPIO ABIERTO-CERRADO (OCP)

'''
Este principio establece que las clases deben estar abiertas para la extensión, pero cerradas para la modificación.

En otras palabras, puedes agregar nuevas funcionalidades a una clase sin modificar su código existente. 
Esto ayuda a evitar errores inesperados en el código ya probado y a facilitar la escalabilidad.
'''

'''
Ventajas:

Protege el código existente
Facilita la extensión
Favorece el diseño modular
'''

# Ejemplo que inclumple OCP

#class CalculadoraArea():
#    def calcular_area(self, forma):
#        if forma.lower() == "circulo":
#            radio = float(input("Introduce el radio de la circunferencia: "))
#            return 3.14 * (radio ** 2)
#        elif forma.lower() == "cuadrado":
#            lado = float(input("Introduce longitud de lado: "))
#            return lado ** 2
#
#print(CalculadoraArea().calcular_area("Circulo"))
#print(CalculadoraArea().calcular_area("cuadrado"))

# Fin Ejemplo que inclumple OCP

# Podemos usar polimorfismo para cumplir con el OCP, creando una clase base o interfaz que permita 
# a las formas geométricas implementar su propio método de cálculo de área.

from abc import ABC, abstractmethod

# Clase abstracta para formas geométricas
#class Forma(ABC):
#    @abstractmethod
#    def calcular_area(self):
#        pass
#
## Implementaciones específicas de formas
#class Circulo(Forma):
#    def __init__(self, radius):
#        self.radius = radius
#        
#    def calcular_area(self):
#        return 3.14 * (self.radius ** 2)
#
#class Cuadrado(Forma):
#    def __init__(self, side):
#        self.side = side
#    
#    def calcular_area(self):
#        return self.side ** 2
#
## Prueba
#formas = [
#    Circulo(5),
#    Cuadrado(4)
#]
#
#for forma in formas:
#    print(forma.calcular_area())  # Output: 78.5, 16

class Calculadora(ABC):
    
    @abstractmethod
    def calcular(self):
        pass

class Suma(Calculadora):
    
    def calcular(self, a, b):
        return a + b

class Resta(Calculadora):
    def calcular(self, a, b):
        return a - b

class Multiplicacion(Calculadora):
    def calcular(self, a, b):
        return a * b

class Division(Calculadora):
    def calcular(self, a, b):
        if b == 0:
            raise ValueError("No se puede dividir por cero")
        return a / b

# Para añadir una quinta operación es sencillo creando un nuevo método abstracto y su correspondiente clase
class Potencia2(Calculadora):
    def calcular(self, a):
        return a ** 2

# Pruebas de calculadora
a = 560
b = 12

operaciones = [
    Suma(),
    Resta(),
    Multiplicacion(),
    Division(),
    Potencia2()
]

for operacion in operaciones:
    if isinstance(operacion, Suma):
        print(f"La suma de {a} y {b} es: {operacion.calcular(a, b)}")
    elif isinstance(operacion, Resta):
        print(f"La resta de {a} y {b} es: {operacion.calcular(a,b)}")
    elif isinstance(operacion, Multiplicacion):
        print(f"La multiplicación de {a} y {b} es: {operacion.calcular(a,b)}")
    elif isinstance(operacion, Division):
        print(f"La división de {a} y {b} es: {operacion.calcular(a,b)}")
    else:
        print(f"El cuadrado de {a} es: {operacion.calcular(a)}")
#
#suma = Suma()
#print(suma.calcular(a, b))
#
#resta = Resta()
#print(resta.calcular(a, b))
#
#multiplicacion = Multiplicacion()
#print(multiplicacion.calcular(a, b))
#
#division = Division()
#print(division.calcular(a, b))
#
#potencia2 = Potencia2()
#print(potencia2.calcular(a))

#### FIN SOLID PRINCIPIO ABIERTO-CERRADO (OCP)