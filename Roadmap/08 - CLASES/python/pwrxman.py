"""
* EJERCICIO:
 * Explora el concepto de clase y crea un ejemplo que implemente un inicializador,
 * atributos y una función que los imprima (teniendo en cuenta las posibilidades
 * de tu lenguaje).
 * Una vez implementada, créala, establece sus parámetros, modifícalos e imprímelos
 * utilizando su función.
"""
class Auto:
      def __init__ (self, marca: str, modelo: str, tipo: str, anio: int, caracteristicas: list):
          self.marca = marca
          self.modelo = modelo
          self.tipo = tipo
          self.anio = anio
          self.caracteristicas = caracteristicas

      def car_info(self):
        return f"El auto solicitado es un {self.marca}:{self.modelo}:{self.tipo}:{self.anio} con el siguiente equipo especial {self.caracteristicas}"  

      def add_carac_especial(self, adicional: str):
          self.caracteristicas.append(adicional)


car = Auto("Honda", "Civic", "Sedan", 2024,["Blanco", "Faros Niebla", "Frenos Ventilados"])
print(car.marca)
print(car.car_info())


car.add_carac_especial("Quemacocos")
car.add_carac_especial("Rines Aluminio")
print(car.car_info())  




"""
* DIFICULTAD EXTRA (opcional):
 * Implementa dos clases que representen las estructuras de Pila y Cola (estudiadas
 * en el ejercicio número 7 de la ruta de estudio)
 * - Deben poder inicializarse y disponer de operaciones para añadir, eliminar,
 *   retornar el número de elementos e imprimir todo su contenido.
"""

# LIFO
class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item):       # Insertar elemento en la pila
        self.stack.append(item)
    
    def pop(self):              # Eliminar elemento de la pila
        if self.count() == 0:
            return None
        return self.stack.pop()
    
    def count(self):
        return len(self.stack)
    
    def print(self):
        for item in reversed(self.stack):
            print(item)

# FIFO

class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, item):
        self.queue.append(item)

    def unqueue(self):
        if self.count() == 0:
            return None
        return self.queue.pop(0)

    def count(self):
        return len(self.queue)
    
    def print(self):
        for item in self.queue:
            print(item)

    


pila = Stack()
cola = Queue()

while True:
    print("PILAS")
    print("\t1 - Agregar elemento en Pila")
    print("\t2 - Eliminar elemento de Pila")
    print("\t3 - Mostrar Elementos de la Pila\n")
    print("\t4 - Contar Elementos de la Pila\n")

    print("COLAS")
    print("\t5 - Agregar elemento en cola")
    print("\t6 - Eliminar elemento de cola")
    print("\t7 - Mostrar Elementos de la cola\n")
    print("\t8 - Contar Elementos de la cola\n")
    print("q - Terminar")

    action= input("Que desea hacer? ")
    match action:
        case '1':
            element=input("Cual es el elemento que desea añadir a la Pila? ")
            pila.push(element)
            # addelem(element, stack)
        case '2':
            pila.pop()
            # pop(stack)
        case '3':
            pila.print()
        case '4':
            pila.count()
        case '5':
            element=input("Cual es el elemento que desea añadir a la Cola? ")
            cola.enqueue(element)
        case '6': 
            cola.unqueue()
        case '7': 
            cola.print()
        case '8': 
            cola.count()

        case 'q':
            print("Hasta la vista...")
            break




