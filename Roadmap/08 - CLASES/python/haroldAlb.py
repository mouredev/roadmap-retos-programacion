### EJERCICIO ###
 # Explora el concepto de clase y crea un ejemplo que implemente un inicializador,
 # atributos y una función que los imprima (teniendo en cuenta las posibilidades
 # de tu lenguaje). Una vez implementada, créala, establece sus parámetros, modifícalos e imprímelos
 # utilizando su función.

class Coche():
    def __init__(self, marca: str, cilindrada: int, color: str):
        self.marca = marca
        self.cilindrada = cilindrada
        self.color = color
        self.motor_encendido: bool = False

    def estado(self):
        print(f"Marca: {self.marca}", f"Cilindrada: {self.cilindrada}", f"Color: {self.color}", f"Estado del motor: {self.motor_encendido}", sep= " | ")

    def arrancar(self):
        self.motor_encendido = True

mercedes = Coche("Mercedes", 2500, "Negro")
mercedes.estado()
mercedes.color = "Rosa"
mercedes.cilindrada = 3000
mercedes.estado()

### EXTRA ###
 # Implementa dos clases que representen las estructuras de Pila y Cola (estudiadas
 # en el ejercicio número 7 de la ruta de estudio).
 # Deben poder inicializarse y disponer de operaciones para añadir, eliminar,
 # retornar el número de elementos e imprimir todo su contenido.

# PILAS - LIFO #
print("#" * 10,"PILAS - LIFO","#" * 10, sep=" ")


class Pila():
    def __init__(self):
        self.pila = []
        self.elemento_borrado = None
       
    def añadir(self, elemento):
        self.pila.append(elemento)

    def eliminar(self):
        self.elemento_borrado = self.pila.pop()

    def num_elementos(self):
        return len(self.pila)

    def mostrar(self):
        print("Elementos de la Pila:")
        for i, e in enumerate(self.pila):
            print(f"    Index_{i}: {e}")

mi_pila = Pila()

mi_pila.añadir(00)
mi_pila.añadir(10)
mi_pila.añadir(20)

print(f"El número de elementos en la pila es de {mi_pila.num_elementos()}")

mi_pila.eliminar()
print(f"El elemento borrado fue {mi_pila.elemento_borrado}")

print(f"El número de elementos en la pila es de {mi_pila.num_elementos()}")

mi_pila.mostrar()

# COLAS - FIFO #
print("#" * 10,"COLAS - FIFO","#" * 10, sep=" ")

class Cola():
    def __init__(self):
        self.cola = []
        self.elemento_borrado = None
    
    def añadir(self, elemento):
        self.cola.append(elemento)

    def eliminar(self):
        self.elemento_borrado = self.cola.pop(0)

    def num_elementos(self):
        return len(self.cola)

    def mostrar(self):
        print("Elementos de la Cola:")
        for i, e in enumerate(self.cola):
            print(f"    Index_{i}: {e}")
    
mi_cola = Cola()

mi_cola.añadir(0)
mi_cola.añadir(10)
mi_cola.añadir(20)

print(f"El número de elementos de la cola es de {mi_cola.num_elementos()}")

mi_cola.eliminar()
print(f"El elemento borrado fue {mi_cola.elemento_borrado}")

print(f"El número de elementos de la cola es de {mi_cola.num_elementos()}")

mi_cola.mostrar()