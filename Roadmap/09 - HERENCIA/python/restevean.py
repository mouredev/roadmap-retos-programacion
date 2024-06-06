"""
Ejercicio 1
"""


# Superclass
class Animal:

    def __init__(self, name: str):
        self.name = name

    def sound(self):
        pass


# Subclass
class Dog(Animal):

    def sound(self):
        return 'Wof!'


class Cat(Animal):

    def sound(self):
        return 'Meow!'


def my_animals():
    print("Exercise")
    animals = [Dog('Odin'), Cat('Misifu')]
    for animal in animals:
        print(f'{animal.name} says {animal.sound()}')


"""
Extra
"""


class Employee:

    def __init__(self, employee_id: int, name: str):
        self.id = employee_id
        self.name = name
        self.employees = []

    def add(self, employee):
        self.employees.append(employee)

    def print_employees(self):
        for employee in self.employees:
            print(employee.name)


class Manager(Employee):

    def coordinate_projects(self):
        print('The manager is coordinating all projects')


class ProjectManager(Employee):

    def manage_project(self):
        print('The project manager is coordinating his own project')


class Programmer(Employee):

    def __init__(self, id: int, name: str, language: str):
        super().__init__(id, name)
        self.language = language

    def code(self):
        print(f"{self.name} is coding using {self.language}.")


def my_employees():
    print('Extra')
    manager = Manager(1, 'John')
    project_manager = ProjectManager(2, 'Paul')
    programmer = Programmer(3, 'Ringo', 'Python')
    manager.add(project_manager)
    manager.add(programmer)
    manager.print_employees()
    project_manager.manage_project()
    programmer.code()
    manager.print_employees()


if __name__ == '__main__':
    my_animals()
    my_employees()
