"""
 * EJERCICIO:
 * Explora el "Principio SOLID Abierto-Cerrado (Open-Close Principle, OCP)" 
 * y crea un ejemplo simple donde se muestre su funcionamiento
 * de forma correcta e incorrecta.
"""

# NO cumple OCP
# Si quiero ampliar otro tipo de cliente, debo modificar toda la clase.
class CalculadoraDescuentos:
    def calcular(self, tipo_cliente, monto):
        if tipo_cliente == "regular":
            return monto * 0.95
        elif tipo_cliente == "vip":
            return monto * 0.90
        elif tipo_cliente == "super_vip":
            return monto * 0.85
        else:
            return monto
        
discount = CalculadoraDescuentos()
monto = 18
cliente = "super_vip"
print(f"Calculado descuento: Monto total: {monto} - Tipo cliente: {cliente} - Total tras descuento: {discount.calcular(cliente, monto)}")


# Cumpliendo OCP

from abc import ABC, abstractmethod #Modulo que contiene clases, metodos y decoradores para crear clases abstractas
                                    #Estas sirven para crear como un contrato o interfaz y decirle a las subclases que deben
                                    #tener un metodo calcular

class EstrategiaDescuento(ABC): # Defino la clase como abstracta. No se puden crear instancias de ellas directamente, deben ser heredadas.
    @abstractmethod             # Indico que este metodo es abstracto y que debe ser implementado en las sublases.
    def calcular(self, monto):
        pass

class DescuentoRegular(EstrategiaDescuento): # Estrategis de descuento. Si quiero añadir blackFriday añado otra clase sin modificar nada.
    def calcular(self, monto):
        return monto * 0.95
    
class DescuentoVip(EstrategiaDescuento):
    def calcular(self, monto):
        return monto * 0.90
    
class DescuentoSuperVip(EstrategiaDescuento):
    def calcular(self, monto):
        return monto * 0.85
    
class CalculadoraDescuentos: # Clase calculadora que recibe una estrategia y llama al metodo calcular de esa estrategia.
    def __init__(self, estrategia: EstrategiaDescuento):
        self.estrategia = estrategia

    def calcular(self, monto): # No sabe a que esta llamando simplemente llama al metodo de la estrategia guardada.
        return self.estrategia.calcular(monto)
    
cliente_regular = DescuentoRegular()
cliente_vip = DescuentoVip()
cliente_super_vip = DescuentoSuperVip()

calculadora = CalculadoraDescuentos(cliente_regular)
print(f"Descuento regular: {calculadora.calcular(100)}")
calculadora = CalculadoraDescuentos(cliente_vip)
print(f"Descuento vip: {calculadora.calcular(100)}")
calculadora = CalculadoraDescuentos(cliente_super_vip)
print(f"Descuento super vip: {calculadora.calcular(100)}")


"""
 * DIFICULTAD EXTRA (opcional):
 * Desarrolla una calculadora que necesita realizar diversas operaciones matemáticas. 
 * Requisitos:
 * - Debes diseñar un sistema que permita agregar nuevas operaciones utilizando el OCP.
 * Instrucciones:
 * 1. Implementa las operaciones de suma, resta, multiplicación y división.
 * 2. Comprueba que el sistema funciona.
 * 3. Agrega una quinta operación para calcular potencias.
 * 4. Comprueba que se cumple el OCP.
"""
class Operation(ABC):
    @abstractmethod
    def calculate(self, *args):
        pass

class Addition(Operation):
    def calculate(self, *args):
        number_1, number_2 = args
        return number_1 + number_2
class Substraction(Operation):
    def calculate(self, *args):
        number_1, number_2 = args
        return number_1 - number_2
    
class Multiplication(Operation):
    def calculate(self, *args):
        number_1, number_2 = args
        return number_1 * number_2
    
class Division(Operation):
    def calculate(self, *args):
        number_1, number_2 = args
        return number_1 / number_2
    
class Exponentiation(Operation):
    def calculate(self, *args):
        number_1, number_2 = args
        return number_1 ** number_2
    
class Calculator:
    def __init__(self, operation: Operation):
        self.operation = operation

    def calculate(self, *args):
        return self.operation.calculate(*args)
    
add = Addition()
sub = Substraction()
mul = Multiplication()
div = Division()
exp = Exponentiation()

num1 = 6
num2 = 3
calculator = Calculator(add)
print(f"{num1} + {num2} = {calculator.calculate(num1, num2)}")
calculator = Calculator(sub)
print(f"{num1} - {num2} = {calculator.calculate(num1, num2)}")
calculator = Calculator(mul)
print(f"{num1} * {num2} = {calculator.calculate(num1, num2)}")
calculator = Calculator(div)
print(f"{num1} / {num2} = {calculator.calculate(num1, num2)}")
calculator = Calculator(exp)
print(f"{num1} ** {num2} = {calculator.calculate(num1, num2)}")