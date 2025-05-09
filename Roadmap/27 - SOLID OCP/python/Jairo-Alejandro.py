
"""
Principio OCP (Abierto-Cerrado)
Establece que una clase debe estar abierta para su extension pero cerrada a la hora  de modificarla 
"""

# Ejemplo incorrecto

#lectura de sensores 

class ReadSensors():
    def read_sensors(self, sensor_type):
        if sensor_type == 'temperature':
            return self.read_sensors_temperature()
        elif sensor_type == 'humidity':
            return self.read_sensors_humidity()
        # en caso de querer agregar otro sensor se debe modificar esta clase 

    def read_sensors_temperature(self):
        return 'Temperature 25 C '
    
    def read_sensors_humidity(self):
        return 'Humidity 50% '

Read = ReadSensors()

print(Read.read_sensors('temperature'))
print(Read.read_sensors('humidity'))

# Ejemplo correcto 

# clase comun para todos los sensores
class Sensor():
    def read(self):
        pass

class ReadTemperature(Sensor):
    def read(self):
        return 'Temperature 34 C'

class ReadHumidity(Sensor):
    def read(self):
        return 'Humidity 70%'

class ReadSensors():
    def __init__(self, sensor):
        self.sensor = sensor
    
    def read_sensor(self):
        return self.sensor.read()
    
temperature = ReadSensors(ReadTemperature())
print(temperature.read_sensor())

humidity = ReadSensors(ReadHumidity())
print(humidity.read_sensor())

"""Dificultad Extra """
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

# Clase comun para totas las operaciones 
class Operation():
    def execute(self,a,b):
        pass
# Clases con las operaciones
class Addition(Operation):
    def execute(self, a, b):
        return a + b 

class Subtraction(Operation):
    def execute(self, a, b):
        return a - b

class Multiplication(Operation):
    def execute(self, a, b):
        return a*b 

class Division(Operation):
    def execute(self, a, b):
        if b == 0 : 
            raise ValueError("Cannot divide by zero")
        return a / b 

# clases de la interfaz 

class Calculator():
    def __init__(self, operation):
        self.operation = operation
    
    def calculate(self , a , b):
        return self.operation.execute(a,b)

addition = Calculator(Addition())
print(addition.calculate(10, 5))  

subtraction = Calculator(Subtraction())
print(subtraction.calculate(10, 5))  

multiplication = Calculator(Multiplication())
print(multiplication.calculate(10, 5))  

division = Calculator(Division())
print(division.calculate(10, 5))  

#agregando la operacion potencia     
class power(Operation):
    def execute(self, a, b):
        return a**b

power = Calculator(power())
print(power.calculate(2, 2))

