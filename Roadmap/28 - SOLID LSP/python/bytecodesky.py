#28 SOLID: PRINCIPIO DE SUSTITUCIÓN DE LISKOV (LSP)

#  * EJERCICIO:
#  * Explora el "Principio SOLID de Sustitución de Liskov (Liskov Substitution Principle, LSP)" 
#  * y crea un ejemplo simple donde se muestre su funcionamiento
#  * de forma correcta e incorrecta.

#El principio LSP establece que los objetos de un programa deben ser reemplazables por instancias de sus subtipos sin alterar la corrección del programa.
#En otras palabras, si S es un subtipo de T, entonces los objetos de tipo T en un programa pueden ser reemplazados por objetos de tipo S sin alterar el comportamiento del programa.


# Ejemplo de código que viola el principio LSP:

class Bird :
    def __init__(self, name):
        self.name = name

    def fly(self):
        print(f"{self.name} is flying")

class Ostrich(Bird):
    def fly(self):
        raise Exception("Ostriches can't fly")
    
def make_bird_fly(bird):
    bird.fly()

bird = Bird("Bird")
ostrich = Ostrich("Ostrich")

make_bird_fly(bird)
make_bird_fly(ostrich)
#En este ejemplo, el método fly() de la clase Ostrich viola el principio LSP, ya que el método fly() de la clase Bird lanza una excepción en lugar de volar.
#Por lo tanto, el objeto de tipo Ostrich no puede reemplazar al objeto de tipo Bird sin alterar el comportamiento del programa.

# Ejemplo de código que cumple con el principio LSP:

class Bird:
    def __init__(self, name):
        self.name = name

    def fly(self):
        print(f"{self.name} is flying")

class Ostrich:
    def __init__(self, name):
        self.name = name

    def fly(self):
        print(f"{self.name} can't fly")

def make_bird_fly(bird):
    bird.fly()

bird = Bird("Bird")
ostrich = Ostrich("Ostrich")

make_bird_fly(bird)
make_bird_fly(ostrich)
#En este ejemplo, el método fly() de la clase Ostrich no viola el principio LSP, ya que el método fly() de la clase Ostrich simplemente imprime que el avestruz no puede volar.
#Por lo tanto, el objeto de tipo Ostrich puede reemplazar al objeto de tipo Bird sin alterar el comportamiento del programa.

#  * DIFICULTAD EXTRA (opcional):
#  * Crea una jerarquía de vehículos. Todos ellos deben poder acelerar y frenar, así como
#  * cumplir el LSP.
#  * Instrucciones:
#  * 1. Crea la clase Vehículo.
#  * 2. Añade tres subclases de Vehículo.
#  * 3. Implementa las operaciones "acelerar" y "frenar" como corresponda.
#  * 4. Desarrolla un código que compruebe que se cumple el LSP.

class Vehicle:
    def __init__(self, name):
        self.name = name

    def accelerate(self):
        raise NotImplementedError

    def brake(self):
        raise NotImplementedError
    
class Car(Vehicle):
    def accelerate(self):
        print(f"{self.name} is accelerating")

    def brake(self):
        print(f"{self.name} is braking")

class Bicycle(Vehicle):
    def accelerate(self):
        print(f"{self.name} is pedaling faster")

    def brake(self):
        print(f"{self.name} is braking")

class Plane(Vehicle):
    def accelerate(self):
        print(f"{self.name} is taking off")

    def brake(self):
        print(f"{self.name} is landing")

def operate_vehicle(vehicle):
    vehicle.accelerate()
    vehicle.brake()

car = Car("Car")
bicycle = Bicycle("Bicycle")
plane = Plane("Plane")

operate_vehicle(car)
operate_vehicle(bicycle)
operate_vehicle(plane)

#En este ejemplo, la clase Vehicle define los métodos accelerate() y brake() como métodos abstractos que deben ser implementados por las subclases. Las clases Car, Bicycle y Plane implementan estos métodos de acuerdo con el comportamiento esperado de cada vehículo. Por lo tanto, el principio LSP se cumple en este caso, ya que los objetos de las subclases pueden reemplazar a los objetos de la superclase sin alterar el comportamiento del programa.