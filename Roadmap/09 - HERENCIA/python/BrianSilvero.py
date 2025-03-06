"""
Ejercicio
"""

class Animal:
    def __init__(self, name: str):
        self.name = name
        
    def sound (self):
        pass

#Subclases

class Perro(Animal):
    def sound(self):
        print("Guau!")

class Gato(Animal):
    def sound(self):
        print("Miau!")

def print_sound(animal: Animal):
    animal.sound()

my_animal = Animal("Animal")
print_sound(my_animal)
my_dog = Perro("Perro")
print_sound(my_dog)
my_cat = Gato("Gato")
print_sound(my_cat)


"""
Extra
"""

class Empleado:
    def __init__(self, id, name):
        self.id = id
        self.name = name
        self.empleados = []

    def add(self, empleado):
        self.empleados.append(empleado)

    def print_empleados(self):
        for empleado in self.empleados:
            print(empleado.name)

class Manager(Empleado):
    def coordinate_projects(self):
        print(f"{self.name} esta coordinando todos los proyectos de la empresa.")

class ProjectManager(Empleado):
    
    def __init__(self, id: int, name: str, proyecto: str):
        super().__init__(id,name)
        self.proyecto = proyecto
        
    def cordinate_project(self):
        print(f"{self.name} esta cordinando su proyecto llamado: {self.proyecto}.")
        
class Programador(Empleado):
    def __init__(self, id: int, name: str, lenguaje: str):
        super().__init__(id,name)
        self.lenguaje = lenguaje
    
    def code (self):
        print(f"{self.name} esta progrmando {self.lenguaje}.")
    def add(self, empleado: Empleado):
        print(f"Un programador no tiene empleados a su cargo. {empleado.name} no se añadira.")
        
my_manager = Manager(1, "Brian")
my_project_manager = ProjectManager(2, "David","Proyecto1")
my_project_manager2 = ProjectManager(3, "Gabriel","Proyecto2")
my_programador = Programador(4,"Maximiliano","Python")
my_programador2 = Programador(5,"Juan", "Java")

my_manager.add(my_project_manager)
my_manager.add(my_project_manager2)

my_project_manager.add(my_programador)
my_project_manager2.add(my_programador2)

my_programador.add(my_programador2) 

my_programador.code()
my_project_manager.cordinate_project()
my_manager.coordinate_projects()
my_manager.print_empleados()
my_project_manager.print_empleados()
my_programador.print_empleados()
