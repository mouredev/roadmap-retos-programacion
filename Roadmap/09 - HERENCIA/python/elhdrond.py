"""
    INHERITANCE AND POLYMORPHISM
"""

# Superclass

class Character:

    def __init__(self, name: str):
        self.name = name

    def attack(self):
        pass

    def __str__(self):
        return f"{self.name} ({self.__class__.__name__})"


# Subclasses

class Warrior(Character):

    def attack(self):
        print(f"{self.name} swings a sword!")


class Mage(Character):

    def attack(self):
        print(f"{self.name} casts a fireball!")


class Rogue(Character):

    def attack(self):
        print(f"{self.name} strikes from the shadows!")


def perform_attack(character: Character):
    character.attack()


hero = Character("Hero")
print(hero)
perform_attack(hero)

warrior = Warrior("Aragorn")
print(warrior)
perform_attack(warrior)

mage = Mage("Gandalf")
print(mage)
perform_attack(mage)

rogue = Rogue("Ezio")
print(rogue)
perform_attack(rogue)


"""
    EXTRA EXERCISE
"""


class Employee:

    def __init__(self, id: int, name: str):
        self.id = id
        self.name = name
        self.employees = []

    def add(self, employee):
        self.employees.append(employee)

    def print_employees(self):
        for employee in self.employees:
            print(f"  - {employee.name}")

    def __str__(self):
        return f"[{self.id}] {self.name}"


class Manager(Employee):

    def coordinate_all(self):
        print(f"{self.name} is coordinating all company projects.")


class ProjectManager(Employee):

    def __init__(self, id: int, name: str, project: str):
        super().__init__(id, name)
        self.project = project

    def coordinate_project(self):
        print(f"{self.name} is coordinating project: {self.project}.")


class Programmer(Employee):

    def __init__(self, id: int, name: str, language: str):
        super().__init__(id, name)
        self.language = language

    def code(self):
        print(f"{self.name} is coding in {self.language}.")

    def add(self, employee):
        print(f"A programmer has no direct reports. {employee.name} was not added.")


manager = Manager(1, "Alice")
pm1 = ProjectManager(2, "Bob", "Project Alpha")
pm2 = ProjectManager(3, "Carol", "Project Beta")
dev1 = Programmer(4, "Dave", "Python")
dev2 = Programmer(5, "Eve", "Go")
dev3 = Programmer(6, "Frank", "Rust")

manager.add(pm1)
manager.add(pm2)
pm1.add(dev1)
pm1.add(dev2)
pm2.add(dev3)
dev1.add(dev2)


print(f"\n{manager.name}'s direct reports:")
manager.print_employees()
manager.coordinate_all()

print(f"\n{pm1.name}'s direct reports ({pm1.project}):")
pm1.print_employees()
pm1.coordinate_project()

print(f"\n{pm2.name}'s direct reports ({pm2.project}):")
pm2.print_employees()
pm2.coordinate_project()

print(f"\n{dev1.name}'s direct reports:")
dev1.print_employees()
dev1.code()

print(f"\n{dev2.name}'s direct reports:")
dev2.print_employees()
dev2.code()

print(f"\n{dev3.name}'s direct reports:")
dev3.print_employees()
dev3.code()