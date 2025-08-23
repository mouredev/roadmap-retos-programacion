'''
ejercicio
'''
class Animal:
    
    def __init__(self, name:str):
        self.name = name
        
    def sound(self):
        pass
        
class Dog(Animal):
    
    def sound(self):
        print("Guau")
        
class Cat(Animal):
    
    def sound(self):
        print("Miau")       
        
def print_sound(animal: Animal):
    animal.sound()
    
# my_dog = Dog("perro")
# print_sound(my_dog)
# my_cat = Cat("gato")
# print_sound(my_cat)

'''
Extra
'''

class Employee:
    
    def __init__(self, id: int, name: str):
        self.id = id
        self.name = name
        self.employees = []
        
    def add(self, employee) :
        
        self.employees.append(employee)
        
    def print_employees(self):
        for employee in self.employees:
            print(employee.name)
                   

class Manager(Employee):
    
    def coordinate_projects(self):
        print(f"{self.name} esta coodinando todos los proyectos")
    
class ProjectManager(Employee):
    def __init__(self, id: int, name: str, project: str):
        super().__init__(id,name)
        self.project = project
    
    def coordinate_project(self):
        print(f"{self.name} esta coodinando su proyecto {self.project}")
    
class Programmer(Employee):
    
    def __init__(self, id: int, name: str, lenguage: str):
        super().__init__(id,name)
        self.lenguage = lenguage
    
    def code(self):
        print(f"{self.name } esta programando en {self.lenguage}")
        
    def add(self, employee) :
        
        pass
        
        
my_manager = Manager(1,'Andres')
my_proyect_manager = ProjectManager(2, "Andres", 'Telecoom')
my_proyect_manager2 = ProjectManager(3, "Alejandro", 'Claro')
my_programmer =  Programmer(4,"satoshi", "java")
my_programmer2 =  Programmer(5,"goru", "Swift")
my_programmer3 =  Programmer(6,"tetop", "Dart")
my_programmer4 =  Programmer(7,"niea", "Php")

my_manager.add(my_proyect_manager)
my_manager.add(my_proyect_manager2)

my_proyect_manager.add(my_programmer)
my_proyect_manager.add(my_programmer2)

my_proyect_manager2.add(my_programmer3)
my_proyect_manager2.add(my_programmer4)

my_programmer4.code()
my_proyect_manager2.coordinate_project()
my_manager.coordinate_projects()
my_manager.print_employees()
my_proyect_manager.print_employees()