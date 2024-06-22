# Problem 09 inheritance

class Animal:

    def speak(self):
        raise NotImplementedError()


class Dog(Animal):

    def speak(self):
        print("Goof Goof")


class Cat(Animal):

    def speak(self):
        print("Meow!")


dog = Dog()
dog.speak()

cat = Cat()
cat.speak()


# Extra

class Employee:

    def __init__(self, identifier, name):
        self.id = identifier
        self.name = name
        self.employees = []

    def show_employees(self):
        print(f"'{self.name} ({self.id})' employees:")
        for employee in self.employees:
            print(employee.name)

    def add_employee(self, employee):
        self.employees.append(employee)


class Manager(Employee):

    def __init__(self, identifier, name):
        super().__init__(identifier, name)

    def current_job(self):
        print(f"Manager '{self.name} ({self.id})' in charge of all the projects.")


class ProjectManager(Employee):

    def __init__(self, identifier, name, project):
        super().__init__(identifier, name)
        self.project = project

    def current_job(self):
        print(f"PM '{self.name} ({self.id})' in charge of '{self.project}' project.")


class Developer(Employee):

    def __init__(self, identifier, name, language):
        super().__init__(identifier, name)
        self.language = language

    def current_job(self):
        print(f"Developer '{self.name} ({self.id})' programs in '{self.language}'.")

    def show_employees(self):
        print("Developers can have other employees in charge.")

    def add_employee(self, employee):
        print("Developers can have other employees in charge.")


manager = Manager(1, "Foo")
pm = ProjectManager(2, "Bar", "Proyectito")
dev = Developer(3, "FB", "Python")

manager.add_employee(pm)
manager.add_employee(dev)
manager.show_employees()
manager.current_job()

pm.current_job()
pm.add_employee(dev)
pm.show_employees()

dev.current_job()
dev.add_employee(pm)
dev.show_employees()
