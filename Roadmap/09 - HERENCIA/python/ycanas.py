# ------ Ejercicio

class Animal:
    
    def __init__(self, age: int, name: str, breed: str):
        self.age = age
        self.name = name
        self.breed = breed

    
    def sound(self):
        pass
        

class Dog(Animal):
    
    def sound(self):
        print("Wouf Wouf!")


class Cat(Animal):
    
    def sound(self):
        print("Mauw Mauw!")


animal = Animal(10, "Appa", "Bisonte")
animal.sound()
gato = Cat(12, "Milo", "Siberiano")
gato.sound()
perro = Dog(4, "Fiona", "Bulldog")
perro.sound()


# ------ Extra

class Employee:

    def __init__(self, id: int, name: str):
        self.id = id
        self.name = name
        self.employees = []

    
    def add_employee(self, employee):
        self.employees.append(employee)

    
    def print_employees(self):
        for employee in self.employees:
            print(employee.name)


class Manager(Employee):

    def coordinate_projects(self):
        print(f"{self.name} está coordinando los proyectos de la empresa.")


class ProjectManager(Employee):

    def __init__(self, id: int, name: str, project: str):
        super().__init__(id, name)
        self.project = project

    
    def coordinate_project(self):
        print(f"{self.name} está coordinando el proyecto {self.project}")


class Programmer(Employee):

    def __init__(self, id: int, name: str, project: str, language: str):
        super().__init__(id, name)
        self.project = project
        self.language = language


    def code(self):
        print(f"{self.name} está programando en {self.language} en el proyecto {self.project}")


    def add_employee(self, employe: Employee):
        print("Error, un programador no puede tener empleados a su cargo")

    
    def print_employees(self):
        print("Error, el programador no tiene empleados a su cargo")


manager = Manager(1, "Espedito")
project_manager = ProjectManager(2, "Rufino", "Image Scanner")
programmer = Programmer(3, "Facundo", "Image Scanner", "Python")

manager.add_employee(project_manager)
manager.add_employee(programmer)

project_manager.add_employee(programmer)

manager.coordinate_projects()
manager.print_employees()

project_manager.coordinate_project()
project_manager.print_employees()

programmer.add_employee(manager)
programmer.print_employees()
programmer.code()
