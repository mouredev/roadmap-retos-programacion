print("\n\n=====================================DEFINICION DE HERENCIA=====================================\n\n")


print("La herencia en Python es un mecanismo que permite crear nuevas clases a partir de clases existentes.\nEsto significa que las nuevas clases heredan los atributos y mÃ©todos de las clases de las que se derivan.")

print("\n\n=====================================EJERCICIO=====================================\n\n")

'''
Explora el concepto de herencia según tu lenguaje. Crea un ejemplo que
implemente una superclase Animal y un par de subclases Perro y Gato,
junto con una función que sirva para imprimir el sonido que emite cada Animal.
'''

class Animal:
  def __init__(self, name):
    self.name = name
    
  def eat(self):
    print(f"{self.name} está comiendo") 
  
  def drink(self):
    print(f"{self.name} está bebiendo")
  
  def sleep(self):
    print(f"{self.name} está durmiendo\n\n")
  
pet = Animal("Mi mascota")
pet.eat()
pet.drink()
pet.sleep()


class Perro(Animal):
  def __init__(self, name, age, sound, colour):
    super().__init__(name)
    self.age = age
    self.sound = sound
    self.colour = colour
    
  def introduce_my_pet(self):
    print(f"Mi perro {self.name} tiene {self.age} años y es de color {self.colour}")
    
  def bark(self):
    print(f"mi perro {self.sound} a los desconocidos")
   
my_dog = Perro("kal", 3, "ladra", "blanco")
my_dog.introduce_my_pet()
my_dog.bark()
my_dog.eat() 
my_dog.drink() 
my_dog.sleep() 

    
class Gato(Animal):
  def __init__(self, name, age, sound, colour, climb):
    super().__init__(name)
    self.age = age
    self.sound = sound
    self.colour = colour
    self.climb = climb
    
  def present_my_pet(self):
    print(f"Mi gato se llama {self.name} tiene {self.age} años, es de color {self.colour} y {self.climb} a los árboles")
    
  def meow(self):
    print(f"Mi gato {self.sound} cuando quiere comer")
    
my_cat = Gato("Madi", 2, "maulla", "gris", "trepa")
my_cat.present_my_pet()
my_cat.meow()
my_cat.eat()
my_cat.drink()
my_cat.sleep()


print("\n\n=====================================DIFICULTAD EXTRA=====================================\n\n")

'''
Implementa la jerarquí­a de una empresa de desarrollo formada por Empleados que
pueden ser Gerentes, Gerentes de Proyectos o Programadores.
Cada empleado tiene un identificador y un nombre.
Dependiendo de su labor, tienen propiedades y funciones exclusivas de su
actividad, y almacenan los empleados a su cargo.
'''

class Empleado:
  def __init__(self, nombre, identificador):
    self.nombre = nombre
    self.identificador = identificador
    
  def hacer_trabajos(self):
    pass

    
class Gerente(Empleado):
  def __init__(self, nombre, identificador, funcion, equipos):
    super().__init__(nombre, identificador)
    self.funcion = funcion
    self.equipos = equipos
  
  equipos_compañia = ["Proyectos", "Administracion", "RRHH", "Ventas", "Fiscal"]
    
  def hacer_trabajos(self):
    print(f"El {self.identificador} es {self.nombre} y su trabajo es {self.funcion} a los diferentes {self.equipos}")
    print(f"El {self.identificador} tambien se ocupa de gestionar la administración de la empresa en todos sus departamentos")
    
  print(f"Los equipos que dependen del Gerente de la compañí­a son: {equipos_compañia}\n")



class Gerente_proyecto(Gerente):
  def __init__(self, nombre, identificador, funcion, equipos, proyecto):
    super().__init__(nombre, identificador, funcion, equipos)
    self.proyecto = proyecto
    
  equipo_proyecto1 = ["programador 1A", "programador 2A", "programador 3A", "programador 4A" ]
  equipo_proyecto2 = ["programador 1B", "programador 2B", "programador 3B", "programador 4B" ]
  equipo_proyecto3 = ["programador 1C", "programador 2C", "programador 3C", "programador 4C" ]
  
  def trabajo_gerente_proyecto(self):
    if self.equipos == "Equipo 1":
      print(f"El equipo que depende de {self.identificador} es {self.equipo_proyecto1}")
    elif self.equipos == "Equipo 2":
      print(f"El equipo que depende de {self.identificador} es {self.equipo_proyecto2}")
    elif self.equipos == "Equipo 3":
      print(f"El equipo que depende de {self.identificador} es {self.equipo_proyecto3}")
        
    
    print(f"{self.nombre} es {self.identificador} y su funcion es {self.funcion} al {self.equipos} para realizar el proyecto {self.proyecto}\n")
    
   
class Programador(Gerente_proyecto):
  def __init__(self, nombre, identificador, funcion, equipos, proyecto, horario):
     super().__init__(nombre, identificador, funcion, equipos, proyecto)
     self.horario = horario
     
  def turno(self):
    print(f"{self.nombre} es {self.identificador} pertenece al {self.equipos}, está trabajando en el {self.proyecto}, su función es {self.funcion} y trabaja en el {self.horario} de tarde\n")  
    
   
gerente = Gerente("Rantamplan", "gerente", "organizar", "equipos de proyecto")
    
director_proyecto1 = Gerente_proyecto("Carlos", "Gerente de proyecto 1", "seleccionar y organizar", "Equipo 1", "Proyecto A")
director_proyecto2 = Gerente_proyecto("Miguel", "Gerente de proyecto 2", "seleccionar y organizar", "Equipo 2", "Proyecto B") 
director_proyecto3 = Gerente_proyecto("Helena", "Gerente de proyecto 3", "seleccionar y organizar", "Equipo 3", "Proyecto C")

programador1A = Programador("Jose Luis", "programador", "limpiar código", "Equipo 1", "proyecto A",  "turno") 
programador2A = Programador("Marina", "programadora", "limpiar código", "Equipo 2", "proyecto B",  "turno") 
programador3A = Programador("Alex", "programadora", "limpiar código", "Equipo 3", "proyecto C",  "turno") 
   

gerente.hacer_trabajos()    
director_proyecto1.trabajo_gerente_proyecto()   
director_proyecto2.trabajo_gerente_proyecto()
director_proyecto3.trabajo_gerente_proyecto()
programador1A.turno()   
programador2A.turno()
programador3A.turno() 
