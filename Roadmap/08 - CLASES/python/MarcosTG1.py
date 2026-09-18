"""
* EJERCICIO:
* Explora el concepto de clase y crea un ejemplo que implemente un inicializador,
* atributos y una función que los imprima (teniendo en cuenta las posibilidades
* de tu lenguaje).
* Una vez implementada, créala, establece sus parámetros, modifícalos e imprímelos
* utilizando su función.
"""

class Futbolista():

    dorsal: int = None
    
    def __init__(self, nombre: str, edad: int, pie_bueno: str, trayectoria: list):

        self.nombre = nombre
        self.edad = edad
        self.pie_bueno = pie_bueno
        self.trayectoria = trayectoria

    def mostrar_jugador(self):
        print(f"El jugador se llama {self.nombre}, tiene {self.edad} años y es {self.pie_bueno} y ha jugado en {self.trayectoria}, juega con el {self.dorsal}.")

jugador_1 = Futbolista("Lionel", 40, "zurdo", ["Newells", "Barça", "PSG", "Miami"])
jugador_1.mostrar_jugador()
jugador_1.dorsal = 10
jugador_1.pie_bueno = "ambidiestro"
jugador_1.mostrar_jugador()



"""
* DIFICULTAD EXTRA (opcional):
* Implementa dos clases que representen las estructuras de Pila y Cola (estudiadas
* en el ejercicio número 7 de la ruta de estudio)
* - Deben poder inicializarse y disponer de operaciones para añadir, eliminar,
*   retornar el número de elementos e imprimir todo su contenido.
"""

class Pila:
    def __init__(self):
        self.pila = []

    def insertar(self, item):
        self.pila.append(item)
    
    def eliminar_ultimo(self):
        del self.pila[len(self.pila) - 1]
    
    def mostrar_pila(self):
        print(self.pila)

    def devolver_numero_elementos(self):
        return (len(self.pila))


mi_pila = Pila()

mi_pila.insertar(1)
mi_pila.insertar(2)
mi_pila.insertar(3)
mi_pila.insertar(4)

mi_pila.eliminar_ultimo()
mi_pila.mostrar_pila()

elementos = mi_pila.devolver_numero_elementos()
print(elementos)

print(type(mi_pila))

class Cola():
    
    def __init__(self):
        self.cola = []
    
    def insertar(self, item):
        self.cola.append(item)
    
    def eliminar(self):
        del self.cola[0]
    
    def mostrar(self):
        print(self.cola)
    
    def devolver_numero_elementos(self):
        return len(self.cola)

mi_cola = Cola()

mi_cola.insertar(1)
mi_cola.insertar(2)
mi_cola.insertar(3)
mi_cola.insertar(4)

mi_cola.eliminar()

mi_cola.mostrar()

elementos_cola = mi_cola.devolver_numero_elementos()
print(f"La cola actualmente tiene {elementos_cola} elementos.")