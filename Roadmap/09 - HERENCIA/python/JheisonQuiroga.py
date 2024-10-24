# Superclase
class Animal:
    def __init__(self, name):
        self.name = name

    def sound(self):
        pass
    

# Herencia
# Subclase    
class Dog(Animal):
    def __init__(self, name, kind):
        super().__init__(name)
        self.kind = kind

    # Polimorfismo
    def sound(self):
        print("Guau!")


class Cat(Animal):
    def __init__(self, name, kind):
        super().__init__(name)
        self.kind = kind

    def sound(self):
        print("Miau!")


d1 = Dog("Tobby", "Yorkshire")        
c1 = Cat("Lucas", "Desconocido")


for obj in (d1, c1):
    print(obj.name, obj.kind)
    obj.sound()


"""
Extra
"""

class Employee:
    def __init__(self, id, firstname, lastname):
        self.id = id
        self.firstname = firstname
        self.lastname = lastname

class Manager(Employee):
    def __init__(self, id, firstname, lastname):
        super().__init__(id, firstname, lastname)
        self.role = "Manager"
        self.employee_in_charge = []

    def add_employee_in_charge(self, employee):
        self.employee_in_charge.append(employee)

class ProjectManager(Employee):
    def __init__(self, id, firstname, lastname):
        super().__init__(id, firstname, lastname)
        self.projects = []

    def add_project(self, project):
        self.projects.append(project)


class Developer(Employee):
    def __init__(self, id, firstname, lastname, language):
        super().__init__(id, firstname, lastname)
        self.language = language

    def code(self):
        print(f"{self.firstname} is programming in {self.language}")

# Creando instancias de los colaboradores

manager = Manager("001", "Duban", "Quiroga")
print(manager.id, manager.firstname, manager.lastname, manager.role)
p_man = ProjectManager("002", "Toji", "Fushiguro")
p_man.add_project("Project1")
print(p_man.id, p_man.firstname, p_man.lastname)
print(p_man.projects)
developer1= Developer("003", "Gojo", "Satoru", "Python")
developer2 = Developer("004", "Suguru", "Geto", "Java")

for obj in (p_man, developer1, developer2):
    manager.add_employee_in_charge(obj)

for empl in manager.employee_in_charge:
    print(f"Employee in charge: {empl.firstname} {empl.lastname}, ID: {empl.id}")