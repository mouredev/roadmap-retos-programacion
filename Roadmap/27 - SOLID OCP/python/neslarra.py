from functools import reduce
from typing import final

"""
 EJERCICIO:
 Explora el "Principio SOLID Abierto-Cerrado (Open-Close Principle, OCP)"
 y crea un ejemplo simple donde se muestre su funcionamiento
 de forma correcta e incorrecta.

 DIFICULTAD EXTRA (opcional):
 Desarrolla una calculadora que necesita realizar diversas operaciones matemáticas.
 Requisitos:
 - Debes diseñar un sistema que permita agregar nuevas operaciones utilizando el OCP.
 Instrucciones:
 1. Implementa las operaciones de suma, resta, multiplicación y división.
 2. Comprueba que el sistema funciona.
 3. Agrega una quinta operación para calcular potencias.
 4. Comprueba que se cumple el OCP.
"""

print(f"{'#' * 47}")
print(f"##  Explicación  {'#' * 30}")
print(f"{'#' * 47}")

print(r"""
Para entender fácilmente los 5 ppios SOLID recomiendo leer:

    https://blog.damavis.com/los-principios-solid-ilustrados-en-ejemplos-sencillos-de-python/

en donde se explican de manera ordenada uno por uno, de manera sencilla y ejemplificada de manera progresiva (de hecho, de ahí
voy a tomar el ejemplo).

El segundo de los ppios SOLID es "Open Close Principle" el cual establece que las clases deberían estar abiertas para su extensión
pero cerradas para su modificación.

Retomando el caso anterior, tenemos la clase Communicator: 

    class Communicator:
    
        def __init__(self, channel):
            self.channel = channel
    
        def communicate(self, duck1 : Duck, duck2: Duck):
            sentence1 = f"{duck1.name}: {duck1.do_sound()}, hello {duck2.name}"
            sentence2 = f"{duck2.name}: {duck2.do_sound()}, hello {duck1.name}"
            conversation = [sentence1, sentence2]
            print(*conversation,
                  f"(via {self.channel})",
                  sep = '\n')

En esta clase No se puede extender la funcionalidad de Communicator para añadir diferentes tipos de conversaciones sin modificar 
el método communicate(). Para cumplir con el segundo principio, se crea una clase AbstractConversation que se encargará de definir 
diferentes tipos de conversaciones en sus subclases con implementaciones de do_conversation(). De esta manera, el método communicate() 
de Communicator solo se regirá a llevar a cabo la comunicación a través de una canal y nunca se requerirá de su modificación (es un método final).

from typing import final


    class Duck:
    
        def __init__(self, name):
            self.name = name
    
        def fly(self):
            print(f"{self.name} is flying not very high")
    
        def swim(self):
            print(f"{self.name} swims in the lake and quacks")
    
        @staticmethod
        def do_sound() -> str:
            return "Quack"
    
    
    class AbstractConversation:
    
        def do_conversation(self) -> list:
            pass
    
    
    class DuckConversation(AbstractConversation):
    
        def __init__(self, duck1: Duck, duck2: Duck):
            self.duck1 = duck1
            self.duck2 = duck2
    
        def do_conversation(self) -> list:
            sentence1 = f"{self.duck1.name}: {self.duck1.do_sound()}, hello {self.duck2.name}"
            sentence2 = f"{self.duck2.name}: {self.duck2.do_sound()}, hello {self.duck1.name}"
            return [sentence1, sentence2]
    
    
    class Communicator:
    
        def __init__(self, channel):
            self.channel = channel
    
        @final
        def communicate(self, conversation: AbstractConversation):
            print(*conversation.do_conversation(), sep="\n")
    
    
    lucas = Duck("Lucas")
    donald = Duck("Donald")
    comm = Communicator(DuckConversation(lucas, donald))
    
    comm.communicate(comm.channel)
    
    scooby = Dog("Scooby")
    pluto = Dog("Pluto")
    comm = Communicator(DogConversation(scooby, pluto))
    
    comm.communicate(comm.channel)

lucas = Duck("Lucas")
donald = Duck("Donald")
comm = Communicator(DuckConversation(lucas, donald))
comm.communicate(comm.channel)

    Lucas: Quack, hello Donald
    Donald: Quack, hello Lucas

Ahora, si necesito extender Comunicator para que puedan conversar dos perros, entonces solo tengo que agregar una clase DogConversation
(subclase de AbstractConversation) que implemente SU versión canina de "do_conversation" dejando "Communicator.communicate sin cambio.

    class Dog:
        
        def __init__(self, name):
            self.name = name
    
        def jump(self):
            print(f"{self.name} is jumpping not very high")
    
        def run(self):
            print(f"{self.name} runs behind the cars")
    
        @staticmethod
        def do_sound() -> str:
            return "Guau"
        
    
    class DogConversation(AbstractConversation):
    
        def __init__(self, dog1: Dog, dog2: Dog):
            self.dog1 = dog1
            self.dog2 = dog2
    
        def do_conversation(self) -> list:
            sentence1 = f"{self.dog1.name}: {self.dog1.do_sound()}, hello {self.dog2.name}"
            sentence2 = f"{self.dog2.name}: {self.dog2.do_sound()}, hello {self.dog1.name}"
            return [sentence1, sentence2]
    
    
scooby = Dog("Scooby")
pluto = Dog("Pluto")
comm = Communicator(DogConversation(scooby, pluto))
comm.communicate(comm.channel)

    Scooby: Guau, hello Pluto
    Pluto: Guau, hello Scooby
""")

