"""	
09 - HERENCIA
Autor de la solución: Oriaj3	
Teoría:	
La herencia es un concepto fundamental en la programación orientada a objetos.
Permite crear nuevas clases a partir de clases existentes, reutilizando su
código y extendiendo su funcionalidad.

La clase original se conoce como superclase, y la nueva clase se conoce como
subclase. La subclase hereda todos los atributos y métodos de la superclase, y
puede agregar nuevos atributos y métodos, o modificar los existentes.

También se pueden llamar hijos y padres a las subclases y superclases. 

En Python, la herencia se especifica en la definición de la clase, pasando la
superclase entre paréntesis después del nombre de la clase.

Ejemplo:
class Animal:
    def __init__(self, nombre):
        self.nombre = nombre

    def hacer_sonido(self):
        pass

class Perro(Animal):
    def __init__(self, nombre, raza):
        super().__init__(nombre)
        self.raza = raza

    def hacer_sonido(self):
        print("Guau guau")
"""

# EJEMPLO BÁSICO
"""
 * EJERCICIO:
 * Explora el concepto de herencia según tu lenguaje. Crea un ejemplo que
 * implemente una superclase Animal y un par de subclases Perro y Gato,
 * junto con una función que sirva para imprimir el sonido que emite cada Animal.
"""

# Clase base o superclase
class Animal:

    def __init__(self, nombre) -> None:
        self.nombre = nombre

    def rugido(self) -> None:
        print("Rugido de animal!!!")

# Subclase perro 
class Perro(Animal):
    def __init__(self, nombre, raza) -> None:
        super().__init__(nombre)
        self.raza = raza

    def rugido(self) -> None:
        print("Guau Guau!!")

# subclase gato
class Gato(Animal):
    def __init__(self, nombre, color) -> None:
        super().__init__(
            nombre,
        )
        self.color = color

    def rugido(self) -> None:
        print("Miau Miau!!")


# Crea un vector de animales
animales = [Animal("Estandar"), Perro("Firulais", "Mestiza"), Gato("Mishi", "Negro")]

# Imprime el sonido de cada animal
for animal in animales:
    print(animal.nombre, end=": ")
    animal.rugido()

print(f"El perro es de raza {animales[1].raza} y el gato es {animales[2].color}")

# EJERCICIO EXTRA
"""
 * DIFICULTAD EXTRA (opcional):
 * Implementa la jerarquía de una empresa de desarrollo formada por Empleados que
 * pueden ser Gerentes, Gerentes de Proyectos o Programadores.
 * Cada empleado tiene un identificador y un nombre.
 * Dependiendo de su labor, tienen propiedades y funciones exclusivas de su
 * actividad, y almacenan los empleados a su cargo.
 */
"""

#clase padre o superclase 
class Empleado:
    
    def __init__(self, nombre, id) -> None:
        self.nombre = nombre
        self.id = id
        self.salario = 1000


    def cobrar(self):
        print(f"El empleado {self.nombre} va a cobrar {self.salario}")

    def __str__(self) -> str:
        return f"Nombre {self.__class__.__name__}: {self.nombre}, ID: {self.id}, SALARIO: {self.salario}"

# Clase superclase o padre
class Jefe:
    def __init__(self, listaEmpleados) -> None:
        self.listaEmpleados = listaEmpleados

    def listarEmpleados(self) -> None:
        print(f"Dirigiendo a {self.__class__.__name__}", end=": ")
        for empleado in self.listaEmpleados:
            print(empleado.id, end=", ")
        print("\n")

# Subclase de Empleado
class Programador(Empleado):
    def __init__(self, nombre, id, lenguaje) -> None:
        super().__init__(nombre, id)
        self.lenguaje = lenguaje
        self.salario = 1300

    def programar(self) -> None:
        print(f"El programador {self.nombre} está programando en {self.lenguaje}")

# Subclase de Empleado y Jefe
class Gerente(Empleado, Jefe):

    def __init__(self, nombre, id, listaEmpleados, bonus) -> None:
        Empleado.__init__(self, nombre, id)
        Jefe.__init__(self, listaEmpleados)
        self.bonus = bonus
        self.salario = 2000 + bonus

# Subclase de Empleado y Jefe
class GerenteProyecto(Empleado, Jefe):
    def __init__(self, nombre, id, listaEmpleados, proyecto) -> None:
        Empleado.__init__(self, nombre, id)
        Jefe.__init__(self, listaEmpleados)
        self.proyecto = proyecto
        self.salario = 1500
    
    def trabajar(self) -> None:
        print(f"El gerente de proyecto {self.nombre} está trabajando en el proyecto {self.proyecto}")


##Ejemplo de uso
empleados = [
    Empleado("Juan", 1),
    Programador("Pedro", 2, "Python"),
    Gerente(nombre="Carlos", id=3, listaEmpleados=[Empleado("Ana", 4), Programador("Maria", 5, "Java")], bonus=500),
    GerenteProyecto(
        "Luis", 6, [Empleado("Sofia", 7), Programador("Jose", 8, "C++")], "Proyecto 1"
    ),
]
print("\n\n##### Lista de empleados #####\n\n")
for empleado in empleados:
    print(empleado.__str__())
    empleado.cobrar()

print("\n\n##### Acciones de los empleados #####\n\n")
for empleado in empleados:
    if isinstance(empleado, Gerente):
        empleado.listarEmpleados()
    if isinstance(empleado, Programador):
        empleado.programar()
    if isinstance(empleado, GerenteProyecto):
        empleado.trabajar()
