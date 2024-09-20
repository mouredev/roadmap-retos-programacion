#09 HERENCIA Y POLIMORFISMO

"""
 * Explora el concepto de herencia según tu lenguaje. Crea un ejemplo que
 * implemente una superclase Animal y un par de subclases Perro y Gato,
 * junto con una función que sirva para imprimir el sonido que emite cada Animal.
"""

class animal():
    def __init__(self, nombre, raza, edad) -> None:
        self.nombre = nombre
        self.raza = raza
        self.edad = edad

    def hacer_sonido(self):
        print("Sonido de algún animal")

    def __str__(self):
        return f"{self.nombre} es un {self.raza} de {self.edad} años"

class perro(animal):
    def sonido(self):
        print("Guaf")

class gato(animal):
    def sonido(self):
        print("Maau")        

def print_sonido(animal):
    animal.sonido()

cat = gato("Sally","Montañeza",5)
cat.sonido()
print(cat)
print_sonido(cat)


"""
 * DIFICULTAD EXTRA (opcional):
 * Implementa la jerarquía de una empresa de desarrollo formada por Empleados que
 * pueden ser Gerentes, Gerentes de Proyectos o Programadores.
 * Cada empleado tiene un identificador y un nombre.
 * Dependiendo de su labor, tienen propiedades y funciones exclusivas de su
 * actividad, y almacenan los empleados a su cargo.
"""

class empleado():

    def __init__(self, nombre, id) -> None:
        self.nombre = nombre
        self.id = id
        self.empleados = []

class gerente(empleado):

    def __init__(self, nombre, id, departamento) -> None:
        super().__init__(nombre, id)
        self.departamento = departamento

    def gestionar(self):
        if len(self.empleados) > 0:
            return print(f"{self.nombre} gestiona el departamento {self.departamento}\nTiene {len(self.empleados)} empleados a cargo")
        else:
            return print(f"{self.nombre} gestiona el departamento {self.departamento}\nFalta asignar empleados a cargo")
        
class proyecto(empleado):

    def __init__(self, nombre, id, proyecto) -> None:
        super().__init__(nombre, id)
        self.proyecto = proyecto

    def asignar(self):
        return print(f"{self.nombre} se encuentra dirigiendo el proyecto {self.proyecto}")


class programador(empleado):

    def __init__(self, nombre, id, lenguajes) -> None:
        super().__init__(nombre, id)
        self.lenguajes = lenguajes

    def programar(self):
        return print(f"{self.nombre} se encuentra programando en los siguientes lenguajes: {self.lenguajes}")
    

manager001 = gerente('Kimm','00001','Estad´siticas')
manager002 = proyecto('Jann','03450','Global46')
program001 = programador('Otto', '33394',['Python','R'])
manager001.empleados = [manager002.nombre, program001.nombre]
manager002.empleados = [program001.nombre]
manager001.gestionar()
manager002.asignar()
program001.programar()
print(f"{manager001.nombre} tiene {len(manager001.empleados)} a cargo: {manager001.empleados}")
print(f"{manager002.nombre} tiene {len(manager002.empleados)} a cargo: {manager002.empleados}")
print(f"La ID de {manager001.nombre} es: {manager001.id}")
print(f"La ID de {manager002.nombre} es: {manager002.id}")
print(f"La ID de {program001.nombre} es: {program001.id}")