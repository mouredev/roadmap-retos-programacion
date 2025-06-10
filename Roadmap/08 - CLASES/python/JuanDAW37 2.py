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
"""

class Vehiculo:
    color = "None"
    
    def __init__(self, marca:str, modelo:str, ruedas: int, cilindrada:int, potencia:int):
        self.marca = marca
        self.modelo = modelo
        self.ruedas = ruedas
        self.cilindrada = cilindrada
        self.potencia = potencia
    
    def imprimir(self):
        print(f"Marca: {self.marca}, Modelo: {self.modelo}, Color: {self.color}, Ruedas {self.ruedas}, Cilindrada: {self.cilindrada}, Potencia: {self.potencia}")
        
mi_coche = Vehiculo('Toyota', 'Auris', 4, 1500, 115)
mi_coche.color = 'Azul'
mi_coche.imprimir()

mi_moto = Vehiculo('Vespa', 'GTS', 2, 300, 75)
mi_moto.color = 'Verde'
mi_moto.imprimir()

# EXTRA
# Pila, LIFO
class Pila:
    def __init__(self):
        self.contenido = []
        
    def anadir(self, item):
        self.contenido.append(item)    
        
    def quitar(self):
        if self.contar() > 0:
            return self.contenido.pop() # Como es una pila, sacamos siempre el último elemento
    
    def contar(self):
        return len(self.contenido)
    
    def imprimir(self):
        for  item in reversed(self.contenido):
            if isinstance(item, Vehiculo):
                item.imprimir()
            else:
                print(item)
            
mi_pila = Pila()
mi_pila.anadir(1)
mi_pila.anadir(mi_moto)
mi_pila.anadir('Juan')
mi_pila.anadir(['A', 'B', 'C', 'D'])
print(mi_pila.contar())
mi_pila.imprimir()
mi_pila.quitar()
print(mi_pila.contar())
mi_pila.imprimir()

# Cola, FIFO
class Cola:
    def __init__(self):
        self.contenido = []
    
    def anadir(self, item):
        self.contenido.append(item)
    
    def quitar(self):
        if self.contar() > 0:
            self.contenido.pop(0) #Como es una cola, sacamos siempre el primer elemento
    
    def contar(self):
        return len(self.contenido)
    
    def imprimir(self):
        for item in self.contenido:
            if isinstance(item, Vehiculo):
                item.imprimir()
            else:
                print(item)
                
mi_cola = Cola()
mi_cola.anadir(3)
mi_cola.anadir(mi_coche)
mi_cola.anadir('Mónica')
mi_cola.anadir(['E', 'F', 'G', 'H'])
print(mi_cola.contar())
mi_cola.imprimir()
mi_cola.quitar()
print(mi_cola.contar())
mi_cola.imprimir()