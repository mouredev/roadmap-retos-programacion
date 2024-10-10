"""
EJERCICIO:
 Explora el "Principio SOLID de Sustitución de Liskov (Liskov Substitution Principle, LSP)"
 y crea un ejemplo simple donde se muestre su funcionamiento
 de forma correcta e incorrecta.

 DIFICULTAD EXTRA (opcional):
 Crea una jerarquía de vehículos. Todos ellos deben poder acelerar y frenar, así como
 cumplir el LSP.
 Instrucciones:
 1. Crea la clase Vehículo.
 2. Añade tres subclases de Vehículo.
 3. Implementa las operaciones "acelerar" y "frenar" como corresponda.
 4. Desarrolla un código que compruebe que se cumple el LSP.
"""
from abc import ABC, abstractmethod
from typing import final

print(f"{'#' * 47}")
print(f"##  Explicación  {'#' * 30}")
print(f"{'#' * 47}")

print(r"""
Para entender fácilmente los 5 ppios SOLID recomiendo leer:

    https://blog.damavis.com/los-principios-solid-ilustrados-en-ejemplos-sencillos-de-python/

en donde se explican de manera ordenada uno por uno, de manera sencilla y ejemplificada de manera progresiva (de hecho, de ahí
voy a tomar el ejemplo).

El tercero de los ppios SOLID es el "Liskov Sustitution Principle" (Barbara Jane Liskov) establece que toda clase base debe poder
substituirse por instancias de sus subclases.

Retomando el caso anterior, podríamos hacer que la clase "Duck" herede de una clase base Bird, por lo tanto, luego podríamos ampliar
a una clase Crow:

    from abc import ABC, abstractmethod
    from typing import final
    
    
    class Bird(ABC):
    
        def __init__(self, name):
            self.name = name
    
        @abstractmethod
        def fly(self):
            pass
    
        @abstractmethod
        def swim(self):
            pass
    
        @abstractmethod
        def do_sound(self) -> str:
            pass
    
    
    class Crow(Bird):
    
        def fly(self):
            print(f"{self.name} is flying high and fast!")
    
        def swim(self):
            raise NotImplementedError("Crows don't swim!")
    
        def do_sound(self) -> str:
            return "Caw"
    
    
    class Duck(Bird):
    
        def fly(self):
            print(f"{self.name} is flying not very high")
    
        def swim(self):
            print(f"{self.name} swims in the lake and quacks")
    
        def do_sound(self) -> str:
            return "Quack"
 
Ahora bien, la clase Conversation depende de la clase "Duck", por lo tanto sería incapaz de aceptar a la clase "Crow". Para ello
la clase Conversation debiera recibir a la clase "Bird" en lugar de "Duck":
  
    class AbstractConversation:
    
        def do_conversation(self) -> list:
            pass
    
    
    class Conversation(AbstractConversation):
    
        def __init__(self, bird1: Bird, bird2: Bird):
            self.bird1 = bird1
            self.bird2 = bird2
    
        def do_conversation(self) -> list:
            sentence1 = f"{self.bird1.name}: {self.bird1.do_sound()}, hello {self.bird2.name}"
            sentence2 = f"{self.bird2.name}: {self.bird2.do_sound()}, hello {self.bird1.name}"
            return [sentence1, sentence2]
    
    
    class Communicator:
    
        def __init__(self, channel):
            self.channel = channel
    
        @final
        def communicate(self, conversation: AbstractConversation):
            print(*conversation.do_conversation(), sep = '\n')

De esta manera Bird puede ser sustituida por cualquiera de sus subclase (Duck o Crow).

    lucas = Duck("Lucas")
    saturnino = Duck("Saturnino")
    channel = Communicator(Conversation(lucas, saturnino))
    channel.communicate(channel.channel)
    
    dandy = Crow("Dandy")
    gordo = Crow("Gordo")
    channel = Communicator(Conversation(dandy, gordo))
    channel.communicate(channel.channel)
    
    Lucas: Quack, hello Saturnino
    Saturnino: Quack, hello Lucas
    
    Dandy: Caw, hello Gordo
    Gordo: Caw, hello Dandy
""")

print(f"{'#' * 52}")
print(f"##  Dificultad Extra  {'#' * 30}")
print(f"{'#' * 52}\n")


