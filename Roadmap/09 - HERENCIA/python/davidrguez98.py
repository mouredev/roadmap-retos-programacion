""" /*
 * EJERCICIO:
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
 */ """

""" class animal():
    def __init__(self, sound):
        self.sound = sound

class dog(animal):
    
    def __init__(self, sound):
        super().__init__(sound)

class cat(animal):
    def __init__(self, sound):
        super().__init__(sound)

my_dog = dog(sound="Guau")
print(my_dog.sound)
my_cat = cat(sound="Miau")
print(my_cat.sound) """

#DIFICULTAD EXTRA

class empleados:
    def __init__(self, id, name):
        self.id = id
        self.name = name

class gerentes(empleados):
    def __init__(self, id, name, work):
        super().__init__(id, name)
        self.work = work
    
    def charge_workers_gerentes():
        print(len(gerentes_proyectos) + len(programadores))

class gerentes_proyectos(empleados):
    def __init__(self, id, name, work):
        super().__init__(id, name)
        self.work = work

    def charge_workers_gerentes_proyectos():
        print(len(programadores))

class programadores(empleados):
    def __init__(self, id, name, work):
        super().__init__(id, name)
        self.work = work

User1 = gerentes_proyectos(1, "Juan", "Gerente de proyecto")
User2 = gerentes_proyectos(2, "Pepe", "Gerente de proyecto")
User3 = gerentes_proyectos(3, "María", "Gerente de proyecto")
User4 = gerentes_proyectos(4, "Carlos", "Gerente de proyecto")


print(User1.id, User1.name, User1.work)
print(User2.id, User2.name, User2.work)
print(User3.id, User3.name, User3.work)
print(User4.id, User4.name, User4.work)
print(gerentes.charge_workers_gerentes)