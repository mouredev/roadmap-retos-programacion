'''Explora el concepto de clase y crea un ejemplo que implemente un inicializador,
 * atributos y una función que los imprima (teniendo en cuenta las posibilidades
 * de tu lenguaje).
 * Una vez implementada, créala, establece sus parámetros, modifícalos e imprímelos
 * utilizando su función.
 *
 * DIFICULTAD EXTRA (opcional):
 * Implementa dos clases que representen las estructuras de Pila y Cola (estudiadas
 * en el ejercicio número 7 de la ruta de estudio)
 * - Deben poder inicializarse y disponer de operaciones para añadir, eliminar,
 *   retornar el número de elementos e imprimir todo su contenido.'''

 #Clases

class Programador:
    def __init__(self, nombre, apellido, lenguajes) -> None:
      self.nombre = nombre
      self.apellido = apellido
      self.lenguajes = lenguajes
    librerias = None

    def programar(self):
      print(f"{self.nombre} {self.apellido} está practicando clases con {self.lenguajes}")

    def datos(self):
       print(f"Datos del programador: Nombre:{self.nombre}, apellido:{self.apellido}, lenguajes:{self.lenguajes}, librerias:{self.librerias}")

my_programador = Programador("Brais","Moure",["Kotlin","Swift"])
print(f"{my_programador.nombre} programa en los lenguajes {my_programador.lenguajes}")
my_programador.datos()

yo = Programador(f"Gabriel","Castro","Python")
yo.programar()
yo.datos()
yo.librerias = ["Pandas","Numpy"]
yo.lenguajes = ["Python","SQL"]
yo.datos()

#Reto extra

class Pila:
    def __init__(self,lista) -> None:
      self.lista = lista
    def pop(self):
        if len(self.lista) == 0:
           print("La pila está vacia")
        else:   
            return self.lista.pop()
      
    def push(self,element):
        self.lista.append(element)
      
    def imprimir(self):
        for elemento in self.lista[::-1]:
            print(elemento)
    
    def cantidad_elementos(self):
       print(len(self.lista))

pila = Pila([1,2,3])
pila.imprimir()
pila.pop()
pila.imprimir()
pila.push(4)
pila.imprimir()
pila.cantidad_elementos()


class Cola:
    def __init__(self,lista) -> None:
        self.lista = lista
    
    def enqueue(self,element):
        self.lista.insert(0,element)
    
    def dequeue(self):
        if len(self.lista) == 0:
            print("Cola vacía")
        else:
            return self.lista.pop()
    
    def imprimir(self):
        for elemento in self.lista:
            print(elemento)
    
    def cantidad_elementos(self):
        print(len(self.lista))

cola = Cola(["a","b","c"])
cola.imprimir()
cola.dequeue()
cola.imprimir()
cola.enqueue("d")
cola.imprimir()
cola.cantidad_elementos()