"""
 * EJERCICIO:
 * Explora el concepto de herencia según tu lenguaje. Crea un ejemplo que
 * implemente una superclase Animal y un par de subclases Perro y Gato,
 * junto con una función que sirva para imprimir el sonido que emite cada Animal.
"""
# Superclase
class Animal:

    def __init__(self,name, age, breed = None):
        self.name = name
        self.age = age
        self.breed = breed if breed else "Unknown"
        self.sound = None

    def feed(self):
        print(f"{self.name} is fed")

    def make_sound(self):
        if self.sound:
            print(self.sound)
        else:
            print(f"{self.name} makes a sound")

class Dog(Animal):
    def __init__(self, name, age, breed = None):
        super().__init__(name, age, breed)
        self.sound = "Guau"


class Cat(Animal):
    def __init__(self, name, age, breed = "None"):
        super().__init__(name, age, breed)
        self.sound = "Miau"

my_dog = Dog("Firulais", 2)
my_cat = Cat("Bruma", 1)
my_cow = Animal("Campana", 8, "lechera")

my_dog.feed()
my_cat.feed()
my_cow.feed()
my_dog.make_sound()
my_cat.make_sound()
my_cow.make_sound()


"""
 * DIFICULTAD EXTRA (opcional):
 * Implementa la jerarquía de una empresa de desarrollo formada por Empleados que
 * pueden ser Gerentes, Gerentes de Proyectos o Programadores.
 * Cada empleado tiene un identificador y un nombre.
 * Dependiendo de su labor, tienen propiedades y funciones exclusivas de su
 * actividad, y almacenan los empleados a su cargo.
 */
"""

class Employee:

    def __init__(self, id: int, name: str):
        self.id = id
        self.name = name
        self.employees =[]

    def add_employee(self, employee):
        self.employees.append(employee)

    def show_employees(self):
        print(f"Employees of {self.id} - {self.name} - {type(self).__name__}:")
        for employee in self.employees:
            print(f"ID: {employee.id}, Name: {employee.name} - {type(employee).__name__} {("- " + employee.language) if isinstance(employee, Programmer) else ""}")


class Programmer(Employee):
    
    def __init__(self, id: int, name: str, language: str):
        super().__init__(id, name)
        self.language = language

    def code(self):
        print(f"{self.id} - {self.name} programa su aplicación")

    def add_employee(self, employee : Employee):
        print("Un programador no puede añadir empleados")

    def show_employees(self):
        print("Los programadores no tienen empleados a su cargo.")


class Project_manager(Employee):

    def __init__(self, id: int, name: str, project: str):
        super().__init__(id, name)
        self.project = project

    def coordinate_project(self):
        print(f"{self.id} - {self.name} sicroniza su proyecto {self.project}")


class Manager(Employee):

    def __init__(self, id: int, name: str):
        super().__init__(id, name)

    def coordinate_projects(self):
        print(f"{self.id} - {self.name} sicroniza los proyectos de la emperesa")


my_manager = Manager(1,"Ignacio")
my_project_manager = Project_manager(2, "Miguel", "NOVA")
my_programmer = Programmer(3,"Pedro", "Python")
my_programmer2 = Programmer(4, "Juan", "Kotlin")
my_project_manager2 = Project_manager(5, "Lorena", "MARCA")
my_programmer3 = Programmer(6,"Sara", "GO")
my_programmer4 = Programmer(7, "Carlos", "Rust")
my_programmer5 = Programmer(8,"Matias", "c#")
my_programmer6 = Programmer(9, "Alvaro", "Python")
my_manager.add_employee(my_project_manager)
my_manager.add_employee(my_project_manager2)
my_project_manager.add_employee(my_programmer)
my_project_manager.add_employee(my_programmer2)
my_project_manager2.add_employee(my_programmer3)
my_project_manager2.add_employee(my_programmer4)
my_project_manager2.add_employee(my_programmer5)
my_project_manager2.add_employee(my_programmer6)

my_manager.coordinate_projects()
my_manager.show_employees()
my_project_manager.coordinate_project()
my_project_manager.show_employees()
my_programmer.code()
my_programmer2.code()
my_project_manager2.coordinate_project()
my_project_manager2.show_employees()
my_programmer3.code()
my_programmer4.code()
my_programmer5.code()
my_programmer6.code()
my_programmer.add_employee(my_programmer6)
my_programmer.show_employees()