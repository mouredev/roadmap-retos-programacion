# /*
#  * EJERCICIO:
#  * Explora el concepto de herencia según tu lenguaje. Crea un ejemplo que
#  * implemente una superclase Animal y un par de subclases Perro y Gato,
#  * junto con una función que sirva para imprimir el sonido que emite cada Animal.
#  *
#  * DIFICULTAD EXTRA (opcional):
#  * Implementa la jerarquía de una empresa de desarrollo formada por Empleados que
#  * pueden ser Gerentes, Gerentes de Proyectos o Programadores.
#  * Cada empleado tiene un identificador y un nombre.
#  * Dependiendo de su labor, tienen propiedades y funciones exclusivas de su
#  * actividad, y almacenan los empleados a su cargo.
#  */

class Animal:

    def __init__(self,name,age):
        self.name = name
        self.age = age

    
    def greetings(self):
        return f'Hi, Im {self.name} the {type(self).__name__}, Im {self.age} years old'
    
    def communicate():
        pass

class Dog(Animal):
    
    def communicate(self):
        return "Woof!"


class Cat(Animal):

    def communicate(self):
        return 'Meow!'


yoel = Animal('yoel',3)
marko = Dog('marko',5)
yuri = Cat("yuri",5)
print(yoel.greetings())
print(marko.greetings())
print(yuri.greetings())
print(marko.communicate())
print(yuri.communicate())

#extra

class Employee:

    def __init__(self,name,idd):
        self.name =  name
        self.id = idd
        self.employees = []
    
    def add_employee(self,employee):
        self.employees.append(employee)

    def supervising(self):
        print(f'{self.name} esta supervisando a {self.employees}')

    def print_employees(self):
        for i in self.employees:
            print(i.name)
class Manager(Employee):

      
    def coordinate_projects(self):
        print(f'{self.name} Esta Coordinando los proyectos de la empresa')

class ProjectManager(Employee):

    def __init__(self, name, id,project):
        super().__init__(name, id)
        self.proyect = project

    def coordinate_projects(self):
        print(f'{self.name} Esta Coordinando sus proyectos')

class Developer(Employee):

    def __init__(self, name, id,language):
        super().__init__(name, id)
        self.language = language

    def code(self):
        print(f'{self.name} Esta escribiendo codigo en {self.language}')

    def add_employee(self,employee):
        print(f"Programador no puede agregar porque no puede tener a empleados a su cargo")

manager = Manager('raul',1000)
project_manager = ProjectManager("carlos",2000,'project1')
project_manager_2 = ProjectManager("juan",3000,'project2')
developer = Developer("yoel",4000,'java')
developer_2 = Developer("yoel",5000,'javascript')
manager.add_employee(project_manager)
manager.add_employee(project_manager_2)
project_manager.add_employee(developer)
project_manager_2.add_employee(developer_2)
manager.supervising()
manager.coordinate_projects()
manager.print_employees()
project_manager.print_employees()
developer.add_employee(developer_2)