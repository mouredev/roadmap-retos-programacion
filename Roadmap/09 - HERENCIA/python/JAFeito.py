 # EJERCICIO:
 # Explora el concepto de herencia según tu lenguaje. Crea un ejemplo que
 # implemente una superclase Animal y un par de subclases Perro y Gato,
 # junto con una función que sirva para imprimir el sonido que emite cada Animal.
 
 # DIFICULTAD EXTRA (opcional):
 # Implementa la jerarquía de una empresa de desarrollo formada por Empleados que
 # pueden ser Gerentes, Gerentes de Proyectos o Programadores.
 # Cada empleado tiene un identificador y un nombre.
 # Dependiendo de su labor, tienen propiedades y funciones exclusivas de su
 # actividad, y almacenan los empleados a su cargo.
 
class Empleado:
    def __init__(self,id : int, nombre : str):
        self.id = id
        self.nombre = nombre
        self.equipo = []

class Gerente(Empleado):

    def add_trabajador(self, trabajador):
        self.equipo.append(trabajador)
        
    def trabajo(self):
        print(f"{self.nombre} es el gerente a cargo del siguiente equipo:")
        
        for i in self.equipo:
            print(f"{i} \n")
    
        
class GerenteP(Empleado):
    
    def add_trabajador(self, trabajador):
        self.equipo.append(trabajador)
        
    def __init__(self, id: int, nombre: str, proyecto: str):
        super().__init__(id, nombre)
        self.proyecto = proyecto    
        
    def trabajo(self):
        print(f"{self.nombre} es gerente de proyectos a cargo del proyecto {self.proyecto} con el siguiente equipo:")
        for i in self.equipo:
            print(f"{i}\n")


class Programador(Empleado):
    def __init__(self, id: int, nombre: str, lenguaje: str):
        super().__init__(id, nombre)
        self.lenguaje = lenguaje
    def trabajo(self):
        print(f"{self.nombre} programando en {self.lenguaje}")
        
        
gerente_1 = Gerente(1,"Paco")
gerente_p_1 = GerenteP(2, "Manolo","Login")
programador_1 = Programador(3, "Antonio", "Python")
programador_2 = Programador(4, "Manel", "Python")
programador_3 = Programador(5, "Laila", "Python")
gerente_1.add_trabajador(programador_1.nombre)
gerente_1.add_trabajador(programador_2.nombre)
gerente_1.add_trabajador(programador_3.nombre)
gerente_1.trabajo()
gerente_p_1.add_trabajador(programador_1.nombre)
gerente_p_1.add_trabajador(gerente_1.nombre)
gerente_p_1.trabajo()