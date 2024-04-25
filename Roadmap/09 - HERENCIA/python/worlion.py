"""
    HERENCIA EN PYTHON
"""
# Clase animal (superclase)
class Animal:
    nombre = ""
    sonido = ""
    icono = ""
    
    def __init__(self, nombre = "", sonido="", icono = "❓") -> None:
        self.nombre = nombre
        self.sonido = sonido
        self.icono = icono

    def hacer_sonido(self):
        print(f"el {self.nombre} hace: {self.sonido} {self.icono}")        

# Clase perro (subclase)
class Perro(Animal):
    def __init__(self) -> None:
        super().__init__("Perro", "guau!", "🐶")
        
# Clase gato (subclase)
class Gato(Animal):
    def __init__(self) -> None:
        super().__init__("Gato", "miau!", "🐱")
        
myDog = Perro()
myDog.hacer_sonido()
        
myCat = Gato()
myCat.hacer_sonido()

"""
DIFICULTAD EXTRA (opcional): Empleados
"""

print("\n ---- 🌩 DIFICULTAD EXTRA 🌩 ----\n")

class Employee:
    
    def __init__(self, id: int, name: str ) -> None:
        self.id = id
        self.name = name
        self.employees_in_charge = []
    
    def add_employee(self, employee):
        if isinstance(employee, Employee):
            self.employees_in_charge.append(employee)
        else:
            print("Invalid Employee")
        
    def print_self(self):
        print(f" - Empleado: id = {self.id} ; nombre = {self.name} ; empleados a cargo = {len(self.employees_in_charge)}" )
        
    def print_employees(self):
        if(len(self.employees_in_charge) > 0):
            print(f"Empleados a cargo de {self.name}")
            for employee in self.employees_in_charge:
                employee.print_self()
            print("\n")

class Manager(Employee):
    
    def print_self(self):
        print(f" - Manager 😈: id = {self.id} ; nombre = {self.name} ; empleados a cargo = {len(self.employees_in_charge)}")
        
    def ask_something(self):
        print(f"Lo siento, {self.name} es demasiado importante y está demasiado ocupado")

class ProyectManager(Employee):
    
    proyects: list[str]
    
    def __init__(self, id: int, name: str, proyects: list[str] = None) -> None:
        super().__init__(id, name)
        if proyects is None:
            self.proyects = []
        else:
            self.proyects = proyects
    
    def print_self(self):
        print(f" - ProyectManager 🤓: id = {self.id} ; nombre = {self.name} ; empleados a cargo = {len(self.employees_in_charge)} ; proyectos a cargo = {len(self.proyects)}")
    
    def add_proyect(self, proyect: str):
        self.proyects.append(proyect)

class Developer(Employee):

    def __init__(self, id: int, name: str, languages: list[str]) -> None:
        super().__init__(id, name)
        self.languages = languages
    
    def add_language(self,language: str):
        self.languages.append(language)
    
    def print_self(self):
        print(f" - Developer 👨‍💻: id = {self.id} ; nombre = {self.name} ; lenguajes: {self.languages}")
    
    def add_employee(self, employee):
        print("Un developer no tiene empleados a cargo")
        
minion1 = Developer(201, "Kevin", ["Python"])
minion1.add_language("Java")
minion1.print_self()

minion2 = Developer(202, "Stuart", ["PHP", "Lisp"])
minion3 = Developer(203, "Jerry", ["Haskel", "Rust", "C#"])
minion2.print_self()
minion3.print_self()

lieutenant1 = ProyectManager(101, "O'Neil", ["proyecto caca"])
lieutenant1.add_employee(minion1)
lieutenant1.add_employee(minion2)
lieutenant1.add_proyect("otro")
lieutenant2 = ProyectManager(102, "Ripley", ["TOP SECRET"])
lieutenant2.add_employee(minion3)
lieutenant1.print_self()
lieutenant1.print_employees()
lieutenant2.print_self()
lieutenant2.print_employees()

the_king = Manager(1, "Jaffe Joffer")
the_king.add_employee(lieutenant1)
the_king.add_employee(lieutenant2)

the_king.print_self()