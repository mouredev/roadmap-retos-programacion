from abc import ABC, abstractmethod
import math
'''
  EJERCICIO
'''
# Incorrecto 

class Circle:
  
  def __init__(self, radius):
    self.radius = radius

class Rectangle:

  def __init__(self, height, width):
    self.height = height
    self.width = width

class Square:

  def __init__(self, side):
    self.side = side

class AreaCalculator:
  def calculate_area(self, shape):
    if isinstance(shape, Circle):
      return math.pi * shape.radius ** 2
    elif isinstance(shape, Rectangle):
      return shape.height * shape.width

# Correcto

class Shape(ABC):
  @abstractmethod
  def area(self):
    pass

class Circle(Shape):
  def __init__(self, radius):
    self.radius = radius

  def area(self):
    return math.pi * self.radius ** 2
  
class Rectangle(Shape):
  def __init__(self, height, width):
    self.height = height
    self.width = width

  def area(self):
    return self.height * self.width
  
class Square(Shape):
  def __init__(self, side):
    self.side = side

  def area(self):
    return self.side ** 2;

class AreaCalculator:
  def calculateArea(self, shape):
    return shape.area()
  

circle = Circle(7)
rectangle = Rectangle(4, 8)
square = Square(13)

calculator = AreaCalculator()

print(f"Área del círculo: {calculator.calculateArea(circle)}")
print(f"Área del rectangulo: {calculator.calculateArea(rectangle)}")
print(f"Área del cuadrado: {calculator.calculateArea(square)}")


'''
  EXTRA
'''

class Operation(ABC):
  def __init__(self, value_a, value_b):
    self.value_a = value_a
    self.value_b = value_b

  @abstractmethod
  def result(self):
    pass

class Add(Operation):
  def result(self):
    return self.value_a + self.value_b

class Subtract(Operation):
  def result(self):
    return self.value_a - self.value_b
  
class Multiply(Operation):
  def result(self):
    return self.value_a * self.value_b
  
class Divide(Operation):
  def result(self):
    return self.value_a / self.value_b
  
class Calculator:
  def operation(self, operation: Operation):
    return operation.result()
  
add = Add(5, 8)
sub = Subtract(5, 8)
mult = Multiply(5, 8)
divd = Divide(5, 8)

calculator = Calculator()

print(f"La suma, 5 + 8 es: {calculator.operation(add)}")
print(f"La resta, 5 - 8 es: {calculator.operation(sub)}")
print(f"La multiplicación, 5 * 8 es: {calculator.operation(mult)}")
print(f"La división, 5 / 8 es: {calculator.operation(divd)}")

class Exponentiation(Operation):
  def result(self):
    return self.value_a ** self.value_b

exp = Exponentiation(5, 8)
print(f"La potencia, 5 ^ 8 es: {calculator.operation(exp)}")