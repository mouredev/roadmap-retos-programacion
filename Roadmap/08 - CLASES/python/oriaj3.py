"""	
08 - CLASES
Autor de la solución: Oriaj3	
Teoría:	
Las clases son una forma de organizar y estructurar el código.
En la mayoría de los lenguajes de programación, las clases son la base de la
programación orientada a objetos.

Una clase es una plantilla para crear objetos. Un objeto es una instancia de una
clase. Cuando se crea un objeto, se le asigna un espacio en memoria y se le
asignan los atributos y métodos de la clase.

Las clases pueden tener atributos y métodos:
*Los atributos son variables que pertenecen a la clase.
*Los métodos son funciones que pertenecen a la clase.

También pueden tener un inicializador, que es un método especial que se ejecuta
cuando se crea un objeto.

En Python, las clases se definen con la palabra clave class, seguida del nombre
de la clase y dos puntos. Los atributos y métodos de la clase se definen dentro
de la clase, con sangría.

Ejemplo:
class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def saludar(self):
        print(f'Hola, me llamo {self.nombre} y tengo {self.edad} años')

También existen los destructores y los métodos estáticos, pero no son tan
comunes. En python se definen con las palabras clave __del__ y @staticmethod
respectivamente.

Para crear un objeto de una clase, se llama al nombre de la clase como si fuera
una función, pasando los argumentos que requiera el inicializador.

Ejemplo:
persona1 = Persona('Juan', 25)
persona1.saludar()

En este ejemplo, se crea un objeto de la clase Persona, con el nombre 'Juan' y
la edad 25. Luego se llama al método saludar del objeto persona1.

Para acceder a los atributos y métodos de un objeto, se utiliza la notación de
punto.

Ejemplo:
print(persona1.nombre)

También es importante mencionar que en Python, todos los atributos y métodos de
una clase son públicos, a menos que se especifique lo contrario. Esto significa
que se pueden acceder y modificar desde cualquier parte del código.

Ejemplo:
persona1.nombre = 'Pedro'

En este ejemplo, se cambia el nombre del objeto persona1 a 'Pedro'.

Ejemplo private:
class Persona:
    def __init__(self, nombre, edad):
        self.__nombre = nombre
        self.__edad = edad

    def saludar(self):
        print(f'Hola, me llamo {self.__nombre} y tengo {self.__edad} años')
        
En este ejemplo, se utiliza dos guiones bajos antes del nombre de los atributos 
"""	

# EJERCICIO BÁSICO:
"""
EJERCICIO:
 Explora el concepto de clase y crea un ejemplo que implemente un inicializador,
 atributos y una función que los imprima (teniendo en cuenta las posibilidades
 de tu lenguaje).
 Una vez implementada, créala, establece sus parámetros, modifícalos e imprímelos
 utilizando su función.
"""

class persona1: 
    def __init__(self, nombre, edad) -> None:
        self.__nombre = nombre
        self.__edad = edad
    
    def setNombre(self, nombre) -> None: 
        self.__nombre = nombre
    
    def getNombre(self) -> str:
        return self.__nombre
    
    def setEdad(self, edad) -> None: 
        self.__edad = edad
    
    def getEdad(self) -> str:
        return self.__edad
    
    def print(self) -> None:
        print(f"La persona se llama {self.__nombre} y tiene {self.__edad} años.")
        
pepe = persona1("Pepe", 23)

pepe.print()

pepe.setNombre("Juan")
pepe.setEdad(25) 

pepe.print()

print(pepe.getNombre())
print(pepe.getEdad())   

"""
DIFICULTAD EXTRA (opcional):
Implementa dos clases que representen las estructuras de Pila y Cola (estudiadas
en el ejercicio número 7 de la ruta de estudio)
- Deben poder inicializarse y disponer de operaciones para añadir, eliminar,
    retornar el número de elementos e imprimir todo su contenido.
"""

class pila:
    lista = []
    
    def anadir(self, elemento) -> None:
        self.lista.append(elemento)
        
    def sacar(self) -> any:
        return self.lista.pop()
    
    def tamano(self) -> int:
        return len(self.lista)
    
    def imprimir(self) -> None:
        print(self.lista)
        
# Ejemplo de uso
p = pila()
p.anadir(1)
p.anadir(2)
p.anadir(3)

print("LISTAS.....")
p.imprimir()
print(f"El tamaño es: {p.tamano()}")
print(p.sacar())
p.imprimir()
print(f"El tamaño es: {p.tamano()}")

        
class cola:
    cola = []
    
    def anadir(self, elemento) -> None:
        self.cola.append(elemento)
        
    def sacar(self) -> any:  # Add return type annotation
        return self.cola.pop(0)
    
    def tamano(self) -> int:
        return len(self.cola)
    
    def imprimir(self) -> None:
        print(self.cola)
        
# Ejemplo de uso
c = cola()
c.anadir(1)
c.anadir(2)
c.anadir(3)

print("COLAS.....")
c.imprimir()
print(f"El tamaño es: {c.tamano()}")
print(c.sacar())
c.imprimir()
print(f"El tamaño es: {c.tamano()}")

    
        