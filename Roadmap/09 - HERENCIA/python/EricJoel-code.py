## Herencia y Polimorfismo

"""Concepto: La Herencia es un pilar de la programación orientada a objetos (POO) que permite a una clase nueva (hija o subclase) adquirir propiedades (atributos) y comportamientos (métodos) de una clase existente (padre o superclase), fomentando la reutilización de código y creando una jerarquía entre las clases. El polimorfismo permite que objetos de diferentes clases se traten como si pertenecieran a una misma superclase, gracias a que implementan el mismo método de formas distintas. Esto se traduce en código más flexible, reutilizable y potente, ya que diferentes objetos responden a la misma solicitud con su comportamiento específico. """

#Clase Padre
class Animal:
    def __init__(self, name):
        self.name = name
        
    def sonido(self):
        pass
    

#Subclases
class Perro(Animal):
    
    def sonido(self):
        print("Guau!")
        
class Gato(Animal):
    
    def sonido(self):
        print("Miau!")
        
        
def imprimir_sonido(animal: Animal):
    animal.sonido()
        
animal = Animal("Animal")
imprimir_sonido(animal)
perro = Perro("Ody")
imprimir_sonido(perro)
gato = Gato("Chiquitina")
imprimir_sonido(gato)

##Extra

class Empleado:
    
    def __init__(self, id:int, name:str):
        self.id = id
        self.name = name
        self.empleados = []
        
    def agregar(self, empleado):
        self.empleados.append(empleado)
        
class Gerente(Empleado):
    
    def cordinar_proyectos(self):
        print(f"{self.name} esta cordinando todos los proyectos de la empresa")
    
class GerenteProyectos(Empleado):
    
    def __init__(self, id:int, name:str, proyecto:str):
        super().__init__(id, name)
        self.proyecto = proyecto
        
    def cordinar_proyecto(self):
        print(f"{self.name} esta cordinando el {self.proyecto}")

class Programador(Empleado):
    def __init__(self, id:int, name:str, lenguaje:str):
        super().__init__(id, name)
        self.lenguaje = lenguaje
        
    def codificar(self):
        print(f"{self.name} esta programando en {self.lenguaje}")
        
    def agregar(self, empleado:Empleado):
        print(f"Un programador no tiene empleados a su cargo. {empleado.name} no se agregara")
        
        
gerente = Gerente(1, "Eric")
gerente_de_proyecto = GerenteProyectos(2, "Joel","Proyecto 1")
gerente_de_proyecto2 = GerenteProyectos(3, "Paul", "Proyecto 2")
programador = Programador(4,"Juan", "Java")
programador2 = Programador(5,"Pepe", "C")
programador3 = Programador(6,"Ana", "C++")

gerente.agregar(gerente_de_proyecto)
gerente.agregar(gerente_de_proyecto2)

gerente_de_proyecto.agregar(programador)

gerente_de_proyecto2.agregar(programador2)
gerente_de_proyecto2.agregar(programador3)

programador.agregar(programador2)

programador2.codificar()
gerente_de_proyecto.cordinar_proyecto()
gerente.cordinar_proyectos()