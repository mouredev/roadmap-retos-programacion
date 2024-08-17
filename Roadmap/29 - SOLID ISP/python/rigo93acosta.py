'''
/*
 * EJERCICIO:
 * Explora el "Principio SOLID de Segregación de Interfaces (Interface Segregation Principle, ISP)" 
 * y crea un ejemplo simple donde se muestre su funcionamiento de forma correcta e incorrecta.
 *
 * DIFICULTAD EXTRA (opcional):
 * Crea un gestor de impresoras.
 * Requisitos:
 * 1. Algunas impresoras sólo imprimen en blanco y negro.
 * 2. Otras sólo a color.
 * 3. Otras son multifunción, pueden imprimir, escanear y enviar fax.
 * Instrucciones:
 * 1. Implementa el sistema, con los diferentes tipos de impresoras y funciones.
 * 2. Aplica el ISP a la implementación.
 * 3. Desarrolla un código que compruebe que se cumple el principio.
 */
'''

'''
Ejercicio

Trabajo con interfaces en las
clases
'''

from abc import ABC, abstractmethod

# SIN ISP

class WorkerInterface(ABC):

    @abstractmethod
    def work(self):
        ...

    @abstractmethod
    def eat(self):
        ...


class Human(WorkerInterface):

    def work(self):
        print("Trabajando")
    
    def eat(self):
        print("Comiendo")


class Robot(WorkerInterface):

    def work(self):
        print("Trabajando")

    def eat(self):
        # Los robot no comen
        pass


human = Human()
human.work()
human.eat()

robot = Robot()
robot.work()
robot.eat() ## Error

# CON ISP

class WorkInterface(ABC):

    @abstractmethod
    def work(self):
        ...

class EatInterface(ABC):

    @abstractmethod
    def eat(self):
        ...

class Human(WorkInterface, EatInterface):

    def work(self):
        print("Trabajando")
    
    def eat(self):
        print("Comiendo")

class Robot(WorkInterface):

    def work(self):
        print("Trabajando")

'''
Extra
'''

