'''
  EJERCICIO
'''

class Animal:
  def __init__(self, name, race):
    self.name = name
    self.race = race

  def __str__(self):
    return f'Nombre: {self.name}, Raza: {self.race}'  

class Dog(Animal):
  def __init__(self, name, race):
    super().__init__(name, race)

  def sound(self):
    print(f"{self.name} ladrando!!")

class Cat(Animal):
  def __init__(self, name, race):
    super().__init__(name, race)

  def sound(self):
    print(f"{self.name} maullando!!")

def animalSound(animal):
  animal.sound()


manchas = Cat("Manchas", "Calicó")
firulais = Dog("Firulais", "Labrador")


print(f'Manchas: {manchas.__str__()}')
animalSound(manchas)
print(f'Manchas es un perro?: {isinstance(manchas, Dog)}')
print(f'Manchas es un gato?: {isinstance(manchas, Cat)}')
print(f'Manchas es un animal?: {isinstance(manchas, Animal)}')
print(f'Firulais: {firulais.__str__()}')
animalSound(firulais)
print(f'Firulais es un perro?: {isinstance(firulais, Dog)}')
print(f'Firulais es un gato?: {isinstance(firulais, Cat)}')
print(f'Firulais es un animal?: {isinstance(firulais, Animal)}')

'''
  EXTRA
'''

class Employee:
  def __init__(self, id, name):
    self.id = id
    self.name = name

  def job(self):
    return "Executing assigned tasks"

class Manager(Employee):
  def __init__(self, id, name, employees):
    super().__init__(id, name)
    self.employees = employees

  def job(self):
    return "Management"

class ProjectManager(Manager):
  def __init__(self, id, name, employees):
    super().__init__(id, name, employees)

  def job(self):
    return "Managing project"

class Programmer(Employee):
  def __init__(self, id, name):
    super().__init__(id, name)

  def job(self):
    return "Working on development"


emp_1 = Employee(1, "Santiago")
emp_2 = Employee(2, "Valentina")
emp_3 = Employee(3, "Camilo")
emp_4 = Employee(4, "Andrés")
emp_5 = Employee(5, "Alejandro")

pgr_1 = Programmer(11, "César")
pgr_2 = Programmer(12, "Christian")
pgr_3 = Programmer(13, "Sebastián")
pgr_4 = Programmer(14, "Miriam")
pgr_5 = Programmer(15, "Nicole")

project_employees = [emp_2, emp_4, emp_5, pgr_1, pgr_3,]

pmng = ProjectManager(101, "Leonardo", project_employees)

full_employees = [emp_1, emp_2, emp_3, emp_4, emp_5, pgr_1, pgr_2, pgr_3, pgr_4, pgr_5, pmng]

mng = Manager(1001, "Mauricio", [emp_1, emp_2, emp_4, ])

for employee in full_employees:
  print(f"{employee.id}. {employee.name}: {employee.job()}")

print("Project manager's employees:")
for employee in pmng.employees:
    print(F"- {employee.name}")

print(f"{mng.id}. {mng.name}: {mng.job()}")