print(f"{'#' * 52}")
print(f"##  Dificultad Extra  {'#' * 30}")
print(f"{'#' * 52}\n")

print(f"\nNO OCP Way {'-' * 27}\n")


class OperateNoOCP:

    def __init__(self, name: str):
        self.name = name

    def addition(self, *args):
        return self.name + " addition = " + str(sum(args))

    def substraction(self, *args):
        return self.name + " substraction = " + str(args[0] + (-1 * sum(args[1:])))

    def product(self, *args):
        return self.name + " product = " + str(reduce(lambda a, b: a * b, args))

    def division(self, dividend: float, divisor: float):
        if divisor == 0:
            return self.name + " Illegal operation: Divisor cannot be zero"
        return self.name + " division = " + str(dividend / divisor)


operaciones = OperateNoOCP("NoOCP")
print(operaciones.addition(1, 2, 3, -4))
print(operaciones.substraction(15, 2, 3, -4))
print(operaciones.product(1, 2, 3, -4))
print(operaciones.division(12, -4))

print(f"\nOCP Way {'-' * 30}\n")


class AbstractOperation:

    def calculate(self):
        pass


class Addition:

    def __init__(self, *args):
        self.name = "OCP addition"
        self.args = args

    def calculate(self):
        return self.name + " = " + str(sum(self.args))


class Substraction:

    def __init__(self, *args):
        self.name = "OCP substraction"
        self.args = args

    def calculate(self):
        return self.name + " = " + str(self.args[0] + (-1 * sum(self.args[1:])))


class Product:
    def __init__(self, *args):
        self.name = "OCP product"
        self.args = args

    def calculate(self):
        return self.name + " = " + str(reduce(lambda a, b: a * b, self.args))


class Division:

    def __init__(self, dividend: float, divisor: float):
        self.name = "OCP division"
        self.dividend = dividend
        self.divisor = divisor

    def calculate(self):
        if self.divisor == 0:
            return self.name + " Illegal operation: Divisor cannot be zero"
        return self.name + " = " + str(self.dividend / self.divisor)


class DoAddition(AbstractOperation):

    def __init__(self, operation: Addition):
        self.operation = operation

    def calculate(self, *args):
        return self.operation.calculate()


class DoSubstraction(AbstractOperation):

    def __init__(self, operation: Substraction):
        self.operation = operation

    def calculate(self, *args):
        return self.operation.calculate()


class DoProduct(AbstractOperation):

    def __init__(self, operation: Product):
        self.operation = operation

    def calculate(self, *args):
        return self.operation.calculate()


class DoDivision(AbstractOperation):

    def __init__(self, operation: Division):
        self.operation = operation

    def calculate(self, *args):
        return self.operation.calculate()


class Communicator:

    def __init__(self, channel):
        self.channel = channel

    @final
    def communicate(self, conversation: AbstractOperation):
        print(conversation.calculate())


suma = Addition(1, 2, 3, -4)
comm = Communicator(DoAddition(suma))
comm.communicate(comm.channel)

resta = Substraction(15, 2, 3, -4)
comm = Communicator(DoSubstraction(resta))
comm.communicate(comm.channel)

producto = Product(1, 2, 3, -4)
comm = Communicator(DoProduct(producto))
comm.communicate(comm.channel)

division = Division(12, -4)
comm = Communicator(DoDivision(division))
comm.communicate(comm.channel)
