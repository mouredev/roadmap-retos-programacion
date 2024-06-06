"""EJERCICIO:
Explora el concepto de herencia según tu lenguaje. Crea un ejemplo que implemente
una superclase Animal y un par de subclases Perro y Gato, junto con una función que
sirva para imprimir el sonido que emite cada Animal"""


class Animal:
    mascot = True

    def __init__(self, name):
        self.name = name

    def print_sound(self, specie, sound):
        print(f'The {specie} {self.name} makes the sound "{sound}"')


class Dog(Animal):
    specie = 'dog'
    sound = 'Wuf'


class Cat(Animal):
    specie = 'cat'
    sound = 'Miau'


dog = Dog(name='Scooby')
cat = Cat(name='Garfield')

dog.print_sound(specie=dog.specie, sound=dog.sound)
cat.print_sound(specie=cat.specie, sound=cat.sound)

"""DIFICULTAD EXTRA (opcional):
Implementa la jerarquía de una empresa de desarrollo formada por Empleados que pueden ser: 
Gerentes, Gerentes de Proyectos o Programadores.
- Cada empleado tiene un identificador y un nombre.
- Dependiendo de su labor, tienen propiedades y funciones exclusivas de su  actividad, 
y almacenan los empleados a su cargo.
"""


class Employee:
    def __init__(self, employee_name, employee_id):
        self.name = employee_name
        self.id = employee_id
        self.subordinate_list = list()

    def show_information(self, position, salary, functions):
        print(f'Employee information\n'
              f'Name: {self.name}\n'
              f'Id: {self.id}\n'
              f'Position: {position}\n'
              f'Salary: {salary}\n'
              f'Functions: {functions}')

    def add_subordinate(self, subordinate):
        self.subordinate_list.append(subordinate)

    def show_subordinate(self):
        print(f'The subordinates of {self.name} are: ')
        for subordinate in self.subordinate_list:
            print(f'Name: {subordinate.name}, Position: {subordinate.position}')


class Manager(Employee):
    position = 'Manager'
    salary = 1000
    functions = 'Decision making'


class ProjectManager(Employee):
    position = 'Project Manager'
    salary = 500
    functions = 'Tech decision'


class Programmer(Employee):
    position = 'Programmer'
    salary = 300
    functions = 'Coding'


programmer1 = Programmer(employee_name='Alpha', employee_id=000)
programmer2 = Programmer(employee_name='Bravo', employee_id=111)

pro_manager1 = ProjectManager(employee_name='Charly', employee_id=222)
pro_manager1.add_subordinate(programmer1)
pro_manager1.add_subordinate(programmer2)

manager1 = Manager(employee_name='Delta', employee_id=333)
manager1.add_subordinate(pro_manager1)
manager1.add_subordinate(programmer1)
manager1.add_subordinate(programmer2)

programmer1.show_information(position=programmer1.position, salary=programmer1.salary, functions=programmer1.functions)
print('**********')
pro_manager1.show_information(position=pro_manager1.position, salary=pro_manager1.salary, functions=pro_manager1.functions)
pro_manager1.show_subordinate()
print('**********')
manager1.show_information(position=manager1.position, salary=manager1.salary, functions=manager1.functions)
manager1.show_subordinate()
print('**********')
