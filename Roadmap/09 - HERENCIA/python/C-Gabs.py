#Reto 09

'''Explora el concepto de herencia según tu lenguaje. Crea un ejemplo que
 * implemente una superclase Animal y un par de subclases Perro y Gato,
 * junto con una función que sirva para imprimir el sonido que emite cada Animal.
 *
 * DIFICULTAD EXTRA (opcional):
 * Implementa la jerarquía de una empresa de desarrollo formada por Empleados que
 * pueden ser Gerentes, Gerentes de Proyectos o Programadores.
 * Cada empleado tiene un identificador y un nombre.
 * Dependiendo de su labor, tienen propiedades y funciones exclusivas de su
 * actividad, y almacenan los empleados a su cargo.'''

class Animal:
    def __init__(self) -> None:
        pass
    def hablar():
        pass

class Perro(Animal):
    def hablar(self):
        print("Guau")

class Gato(Animal):
    def hablar(self):
        print("Miau")

gato = Gato()
gato.hablar()

perro = Perro()
perro.hablar()


#Reto extra
class Empleado:
    def __init__(self, nombre, id) -> None:
        self.nombre = nombre
        self.id = id
        self.empleados = []
    
    def añadir_empleados(self,nombre,id):
        self.empleados.append((nombre,id))
        print(f"Se añade el empleado {nombre} a la lista del gerente {self.nombre}")

class Gerente(Empleado):
    def gestion_proyectos(self):
        print(f"{self.nombre} gestiona los proyectos")
    
    def define_mision(self):
        print(f"{self.nombre} define la misión de la empresa")
    
    def define_vision(self):
        print(f"{self.nombre} define la visión de la empresa")

class GerentesDeProyecto(Empleado):
    def __init__(self, nombre, id, proyecto) -> None:
        super().__init__(nombre, id)
        self.proyecto = proyecto


    def planificacion_proyecto(self):
        print(f"{self.nombre} planifica el proyecto: {self.proyecto}")
    
    def supervicion_proyecto(self):
        print(f"{self.nombre} supervisa el proyecto: {self.proyecto}")
    
    def ejecucion_proyecto(self):
        print(f"{self.nombre} ejecuta el proyecto: {self.proyecto}")

class Programador(Empleado):
    def añadir_empleados(self):
        pass

    def desarrollar_codigo(self):
        print(f"{self.nombre} programa el código")
    
    def mantener_codigo(self):
        print(f"{self.nombre} mantiene el código")

gerente_1 = Gerente("Juan",1)
gerente_1.define_mision()
gerente_1.define_vision()
gerente_1.gestion_proyectos()
gerente_proyecto_1 = GerentesDeProyecto("Carlos",2, "proyecto 1")
gerente_1.añadir_empleados(gerente_proyecto_1.nombre, gerente_proyecto_1.id)
gerente_proyecto_1.planificacion_proyecto()
gerente_proyecto_1.supervicion_proyecto()
gerente_proyecto_1.ejecucion_proyecto()
programador_1 = Programador("Gabriel",3)
gerente_proyecto_1.añadir_empleados(programador_1.nombre, programador_1.id)
programador_1.desarrollar_codigo()
programador_1.mantener_codigo()
