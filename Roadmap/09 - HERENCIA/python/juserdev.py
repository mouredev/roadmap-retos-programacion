""" /*
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
 */ """

'''
  ### HERENCIA ###
  
  ->  en este ejemplo simplemente crear una clase basica Animal que sirve para darle nombre al animal
      ademas retorna su nombre
  ->  cree dos herencias, una para perro y otra para gato
  ->  se heredan asi
      ->  class Perro(Aniaml): 
      ->  se debe poner la calse anterior como parametro de la nueva clase
      ->  cada uno tiene una fucnion clara adentro que retorna el nombre del aniaml y su sonido
          
          def perro(self):
            return f"mi nombre es {self.nombre} y ladro: Guau!"

  ->  De esta manera entendemos el concepto de Herencia

  ->  como Programer hereda las funciones de la superclase Employee tambien hereda la funcion add
      entonces en este caso creamos una funcion add especifica para Programer con el fin que no 
      haga lo que dice que debe hacer la superclase ya que esta es una subclase
  
  ->  La manera de heredar en la que las subclases herenda de las superclases basandonos en el ejemplo extra
      es de esta manera -> Manager(Employee), Manager hereda todas las funciones de Employee

'''

class Animal:
  def __init__(self, nombre):
    self.nombre = nombre
  
  def presentarse(self):
    return f"Me llamo {self.nombre}"
  
perro_1 = Animal("Lucas")

print(perro_1.nombre)
print(perro_1.presentarse())

class Perro(Animal):
  def perro(self):
    return f"mi nombre es {self.nombre} y ladro: Guau!"
  
class Gato(Animal):
  def gato(self):
    return f"mi nombre es {self.nombre} y maullo: Miau!"
  
perro_1 = Perro("Lucas")
gato = Gato("Michi")

print(perro_1.perro())
print(gato.gato())

### DIFICULTAD EXTRA ###

class Employee:

  def __init__(self, id: int, name: str):
    self.id = id
    self.name = name
    self.employess = []

  def add(self, employee):
    self.employess.append(employee)

  def print_employess(self):
    for employee in self.employess:
      print(employee.name)

class Manager(Employee):

  def coordinate_projects(self):
    print(f"{self.name} esta coordinando todos los proyectos de la empresa")

class ProjectManager(Employee):
  def __init__(self, id: int, name: str, project: str):
    super().__init__(id,name)
    self.project = project

  def coordinate_project(self):
    print(f"{self.name} esta coodinando su proyecto")

class Programer(Employee):
  def __init__(self, id: int, name: str, lenguage: str):
    super().__init__(id, name)
    self.lenguage = lenguage
  
  def code(self):
    print(f"{self.name} esta programando en {self.lenguage}")

  def add(self, employee: Employee):
    print(f"Un programador no tiene empleadosa su cargo. {employee.name} no se añadira")


my_manager = Manager(1, "Juserdev")
my_project_manager_1 = ProjectManager(2, "Juan", "proyecto 1")
my_project_manager_2 = ProjectManager(3, "Sebastian", "proyecto 2")
my_programer_1 = Programer(4,"Max", "Javascript")
my_programer_2 = Programer(5,"Laura", "Tavascript")
my_programer_3 = Programer(6,"Carlos", "Python")
my_programer_4 = Programer(7,"Pedro", "Java")

my_manager.add(my_project_manager_1)
my_manager.add(my_project_manager_2)

my_project_manager_1.add(my_programer_1)
my_project_manager_1.add(my_programer_2)
my_project_manager_2.add(my_programer_3)
my_project_manager_2.add(my_programer_4)

my_programer_2.add(my_programer_3)

my_programer_1.code()
my_project_manager_1.coordinate_project()
my_manager.coordinate_projects()

my_manager.print_employess()
my_project_manager_1.print_employess()
my_project_manager_2.print_employess()
my_programer_1.print_employess()