#  * EJERCICIO:
#  * Explora el concepto de clase y crea un ejemplo que implemente un inicializador,
#  * atributos y una función que los imprima (teniendo en cuenta las posibilidades
#  * de tu lenguaje).
#  * Una vez implementada, créala, establece sus parámetros, modifícalos e imprímelos
#  * utilizando su función.

# Creando la clase Persona:
class Persona:
    def __init__(self, nombre, apellido, edad, email):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.email = email
    def saludar(self):
        print(f"Hola, como estas?. Mi nombre es {self.nombre}!")
    def get_information(self):
        print(f"Nombre: {self.nombre}")
        print(f"Apellido: {self.apellido}")
        print(f"Edad: {self.edad}")
        print(f"Email: {self.email}")

# Instanciando de la clase Persona y estableciendo sus parametros:
persona1 = Persona("Alvaro", "Neyra", 19, "alvaro.neyra.salazar@gmail.com")
# Modificando uno de sus atributos:
persona1.edad = 10
print(f"Edad modificada: {persona1.edad}")
# Usando sus metodos:
persona1.saludar()
# Imprimiendo la informacion del objeto instanciado usando su metodo "get_information":
persona1.get_information()

#  * DIFICULTAD EXTRA (opcional):
#  * Implementa dos clases que representen las estructuras de Pila y Cola (estudiadas
#  * en el ejercicio número 7 de la ruta de estudio)
#  * - Deben poder inicializarse y disponer de operaciones para añadir, eliminar,
#  *   retornar el número de elementos e imprimir todo su contenido.

# * Pilas:
# Definiendo la clase Pila (Stack)
class Pila:
    def __init__(self):
        self.items = []
    def add(self, value):
        self.items.append(value)
        print(self.items)
    def delete(self):
        elemento_eliminado = self.items.pop()
        return elemento_eliminado
    def number_of_elements(self):
        numero_de_elementos = len(self.items)
        if numero_de_elementos == 0:
            return 0
        else:
            return numero_de_elementos
    def get_information(self):
        print(self.items)
# Instanciando un objeto de la clase Pila
pila1 = Pila()
# Usando sus metodos:
## Anadiendo elementos:
pila1.add(1)
pila1.add("Segundo elemento")
pila1.add(True)
## Obteniendo el numero de elementos:
numero_de_elementos_de_la_pila = pila1.number_of_elements()
print(f"Este es el numero de elementos de la pila iniciada: {numero_de_elementos_de_la_pila}")
## Conseguiendo los elementos de la pila:
pila1.get_information()
## Eliminando el elemento:
elemento = pila1.delete()
print(f"Este es el elemento eliminado: {elemento}")
## Consiguiendo los elementos de la pila actual:
print(f"Estructura de la pila actual:")
pila1.get_information()

# * Colas:
# Definiendo la clase de la cola (Queue)
class Cola:
    def __init__(self):
        self.items = []
    def add(self, value):
        self.items.insert(0, value)
        print(self.items)
    def delete(self):
        elemento_eliminado = self.items.pop()
        return elemento_eliminado
    def number_of_elements(self):
        numero_de_elementos = len(self.items)
        if numero_de_elementos == 0:
            return 0
        else:
            return numero_de_elementos
    def get_information(self):
        print(self.items)
# Instanciando un objeto de la clase Cola
cola1 = Cola()
# Usando sus metodos:
## Anadiendo elementos
cola1.add("Primer elemento")
cola1.add(2)
cola1.add(False)
## Obteniendo el numero de elementos:
numero_de_elementos_de_la_cola = cola1.number_of_elements()
print(f"Este es el numero de elementos de la cola iniciada: {numero_de_elementos_de_la_cola}")
## Conseguiendo los elementos de la cola:
cola1.get_information()
## Eliminando el elemento:
elemento = cola1.delete()
print(f"Elemento eliminado: {elemento}")
## Conseguiendo los elementos de la cola actual:
print(f"Estructura actual de la cola:")
cola1.get_information()