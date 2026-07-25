#Inheritance

class Animal:
    def __init__(self, name):
        self.name = name
        
    def sound(self):
        return "This animal does not have a specific sound"

    def print(self):
        print(f"{self.name}: {self.sound()}")


class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed

    def print(self):
        print(f"{self.name} ({self.breed}): {self.sound()}")

    def sound(self):
        return "Woof"


class Cat(Animal):
    def sound(self):
        return "Meow"


def print_sound(animal: Animal):
    print(animal.sound())


# Create objects
dog = Dog("Bobbi", "Beagle")
cat = Cat("Kuba")

# Print their sounds
print_sound(dog)  # Woof
print_sound(cat)  # Meow

# Print full profile
dog.print()  # Bobbi: Woof
cat.print()  # Kuba: Meow


#Extra Exercise

class Employee:

    def __init__(self, id, name):
        self.id = id
        self.name = name
        self.employees = []

    def add(self, employee):
        self.employees.append(employee)

    def print_employees(self):
        for employee in self.employees:
            print(employee.name)

class Manager(Employee):
    def coordinate_projects(self):
        print(f"{self.name} is coordinating all the projects")

class ProjectManager(Employee):
    def __init__(self, id, name, project):
        super().__init__(id, name)
        self.project = project

    def coord_project(self):
        print(f"{self.name} is coordinating  it owns project")



class Programmer(Employee):
    def __init__(self, id, name, language):
        super().__init__(id, name)
        self.language = language

    def code(self):
        print(f"{self.name} is coding in {self.language}")

    def add(self, employee):
        print(f"A programmer doesn’t supervise any employees. {employee.name} will not be added.")

my_manager = Manager(1, "Anna")
my_project_manager = ProjectManager(2, "Pablo", "Project 1")
my_project_manager2 = ProjectManager(3, "David", "Project 2")
my_programmer = Programmer(4, "Rose", "Java")
my_programmer2 = Programmer(5, "Ross", "JavaScript")
my_programmer3 = Programmer(6, "Marta", "Python")

my_manager.add(my_project_manager)
my_manager.add(my_project_manager2)
my_project_manager.add(my_programmer2)
my_project_manager2.add(my_programmer3)
my_project_manager.add(my_programmer)

my_programmer3.add(my_programmer3)


my_programmer.code()
my_manager.coordinate_projects()
my_project_manager.coord_project()
my_manager.print_employees()
my_project_manager.print_employees()
my_project_manager2.print_employees()