class Vehicle(ABC):

    def __init__(self, vehicle_type: str):
        self.vehicle_type = vehicle_type

    @abstractmethod
    def accelerate(self, degree: int):
        pass

    @abstractmethod
    def stop(self, degree: int):
        pass


class Sedan(Vehicle):

    def __init__(self):
        super().__init__("Sedan")
        self.doors = 4
        self.max_velocity = 180
        self.current_velocity = 0

    def accelerate(self, degree: int):
        if degree < 0:
            degree = 0
        elif degree >= self.max_velocity:
            degree = self.max_velocity

        self.current_velocity = degree
        return self.current_velocity if self.current_velocity <= self.max_velocity else self.max_velocity

    def stop(self, degree: int):
        if degree < 0:
            degree = 0
        elif degree > self.current_velocity:
            degree = self.current_velocity

        self.current_velocity = degree
        return self.current_velocity


class PickUp(Vehicle):

    def __init__(self, cabin: int):
        super().__init__("PickUp")
        if cabin in (1, 2):
            self.cabin = cabin
            self.doors = 2 * cabin
        else:
            raise ValueError("Cabin mut be 1 (single) or 2 (double")
        self.max_velocity = 150
        self.current_velocity = 0

    def accelerate(self, degree: int):
        if degree < 0:
            degree = 0
        elif degree >= self.max_velocity:
            degree = self.max_velocity

        self.current_velocity = degree
        return self.current_velocity if self.current_velocity <= self.max_velocity else self.max_velocity

    def stop(self, degree: int):
        if degree < 0:
            degree = 0
        elif degree > self.current_velocity:
            degree = self.current_velocity

        self.current_velocity = degree
        return self.current_velocity


class Coupe(Vehicle):

    def __init__(self, roof: str):
        super().__init__("Coupe")
        self.roof = roof
        self.doors = 2
        self.max_velocity = 250
        self.current_velocity = 0

    def accelerate(self, degree: int):
        if degree < 0:
            degree = 0
        elif degree >= self.max_velocity:
            degree = self.max_velocity

        self.current_velocity = degree
        return self.current_velocity if self.current_velocity <= self.max_velocity else self.max_velocity

    def stop(self, degree: int):
        if degree < 0:
            degree = 0
        elif degree > self.current_velocity:
            degree = self.current_velocity

        self.current_velocity = degree
        return self.current_velocity


class AbstractMovement:

    def move(self, degree: int):
        pass


class VehicleMovement(AbstractMovement):

    def __init__(self, vehicle: Vehicle):
        self.vehicle = vehicle

    def move(self, degree: int):
        if degree < 0:
            velocity = self.vehicle.stop(abs(degree))
        else:
            velocity = self.vehicle.accelerate(degree)
        return velocity


class MoveVehicle:

    def __init__(self, control):
        self.control = control

    @final
    def move(self, movement: AbstractMovement, degree: int = 0):
        print(movement.move(degree))


a3 = Sedan()
control_a3 = MoveVehicle(VehicleMovement(a3))
print(f"Acelero A3 {control_a3.control.move(100)}")
print(f"Acelero A3 {control_a3.control.move(120)}")
print(f"Desacelero A3 {control_a3.control.move(-80)}")
print(f"Acelero A3 {control_a3.control.move(250)}")
print(f"Descelero A3 {control_a3.control.move(-30)}")

hilux = PickUp(2)
control_hilux = MoveVehicle(VehicleMovement(hilux))
print(f"\nAcelero Hilux {control_hilux.control.move(100)}")
print(f"Acelero Hilux {control_hilux.control.move(220)}")
print(f"Desacelero Hilux {control_hilux.control.move(-100)}")
print(f"Acelero Hilux {control_hilux.control.move(250)}")
print(f"Descelero Hilux {control_hilux.control.move(0)}")

fuego = Coupe("sliding")
control_fuego = MoveVehicle(VehicleMovement(fuego))
print(f"\nAcelero Fuego {control_fuego.control.move(100)}")
print(f"Acelero Fuego {control_fuego.control.move(220)}")
print(f"Desacelero Fuego {control_fuego.control.move(150)}")
print(f"Acelero Fuego {control_fuego.control.move(250)}")
print(f"Descelero Fuego {control_fuego.control.move(0)}")
