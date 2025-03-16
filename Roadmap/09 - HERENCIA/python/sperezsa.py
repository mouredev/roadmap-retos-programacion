#09 HERENCIA Y POLIMORFISMO

# Superclase
class Animal:
    def __init__(self, name: str):
        self.name = name
    
    def sound(self):
        pass #personalizado en cada una de las subclases

# Subclases
class Dog(Animal):
    def sound(self):
        print(f" {self.name} hace guau!")

class Cat(Animal):
    def sound(self):
        print(f" {self.name} hace miau!")


my_animal = Animal("Ferny")
my_animal.sound()

my_dog = Dog("Oddy")
my_dog.sound()

my_cat = Cat("Duchess")
my_cat.sound()


"""
Extra
"""

class Employee:
    def __init__(self, id: int, name: str):
        self.id = id
        self.name = name
        self.employees = []
        
    def add(self, employee):
        self.employees.append(employee)

    def count_employees(self):
        print(f"{self.name} tiene a su cargo {len(self.employees)} empleados.")
        

class Manager(Employee):
    def manage(self):
        print(f"El manager {self.name} gestiona los proyectos.")

     
class ProjectManager(Employee):
    def __init__(self, id: int, name: str, project: str):
        super().__init__(id, name)
        self.project = project
    
    def manage_project(self):
        print(f"El PM {self.name} gestiona el proyecto {self.project}.")
        
    
class Programmer(Employee):
    def __init__(self, id: int, name: str, language: str):
        super().__init__(id, name)
        self.language = language
    
    def coding(self):
        print(f"El programador {self.name} codifica en el lenguaje {self.language}.")
        
    def add(self, id: int):
        print(f"Programadores no pueden tener personal a su cargo. {id} no asignado.")


pg1 = Programmer(1, 'Anne', 'Python')
pg2 = Programmer(2, 'John', 'JS')
pg3 = Programmer(3, 'Morgan', 'Python')
pg4 = Programmer(4, 'Lilly', 'Java')
pg5 = Programmer(5, 'Clark', 'PHP')
pm1 = ProjectManager(6, 'Carl', 'secreto')
pm2 = ProjectManager(7, 'Kevin', 'interno')
mng = Manager(8, 'Susan')

pg1.add(4)
pg1.coding()
pg2.coding()
pg3.coding()
pg4.coding()
pg5.coding()
pm1.add(pg3)
pm1.add(pg2)
pm1.add(pg1)
pm1.manage_project()
pm1.count_employees()
pm2.add(pg4)
pm2.add(pg5)
pm2.manage_project()
pm2.count_employees()
mng.add(pm1)
mng.add(pm2)
mng.manage()
mng.count_employees()
pg1.count_employees()