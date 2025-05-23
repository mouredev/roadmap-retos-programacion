"""
Herencia

En Python, la herencia es un mecanismo que permite a una clase derivada 
(subclase) 
adquirir las propiedades y comportamientos (atributos y métodos) 
de otra clase base 
(superclase).

"""

"""
 ¿Qué es el polimorfismo en Python?

El polimorfismo es la capacidad de distintas clases de 
responder al mismo método de formas diferentes.

Es decir, mismo nombre de método, pero comportamiento 
distinto dependiendo del objeto que lo utilice.


"""

#Superclase


class Animal:

    def __init__(self, name: str):
        self.name= name

    def sound(self):
        pass
        #print ("Este animal emite un sonido no determinado")


    def sound (self):
        pass
        #print ("Este animal emite un sonido no determinado")


    #Subclases


"""

   def __init__(self, name: str):
        self.name = name

    def sound ():

        print ("Guau!")

"""

class Dog (Animal):

    def sound (self):
        print ("Guau!")


 
"""
    def __init__(self, name: str):

        self.name = name

    def sound ():
         
         print ("Miau!")

"""
class Cat (Animal):

    def sound (self):
        print ("Miau!")



def print_sound (animal: Animal):
    animal.sound()


my_animal = Animal("Animal")
my_animal.sound ()
my_dog = Dog ("Perro")
my_dog.sound ()
my_cat = Cat ("Gato")
my_cat.sound ()
        

"""
Extra

"""


class Employee:

    def __init__(self, id: int, name:str):
        self.id = id
        self.name = name
        self.employees = []
        
    def add (self, employee):
        self.employees.append(employee)

class Manager (Employee):

    def coordinate_projects(self):
        print(f"{self.name} está coordinando todos los proyectos de la empresa")

class ProjectManager (Employee):

    def __init__(self, id: int, name: str, project: str):
        super().__init__(id, name)
        self.project = project

    def coordinate_project(self):
        print (f"{self.name} está coordinando su proyecto.")

class Programmeer(Employee):

    def __init__(self, id: int, name:str, language: str):
        super().__init__(id, name)
        self.language = language

    def code(self):
        print (f"{self.name} está programando en {self.language}")
    
    def add (self, employee: Employee):
        print(
            f"Un programador no tiene empleados a su cargo. {employee.name} no se añadirá.")

my_manager = Manager(1, "Yanines")
my_project_manager = ProjectManager(2, "Yani", "Proyecto 1")
my_project_manager2 = ProjectManager (3, "Nes", "Proyecto 2")

my_programmer = Programmeer(4, "Sofía", "Swift")
my_programmer2 = Programmeer(5, "Toto", "cobol")
my_programmer3 = Programmeer(6, "Manu", "Dart")
my_programmer4 = Programmeer(7, "Romi", "Python")

my_manager.add(my_project_manager)
my_manager.add(my_project_manager2)

my_project_manager.add(my_programmer)
my_project_manager.add(my_programmer2)
my_project_manager2.add(my_programmer3)
my_project_manager2.add(my_programmer4)

my_programmer.add(my_programmer2)

my_programmer.code()
my_project_manager.coordinate_project()
my_manager.coordinate_projects()