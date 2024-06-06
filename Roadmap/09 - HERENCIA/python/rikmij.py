class Animal:
    patas = 4
    cola = True
    
    def talk(self):
        pass

class Perro(Animal):
    def talk(self):
        return "<Guau>"

class Gato(Animal):
    def talk(self):
        return "<Miau>"

canino = Perro()
print(canino.talk())
print(canino.patas)

michi = Gato()
print(michi.talk())
print(michi.cola)


print('\n', '~'*7, "EJERCICIO EXTRA", '~'*7)

class Employee:
    def __init__(self, name, id, employment, employee):
        self.name = name
        self.id = id
        self.employment = employment
        self.employee = employee
    
    def meet_employee(self):
        return f"{self.name}: id - {self.id}"
    
    def get_employees(self):
        print(f"\n-> {self.name} está a cargo de:")
        for employ in self.employee:
            print(f"{employ.name} ({employ.employment}): id - {employ.id}")

class Programmer(Employee):
    def __init__(self, name, id, employment, language, employee):
        super().__init__(name, id, employment, employee)
        self.language = language
    
    def work(self):
        return f"{self.name}: Estoy trabajando en {self.language}"

class ProjectManager(Employee):
    def __init__(self, name, id, employment, employee, project):
        super().__init__(name, id, employment, employee)
        self.project = project
    
    def supervise(self):
        return f"{self.name}: Estoy \"supervisando\" {self.project}. ¿Cómo vais muchachos?"
    
class Manager(Employee):
    def __init__(self, name, id, employment, employee, organization):
        super().__init__(name, id, employment, employee)
        self.organization = organization
    
    def organize(self):
        return f"{self.name}: Estoy organizando {self.organization}"
    
victor = Programmer("Víctor", 11, "Programador", "Python", [])
joel = Programmer("Joel", 12, "Programador", "Kotlin", [])
print(victor.work())
print(joel.meet_employee())

programmer_list = []
programmer_list.append(victor)
programmer_list.append(joel)

giovanni = ProjectManager("Giovanni", 13, "Project Manager", programmer_list, "COBOL Multiplatform")
giovanni.get_employees()
print(giovanni.supervise())

boss_list = []
for emp in programmer_list:
    boss_list.append(emp)
boss_list.append(giovanni)

guido = Manager("Guido Van Rossum", 14, "Manager", boss_list, "Python")
guido.get_employees()
print(guido.organize())
