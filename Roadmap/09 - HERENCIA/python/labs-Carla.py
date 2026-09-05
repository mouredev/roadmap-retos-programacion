"""Herencia y Polimorfismo"""

#Herenecia: Hereda propiedades o métodos
#Polimorfismo: Capacidad de un objeto de tomar muchas formas

#Superclase Animal

class Animal:

    def __init__(self, name:str):
        self.name = name

    def sound(self):
        pass

#Subclases

class Gato(Animal):
    def sound(self):
        print("Miau!")


class Perro(Animal):
    def sound(self):
        print("Guau!")

def print_sound(animal: Animal):
    animal.sound()

my_animal = Animal("Animal")   
print_sound(my_animal)
my_dog = Perro("Carla")
print_sound(my_dog)
my_cat = Gato("Carla")
print_sound(my_cat)

"""Extra"""

class Empleados:
    def __init__(self, id:int, nombre:str):
        self.id = id
        self.nombre = nombre
        self.employees = []

    def add(self,empleado):
        self.employees.append(empleado)

    def print_employees(self):
         for employee in self.employees:
              print(employee.nombre)

 
class Manager(Empleados):
    def coordinate_projects(self):
        print(f"{self.nombre} está coordinando los proyectos de la empresa.")

class ProjectManager(Empleados):
     
    def __init__(self, id:int, nombre:str, proyectos:str):
                super().__init__(id,nombre)
                self.proyectos = proyectos

    def coordinate_project(self):
        print(f"{self.nombre} está coordinando su proyecto.")

class Programmer(Empleados):
    def __init__(self, id:int, nombre:str, language:str):
            super().__init__(id,nombre)
            self.language = language

    def programming(self):
        print(f"{self.nombre} está programando en {self.language}")

    def add(self, employee: Empleados):
        print(f"Un programador no tiene empleados a su cargo. {employee.nombre} no se añade")

my_manager = Manager(1,"Carla Dev")
my_project_manager = ProjectManager(2, "Tatiana", "Proyecto1")
my_project_manager2 = ProjectManager(3, "Carla Manager", "Proyecto2")
my_programmer = Programmer(4, "Kathy", "Python")
my_programmer2 = Programmer(5, "Marí", "React")
my_programmer3 = Programmer(6, "Ruby", "Go")
my_programmer4 = Programmer(7, "Adrián", "C++")

my_manager.add(my_project_manager)
my_manager.add(my_project_manager2)

my_project_manager.add(my_programmer)
my_project_manager.add(my_programmer2)

my_project_manager2.add(my_programmer3)
my_project_manager2.add(my_programmer4)

my_programmer.add(my_programmer)

my_programmer.programming()
my_project_manager.coordinate_project()
my_manager.coordinate_projects()
my_manager.print_employees()
my_project_manager.print_employees()
my_project_manager2.print_employees()