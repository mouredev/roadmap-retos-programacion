# /*
#  * EJERCICIO:
#  * Explora el concepto de herencia según tu lenguaje. Crea un ejemplo que
#  * implemente una superclase Animal y un par de subclases Perro y Gato,
#  * junto con una función que sirva para imprimir el sonido que emite cada Animal.
#  *
#  * DIFICULTAD EXTRA (opcional):
#  * Implementa la jerarquía de una empresa de desarrollo formada por Empleados que
#  * pueden ser Gerentes, Gerentes de Proyectos o Programadores.
#  * Cada empleado tiene un identificador y un nombre.
#  * Dependiendo de su labor, tienen propiedades y funciones exclusivas de su
#  * actividad, y almacenan los empleados a su cargo.
#  */

class Animal:

    def __init__(self,name,age):
        self.name = name
        self.age = age

    
    def greetings(self):
        return f'Hi, Im {self.name} the {type(self).__name__}, Im {self.age} years old'
    
    def communicate():
        pass

class Dog(Animal):
    
    def communicate(self):
        return "Woof!"


class Cat(Animal):

    def communicate(self):
        return 'Meow!'


yoel = Animal('yoel',3)
marko = Dog('marko',5)
yuri = Cat("yuri",5)
print(yoel.greetings())
print(marko.greetings())
print(yuri.greetings())
print(marko.communicate())
print(yuri.communicate())

#extra

class Employee:

    def __init__(self,name,id):
        self.name =  name
        self.id

class Manager(Employee):
    
    def coordinate_projects(self):
        print(f'{self.name} Esta Coordinando los proyectos de la empresa')

class ProjectManager(Employee):
    
    def coordinate_projects(self):
        print(f'{self.name} Esta Coordinando sus proyectos')

class Developer(Employee):

    def code(self):
        print(f'{self.name} Esta escribiendo codigo')