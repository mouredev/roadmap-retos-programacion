class Animal:
  def __init__(self, name, sound):
    self.name = name
    self.sound = sound
  
  def makeSound(self):
    print(f"{self.name} dice {self.sound}")

class Dog(Animal):
  def __init__(self, name):
    super().__init__(name, 'Woof')

class Cat(Animal):
  def __init__(self, name):
    super().__init__(name, "Meow")


myDog = Dog("Dolly")
myDog.makeSound()

myCat = Cat("Snowball")
myCat.makeSound()


# DIFICULTAD EXTRA

class Empleado:
  def __init__(self, id, name, tasks, staff):
    self.id = id
    self.name = name
    self.tasks = tasks
    self.staff = staff
  
  def makePresentation(self):
    print(f"Hola, mi nombre es {self.name}")

  def showTasksList(self):
    print(f"Lista de tareas: {self.tasks}")

  def showTeam(self):
    print(f"A cargo de: {self.staff}")

class Gerente(Empleado):
  def __init__(self, name):
    super().__init__('Gerente', name, {'Obtener clientes', 'Ventas'}, {'Gerente de Proyecto', 'Programador'})

class GerenteDeProyecto(Empleado):
  def __init__(self, name):
    super().__init__('Gerente de Proyecto', name, {'Gestionar proyectos', 'Crear tickets', 'Agendar meets'}, {'Programador'})

class Programador(Empleado):
  def __init__(self, name):
    super().__init__('Programador', name, {'Resolver tickets'}, {'No tiene nadie a cargo'})

gerente = Gerente("Brais Moure")
gerente.makePresentation()
gerente.showTasksList()
gerente.showTeam()

gerenteDeProyecto = GerenteDeProyecto("Edith Romero")
gerenteDeProyecto.makePresentation()
gerenteDeProyecto.showTasksList()
gerenteDeProyecto.showTeam()

programador = Programador("Andres Chapeton")
programador.makePresentation()
programador.showTasksList()
programador.showTeam()

