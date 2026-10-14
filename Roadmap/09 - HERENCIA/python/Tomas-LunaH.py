"""
Ejercicio
"""
#Super Clase

class Animal :
    def __init__(self, name : str):
        self.name = name
    def sound (self):
        pass
#Sub clases

class Dog (Animal):
    def sound (self):
        print("Guaf!")


class Cat (Animal):
    def sound (self):
        print("Miau!")

def print_sound (animal: Animal):
    animal.sound()




my_animal = Animal ("Animal")
print_sound(my_animal)
my_dog = Dog("Perro")
my_cat = Cat("Gato")
print_sound(my_dog)
print_sound(my_cat)


"""
EXTRA
"""
#!Version Propia

class Employ:
    def __init__(self, id : int, name : str):
        self.id = id
        self.name = name
    def print_info (self):
        print(f"ID del superior : {self.id } Nombre del superior: {self.name}")

class Manager(Employ):
    def __init__(self, id, name):
        super().__init__(id, name)
        self.Subordinates = []
        self.proyects = []
    def create_proyect(self, subordinate, name_proyect: str):
        print(f"Asiganando el proyecto {name_proyect} al gerente de proyectos ")
        subordinate.get_proyect(name_proyect)
        self.proyects.append(name_proyect)
    def add_subordinates(self,subordinate : str):
        self.Subordinates.append(subordinate)  
    def print_info (self):
        super().print_info()
        if len(self.Subordinates) < 1:
            print("No hay subordinarios")
        else:
            for num, man_proy in enumerate(self.Subordinates, start =1):
                print(f"Numero {num}, Nombre de los subordinarios {man_proy.name}")
    

class Proyect_Manager(Employ):
    def __init__(self, id, name):
        super().__init__(id, name)
        self.developers = []
        self.proyects = []
    def add_developers (self, developer : str):
        self.developers.append(developer)
    def print_info(self):
        super().print_info()
        if len(self.developers) < 1:
            print("No hay desarrolladores")
        else:
            for num, employs in enumerate(self.developers, start =1):
                print(f"Numero {num}, Nombre de desarroladores {employs}")
    def get_proyect(self,name_proyect):
        self.proyects.append(name_proyect)
    def assign_proyect(self,developer, name_proyect: str):
            if len(self.proyects ) == 0 :
                print("No tiene proyectos")
            else:
                print(f"Asiganando el proyecto {name_proyect} al desarrolador ")
                developer.get_proyect(name_proyect)
                self.proyects.append(name_proyect)



class Developer (Employ):
    def __init__(self, id, name, lengauges):
        super().__init__(id, name)
        self.proyects = []
        self.lenguages = lengauges
    def get_proyect (self,name_proyect):
        self.proyects.append(name_proyect)

    def print_info(self):
        print(f"ID del desarolador : {self.id } Nombre del desarrolador {self.name} lenguajes {self.lenguages}")
    def execute_task (self):
        if len(self.proyects) == 0 :
            print("No hay proyectos")
        else:
            print("El desarrollador a creado una solucion al problema")
            self.proyects.pop(0)
    
my_manger = Manager(20, "Jefe")
my_developer = Developer(19,"Tomas", "Python")
my_proyect_manager = Proyect_Manager(10, "Kiki")
my_manger.add_subordinates(my_proyect_manager)
my_manger.create_proyect(my_proyect_manager, "Solucionar el inventario del almacen")
my_proyect_manager.add_developers(my_developer)
my_proyect_manager.assign_proyect(my_developer, "Desarrollo de una app para el invenatario")
my_developer.execute_task()
my_manger.print_info()

#!Version de Brais
class Employee:
    def __init__(self, id:int, name:str):
        self.id = id
        self.name = name
        self.employees = []
    def add(self,employee):
        self.employees.append(employee)
    def print_employye (self):
        for employee in self.employees:
            print(employee.name)
class Manger(Employee):
    def cordinate_proyects(self):
        print(f"{self.name} está coordinando todos los proyectos de la empresa.")
class ProyectManager(Employee):
    def __init__(self, id:int, name:str, proyect:str):
        super().__init__(id, name)
        self.proyect= proyect
    def cordinate_proyect(self):
        print(f"{self.name} está coordinando su proyecto.")
class Programmer(Employee):
    def __init__(self, id:int, name:str, lenguage : str):
        super().__init__(id, name)
        self.lenguage=self.lenguage
    def code(self):
        print(f"{self.name} está programando en {self.language}.")

    def add(self, employee: Employee):
        print(
            f"Un programador no tiene empleados a su cargo. {employee.name} no se añadirá.")

my_manager = Manager(1, "MoureDev")
my_project_manager = ProyectManager(2, "Brais", "Proyecto 1")
my_project_manager2 = ProyectManager(3, "Moure", "Proyecto 2")
my_programmer = Programmer(4, "Kontrol", "Swift")
my_programmer2 = Programmer(5, "Ros", "Cobol")
my_programmer3 = Programmer(6, "Bushi", "Dart")
my_programmer4 = Programmer(7, "Nasos", "Python")

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
my_manager.print_employees()
my_project_manager.print_employees()
my_programmer.print_employees()


