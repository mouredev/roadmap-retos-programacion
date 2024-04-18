"""
HERENCIA Y POLIMORFISMO
"""

# SuperClase

class Animal:

    def __init__(self,name):
        self.name = name
    
    def sound(self):
        pass

#SubClases

class Dog(Animal): # Herencia
    def sound(self):
        print("Guau") #Polimorfismo
        
class Cat(Animal):
    def sound(self):
        print("Miau")
    
def print_Sound(animal: Animal):
    animal.sound()


my_Dog = Dog("Perro")
print_Sound(my_Dog)

my_Cat = Cat("Gato")
print_Sound(my_Cat)


"""
Extra
"""

class Employees:

    def __init__(self,name:str,identification:int):
        self.name = name
        self.identification = identification
        self.employee = []

    def add(self,employee):
        self.employee.append(employee)

    def printEmployees(self):
        for i in self.employee:
            print(i.name)

class Manager(Employees):
    def manager_Coordinate(self):
        print(f"{self.name} maneja proyectos")

class ProjectManager(Employees):

    def __init__(self, name: str, identification: int, project:str):
        super().__init__(name, identification)
        self.project = project

    def project_Coordinate(self):
        print(f"{self.name} proyecta a futro los costos")


class Developers(Employees):
    
    def __init__(self,name:str,identification:int,language:str):
        super().__init__(name,identification)
        self.language = language

    def programming(self):
        print(f"{self.name} Está programando en {self.language}")

    def add(employee:Employees):
        print(
            f"Un programador no tiene empleados a su cargo{employee.name} no se añadirá")

my_manager = Manager("Yenner Alayon", 21)
my_projectManager_1 = ProjectManager("Lucas", 22, "Heladeria")
my_projectManager_2 = ProjectManager("David", 23, "Panaderia")
my_projectManager_3 = ProjectManager("Pedrp", 24, "Salchipapa")
my_developer = Developers("Pawel Alayon", 25, "Kotlin")
my_developer1 = Developers("Juan Gomez", 26, "Python")

my_manager.add(my_projectManager_1)
my_manager.add(my_projectManager_2)

my_projectManager_3.add(my_developer)

my_developer1.programming()
my_projectManager_3.project_Coordinate()
my_manager.manager_Coordinate()

my_manager.printEmployees()
my_projectManager_3.printEmployees()