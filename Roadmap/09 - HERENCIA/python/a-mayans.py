# Superclase
class Animal:
  def __init__(self, nombre, onomatopeya):
    self.nombre = nombre
    self.onomatopeya = onomatopeya

  def sonido(self):
    print(f'{self.nombre} está haciendo {self.onomatopeya}')

# Subclase con herencia de la superclase
class Perro(Animal):
  def jugar(self):
    print(f'El perro que se llama {self.nombre} está jugando y haiendo {self.onomatopeya}')

class Gato(Animal):
  def jugar(self):
    print(f'El gato que se llama {self.nombre} está jugando y haiendo {self.onomatopeya}')

perro = Perro('Sirius', 'Guau!')
perro.jugar()
gato = Gato('Obi', 'Miau!')
gato.jugar()


""" EJERCICIO EXTRA """

class Empleados:
  def __init__(self, id, nombre):
    self.id = id
    self.nombre = nombre


class Gerente(Empleados):
  def __init__(self, id, nombre, personal):
    super().__init__(id, nombre)
    self.personal = personal

  def reunion(self):
    print(f'El gerente {self.nombre} se ha reunido con sus gerentes de proyectos {self.personal}')

  def gestion_de_personal(self):
    print(f'{self.nombre} se ha asegurado de que los objetivos se están llevando a cabo')


class GerenteProyectos(Empleados):
  def __init__(self, id, nombre, equipo):
    super().__init__(id, nombre)
    self.equipo = equipo

  def gestion_de_equipo(self):
    print(f'{self.nombre} está gestionando un equipo para su proyecto')

  def fijar_tareas(self):
    print(f'{self.nombre} en la reunion con su equipo formado por {self.equipo} ha fijado las tareas individuales y el objetivo grupal')


class Programador(Empleados):
  def __init__(self, id, nombre, lenguajes):
    super().__init__(id, nombre)
    self.lenguajes = lenguajes

  def programar(self):
    print(f'{self.nombre} está programando en los siguientes lenguajes: {self.lenguajes}')

# casos de uso
## gerente
gerente = Gerente(1, 'Toni', ['Gerard', 'Ruben', 'Lucas'])
gerente.reunion()
gerente.gestion_de_personal()

## gerente de proyectos
gerente_proyecto = GerenteProyectos(2, 'Carolina', ['Alberto', 'Laura', 'Rodri'])
gerente_proyecto.gestion_de_equipo()
gerente_proyecto.fijar_tareas()

## programador
programador = Programador(3, 'Alex', ['Python', 'JS'])
programador.programar()