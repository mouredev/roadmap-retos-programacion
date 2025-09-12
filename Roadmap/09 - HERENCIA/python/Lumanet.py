class Animal:
    def __init__(self, name):
        self.name = name

    def sound(self):
        pass # Método abstracto que será implementado por las subclases

class Perro(Animal):
    def sound(self): # Polimorfismo (sobrescritura de método)
        print(f"{self.name} hace ¡Guau!")
    
class Gato(Animal):
    def sound(self):
        print(f"{self.name} hace ¡Miauuuu!")
        
def suena(animal):
    animal.sound()

perro = Perro("Tom")
perro.sound() # Tom hace ¡Guau!
gato = Gato("Rusby")
gato.sound() # Rusby hace ¡Miauuuu!


"""
DIFICULTAD EXTRA (opcional):
Implementa la jerarquía de una empresa de desarrollo formada por Empleados que
pueden ser Gerentes, Gerentes de Proyectos o Programadores.
Cada empleado tiene un identificador y un nombre.
Dependiendo de su labor, tienen propiedades y funciones exclusivas de su
actividad, y almacenan los empleados a su cargo.
"""
class Empleado:
    def __init__(self, id, nombre):
        self.id = id
        self.nombre = nombre
        self.empleados = []

    def add(self, empleado):
        self.empleados.append(empleado)

    def listar_empleados(self):
        print(f"Empleados a cargo de {self.nombre}:")
        for empleado in self.empleados:
            print(empleado.nombre)

    def __str__(self):
        return f"{self.__class__.__name__}: {self.nombre} - ID: {self.id}"

class Gerente(Empleado):
    def __init__(self, id, nombre):
        super().__init__(id, nombre) # Llamada al constructor de la clase padre

    def coordinar_proyectos(self):
        print(f"{self.nombre} está coordinando todos los proyectos de la empresa.")

class GerenteProyecto(Empleado):
    def __init__(self, id, nombre):
        super().__init__(id, nombre)

    def asignar_tareas(self):
        print(f"{self.nombre} está asignando tareas a los programadores.")
        
class Programador(Empleado):
    def __init__(self, id, nombre, lenguaje):
        super().__init__(id, nombre)
        self.lenguaje = lenguaje

    def programar(self):
        print(f"{self.nombre} está programando en {self.lenguaje}.")
        
    def add(self, empleado):
        print(f"Un programador ({self.nombre}) no tiene empleados a su cargo. {empleado.nombre} no se añadirá.")
    
    def listar_empleados(self):
        print(f"El programador {self.nombre} no tiene empleados a su cargo.")
        
gerente = Gerente(1, "Marcos")
gerente_proyecto = GerenteProyecto(2, "Susi")
gerente_proyecto2 = GerenteProyecto(3, "Laura")
programador = Programador(4, "Juan", "Python")
programador2 = Programador(5, "Pedro", "Java")
programador3 = Programador(6, "Luis", "Javascript")

print(gerente)
gerente.add(gerente_proyecto)
gerente.add(gerente_proyecto2)
gerente.listar_empleados()
gerente.coordinar_proyectos()
gerente_proyecto.add(programador)
gerente_proyecto.add(programador2)
gerente_proyecto2.add(programador3)
gerente_proyecto.listar_empleados()
gerente_proyecto.asignar_tareas()
gerente_proyecto2.listar_empleados()
gerente_proyecto2.asignar_tareas()
programador.add(gerente)
programador.listar_empleados()
