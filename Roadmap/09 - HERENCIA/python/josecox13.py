'''
/*
 * EJERCICIO 9:
 * Explora el concepto de herencia según tu lenguaje. Crea un ejemplo que
 * implemente una superclase Animal y un par de subclases Perro y Gato,
 * junto con una función que sirva para imprimir el sonido que emite cada Animal.
 *
 * DIFICULTAD EXTRA (opcional):
 * Implementa la jerarquía de una empresa de desarrollo formada por Empleados que
 * pueden ser Gerentes, Gerentes de Proyectos o Programadores.
 * Cada empleado tiene un identificador y un nombre.
 * Dependiendo de su labor, tienen propiedades y funciones exclusivas de su
 * actividad, y almacenan los empleados a su cargo.
 */
'''
# Superclase
class Animal():
    def __init__(self, nombre:str) -> None:
        self.nombre = nombre
    def sonido(self):
        print('Sonido no determinado')

#Subclase

class Perro(Animal):
    def sonido(self:str):
        print('Guau')

class Gato(Animal):
    def sonido(self:str):
        print('Miau')

Generic_Animal = Animal('Animal')
Misifu = Gato('Misifu')
Tobi = Perro('Tobi')

Generic_Animal.sonido()
Misifu.sonido()
Tobi.sonido()


"""
Ejericio extra
"""

class Empleado():
    def __init__(self, nombre:str, id:int) -> None:
        self.nombre = nombre
        self.id = id
        self.empleados = []
    def gestionar(self, empleado):
        self.empleados.append(empleado)
    def gestionados(self):
        print(f'{self.nombre} gestiona a los siguientes empleados:')
        for empleado in self.empleados:
            print(f'Empleado: {empleado.nombre}')
    
class Programador(Empleado):
    def __init__(self, nombre:str, id:int, languaje:str) -> None:
        super().__init__(nombre, id)
        self.lenguaje = languaje
        self.cargo = 'Programador'
    def programar(self):
        print(f'{self.nombre} programando en {self.lenguaje}')
    def gestionar(self, empleado):
        print('Un programador no puede gestionar empleados')

class Gerente(Empleado):
    def __init__(self, nombre:str, id:int) -> None:
        super().__init__(nombre, id)
        self.cargo = 'Gerente'
    def coordinar(self):
        print('Coordinando a {}')

class Gerente_Proyecto(Empleado):
    def __init__(self, nombre, id, proyecto:str):
        super().__init__(nombre, id)
        self.proyecto = proyecto
        self.cargo = 'Gerente de Proyecto'


    
    def coordinar(self):
        print(f'Gestionando el proyecto {self.proyecto}')

Gerente_1 = Gerente('Pedro', 4)
Gerente_Proyecto_1 = Gerente_Proyecto('Juan', 5 , 'Proyecto Casas')
Gerente_Proyecto_2 = Gerente_Proyecto('Alvaro', 6 , 'Proyecto Universidad')
Empleado_1 = Programador('Luis', 1, 'C++')
Empleado_2 = Programador('Maria', 2, 'Python')
Empleado_3 = Programador('Ana', 3, 'Java')

Gerente_Proyecto_1.gestionar(Empleado_1)
Gerente_Proyecto_1.gestionar(Empleado_2)
Gerente_Proyecto_2.gestionar(Empleado_3)
Gerente_1.gestionar(Gerente_Proyecto_1)
Gerente_1.gestionar(Gerente_Proyecto_2)


Gerente_1.gestionados()
Empleado_1.gestionar(Empleado_2)
