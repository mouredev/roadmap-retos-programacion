#clases

"""
que es una clase en python
Una clase en Python es una plantilla o un molde para crear objetos. 
Define un conjunto de atributos (propiedades o datos) y métodos (funciones) que los objetos creados a partir de la clase tendrán. 
Las clases permiten encapsular datos y comportamientos relacionados, 
facilitando la organización y reutilización del código.
"""

class Persona: #definimos una clase llamada Persona
    surname: str 
    def __init__(self, nombre: str, edad: int, lenguaje: list): #el metodo __init__ es el constructor de la clase, se ejecuta automaticamente al crear un objeto de la clase
        self.nombre = nombre #self es una referencia al objeto actual, se usa para acceder a los atributos y metodos de la clase
        self.edad = edad #aqui estamos definiendo los atributos de la clase, que son nombre y edad
        self.lenguaje = lenguaje

    def saludar(self): #aqui estamos definiendo un metodo de la clase, que es saludar
        print(f"Hola, soy {self.nombre} {self.surname} y tengo {self.edad} años y estoy aprendiendo logica de programacion en {self.lenguaje}.") #aqui estamos definiendo el comportamiento del metodo saludar

"""
Aquí, Persona es una clase que describe cómo será cada persona: qué datos tendrá (nombre, edad) y qué podrá hacer (saludar).
"""

persona1 = Persona("Ivan", 25, "Python") #creamos un objeto de la clase Persona, llamado persona1
persona1.surname = "RN" #asignamos un valor al atributo surname del objeto persona1
print(persona1.nombre)  # Imprime: Ivan
persona1.saludar()  # Imprime: Hola, soy Ivan RN y tengo 25 años y estoy aprendiendo logica de programacion en Python.
persona2 = Persona("Ana", 30, ["Python", "Java", "C++", "JavaScript"]) #creamos otro objeto de la clase Persona, llamado persona2
persona2.surname = "Doe" #asignamos un valor al atributo surname del objeto persona2
persona2.saludar()  # Imprime: Hola, soy Ana Doe y tengo 30 años y estoy aprendiendo logica de programacion en ['Python', 'Java', 'C++', 'JavaScript'].
print(persona2.edad)  # Imprime: 30
persona1.edad = 26 #modificamos el atributo edad del objeto persona1
persona1.saludar()  
# Imprime: Hola, soy Ivan RN y tengo 26 años y estoy aprendiendo logica de programacion en Python. 
#(ya que hemos modificado la edad)



"""
Aquí, hemos creado dos objetos de la clase Persona: persona1 y persona2.

Cada uno tiene sus propios atributos (nombre, apellido, edad y lenguajes) 
y puede realizar acciones (saludar) de forma independiente.

Las clases son fundamentales en la programación orientada a objetos (POO)
 y permiten crear estructuras de datos complejas y comportamientos personalizados.
"""

#XtraJ

class pila: #LIFO (Last In, First Out)
    def __init__(self):
        self.stack = []  # Inicializa una lista vacía para almacenar los elementos de la pila

    def push(self, item):
        self.stack.append(item)  # Añade un elemento a la cima de la pila

    def pop(self):
        if len(self.stack) > 0: # Verifica si la pila no está vacía
            return self.stack.pop()  # Remueve y devuelve el elemento de la cima de la pila
        return None  # Si la pila está vacía, devuelve None
        

    def size(self):
        return len(self.stack)  # Devuelve el número de elementos en la pila
    
    def print(self):
        for item in reversed(self.stack): # Recorre los elementos de la pila
            print(item)  # Imprime cada elemento

# Instanciación y uso de la clase pila fuera de la definición de la clase
mi_pila = pila()  # Crea una instancia de la clase pila

mi_pila.push(1)  # Añade el elemento 1 a la pila
mi_pila.push(2)  # Añade el elemento 2 a la pila
mi_pila.push(3)  # Añade el elemento 3 a la pila
print("Tamaño de la pila:", mi_pila.size())  # Imprime el tamaño actual de la pila
mi_pila.print()  # Imprime los elementos actuales de la pila
elemento = mi_pila.pop()  # Remueve el elemento de la cima de la pila
print("Elemento removido:", elemento)  # Imprime el elemento removido
print("Tamaño de la pila después de pop:", mi_pila.size())  # Imprime el tamaño de la pila después de la operación pop
    

#cola FIFO (First In, First Out)
class Cola: 
    def __init__(self):
        self.queue = []  # Inicializa una lista vacía para almacenar los elementos de la cola

    def enqueue(self, item):
        self.queue.append(item)  # Añade un elemento al final de la cola

    def dequeue(self):
        if len(self.queue) > 0: # Verifica si la cola no está vacía
            return self.queue.pop(0)  # Remueve y devuelve el primer elemento de la cola
        return None  # Si la cola está vacía, devuelve None

    def size(self):
        return len(self.queue)  # Devuelve el número de elementos en la cola
    
    def print(self):
        for item in self.queue: # Recorre los elementos de la cola
            print(item)  # Imprime cada elemento
# Instanciación y uso de la clase Cola fuera de la definición de la clase
mi_cola = Cola()  # Crea una instancia de la clase Cola
mi_cola.enqueue(1)  # Añade el elemento 1 a la cola
mi_cola.enqueue(2)  # Añade el elemento 2 a la cola
mi_cola.enqueue(3)  # Añade el elemento 3 a la cola
print("Tamaño de la cola:", mi_cola.size())  # Imprime el tamaño
mi_cola.print()  # Imprime los elementos actuales de la cola
elemento = mi_cola.dequeue()  # Remueve el primer elemento de la cola
print("Elemento removido:", elemento)  # Imprime el elemento removido
print("Tamaño de la cola después de dequeue:", mi_cola.size())  # Imprime el tamaño de la cola después de la operación dequeue


 