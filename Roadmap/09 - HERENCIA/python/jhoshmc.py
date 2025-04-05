
"""
! EJERCICIO:
 * Explora el concepto de herencia según tu lenguaje. Crea un ejemplo que
 * implemente una superclase Animal y un par de subclases Perro y Gato,
 * junto con una función que sirva para imprimir el sonido que emite cada Animal.
"""

class Animal:
  def __init__(self,nombre):
    self._nombre = nombre
  def get_sonido(self):
    print("sonido default que se va apisar")

class Perro(Animal):
  def __init__(self, nombre):
    super().__init__(nombre)
  def get_sonido(self):
    print(f"{self._nombre}: Guau!")

class Gato(Animal):
  def __init__(self, nombre):
    super().__init__(nombre)
  def get_sonido(self):
    print(f"{self._nombre}: Miau!")

def ejercicio():
  chester= Perro("Chester")
  lita = Gato("Lita")
  chester.get_sonido()
  lita.get_sonido()

# ejercicio()
# todo extra

"""
 ! DIFICULTAD EXTRA (opcional):
 * Implementa la jerarquía de una empresa de desarrollo formada por Empleados que
 * pueden ser Gerentes, Gerentes de Proyectos o Programadores.
 * Cada empleado tiene un identificador y un nombre.
 * Dependiendo de su labor, tienen propiedades y funciones exclusivas de su
 * actividad, y almacenan los empleados a su cargo.
"""

class Empleado:
  #? constructor
  def __init__(self,id,nombre,cargo):
    self._id = id
    self._nombre=nombre
    self._cargo=cargo
  #?metodos
  def get_info_empleado(self):
    print(f"Empleado: {self._id}: {self._nombre}  cargo: {self._cargo}")

class Gerente(Empleado):
  #?atributos (herecados y creados en esta clase)
  def __init__(self, id, nombre, cargo):
    #?inicializando los atributos heredados
    super().__init__(id, nombre, cargo)
    #? atributo propiedo de esta clase
    self.personal=[]
  #? metodos de esta clase
  def set_agregar_personal(self,nuevo_P):
    self.personal.append(nuevo_P)
  def get_personal(self):
    print(f"Gerente: {self._nombre} con personal a cargo :\n")
    for empleado in self.personal:
      empleado.get_info_empleado()

class Gerente_Proyecto(Empleado):
  def __init__(self, id, nombre, cargo):
    super().__init__(id, nombre, cargo)
    self.equipo=[]
    self.proyectos =[]
  def set_personal_a_cargo(self,miembro):
    self.equipo.append(miembro)
  def set_proyectos(self,nombre_proyecto):
    self.proyectos.append(nombre_proyecto)
  def get_equipo(self):
    print(f"Gerente de proyectos {self._nombre} con miembors en su equipo: \n")
    for integrante in self.equipo:
      integrante.get_info_empleado()
  def get_proyectos(self):
    print(f"Gerente de proyectos {self._nombre} con proyectos a cargo: \n")
    for proyecto in self.proyectos:
      print(proyecto)

class Programador(Empleado):
  def __init__(self,id,nombre,cargo):
    super().__init__(id,nombre,cargo)
    self._proyecto_en_curso = "ninguno"
  def set_proyecto(self,proyecto):
    self._proyecto_en_curso = proyecto
  def get_proyectos_accinados(self):
    print(f"Programador: {self._nombre}")
    print(f"proyecto en curso: {self._proyecto_en_curso}")  



manuel = Gerente("G989","manuel","Gerente")
jonas = Gerente_Proyecto("G233", "Jonas Marques","Gerente de proyectos")
roberto= Programador("P564", "Roberto Hernandez","programador")
jonas.get_info_empleado()
roberto.get_info_empleado()
manuel.set_agregar_personal(jonas)
manuel.set_agregar_personal(roberto)
manuel.get_personal()
jonas.set_personal_a_cargo(roberto)
jonas.set_proyectos("Cambiar color de boton")
jonas.set_proyectos("Reiniciar la pc")
jonas.get_equipo()
jonas.get_proyectos()
roberto.set_proyecto("Cambiar color de boton")
roberto.get_proyectos_accinados()