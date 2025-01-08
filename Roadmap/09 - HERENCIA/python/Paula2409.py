""" 
 * EJERCICIO:
 * Explora el concepto de herencia según tu lenguaje. Crea un ejemplo que
 * implemente una superclase Animal y un par de subclases Perro y Gato,
 * junto con una función que sirva para imprimir el sonido que emite cada Animal.
"""
class Animal:
    def __init__(self, tipo: str, sonido: str):
        self.tipo = tipo
        self.sonido = sonido
        
    def hablar(self):
        return f"El animal {self.tipo} hace {self.sonido}"
    
class Perro(Animal):
    def __init__(self, tipo, sonido):
        super().__init__(tipo, sonido)
        
class Gato(Animal):
    def __init__(self, tipo, sonido):
        super().__init__(tipo, sonido)
        
perro = Perro('perro', 'guau')
gato = Gato('gato', 'miau')
print(perro.hablar())
print(gato.hablar())

"""
 * DIFICULTAD EXTRA (opcional):
 * Implementa la jerarquía de una empresa de desarrollo formada por Empleados que
 * pueden ser Gerentes, Gerentes de Proyectos o Programadores.
 * Cada empleado tiene un identificador y un nombre.
 * Dependiendo de su labor, tienen propiedades y funciones exclusivas de su
 * actividad, y almacenan los empleados a su cargo. 
"""

class Empleados:
    id = 0
    empleados = {}
    
    @classmethod
    def agregar_empleado(cls):
        cls.id += 1
        return cls.id
            
    def __init__(self, nombre: str, puesto: str, funcion: str):
        self.id = Empleados.agregar_empleado()
        self.nombre = nombre
        self.puesto = puesto
        self.funcion = funcion
        Empleados.empleados[self.id] = self.nombre
        
        
class GerenteDeProyectos(Empleados):
    gerente_proyecto = {}
    a_cargo_gp = []
    
    def agrega_gerente_proyecto(self):
        GerenteDeProyectos.gerente_proyecto['Nombre'] = self.nombre
        GerenteDeProyectos.gerente_proyecto['Puesto'] = self.puesto
        GerenteDeProyectos.gerente_proyecto['Proyecto'] = self.proyecto
    
    def __init__(self, nombre: str, puesto: str, funcion: str, proyecto: str):
        super().__init__(nombre, puesto, funcion)
        self.proyecto = proyecto
        GerenteDeProyectos.agrega_gerente_proyecto(self)
        Empleados.empleados[self.id] = GerenteDeProyectos.gerente_proyecto

        
    def __str__(self):
        return f"Nombre: {self.nombre}, Puesto: {self.puesto}, Proyecto: {self.proyecto}"

class Gerente(Empleados):
    gerentes = {}
    a_cargo_g = []
    
    def agrega_gerente(self):
        Gerente.gerentes['Nombre'] = self.nombre
        Gerente.gerentes['Puesto'] = self.puesto
        Gerente.gerentes['Proyecto'] = self.proyecto
        GerenteDeProyectos.a_cargo_gp.append(Gerente.gerentes)
    
    def __init__(self, nombre: str, puesto: str, funcion: str, proyecto: str):
        super().__init__(nombre, puesto, funcion)
        self.proyecto = proyecto
        Gerente.agrega_gerente(self)
        Empleados.empleados[self.id] = Gerente.gerentes

    def __str__(self):
        return f"Nombre: {self.nombre}, Puesto: {self.puesto}, Proyecto: {self.proyecto}"

class Programador(Empleados):
    programadores = {}
    
    def agregar_programador(self):
        Programador.programadores['nombre'] = self.nombre
        Programador.programadores['puesto'] = self.puesto
        Programador.programadores['salario'] = self.salario
        Gerente.a_cargo_g.append(Programador.programadores)
        
    def __init__(self, nombre: str, puesto: str, funcion: str, salario: int):
        super().__init__(nombre, puesto, funcion)
        self.salario = salario
        Programador.agregar_programador(self)
        Empleados.empleados[self.id] = Programador.programadores
        
    def __str__(self):
        return f"Nombre: {self.nombre}, Puesto: {self.puesto}, Salario: {self.salario}"

empleado1 = Programador('Paula','Programador', 'Programar', 1000)
empleado2 = Gerente('Jose','Gerente','Gestion','Web')
empleado3 = GerenteDeProyectos('Marcos','Gerente de Proyectos','Coordinar','Web')
print(f"Empleados: {Empleados.empleados}")
print(f"Gerentes: {Gerente.gerentes}")
print(f"Gerentes de Proyecto: {GerenteDeProyectos.gerente_proyecto}")
print(f"Personal a cargo de Gerentes: {Gerente.a_cargo_g}")
print(f"Personal a cargo de Gerentes de Proyectos: {GerenteDeProyectos.a_cargo_gp}")
