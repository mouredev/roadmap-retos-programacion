from abc import ABC, abstractmethod

# Correcto

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return 3.14 * self.radius * self.radius

class Square(Shape):
    def __init__(self, side):
        self.side = side
    
    def area(self):
        return self.side * self.side
    
class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height
    
    def area(self):
        return 0.5 * self.base * self.height

class AreaCalculator:
    def calculate_area(self, shape: Shape):
        return shape.area()

shapes = [Circle(2), Square(3), Triangle(4, 5)]
calculator = AreaCalculator()
for shape in shapes:
    print(calculator.calculate_area(shape))

    
# Incorrecto

class Circle:
    def __init__(self, radius):
        self.radius = radius

class Square:
    def __init__(self, side):
        self.side = side

class AreaCalculator:
    def calculate_area(self, shape):
        if isinstance(shape, Circle):
            return 3.14 * shape.radius * shape.radius
        elif isinstance(shape, Square):
            return shape.side * shape.side
        # Si queremos agregar una nueva forma, necesitamos modificar esta clase.


### Ejercicio Extra ###

class Operation(ABC):
    @abstractmethod
    def execute(self, a, b):
        pass

class Addition(Operation):
    def execute(self, a, b):
        return a + b
    
class Subtraction(Operation):
    def execute(self, a, b):
        return a - b
    
class Multiplication(Operation):
    def execute(self, a, b):
        return a * b
    
class Division(Operation):
    def execute(self, a, b):
        return a / b
    
class Power(Operation):
    def execute(self, a, b):
        return a ** b
    
class Calculator:
    def __init__(self):
        self.operations = {}
    
    def add_operation(self, name, operation):
        self.operations[name] = operation

    def execute_operation(self, name, a, b):
        if name not in self.operations:
            raise ValueError(f"Operation {name} Not Found")
        return self.operations[name].execute(a, b)

addition = Addition()
subtraction = Subtraction()
multiplication = Multiplication()
division = Division()
power = Power()
calculator = Calculator()

calculator.add_operation("add", addition)
calculator.add_operation("subtract", subtraction)
calculator.add_operation("multiply", multiplication)
calculator.add_operation("divide", division)
calculator.add_operation("power", power)

print(calculator.execute_operation("add", 5, 3))        
print(calculator.execute_operation("subtract", 5, 3))   
print(calculator.execute_operation("multiply", 5, 3))   
print(calculator.execute_operation("divide", 5, 3))     
print(calculator.execute_operation("power", 4, 2))     
