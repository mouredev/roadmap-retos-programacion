#09 HERENCIA
#### Dificultad: Media | Publicación: 26/02/24 | Corrección: 04/03/24

## Ejercicio


"""
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
 """

class Animal:
    def __init__(self, nombre, sonido):
        self._nombre = nombre
        self._sonido = sonido

    # getters y setters
    @property
    def nombre(self):
        return self._nombre
    
    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre
    
    @property
    def sonido(self):
        return self._sonido
    
    @sonido.setter
    def sonido(self, sonido):
        self._sonido = sonido

    def emitir_sonido(self):
        return self._sonido

class Perro(Animal):
    def __init__(self, nombre):
        super().__init__(nombre, "AWUUUFFF!")

class Gato(Animal):
    def __init__(self, nombre):
        super().__init__(nombre, "Mmmmmmeeeeeoooowww!")

# Creo un perro y un gato
perro = Perro("Sora")
gato = Gato("Doña Tecla")

# Muestro el sonido que emiten
print(f"Hola soy {perro._nombre} escucha esto: {perro.emitir_sonido()}")
print(f"Hola soy {gato._nombre} escucha esto: {gato.emitir_sonido()}")