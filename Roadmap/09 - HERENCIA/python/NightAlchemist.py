'''
Exercise
'''

class Animal():
    def __init__(self, race):
        self.race = race


class Dog(Animal):
    def __init__(self, race = "Dog", sound = "Woof"):
        super().__init__(race)
        self.sound = sound

    def __str__(self):
        return (f"I am a {self.race} and I say {self.sound}")

class Cat(Animal):
    def __init__(self, race = "Cat", sound = "Meow"):
        super().__init__(race)
        self.sound = sound

    def __str__(self):
        return (f"I am a {self.race} and I say {self.sound}")

michi = Cat()
print(michi)

doggy = Dog()
print(doggy)

sphinx = Cat("Sphinx")
print(sphinx)

doberman = Dog("Doberman", "Bark!")
print(doberman)

'''
Extra
'''
#Main Class

class Employee():
    def __init__(self, name: str, id: int):
        self.name = name
        self.id = id
        self.employees = []

    def __str__(self):
        return f"Name: {self.name}, ID Number: {self.id}"
    
    def add(self, employee):
        self.employees.append(employee)
    
    def print_employees(self):
        for employee in self.employees:
            print(employee.name)
    
    def checkin(self):
        return True
    
    def checkout(self):
        return False

#CEO Class

class Ceo(Employee):
    def __init__(self, name, id, position = "CEO"):
        super().__init__(name, id)
        self.position = position

    def __str__(self):
        return super().__str__() + f" Position: {self.position}"
    
    def coordinate_projects(self):
        print(f"{self.name} is coordinating all the projects in the company.")


#Project Manager Class

class ProjectManager(Employee):
    def __init__(self, name, id, position = "Project Manager", project: str = None):
        super().__init__(name, id)
        self.position = position
        self.project = project

    def __str__(self):
        return super().__str__() + f" Position: {self.position}"
    
    def coordinate_project(self):
        if self.project == None:
            return f"{self.name} is not coordinating any project at the moment."
        else:
            return f"{self.name} is coordinating the {self.project} project."

#Programmer Class

class Programmer(Employee):
    def __init__(self, name, id, language, position = "Programmer"):
        super().__init__(name, id)
        self.language = language
        self.position = position

    def __str__(self):
        return super().__str__() + f" Position: {self.position}"
    
    def code(self):
        print(f"{self.name} is programming in {self.language}.")

    def add(self, employee: Employee):
        print(
            f"A programmer doesn't have employees under them. {employee.name} won't be added.")


#try

jack = Ceo("Jack Donovan", 231)

jill = ProjectManager("Jill Valentine", 563)

jhoao = Programmer("Jhoao Fajardo", 502, "Python")
print(jhoao)

jack.add(jill)
jill.add(jhoao)
jhoao.add(jill)

jack.coordinate_projects()

print(jill)
print(jill.coordinate_project())
jill.project = "Restaurant"
print(jill.coordinate_project())

jhoao.code()

print(jhoao.checkin())
print(jill.checkout())