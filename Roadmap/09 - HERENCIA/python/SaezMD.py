#09 Herencia
"""
 * EJERCICIO:
 * Explora el concepto de herencia según tu lenguaje. Crea un ejemplo que implemente una superclase Animal y un par de subclases Perro y Gato,
 * junto con una función que sirva para imprimir el sonido que emite cada Animal.
 *
 * DIFICULTAD EXTRA (opcional):
 * Implementa la jerarquía de una empresa de desarrollo formada por Empleados que pueden ser Gerentes, Gerentes de Proyectos o Programadores.
 * Cada empleado tiene un identificador y un nombre.
 * Dependiendo de su labor, tienen propiedades y funciones exclusivas de su actividad, y almacenan los empleados a su cargo.
"""
#Superclase:
class Animal():
    def __init__(self, name: str) -> None:
        self.name = name
    
    def talk(self):
        pass


#Subclases:
class Dog(Animal):
    def talk(self):
        print("¡GUAU!")

class Cat(Animal):
    def talk(self):
        print("¡MIAU!")

myDog = Dog("Perrito")
myDog.talk()

myCat = Cat("Micho")
myCat.talk()

#polimorfismo
def printSound(animal: Animal):
    animal.talk()

myAnimal = Animal("Animal")
printSound(myAnimal)
myDog = Dog("Perrito Caliente")
printSound(myDog)
myCat = Cat("bisbi")
printSound(myCat)


#EXTRA

class Employee():
    def __init__(self, idNumber: int, name: str):
        self.name = name
        self.id = idNumber
        self.employees = []
    
    def addEmployee(self, employee):
        self.employees.append(employee)

    def printAll(self):
        for employee in self.employees:
            print(employee.name)

class Manager(Employee):
    def budgetControl(self):
        return print(f"{self.name} is controlling the Budget")
    
    def resources(self):
        return print(f"{self.name} is organizating the resources")
    
class ProjectManager(Employee):
    def __init__(self, idNumber: int, name: str, project: str):
        super().__init__(idNumber, name)
        self.project = project 

    def peopleTasks(self):
        return print(f"{self.name} is controlling the people tasks")

class Programmer(Employee):

    def __init__(self, idNumber: int, name: str, language: str):
        super().__init__(idNumber, name)
        self.language = language

    def develop(self):
        return print(f"{self.name} is programming in: {self.language}.")
                     
    def coffee(self):
        return "make coffee"
    
    def addEmployee(self, employee: Employee):
        print(f"Programmer can't have employees. {employee.name} not added.")


myManager = Manager(1,"SaezMD")
myProjectManager = ProjectManager(2, "Antonio Marcelo", "Project 1")
myProjectManager2 = ProjectManager(3, "Barcelo", "Project 2")
myProgrammer = Programmer(4, "Carlos", "Python")
myProgrammer2 = Programmer(5, "Dario", "Kobol")
myProgrammer3 = Programmer(6, "Elena", "Go")
myProgrammer4 = Programmer(7, "Fran", "Java")

#add people:
myManager.addEmployee(myProjectManager)
myManager.addEmployee(myProjectManager2)

myProjectManager.addEmployee(myProgrammer)
myProjectManager.addEmployee(myProgrammer2)
myProjectManager2.addEmployee(myProgrammer3)
myProjectManager2.addEmployee(myProgrammer4)

myProgrammer.addEmployee(myProgrammer2)

myProgrammer.develop()
myProjectManager.peopleTasks()
myManager.budgetControl()

myManager.printAll()
myProjectManager.printAll()
myProgrammer.printAll()

