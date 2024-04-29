"""
* EJERCICIO:
 * Explora el concepto de herencia según tu lenguaje. Crea un ejemplo que
 * implemente una superclase Animal y un par de subclases Perro y Gato,
 * junto con una función que sirva para imprimir el sonido que emite cada Animal.
 *
 * DIFICULTAD EXTRA (opcional):
 * Implementa la jerarquía de una empresa de desarrollo formada por Empleados que
 * pueden ser Gerentes, Gerentes de Proyectos o Programadores.
 * Cada empleado tiene un identificador y un nombre.
 * Dependiendo de su labor, tienen propiedades y funciones exclusivas de su
 * actividad, y almacenan los empleados a su cargo.
"""
#Crear la superclase Animal
class Animal():
    
    def __init__(self, name: str, age: int, color: str):
        self.name = name
        self.age = age
        self.color = color
    
#Crer la subclase Perro y Gato que heredan de la clase Animal
class Perro(Animal):
    
    def __init__(self, name: str, age: int, color: str, race: str):
        super().__init__(name, age, color)
        self.race = race
        
    def bark(self):
        print(f"{self.name} started to bark")
        
    def features(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Race: {self.race}")
        print(f"Color: {self.color}")
        
        
class Gato(Animal):
    
    def __init__(self, name: str, age: int, color: str, race: str):
        super().__init__(name, age, color)
        self.race = race
        
    def meow(self):
        print(f"{self.name} started to meow")
        
    def features(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Race: {self.race}")
        print(f"Color: {self.color}")
        
#Instanciar objetos de clase
rex = Perro("Rex", 10, "Brown", "German Shepherd")
tom = Gato("Tom", 7, "Grey", "Russina Blue")

rex.features()
rex.bark()

tom.features()
tom.meow()




#-----EXTRA-----

#Crear superclase Employee

class Employee():
    
    def __init__(self, employee_id: int, name: str, surname: str, level: str, salary: int):
        self.employee_id = employee_id
        self.name = name
        self.surname = surname
        self.level = level
        self.salary = salary
        
    def data(self):
        print(f"Employee ID: {self.employee_id}")
        print(f"Name: {self.name}")
        print(f"Surname: {self.surname}")
        print(f"Level: {self.level}")
        print(f"Salary: {self.salary}$")

       
#Crear subclases Manager, ProjectManager y Developer que heredan de la superclase Employee

class Manager(Employee):
    
    def __init__(self, employee_id: int, name: str, surname: str, level: str, salary: int, position: str):
        super().__init__(employee_id, name, surname, level, salary)
        self.position = position
        self.pm_list = []
        self.dev_list = []
        
    def hire_employee(self, new_employee):
        if new_employee.level.lower() == "pm":
            self.pm_list.append(new_employee)
            print(f"¡¡Welcome to the team {new_employee.name} {new_employee.surname} as Project Manger!!\n")
        elif new_employee.level.lower() == "dev":
            self.dev_list.append(new_employee)
            print(f"¡¡Welcome to the team {new_employee.name} {new_employee.surname} as Developer!!\n")
        else:
            print("We are not hiring people with your skills. Thanks for your time.\n")
            
    def fire_employee(self, employee):
        if employee in self.pm_list:
            self.pm_list.remove(employee)
            print(f"{employee.name} {employee.surname} thank you for your work.\n")
        elif employee in self.dev_list:
            self.dev_list.remove(employee)
            print(f"{employee.name} {employee.surname} thank you for your work.\n")
        else:
            print("The employee doesn't exsist.")
        
    def assign_project(self, pm_id, project):
        for team_member in self.pm_list: 
            if team_member.employee_id == pm_id:
                print(f"{team_member.name} {team_member.surname} is assign to: {project}\n")
                return
        print(f"¡¡ERROR!! No existe un empleado con el id {pm_id}.\n")
        
    def show_employees(self):
        print("Project Manager List:\n")
        for pm in (self.pm_list):
            pm.data()
            print()

        print("Developers List:\n")
        for dev in (self.dev_list):
            dev.data()
            print()
    
    def manager_data(self):
        self.data()
        print(f"Position: {self.position}\n")
            
class ProjectManager(Employee):
    
    def __init__(self, employee_id: str, name: str, surname: str, level: str, salary: int, projects: str):
        super().__init__(employee_id, name, surname, level, salary)
        self.projects = projects
        self.project_team = []
        
    def show_project(self):
        print(f"{self.name} is on charge of the {self.projects} project.\n")
        
    def add_project_employee(self, new_developer, projects):
        self.project_team.append(new_developer)
        print(f"{self.name}: ¡¡Welcome {new_developer.name} to the {projects} project!!\n")
        
    def show_team(self):
        print(f"Team {self.projects}\n")
        print(f"Project Manager: {self.name} {self.surname}\n")
        print("Developers:\n")
        for project_member in self.project_team:
            print(f"Name: {project_member.name}")
            print(f"Surname: {project_member.surname}")
            print(f"Level: {project_member.level}\n")
            
class Developer(Employee):
    
    def __init__(self, employee_id: int, name: str, surname: str, level: str, salary: int, languages: list):
        super().__init__(employee_id, name, surname, level, salary)
        self.languages = languages
        
    def new_functionality(self, code_language):
        for language in self.languages:
            if language.lower() == code_language.lower():
                print(f"{self.name} {self.surname} is developing a new functionality in {code_language}.")
                return
        print(f"{self.name} {self.surname}: We need a new {code_language} developer.")
            
    def fix_bug(self,bug: str):
        print(f"{self.name} {self.surname} is working on the issue '{bug}'.")
        


#Instanciar clases 

dev_01 = Developer(21, "Miguel", "Ciriano", "Dev", 30000, ["Python", "SQL"])
dev_02 = Developer(22, "Gabriel", "Rojo", "Dev", 30000, ["JS", "SQL"])
dev_03 = Developer(23, "Ana", "García", "Dev", 30000, ["Rust", "JS","HTML", "CSS"])
dev_04 = Developer(24, "Beatriz", "Mandel", "Dev", 30000, ["TypeScrip", "Java"])
dev_05 = Developer(25, "Pedro", "Zamora", "Dev", 30000, ["Java", "SQL", "JS", "HTML", "CSS"])


pm_01 = ProjectManager(31, "Juanito", "Pérez", "PM", 50000, "Backend")
pm_02 = ProjectManager(32, "Alfonso", "Molinero", "PM", 50000, "UX/UI")
pm_03 = ProjectManager(33, "Rodrigo", "Salta", "PM", 50000, "Frontend")
pm_04 = ProjectManager(34, "Valeria", "Araya", "PM", 50000, "Marketing")
pm_05 = ProjectManager(35, "Susana", "Jara", "PM", 50000, "Sales")

designer = Employee(41, "Juan", "Lorca", "Dsgn", 30000)

manager_01 = Manager(1, "Elon", "Musk", "CEO", 100000, "Management")

#Funcionalidades de la clase Manager
manager_01.hire_employee(dev_01)
manager_01.hire_employee(dev_02)
manager_01.hire_employee(dev_03)
manager_01.hire_employee(dev_04)
manager_01.hire_employee(dev_05)

manager_01.hire_employee(designer)

manager_01.hire_employee(pm_01)
manager_01.hire_employee(pm_02)
manager_01.hire_employee(pm_03)
manager_01.hire_employee(pm_04)
manager_01.hire_employee(pm_05)

manager_01.show_employees()

manager_01.fire_employee(dev_03)
manager_01.fire_employee(pm_03)

manager_01.show_employees()

manager_01.assign_project(35, "Sales")
manager_01.assign_project(32, "UX/UI")
manager_01.assign_project(4, "UX/UI")

manager_01.manager_data()

#Funcionalidades de la clase Project Manager
pm_01.show_project()
pm_05.add_project_employee(dev_05, "Sales")
pm_05.add_project_employee(dev_03, "Sales")

pm_05.show_team()

#Funcionalidades de la clase Developer

dev_01.new_functionality("PYTHON")
dev_01.new_functionality("HTML")

dev_03.fix_bug("Cancelation order")
