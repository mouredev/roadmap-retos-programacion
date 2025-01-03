from enum import Enum

#  * EJERCICIO:
#  * Explora el "Principio SOLID Abierto-Cerrado (Open-Close Principle, OCP)" 
#  * y crea un ejemplo simple donde se muestre su funcionamiento
#  * de forma correcta e incorrecta.


"""
# -------------------------------
# | OPEN-CLOSE PRINCIPLE (OCP)  |  Información extraída de -> https://devexpert.io/principios-solid-guia-gratis/ 
# -------------------------------


OPEN-CLOSE PRINCIPLE (OCP) 
Este prinicipio indica que una entidad de software debe estar abierta para extension pero cerrada para modificaciones.

la forma de llegar a esto está muy relacionada con el principio SRP, aunque decir que se cumple el principio OPEN-CLOSE no 
necesariamente determinará que se cumpla el SRP y viceversa.

El principio OPEN-CLOSE generalmente se resuelve utilizando HERENCIA/POLIMORFISMO. en vez de obligar a la clase principal a saber
cómo realizar una operación, delega esta a los objetos que utiliza, de tal forma que no necesita saber explícitamente cómo
llevarla a cabo. Estos objetos tendrán una interfaz común que implementarán de forma específica segun sus requerimientos.

¿CÓMO DETECTAR QUE ESTAMOS VIOLANDO EL PRINCIPIO OPEN/CLOSED?

R. una de las formas más sencillas para detectarlo es darnos cuenta de qué clases modificamos a menudo. Si cada vez que hay
un nuevo requisito o una modificación de los existentes, las mismas clases se ven afectadas, podemos empezar a entender que se
está violando este principio.

"""

#  -------------------------- INICIO FUNCIONAMIENTO INCORRECTO DEL OCP --------------------------

"""
En este ejemplo existe la clase Vehicle, la cual puede representar un vehículo de tipo CAR o de tipo MOTORBIKE.
Imagina que hay una clase con un metodo que se encarga de dibujar un vehiculo por pantalla, por supuesto cada vehiculo
tiene su forma de ser pintado.

"""

print("------------ FUNCIONAMIENTO INCORRECTO OCP ------------")

class VehicleType(Enum):
    CAR = 1
    MOTORBIKE = 2

class Vehicle:
    def __init__(self, vehicleType: VehicleType) -> None:
        self.type = vehicleType
        
class VehiclePrinter:
    
    @staticmethod
    def draw(vehicle: Vehicle):
        if vehicle.type == VehicleType.CAR:
            VehiclePrinter.draw_car(vehicle)
        elif vehicle.type == VehicleType.MOTORBIKE:
            VehiclePrinter.draw_motorbike(vehicle)
    
    @staticmethod
    def draw_car(vehicle: Vehicle):
        print("Drawing a car")
    
    @staticmethod
    def draw_motorbike(vehicle: Vehicle):
        print("Drawing a motorbike")
    

car_bmw = Vehicle(VehicleType.CAR)
motorbike_ninja = Vehicle(VehicleType.MOTORBIKE)

VehiclePrinter.draw(car_bmw)
VehiclePrinter.draw(motorbike_ninja)


"""
Mientras no se necesiten pintar otros tipos de vehiculos ni veamos que la secuencia de 
"if vehicle.type == VehicleType.CAR / MOTORBIKE" se repita mucho en el codigo, esto deberia estar bien, pero:

¿QUE PASA SI SE NECESITA AGREGAR UN NUEVO TIPO DE VEHICULO? Y LUEGO OTRO, Y OTRO Y OTRO.. 

si esto ocurre, el metodo draw crecerá cada vez que se registre un nuevo tipo de vehiculo y a la vez, 
se deberá crear un nuevo metodo para que dicho tipo de vehiculo sea pintado: ejemplo - draw_truck() - draw_airplane(), etc... 

esto implica:
- Un nuevo enumerado
- nuevo case o ifs anidados
- nuevo metodo para pintar el nuevo tipo de vehiculo

En este caso seria buena idea aplicar el principio OPEN/CLOSED
"""
#  -------------------------- INICIO FUNCIONAMIENTO CORRECTO DEL OCP --------------------------
print("------------ FUNCIONAMIENTO CORRECTO OCP ------------")

"""
Solucion:
- Crear una interface Vehicle que contenga el metodo draw (que luego se definirá en la clase concreta)
- las clases concretas representaran al tipo de vehiculo (Car,Truck,Motorbike,etc)
- el metodo estatico draw_vehicle de VehiclePrinter recibe cualquier vehiculo identificandolo por su interface Vehicle.

cada vez que se cree un nuevo tipo de vehiculo, debe implementar la interface Vehicle e sobreescribir el metodo draw.
el metodo estatico draw_vehicle de VehiclePrinter recibe un objeto vehicle: Vehicle que llama a su metodo draw.

esto cumple el principio OPEN-CLOSED ya que si se ingresa un nuevo tipo de vehiculo solo debe implementar la interface 
Vehicle y hacer un override al metodo. no se modifica ninguna otra clase, a diferencia del ejemplo anterior.
"""

from abc import ABC, abstractmethod

class Vehicle(ABC):
    
    @abstractmethod
    def draw(self):
        pass 
    
class Car(Vehicle):
    
    def draw(self):
        print("Drawing car")
    
class MotorBike(Vehicle):
    
    def draw(self):
        print("Drawing motorbike")
        
class Truck(Vehicle):
    
    def draw(self):
        print("Drawing truck")
        
        
class VehiclePrinter():
    
    @staticmethod
    def draw_vehicle(vehicle: Vehicle):
        vehicle.draw()


truck = Truck()
car = Car()
motorbike = MotorBike()

VehiclePrinter.draw_vehicle(truck)
VehiclePrinter.draw_vehicle(car)
VehiclePrinter.draw_vehicle(motorbike)

#  *
#  * DIFICULTAD EXTRA (opcional):
#  * Desarrolla una calculadora que necesita realizar diversas operaciones matemáticas. 
#  * Requisitos:
#  * - Debes diseñar un sistema que permita agregar nuevas operaciones utilizando el OCP.
#  * Instrucciones:
#  * 1. Implementa las operaciones de suma, resta, multiplicación y división.
#  * 2. Comprueba que el sistema funciona.
#  * 3. Agrega una quinta operación para calcular potencias.
#  * 4. Comprueba que se cumple el OCP.

print("------------- DIFICULTAD EXTRA ----------------")
    
class Operation(ABC):
    
    @abstractmethod
    def execute(a,b):
        pass

    
class Calculator:
    
    def __init__(self) -> None:
        self.operations = {}
    
    def add_operation(self, name: str ,operation: Operation):
        self.operations[name] = operation
        
    def calculate(self, operation_name,a,b):
        if operation_name not in self.operations:
            raise ValueError(f"La operación {operation_name} no está soportada.")
        return self.operations[operation_name].execute(a, b)
        

class Addition(Operation):
    def execute(self, a, b):
        return a + b

class Substraction(Operation):
    def execute(self, a, b):
        return a - b

class Multiplication(Operation):
    def execute(self, a, b):
        return a * b
    
    
calculator = Calculator()
calculator.add_operation("addition", Addition())
calculator.add_operation("substraction", Substraction())
calculator.add_operation("multiplication", Multiplication())

print(calculator.calculate("addition",2,5))         # 7
print(calculator.calculate("substraction",2,5))     # -3
print(calculator.calculate("multiplication",2,5))   # 10