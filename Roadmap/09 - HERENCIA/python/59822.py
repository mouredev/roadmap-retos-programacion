class Animal:
    animal = "Ser vivo"
    
    def __init__(self, color, sonido):
        self.color = color
        self.sonido = sonido
        
    def hacer_sonido(self):
        print(f"hola {self.sonido}")
        
class Perro(Animal):
    
    def __init__(self, color, sonido, raza):
        self.raza = raza
        super().__init__(color, sonido)
    
    def saludo(self):
        print(f"hola soy un perro de raza {self.raza} y mi color es {self.color}")

class Gato(Animal):
    def __init__(self, color, sonido, pelaje):
        self.pelaje = pelaje
        super().__init__(color, sonido)
    
    def saludo(self):
        print(f"hola soy un gato con pelaje {self.pelaje} y mi color es {self.color}")
    
perro = Perro("cafe", "guau", "labrador")
perro.hacer_sonido()


''' Ejercicios de Herencia'''

class Empresa:
    
    def __init__(self, id, name, cargo):
        self.id = id
        self.name = name
        self.cargo = cargo
    
    def presentacion(self):
        print(f"Hola, soy {self.name} y mi cargo  es {self.cargo}")
        
class Gerente(Empresa):
    def __init__(self, id, name, cargo):
        super().__init__(id, name, cargo)
    
    def personal(self, numero_personal):
        print(f"Mi numero de personal es {numero_personal}")
    
class Gerente_proyectos(Empresa):
    def __init__(self, id, name, cargo):
        super().__init__(id, name, cargo)
    
    def proyectos(self, numero_proyectos):
        print(f"Mi numero de proyectos es {numero_proyectos}")

class Programador(Empresa):
    def __init__(self, id, name, cargo):
        super().__init__(id, name, cargo)
    
    def tareas(self, numero_tareas):
        print(f"Mi numero de tareas es {numero_tareas}")
        
        
# Crear un objeto de la clase Empresa
programador = Programador(2, "Juan", "Programador")
programador.tareas(5)
gerente = Gerente(3, "Ana", "Gerente")
gerente.personal(10)
gerente_proyecto = Gerente_proyectos(4, "Carlos", "Gerente de Proyecto")
gerente_proyecto.proyectos(15)

        