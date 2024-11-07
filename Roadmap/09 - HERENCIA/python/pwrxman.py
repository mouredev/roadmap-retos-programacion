"""
video en  https://youtu.be/PVBs5PWjedA?si=gkpzPPTm0WUjsXAJ
* EJERCICIO:
 * Explora el concepto de herencia según tu lenguaje. Crea un ejemplo que
 * implemente una superclase Animal y un par de subclases Perro y Gato,
 * junto con una función que sirva para imprimir el sonido que emite cada Animal.
 *
"""

class Animal:
    def __init__ (self, grupo: str, categoria: str, alimentacion: str, name: str):
          self.grupo = grupo        # Vertebrados, Invertebrados
          self.categoria = categoria    # vertebrados: Aves, Peces, Reptiles, Mamiferos     #invertebrados: Insectos,
          self.alimentacion = alimentacion      # Omnivoros, Herbivoros, Carnivoeros, Insectivoros
          self.name = name
          
    def sound(self):
        pass

class Dog(Animal):
  
    def sound(self):
          print("Guau!")

class Cat(Animal):
    def sound(self):
          print("Miau!")

def print_sound(animal: Animal):
  animal.sound()          

animal = Animal("V", "M", "C", "Animal")
animal.sound()

dog = Dog("M", "M", "C", "Perro")
dog.sound()

cat = Cat("M", "M", "C", "Cat")
cat.sound()
print("> > > > > > > > > > >")
print_sound(animal)
print_sound(dog)
print_sound(cat)


"""
* DIFICULTAD EXTRA (opcional):
 * Implementa la jerarquía de una empresa de desarrollo formada por Empleados que
 * pueden ser Gerentes, Gerentes de Proyectos o Programadores.
 * Cada empleado tiene un identificador y un nombre.
 * Dependiendo de su labor, tienen propiedades y funciones exclusivas de su
 * actividad, y almacenan los empleados a su cargo.
"""
print("DIFICULTAD EXTRA\n")

class Employee:
    def __init__(self, id: str, name: str):
        self.id = id
        self.name = name
        self.employees = []

    def add(self, employee):
        self.employees.append(employee)

    def get_employees(self):
        print(f"los colabores de {self.name} son:")
        for employee in self.employees:
            print(employee.name)

class Manager(Employee):
    def coordina_proyectos(self):
        print(f"{self.name} esta coordinando los proyectos")

class ProjectManager(Employee):

    def __init__(self, id: str, name: str, project: str):
        super().__init__(id, name)    # reutiliza el inicialiador de la superclase
        self.project = project

    def coordina_proyecto(self):
        print(f"{self.name} esta coordinando un proyecto")

class Programmer(Employee):
    def __init__(self, id: str, name: str, language: str):
        super().__init__(id, name)    # reutiliza el inicialiador de la superclase
        self.language = language
    
    def code(self):
        print(f"{self.name} esta programando en {self.language}")
    
    def add(self, employee):
        print(f"{employee.name} No puede ser añadido porque {self.name} es programador y no puede tener empleados a su cargo")

mgr = Manager("mgr1", "Tony")
mgr2 = Manager("mgr2", "Katy")


pm = ProjectManager("pm1", "Chucho", "Project 1")
pm2 = ProjectManager("pm2", "Vic", "Project 2")

prgmr = Programmer("pr1", "Gonza", "Java")
prgmr2 = Programmer("pr2", "Luis", "Python")
prgmr3 = Programmer("pr3", "Vero", "C#")
prgmr4 = Programmer("pr4", "Pilar", "React")
prgmr5 = Programmer("pr5", "Mary", "Python")

mgr.add(pm)
mgr2.add(pm2)

pm.add(prgmr)
pm.add(prgmr2)
pm2.add(prgmr3)
pm2.add(prgmr4)
pm2.add(prgmr5)

prgmr.add(prgmr3)

prgmr2.code()

pm.coordina_proyecto()

mgr.coordina_proyectos()

mgr.get_employees()
mgr2.get_employees()

pm.get_employees()
pm2.get_employees()

