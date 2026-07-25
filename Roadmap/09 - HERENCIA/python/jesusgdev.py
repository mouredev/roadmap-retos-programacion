'''
 * EJERCICIO:
 * Explora el concepto de herencia según tu lenguaje. Crea un ejemplo que
   implemente una superclase Animal y un par de subclases Perro y Gato,
   junto con una función que sirva para imprimir el sonido que emite cada Animal.
  
 * DIFICULTAD EXTRA (opcional):
 * Implementa la jerarquía de una empresa de desarrollo formada por Empleados que
   pueden ser Gerentes, Gerentes de Proyectos o Programadores.
 * Cada empleado tiene un identificador y un nombre.
 * Dependiendo de su labor, tienen propiedades y funciones exclusivas de su
   actividad, y almacenan los empleados a su cargo.
'''

class Animal:
    def __init__(self, name):
        self.name = name
    
    def sound(self):
        pass


class Dog(Animal):
    def __init__(self, name):
        super().__init__(name)

    def sound(self):
        print(f"Este es un perro, su nombre es {self.name}, y hace gua,gua!")

dog = Dog("Marcus")
dog.sound()

class Cat(Animal):
    def __init__(self, name):
        super().__init__(name)

    def sound(self):
        print(f"Este es un gato, su nombre es {self.name}, y hace miau,miau!")

cat = Cat("Snow")
cat.sound()
print("")
'''
Extra
'''

# Clase base para todos los empleados
class Employee:
    def __init__(self, id, name):
        # Atributos comunes: identificación y nombre
        self.id = id
        self.name = name
        
    # Muestra la lista de empleados que han sido contratados
    def employees_list(self):
        for employee in self.employees:
            print(f"ID: {employee.id} | Empleado: {employee.name}")

    # Método base para contratar (solo para que exista, lo usaremos en Manager)
    def hire_employee(self, id, name, position, language):
        pass

# Clase Manager, hereda de Employee
class Manager(Employee):
    def __init__(self, id, name):
        super().__init__(id, name)  # Llama al constructor de Employee
        self.employees = []  # Lista de todos los empleados contratados
        self.project_name = ""  # Nombre del proyecto que administra
        self.projects_info = {}  # Diccionario {proyecto: director}
        self.team_projects_info = {}  # Diccionario {proyecto: [empleados]}
        self.position = ""  # Rol del empleado (ProjectManager o Programador)
        self.projectmanagers = []  # Lista de ProjectManager contratados
        self.programmers = []  # Lista de programadores contratados
        self.language = ""  # Lenguaje del programador (opcional)


    # Contrata a un nuevo empleado según su posición
    def hire_employee(self, id, name, position, language = None):
        if position == "ProjectManager":
            # Crea un ProjectManager y lo agrega a las listas
            new_employee = ProjectManager(id, name)
            self.employees.append(new_employee)
            self.projectmanagers.append(new_employee)

        elif position == "Programador":
            # Crea un Programador y lo agrega a las listas
            new_employee = Programmer(id, name, language)        
            self.employees.append(new_employee)
            self.programmers.append(new_employee)
        
        print(f"{name} ha sido contratado/a como {position}")

    # Muestra los ProjectManager contratados
    def projectmanagers_list_info(self):
        if len(self.projectmanagers) == 0:
            print("\nNo se han contratado directores de proyecto aun")
        else:
            print("\nLista de ProjectManagers contratados:")
            for projectmanager in self.projectmanagers:
                print(f"ID: {projectmanager.id} | Name: {projectmanager.name}")

    # Muestra los programadores contratados
    def programmers_list_info(self):
        if len(self.programmers) == 0:
            print("\nNo se han contratado programadores aun")
        else:
            print("\nLista de Programadores contratados:")
            for programmer in self.programmers:
                print(f"ID: {programmer.id} | Name: {programmer.name} | Language: {programmer.language}")
    
    # Asigna un proyecto a un ProjectManager
    def assign_project(self, name, project_name):
        if name not in self.projects_info.values():
            if project_name not in self.projects_info.keys():
                self.projects_info[project_name] = name
                print(f'{name} ha sido asignado a dirigir el proyecto "{project_name}"')
            else:
                print(f"El proyecto {project_name} ya fue asignado a otro empleado")
        else:
            print(f"Ya el empleado {name} tiene un proyecto asignado")

    # Muestra qué empleado dirige qué proyecto
    def show_project_info(self):
            print("")
            print("Informacion actual de Proyectos:")
            for project, emplooye in self.projects_info.items():
                print(f"{emplooye} esta dirigiendo el proyecto {project}")


    # Asigna programadores a un proyecto
    def assing_team_project(self, name, project_name):
        # Verifica si el programador ya está en otro proyecto
        for project, team in self.team_projects_info.items():
            if name in team:
                if project == project_name:
                    print(f"{name} ya esta trabajando actualmente en el proyecto {project_name}")
                else:
                    print(f"{name} ya esta trabajando en otro proyecto ({project})")
                return  # Detiene el proceso, no se vuelve a asignar

        # Si no existe el proyecto en el diccionario, se crea
        if project_name not in self.team_projects_info:
            self.team_projects_info[project_name] = []

        # Se agrega el programador al proyecto
        self.team_projects_info[project_name].append(name)
        print(f"{name} ha sido asignado a trabajar en el proyecto {project_name}")
    
    # Muestra todos los proyectos con su equipo asignado
    def show_team_project_info(self):
        print("")
        print("Informacion de equipos de proyectos:")
        for project, emplooyes in self.team_projects_info.items():
            for emplooye in emplooyes:
                print(f"{emplooye} esta trabajando en el proyecto {project}")

# Clase ProjectManager, hereda de Employee            
class ProjectManager(Employee):
    def __init__(self, id, name):
        super().__init__(id, name)

# Clase Programmer, hereda de Employee
class Programmer(Employee):
    def __init__(self, id, name, language):
        super().__init__(id, name)
        self.language = language


my_manager = Manager(1, "Jesus")

my_manager.hire_employee(2, "John", "ProjectManager")
my_manager.hire_employee(3, "Andrew", "ProjectManager")

my_manager.hire_employee(4, "Sam", "Programador", "Java")
my_manager.hire_employee(5, "Laura", "Programador", "Python")
my_manager.hire_employee(6, "Michael", "Programador", "Javascript")
my_manager.hire_employee(7, "Louis", "Programador", "C")


my_manager.projectmanagers_list_info()
my_manager.programmers_list_info()

print("")

my_manager.assign_project("John", "Gestor Clinica Santa Maria")
my_manager.assign_project("John", "Aplicacion Movil Banco Globalbank")
my_manager.assign_project("Andrew", "Aplicacion Movil Banco Globalbank")

my_manager.show_project_info()

my_projectmanager1 = ProjectManager("2", "John")
my_projectmanager2 = ProjectManager("3", "Andrew")

print("")

my_manager.assing_team_project("Sam", "Gestor Clinica Santa Maria")
my_manager.assing_team_project("Laura", "Gestor Clinica Santa Maria")
my_manager.assing_team_project("Michael", "Aplicacion Movil Banco Globalbank")
my_manager.assing_team_project("Louis", "Aplicacion Movil Banco Globalbank")

my_manager.show_team_project_info()

print("")

my_manager.employees_list()
