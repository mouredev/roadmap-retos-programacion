#28 { Retos para Programadores } Principio SOLID de Sustitución de Liskov (Liskov Substitution Principle, LSP) 

# Bibliography reference:
# The Web Development Glossary (Jens Oliver Meiert) (Z-Library)
# I use GPT as a reference and sometimes to correct or generate proper comments.

"""  
 * EJERCICIO:
 * Explora el "Principio SOLID de Sustitución de Liskov (Liskov Substitution Principle, LSP)"
 * y crea un ejemplo simple donde se muestre su funcionamiento
 * de forma correcta e incorrecta.
 *
 * DIFICULTAD EXTRA (opcional):
 * Crea una jerarquía de vehículos. Todos ellos deben poder acelerar y frenar, así como
 * cumplir el LSP.
 * Instrucciones:
 * 1. Crea la clase Vehículo.
 * 2. Añade tres subclases de Vehículo.
 * 3. Implementa las operaciones "acelerar" y "frenar" como corresponda.
 * 4. Desarrolla un código que compruebe que se cumple el LSP.

 """
import time

# Shorthan for print
log = print

# Simulate the loading of the application
def main():
    # Simulate a delay before showing an alert
    time.sleep(2)
    log('Retosparaprogramadores #28.')

# Base class for shapes
class Shape:
    def area(self):
        raise NotImplementedError("Method 'area' must be implemented")

# Rectangle class inheriting from Shape
class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

# Square class inheriting from Shape
class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side * self.side

# Function to calculate the area of a shape
def calculate_area(shape):
    return shape.area()

# Create instances of Rectangle and Square
rectangle = Rectangle(83, 105)
square = Square(40)

# Log the areas of the shapes
log(calculate_area(rectangle))  # 8715
log(calculate_area(square))      # 1600   

# Extra Difficulty Exercise

# Car class definition
class Car:
    def __init__(self, brand, model, max_speed, acceleration, deceleration):
        self.brand = brand
        self.model = model
        self.max_speed = max_speed  # Maximum speed in km/h
        self.acceleration = acceleration  # Acceleration in km/h per second
        self.deceleration = deceleration  # Deceleration in km/h per second
        self.current_speed = 0  # Current speed in km/h

    def accelerate(self, seconds):
        new_speed = self.current_speed + (self.acceleration * seconds)
        self.current_speed = min(new_speed, self.max_speed)
        log(f"{self.brand} {self.model} accelerated to {self.current_speed} km/h.")

    def brake(self, seconds):
        new_speed = self.current_speed - (self.deceleration * seconds)
        self.current_speed = max(new_speed, 0)
        log(f"{self.brand} {self.model} braked to {self.current_speed} km/h.")

# SportsCar class inheriting from Car
class SportsCar(Car):
    def __init__(self, brand, model):
        super().__init__(brand, model, 300, 30, 20)  # Hardcoded values for sports cars

# FamilyCar class inheriting from Car
class FamilyCar(Car):
    def __init__(self, brand, model):
        super().__init__(brand, model, 200, 15, 10)  # Hardcoded values for family cars

# Function to test the car's acceleration and braking
def test_car(car):
    car.accelerate(5) 
    car.brake(2)      

# List of sports cars
sports_cars = [
    {"brand": "Ferrari", "model": "488", "max_speed": 330, "acceleration": 30, "deceleration": 20},
    {"brand": "Porsche", "model": "911 Turbo S", "max_speed": 320, "acceleration": 28, "deceleration": 18},
    {"brand": "Lamborghini", "model": "Huracán", "max_speed": 325, "acceleration": 32, "deceleration": 22}
]

# List of family cars
family_cars = [
    {"brand": "Toyota", "model": "Sienna", "max_speed": 180, "acceleration": 10, "deceleration": 8},
    {"brand": "Honda", "model": "Odyssey", "max_speed": 175, "acceleration": 9, "deceleration": 7},
    {"brand": "Chrysler", "model": "Pacifica", "max_speed": 180, "acceleration": 9, "deceleration": 7}
]

# Create instances of SportsCar and FamilyCar
sports_car = SportsCar(sports_cars[0]['brand'], sports_cars[0]['model'])  # Using the first sports car from the list
family_car = FamilyCar(family_cars[1]['brand'], family_cars[1]['model'])  # Using the second family car from the list

# Test the cars
test_car(sports_car)  # Example output: Ferrari 488 accelerated to 150 km/h.
test_car(family_car)  # Example output: Honda Odyssey accelerated to 75 km/h.

# Call the main function to simulate the loading of the application
if __name__ == "__main__":
    main()

# Output:
"""  
Ferrari 488 accelerated to 150 km/h.
Ferrari 488 braked to 110 km/h.
Honda Odyssey accelerated to 75 km/h.
Honda Odyssey braked to 55 km/h.
Retosparaprogramadores #28.

"""