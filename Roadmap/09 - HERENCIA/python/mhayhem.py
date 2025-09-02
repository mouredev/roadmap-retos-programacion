import random

# EJERCICIO:
# Explora el concepto de herencia según tu lenguaje. Crea un ejemplo que
# implemente una superclase Animal y un par de subclases Perro y Gato,
# junto con una función que sirva para imprimir el sonido que emite cada Animal.

class Animal:
    def __init__(self, name):
        self.name = name.capitalize()
        def sound():
            pass

class Dog(Animal):
    def sound(self):
        return f"{self.name} hace guau!."

class Cat(Animal):
    def sound(self):
        return f"{self.name} hace miau!."
    
# DIFICULTAD EXTRA (opcional):
# Implementa la jerarquía de una empresa de desarrollo formada por Empleados que
# pueden ser Gerentes, Gerentes de Proyectos o Programadores.
# Cada empleado tiene un identificador y un nombre.
# Dependiendo de su labor, tienen propiedades y funciones exclusivas de su
# actividad, y almacenan los empleados a su cargo.

class CompanyEmployee:
    def __init__(self, name:str):
        self.id = random.randint(100, 999)
        self.name = name
        self.employees = []
        
    def add_employee(self, employee):
        self.employees.append(employee)
        return self.employees
    
    def show_employee(self):
        if self.employees:
                return [f"{e.name}: {e.rol}" for e in self.employees]
        else:
            return "No tiene empleados a su cargo."
    
    def work(self, project):
        return f"{self.name} comienza {project}"
    
    def __str__(self):
        return f"{self.name} ({self.id}: {self.rol})"
    
        
class Chief(CompanyEmployee):
    def __init__(self, name, department: str):
        super().__init__(name)
        self.rol = "ceo"
        self.department = department
    
    def evaluate_employee(self):
        if self.employees:
            return [f"Evaluación del empleado {e.name} con ID {e.id}, ha sido positiva." for e in self.employees]
        else:
            return "No hay empleados a cargo."
    
    def assing_task(self):
        if self.employees:
            task_to_do = []
            for e in self.employees:
                match e.rol:
                    case "developer":
                        task_to_do.append(f"Sr. {e.name} factorice el codigo del producto.")
                    case "project manager":
                        task_to_do.append(f"Sr. {e.name} presente informe del producto.")
            return task_to_do
        else:
            return f"No hay empleados a su cargo."
    
class ProjectManager(CompanyEmployee):
    def __init__(self, name, current_project: str):
        super().__init__(name)
        self.rol = "project manager"
        self.current_project = current_project
        
    def sprint_planning(self):
        if self.employees:
            return [f"{e.name} fecha final del sprint en dos semanas." for e in self.employees]
        else:
            return "No hay empleados a cargo."
    
    def report_progress(self, project: str, percentage: int):
        return f"La app '{project}' esta al {percentage} %."
    

class Developer(CompanyEmployee):
    def __init__(self, name, level: str):
        super().__init__(name)
        self.rol = "developer"
        self.level = level
        self.languages = []
        
    def dev_languages(self, *args):
        for item in args:
            self.languages.append(item)
    
    def show_languages(self):
        return f"Conocimiento de los siguientes lenguajes/frameworks: {self.languages}."
    
    def click_code(self):
        return f"desarrollaror {self.name} empieza a picar código."