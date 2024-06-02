"""
/*
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

class Operario_Quimico():

    def __init__(self, name:str, work:list, age:int):
        self.name = name
        self.work = work
        self.age = age
    
    def print(self):
        return print(
            f"Nombre {self.name}| Puesto de trabajo {self.work}| Edad {self.age}")
    


operario_1 = Operario_Quimico("Antonio",["Thermos,Slitter"], 48)
operario_1.print()
print(type(operario_1))


"""
Extra
"""

class stack():
    def __init__(self):
        self.stack = []

    def añadir(self, item:int):
        self.stack.append(item)
    
    def eliminar(self):
        if self.contar() == 0:
            return None
        self.stack.pop()

    def contar(self):
        return len(self.stack)
    
    def imprimir(self):
        for item in reversed(self.stack):
            print(item)

mi_pila = stack()
mi_pila.añadir(5)
mi_pila.añadir(4)
mi_pila.añadir(3)
mi_pila.añadir(2)
mi_pila.añadir(1)
print(mi_pila.contar())
mi_pila.imprimir()
mi_pila.eliminar()


class queue():
    def __init__(self):
        self.queue = []

    def encolar(self, item:int):
        self.queue.append(item)
    
    def desencolar(self):
        if self.contar() == 0:
            return None
        self.queue.pop()

    def contar(self):
        return len(self.queue)
    
    def imprimir(self):
        for item in self.queue:
            print(item)

mi_cola = queue()
mi_cola.encolar(1)
mi_cola.encolar(2)
mi_cola.encolar(3)
mi_cola.encolar(4)
mi_cola.encolar(5)
print(mi_cola.contar())
mi_cola.imprimir()
mi_cola.desencolar()
print(mi_cola.desencolar())
print(mi_cola.contar())
print(mi_cola.desencolar())