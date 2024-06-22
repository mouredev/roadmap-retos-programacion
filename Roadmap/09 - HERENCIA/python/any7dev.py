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

# EJERCICIO
class Animal:
    def __init__(self, nombre):
        self.nombre = nombre
    def sonido(self):
        pass

class Perro(Animal):
    def sonido(self):
        print(f"Soy {self.nombre} guau")
    
class Gato(Animal):
    def sonido(self):
        print(f"Soy {self.nombre} miau")

mi_perro = Perro("Firulais")
mi_gato = Gato("Peluso")
mi_perro.sonido()
mi_gato.sonido()

    

