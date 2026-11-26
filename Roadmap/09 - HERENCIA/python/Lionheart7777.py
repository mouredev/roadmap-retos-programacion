"""
Ejercicio
"""

# SUPERCLASE

class Animal :
    def __init__(self, name:str):
        self.name = name
       
    def sound(self):
        pass

# subclases

class Dog(Animal) :
    
        
    def sound(self):
        print("Guau")
    
class Cat(Animal) :
    
        
    def sound(self):
        print("Miau")
        
def print_sound(cualquier_animal:Animal):
    cualquier_animal.sound()
                    

my_animal = Animal("XX")
my_animal.sound()
print_sound(my_animal)

my_dog = Dog("firulais")
#my_dog.sound()
#print_sound(my_dog)

my_cat = Cat("kitty")
#my_cat.sound()
#print_sound(my_cat)


"""
EXTRA
"""

class Employee :
    
    def __init__(self, id: int, name: str):
        self.id = id
        self.name = name
        self.employees = []
        
    def add(self,employee):
        self.employees.append(employee)
        
    def print_employees(self):
        for employee in self.employees:
            print(employee.name)
        

class Manager(Employee):
    
    def coordinate_projects(self):
        print(f" {self.name} está coordinando todos los proyectos de la empresa")
        
    
class Project_Manager(Employee):
    
    def __init__(self, id :int, name: str, project:str):
            super().__init__(id, name)
            self.project = Project_Manager
    
    def coordinate_project(self):
        print(f" {self.name} ya está coordinanado SU proyecto de la empresa")
    

class Programmer(Employee):
    
    def __init__(self, id :int, name: str, language:str):
        super().__init__(id, name)
        self.language = language
    
    def code(self):
        print(f" {self.name} está programando en {self.language} ")  
    
    def add(self,employee: Employee):
        print(f"un programador no tiene empleados a su cargo. {employee.name} no se añadirá")    


my_manager = Manager(1, "Rick")
my_proyecto_manager1 = Project_Manager(2,"Rupert", "Proyecto 1")
my_proyecto_manager2 = Project_Manager(3,"Emilio", "Proyecto 2")
my_programador1 = Programmer(4, "Aldo", "Swift")
my_programador2 = Programmer(5, "Eddie", "Cobol")
my_programador3 = Programmer(6, "Christian", "Dart")
my_programador4 = Programmer(7, "Rafael", "Python")              

my_manager.add(my_proyecto_manager1)
my_manager.add(my_proyecto_manager2)

my_proyecto_manager1.add(my_programador1)
my_proyecto_manager1.add(my_programador2)
my_proyecto_manager2.add(my_programador3)
my_proyecto_manager2.add(my_programador4)

my_programador1.add(my_programador2)

my_programador1.code()

my_proyecto_manager1.coordinate_project()
my_proyecto_manager1.print_employees()
my_proyecto_manager2.print_employees()


my_manager.coordinate_projects()
my_manager.print_employees()

my_programador1.print_employees()