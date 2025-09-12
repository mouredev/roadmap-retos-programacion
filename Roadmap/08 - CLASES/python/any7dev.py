# /*
#  * EJERCICIO:
#  * Explora el concepto de clase y crea un ejemplo que implemente un inicializador,
#  * atributos y una función que los imprima (teniendo en cuenta las posibilidades
#  * de tu lenguaje).
#  * Una vez implementada, créala, establece sus parámetros, modifícalos e imprímelos
#  * utilizando su función.
#  *
#  * DIFICULTAD EXTRA (opcional):
#  * Implementa dos clases que representen las estructuras de Pila y Cola (estudiadas
#  * en el ejercicio número 7 de la ruta de estudio)
#  * - Deben poder inicializarse y disponer de operaciones para añadir, eliminar,
#  *   retornar el número de elementos e imprimir todo su contenido.
#  * 
#  */

# EJERCICIO
class Vehiculo:
    def __init__(self, tipo, marca, modelo):
        self.tipo = tipo
        self.marca = marca
        self.modelo = modelo
    def imprimir(self):
        print(f"Soy un {self.tipo} de la marca {self.marca} modelo {self.modelo}")

mi_vehiculo = Vehiculo("coche", "Toyota", "Auris")
mi_vehiculo.imprimir()

#DIFICULTAD EXTRA
class Pila:
    def __init__(self, lista):
        self.lista = lista
    def añadir(self, numero):
        self.lista.append(numero)
    def eliminar(self):
        self.lista.pop()
    def elementos(self):
        return len(self.lista)
    def imprimir(self):
        print(self.lista)

mi_pila = Pila(lista=[1, 2, 3, 4, 5])
mi_pila.añadir(6)
mi_pila.eliminar()
print(mi_pila.elementos())
mi_pila.imprimir()

class Cola:
    def __init__(self, cola):
        self.cola = cola
    def añadir(self, numero):
        self.cola.append(numero)
    def eliminar(self):
        self.cola.pop(0)
    def elementos(self):
        return len(self.cola)
    def imprimir(self):
        print(self.cola)

mi_cola = Cola(cola=[6, 7, 8, 9, 10])
mi_cola.añadir(11)
mi_cola.eliminar()
print(mi_cola.elementos())
mi_cola.imprimir()