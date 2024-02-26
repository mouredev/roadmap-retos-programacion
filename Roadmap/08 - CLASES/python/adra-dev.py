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



class Pila:
    """ Clase pila, para almacenar objetos """

    def __init__(self) -> None:
        """ Constructor """
        self.pila = []          # Atributo con valor por defecto


    def __del__(self):
        """ Destructor """
        del self.pila 
        print("Destruyendo la pila")

    def almacenar(self, *args):
        """ Almacena un objeto en la pila  """
        self.pila.append(args)
        mensaje = f"Almacenando {args}"
        return mensaje


    def extraer(self):
        """ Extrae el ultimo elemento almacenado en la pila """
        lste = self.pila.pop() 
        mensaje = f"Extrayendo el elemento: {lste}"
        return mensaje

    def estado(self):
        """ Muestra en pantalla el estado de la pila """
        mensaje = f"numero de elementos : {len(self.pila)}"
        if len(self.pila) > 0:
            mensaje += ' almacenados en la pila'
        else:
            mensaje += ' la pila esta vacia'
        return mensaje
    
    def contenido(self):
        "Muestra el contenido de la pila"
        if len(self.pila) == 0:
            print('La pila esta vacia')
        else:
            print(self.pila)
    

pila = Pila()                              # creamos el objeto

print(pila.pila)                           # accedemos a un atributo

print(pila.almacenar(1))                   # invocamos un metodo

print(pila.almacenar(1))                   # invocamos un metodo

print(pila.almacenar(3))                   # invocamos un metodo

print(pila.almacenar(2))                   # invocamos un metodo

print(pila.estado())                       # invocamos un metodo

print(pila.extraer())                      # accedemos al atributo

print(pila.estado())                       # invocamos un metodo

print(pila.contenido())                    # invocamos un metodos
            

class Cola:
    """ Clase cola """

    def __init__(self) -> None:
        """ Constructor """
        self.queue = []

    def __del__(self):
        """ Destructor """
        del self.queue 
        print("Destruyendo la cola")

    def anadir(self, *args):
        """ Agrega un documento a la cola """
        self.queue.append(args)
        mensaje = f"Aniadiendo {args}"
        return mensaje

    def extraer(self,):
        """ Extrae el ultimo documento de la cola """
        elemento = self.queue.pop(0)
        mensaje = f"Extrayendo el elemento: {elemento}"
        return mensaje

    def estado(self):
        """ Muestra en pantalla el estado de cola """
        mensaje = f"numero de elementos : {len(self.queue)}"
        if len(self.queue) > 0:
            mensaje += ' almacenados en la cola'
        else:
            mensaje += ' la cola esta vacia'
        return mensaje
    
    def contenido(self):
        "Muestra el contenido de la pila"
        if len(self.queue) == 0:
            print('La cola esta vacia')
        else:
            print(self.queue)


cola = Cola()                              # creamos el objeto

print(cola.queue)                           # accedemos a un atributo

print(cola.anadir(1))                   # invocamos un metodo

print(cola.anadir(2))                   # invocamos un metodo

print(cola.anadir(1))                   # invocamos un metodo

print(cola.anadir(3))                   # invocamos un metodo

print(cola.estado())                       # invocamos un metodo

print(cola.extraer())                      # accedemos al atributo

print(cola.estado())                       # invocamos un metodo

print(cola.contenido())                    # invocamos un metodos