"""
* EJERCICIO:
* Explora el concepto de clase y crea un ejemplo que implemente un inicializador,
* atributos y una función que los imprima (teniendo en cuenta las posibilidades
* de tu lenguaje).
* Una vez implementada, créala, establece sus parámetros, modifícalos e imprímelos
* utilizando su función.
*
* DIFICULTAD EXTRA (opcional):
* Implementa dos clases que representen las estructuras de Pila y Cola (estudiadas
* en el ejercicio número 7 de la ruta de estudio)
* - Deben poder inicializarse y disponer de operaciones para añadir, eliminar,
*   retornar el número de elementos e imprimir su contenido al completo.
*
"""


class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def imprimir_informacion(self):
        print("Nombre:", self.nombre)
        print("Edad:", self.edad)


# Crear una instancia de la clase Persona
persona1 = Persona("Juan", 30)

# Imprimir la información utilizando el método de la clase
persona1.imprimir_informacion()

# Modificar los atributos y volver a imprimir la información
persona1.nombre = "María"
persona1.edad = 25
persona1.imprimir_informacion()
