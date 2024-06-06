#Definir clase padre
class Animal():   
    def __init__(self, especie: str, edad: int):
        self.especie= especie
        self.edad = edad
    
    def __str__(self):
        msg = f"Clase de animal: {self.especie.capitalize()}\nEdad: {self.edad}"
        return msg

#Clases Hijas de Animal
class Perro(Animal):   
    def hacer_sonido(self):
        return "Guau Guau Guau!!"


class Gato(Animal):    
    def hacer_sonido(self):
        return "miauuu"


    
perro = Perro("perro", 14)
print(perro)
print(perro.hacer_sonido())

gato = Gato("siames", 5)
print(gato)
print(gato.hacer_sonido())
print()

###############################################################################
## Dificulatad Extra
###############################################################################
class BusinessEmployee:
    def __init__(self, employee_id: int, name: str):
        self.employee_id = employee_id
        self.name = name
        self._salary = 1000

    def __str__(self):
        return f"Employee name: {self.name.capitalize()}\nIdentifying: {self.employee_id}\nSalary: {self._salary}"

class Manager(BusinessEmployee):
    def __init__(self, employee_id: int, name: str):
        super().__init__(employee_id, name)
        self._salary = 3000
        self._subordinates = []

    def add_subordinate(self, subordinate):
        self._subordinates.append(subordinate)
    
    def __str__(self):
        if self._subordinates:
            subordinates_str = ", ".join(subordinate.name for subordinate in self._subordinates)
            return super().__str__() + f"\nSubordinates: {subordinates_str}"
        

class ProjectManager(BusinessEmployee):
    def __init__(self, employee_id: int, name: str):
        super().__init__(employee_id, name)
        self._salary = 6000
        self._subordinates = [] 
        
    def add_subordinate(self, subordinate):
        self._subordinates.append(subordinate)
    
    def __str__(self):
        if self._subordinates:
            subordinates_str = ", ".join(subordinate.name for subordinate in self._subordinates)
            return super().__str__() + f"\nSubordinates: {subordinates_str}"


class Programmer(BusinessEmployee):
    def __init__(self, employee_id: int, name: str):
        super().__init__(employee_id, name)
        self._salary = 1500


# Pruebas
print()
employee_one = BusinessEmployee(1, "Daniel")
print(employee_one)
print()

manager_one = Manager(2, "Alice")
manager_one.add_subordinate(employee_one)
print(manager_one)
print()

programmer_one = Programmer(4, "Charlie")
print(programmer_one)
programmer_two = Programmer(5, "Eduardo")
print()

project_manager_one = ProjectManager(3, "Bob")
project_manager_one.add_subordinate(programmer_one)
project_manager_one.add_subordinate(programmer_two)
print(project_manager_one)
print()
