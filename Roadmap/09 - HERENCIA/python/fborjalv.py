

class Animal: 
    def __init__(self, name: str):
        self.name = name
    def make_sound():
        print("Esta clase no hace ruido")


class Dog(Animal): 
    def make_sound(self):
        print("Guau")
        
class Cat(Animal):

    def make_sound(self):
        print("miau")


my_dog = Dog("Currito")
my_dog.make_sound()

my_cat = Cat("Don Gato")
my_cat.make_sound()
print(my_cat.name)


"""DIFICULTAD EXTRA (opcional):
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
        self.employees = []
    
    def add_employee(self, employees):
        self.employees.append(employees)
    def show_employee(self):
        return self.employees

class Manager(Employee):
    def coordinate_projects(self):
        print(f"{self.name} está coordinando varios proyectos")

class ProjectManager(Employee):
    def __init__(self, id: int, name: str, project: str):
        super().__init__(id, name)
        self.project = project

    def coordinate_project(self):
        print(f"{self.name} está coordinando {self.project}")



class Developer(Employee):

    def __init__(self, id: int, name: str, languages: str):
        super().__init__(id, name)
        self.language = languages
    def coding(self):
        print(f"{self.name} está programando en {self.language}")



my_manager = Manager(53, "Loli")
my_manager.coordinate_projects()

my_project_manager = ProjectManager(2, "Brais", "Data Analysis")
my_project_manager.coordinate_project()

my_developer = Developer(13, "Pilar", "Pyton")
my_developer.coding()
print(my_developer.name)
print(my_developer.id)
print(my_developer.language)
