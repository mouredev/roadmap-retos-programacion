# @Author Daniel Grande (Mhayhem)

from abc import ABC, abstractmethod

# EJERCICIO:
# Explora el "Principio SOLID de Sustitución de Liskov (Liskov Substitution Principle, LSP)" 
# y crea un ejemplo simple donde se muestre su funcionamiento
# de forma correcta e incorrecta.

class Rectengle:
    def __init__(self, width: float, height: float):
        self.width = width
        self.height = height
    
    def set_width(self, width: float):
        self.width = width
    
    def set_height(self, height: float):
        self.height = height
    
    def area(self) -> float:
        return self.width * self.height

# clase hijo que no cumple el principio Liskov Substitution Principle (LSP)

class Square(Rectengle):
    # el cuadrado todos sus lados son iguales
    def set_width(self, width: float):
        self.width = width
        self.height = width
    
    def set_height(self, height: float):
        self.height = height
        self.width = height
    
def test_area(rectangle: Rectengle):
    rectangle.set_width(6)
    rectangle.set_height(5)
    
    # hacemos un assert para comprobar si cumple o no el LSP
    
    assert rectangle.area() == 30, "El area debe ser 30"


# correcto
class Form(ABC):
    @abstractmethod
    def area(self) -> float:
        pass

class Rectangle(Form):
    def __init__(self, width: float, height: float):
        self.width = width
        self.height = height
    
    def set_width(self, width: float):
        self.width = width 
    
    def set_height(self, height: float):
        self.height = height
    
    def area(self) -> float:
        return self.height * self.width

class Square(Form):
    def __init__(self, side: float):
        self.side = side
    
    def set_side(self, side: float):
        self.side = side
    
    def area(self) -> float:
        return self.side ** 2

def display_area(form: Form):
    return form.area()




# DIFICULTAD EXTRA (opcional):
# Crea una jerarquía de vehículos. Todos ellos deben poder acelerar y frenar, así como
# cumplir el LSP.
# Instrucciones:
# 1. Crea la clase Vehículo.
# 2. Añade tres subclases de Vehículo.
# 3. Implementa las operaciones "acelerar" y "frenar" como corresponda.
# 4. Desarrolla un código que compruebe que se cumple el LSP

class Vehicle(ABC):
    
    def accelerate(self, speed_increment):
        self._current_speed += speed_increment
        
        # the current speed can´t be higher than maximun speed
        if self._current_speed > self.max_speed:
            self._current_speed = self.max_speed
            return f"Velocidad máxima alcanzada, {self._current_speed} km/h."
        return f"Acelerando hasta {self._current_speed} km/h."

    def brake(self, reduce_speed: int):
        self._current_speed -= reduce_speed
        
        # the current speed can´t be a negative value
        if self._current_speed < 0:
            self._current_speed = 0
            return "Se ha detenido por completo."
        return f"Velocidad reducida a {self._current_speed} km/h."

    def get_current_speed(self):
        return f"{self.model}: {self._current_speed} km/h."

    @abstractmethod
    def get_vehicle_info(self):
        pass

class Car(Vehicle):
    def __init__(self, brand: str, model: str, type: str, max_speed: int):
        self.brand = brand.capitalize()
        self.model = model.capitalize()
        self.type = type
        self.max_speed = max_speed
        self._current_speed = 0

    def get_vehicle_info(self):
        return f"Marca {self.brand} - Modelo {self.model} - Segmento {self.type} - Velocidad máxima {self.max_speed} km/h."
    
class Truck(Vehicle):
    def __init__(self, brand: str, model: str, max_speed: int, num_axles: int):
        self.brand = brand
        self.model = model
        self.max_speed = max_speed
        self.num_axles = num_axles
        self._current_speed = 0

    def get_vehicle_info(self):
        return f"Marca {self.brand} - Modelo {self.model} - Numero ejes {self.num_axles} - Velocidad máxima {self.max_speed} km/h."

class Motorcycle(Vehicle):
    def __init__(self, brand: str, model: str, max_speed: int, cubic_centimeters: int):
        self.brand = brand
        self.model = model
        self.max_speed = max_speed
        self.cubic_centimeters = cubic_centimeters
        self._current_speed = 0

    def get_vehicle_info(self):
        return f"Marca {self.brand} - Modelo {self.model} - Cilindrada {self.cubic_centimeters} CC - Velocidad máxima {self.max_speed} km/h."

def test_accelerate(vehicle: Vehicle):
    vehicle._current_speed = 0
    vehicle.accelerate(20)

    assert vehicle._current_speed == 20


def test_brake(vehicle: Vehicle):
    vehicle._current_speed = 100
    vehicle.brake(50)

    assert vehicle._current_speed == 50