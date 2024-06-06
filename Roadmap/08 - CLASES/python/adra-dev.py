"""
EJERCICIO:
Explora el concepto de clase y crea un ejemplo que implemente un 
inicializador, atributos y una funcion que los imprima (teniendo en 
cuenta las posibilidades de tu lenguaje).
Una vez implementada, creala, establece sus parametros, modificalos e
imprimelos utilizando una funcion.

DIFICULTAD EXTRA (opcional):
- Implementa dos clases que representen las estructuras de Pila y 
Cola (estudiadas en el ejercicio numero 7 de la ruta de estudio)
- Deben poer inicializarse y disponer de operaciones para añadir, 
eliminar, retornar el número de elementos e imprimir todo su 
contenido.

by adra-dev.
"""

# POO (Programacion Orientada a Objetos.)

"""
            Todo en python es un objeto.

La progamacion orientada a objetos es un paradigma de progamacion, es
decir, un estilo y tecnica de programacion, que va mas alla de la 
propia implementacion. Este paradigma se fundamenta en el concepto de
<<objeto>>, el cual puede contener tando datos, bajo la forma de 
campos denominados atributos, como codigo para su manipulacion, bajo 
la forma de procedimientos y funciones, denominados <<metodos>>.
Gracias a esto podemos agruparlo todo bajo un solo tipo de dato (la 
<<clase>> objeto), la cual facilita la modularidad y la reusabilidad 
del codigo.

Los cuatro principios fundamentales de este paradigma son los 
siguientes:
            Abstraccion de datos.
            Encapsulacion
            Herencia
            Polimorfismo.

"""


"""
Clases:
Una clase es como un tipo abstracto para los objetos que, ademas de 
almacenar valores denominados atributos, tiene asociados una serie de
funciones que llamamos metodos. Una instacia de una clase es lo mismo
que decir un objeto de esa clase. Instanciar una clase hace referencia
a la creacion de un objeto que pertenece a esa clase.

"""

class Dispositivo:
    """ Clase dispositivo, para objetos conectados a la red """

    def __init__(self, IP) -> None:
        """ Constructor """
        self.IP = IP            # Atributo con valor definido
        self.encendido = False  # Atributo con valor por defecto

    def __del__(self):
        """ Destructor """
        print("Destruyendo el dispositivo en", self.IP)

    def encender(self):
        """ Enciende el dispositivo """
        self.encendido = True

    def apagar(self):
        """ Apaga el dispositivo """
        self.encendido = False

    def estado(self):
        """ Muestra en pantalla el estado del dispositivo """
        mensaje = f"IP: {self.IP}\n"
        if self.encendido:
            mensaje += 'Estado: encendido'
        else:
            mensaje += 'Estado: apagado'
        return mensaje
    
# Instanciacion
    
tv = Dispositivo('4.6.2.3')            # creamos el objeto

print(tv.encendido)                    # accedemos a un atributo

print(tv.IP)                           # accedemos a otro atributo

print(tv.encender())                   # invocamos un metodo

print(tv.encendido)                    # accedemos al atributo

print(tv.estado())                     # invocamos un metodo



"""
Extra
"""

# LIFO


class Stack:

    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if self.count() == 0:
            return None
        return self.stack.pop()

    def count(self):
        return len(self.stack)

    def print(self):
        for item in reversed(self.stack):
            print(item)


my_stack = Stack()
my_stack.push("A")
my_stack.push("B")
my_stack.push("C")
print(my_stack.count())
my_stack.print()
my_stack.pop()
print(my_stack.count())
print(my_stack.pop())
print(my_stack.pop())
print(my_stack.pop())
print(my_stack.pop())
print(my_stack.pop())
print(my_stack.count())

# FIFO


class Queue:

    def __init__(self):
        self.queue = []

    def enqueue(self, item):
        self.queue.append(item)

    def dequeue(self):
        if self.count() == 0:
            return None
        return self.queue.pop(0)

    def count(self):
        return len(self.queue)

    def print(self):
        for item in self.queue:
            print(item)


my_queue = Queue()
my_queue.enqueue("A")
my_queue.enqueue("B")
my_queue.enqueue("C")
print(my_queue.count())
my_queue.print()
my_queue.dequeue()
print(my_queue.count())
print(my_queue.dequeue())
print(my_queue.dequeue())
print(my_queue.dequeue())
print(my_queue.dequeue())
print(my_queue.dequeue())
print(my_queue.count())
