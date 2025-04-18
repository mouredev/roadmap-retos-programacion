"""
Herencia
"""

class Animal():
    def __init__(self, nombre) -> None:
        self.nombre = nombre
    
    def ruido(self):
        pass

class Perro(Animal):
      
    def ruido(self):
        print("guau")
        
class Gato(Animal):
      
    def ruido(self):
        print("Miau")

def hacer_sonido(animal : Animal):
    animal.ruido()
    
animal1 = Animal("James")
perro = Perro("Peter")
gato = Gato("Gato")

perro.ruido()
gato.ruido()
print("------------")
hacer_sonido(perro)
print("------------")
hacer_sonido(gato)

"""
 * DIFICULTAD EXTRA (opcional):
 * Implementa la jerarquía de una empresa de desarrollo formada por Empleados que
 * pueden ser Gerentes, Gerentes de Proyectos o Programadores.
 * Cada empleado tiene un identificador y un nombre.
 * Dependiendo de su labor, tienen propiedades y funciones exclusivas de su
 * actividad, y almacenan los empleados a su cargo.
"""

class Empleado():
    def __init__(self, nombre : str, identificador : int):
        self.nombre = nombre
        self.identificador = identificador
        self.empleados = []
    
    def add_empleado(self, empleado):
        self.empleados.append(empleado)
    
    def print_empleados(self):
        for empleado in self.empleados:
            print(empleado)
        
    
class Gerente(Empleado):
    
    def cordinar_proyecto(self):
        print(f"{self.nombre} está coordinando todos los proyectos de la empresa")

class GerenteProyecto(Empleado):
    def __init__(self, nombre, identificador, proyecto):
        super().__init__(nombre, identificador)
        self.proyecto = proyecto
    def cordinar_proyecto(self):
        print(f"{self.nombre} está coordinando su proyecto de {self.proyecto}")    

class Programador(Empleado):
    def __init__(self, nombre,  identificador, lenguaje):
        super().__init__(nombre, identificador)
        self.lenguaje = lenguaje

    def programar(self):
        print(f"{self.nombre} está programando con el lenguaje {self.lenguaje}")

    def add_empleado(self, empleado : Empleado):
        print(f"Un programador no tiene empleados a su cargo, {empleado.nombre} no se añadirá")
        

# Caso de uso
gerente = Gerente("Juan", 1)
gerente_proyecto = GerenteProyecto("Maria", 2, "Biomedicina")
programador = Programador("Juanma", 3, "Python")

gerente.add_empleado(gerente_proyecto)
gerente.cordinar_proyecto()
print("--------------")
gerente_proyecto.add_empleado(programador)
gerente_proyecto.cordinar_proyecto()
print("--------------")
programador.add_empleado(programador)
programador.programar()