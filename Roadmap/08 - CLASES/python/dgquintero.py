# Estudio de Clases en python
# Autor: Daniel Quintero

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
 *   retornar el número de elementos e imprimir todo su contenido.
 * 
 */
"""

class Clase:
  def __init__(self, nombre, edad):
    self.nombre = nombre
    self.edad = edad

  def imprimir(self):
    print("Nombre: ", self.nombre)
    print("Edad: ", self.edad)


clase = Clase("Daniel", 32)
clase.imprimir()
clase.nombre = "Daniel Quintero"
clase.imprimir()

class Pila:
  def __init__(self):
    self.pila = []

  def apilar(self, elemento):
    self.pila.append(elemento)

  def desapilar(self):
    return self.pila.pop()

  def esta_vacia(self):
    return len(self.pila) == 0

  def tamano(self):
    return len(self.pila)

  def imprimir(self):
    print(self.pila)


pila = Pila()
pila.apilar(1)
pila.apilar(2)
pila.apilar(3)
pila.imprimir()
print(pila.desapilar())
print(pila.desapilar())
print(pila.desapilar())

class Cola:
  def __init__(self):
    self.cola = []

  def agregar(self, elemento):
    self.cola.append(elemento)

  def quitar(self):
    return self.cola.pop(0)

  def esta_vacia(self):
    return len(self.cola) == 0

  def tamano(self):
    return len(self.cola)

  def imprimir(self):
    print(self.cola)

cola = Cola()
cola.agregar(1)
cola.agregar(2)
cola.agregar(3)
cola.imprimir()
print(cola.quitar())
print(cola.quitar())
print(cola.quitar())

