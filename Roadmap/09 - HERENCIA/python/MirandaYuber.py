print("""
HERENCIA Y POLIMORFISMO
""")


class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @staticmethod
    def make_sound(self):
        print('Esta animal hace algun sonido')


class Dog(Animal):
    def __init__(self, name, age, race):
        super().__init__(name, age)
        self.race = race

    def make_sound(self):
        print('El perro hace guau guau')


dog = Dog(name='Lucas', age=5, race='Labrador')
print(f'El nombre del perro es: {dog.name}')
print(f'El edad del perro es: {dog.age}')
print(f'El raza del perro es: {dog.race}')
print(dog.make_sound())
print()


class Cat(Animal):
    def __init__(self, name, age, race):
        super().__init__(name, age)
        self.race = race

    def make_sound(self):
        print('El gato hace miau miau')


cat = Cat(name='Miel', age=2, race=None)
print(f'El nombre del gato es: {cat.name}')
print(f'El edad del gato es: {cat.age}')
print(f'El raza del gato es: {cat.race}')
print(cat.make_sound())
print()

print("""
EXTRA
""")


class Employee:
    def __init__(self, identification: int, name: str):
        self.identification = identification
        self.name = name
        self.employees = []

    def add(self, employee):
        self.employees.append(employee)

    def print_employees(self):
        for employee in self.employees:
            print(employee.name)


class Manager(Employee):
    def coordinate_projects(self):
        print(f'{self.name} esta coordinando todos los proyectos de la empresa')


class ProjectManager(Employee):
    def __init__(self, identification: id, name: str, project: str):
        super().__init__(identification, name)
        self.project = project

    def coordinate_project(self):
        print(f'{self.name} esta coordinando su proyecto')


class Programmer(Employee):
    def __init__(self, identification: int, name: str, language: str):
        super().__init__(identification, name)
        self.language = language

    def code(self):
        print(f'{self.name} esta programando en {self.language}')

    def add(self, employee):
        print('Un progrmamador no puede tener empleados a cargo.')


my_manager = Manager(1, 'Yuber')
my_project_manager = ProjectManager(2, 'Esteban', 'Proyecto 1')
my_project_manager2 = ProjectManager(3, 'Esteban2', 'Proyecto 2')
my_programmer = Programmer(4, 'Julio', language='PHP')
my_programmer2 = Programmer(5, 'Omar', language='Python')
my_programmer3 = Programmer(6, 'Mateo', language='NodeJS')
my_programmer4 = Programmer(7, 'Pedro', language='JS')

my_manager.add(my_project_manager)
my_manager.add(my_project_manager2)

my_project_manager.add(my_programmer)
my_project_manager.add(my_programmer2)
my_project_manager2.add(my_programmer3)
my_project_manager2.add(my_programmer4)

my_programmer.add(my_programmer2)
my_project_manager.coordinate_project()
my_manager.coordinate_projects()
my_manager.print_employees()
my_project_manager.print_employees()
my_programmer.print_employees()
