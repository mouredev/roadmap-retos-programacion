'''EJERCICIO:
 * Explora el concepto de clase y crea un ejemplo que implemente un inicializador,
 * atributos y una función que los imprima (teniendo en cuenta las posibilidades
 * de tu lenguaje).
 * Una vez implementada, créala, establece sus parámetros, modifícalos e imprímelos
 * utilizando su función.'''

# Clases: representan y definen objetos
# Objetos: son las instancias de las clases (int, str, list, dict...)
# Atributos: características asociadas a un tipo / type (ej. color y sabor de una manzana)
# Métodos: funciones asociadas a un tipo (ej. lo que vayamos a hacer con la manzana, comerla, cortarla...)

# Constructores de Clases : __init__  
# Método especial que se usa para inicializar los atributos de un objeto al crear una nueva instancia de esta clase.

class Person:

    lugar : str = "Federación"       # Puedo crear un atributo fuera del inicializador y después imprimirlo. Puedo dejarlo en None

    def __init__ (self, name, edad):      # 'self' hace referencia a la instancia en la que estamos
        self.name = name
        self.edad = edad

    def imprimir (self):
        print (f"Hola mundo, me llamo {self.name}, vivo en {self.lugar} y tengo {self.edad} años.")

person1 = Person ("Troy", 45)        # creo una nueva instancia 'person1' de la clase 'Person'
person1.imprimir()

person1.lugar ="Vulcano"
person1.imprimir()

person1.edad = "44"     # Modifico un atributo
person1.imprimir()

# Constructores de Clases : __str__  
# Método especial útil si tengo que andar imprimiendo mucho después

class Person2:
    def __init__ (self, name, edad):      
        self.name = name
        self.edad = edad

    def __str__ (self):
        return "Hola mundo, me llamo {}, y tengo {} años.".format(person2.name, person2.edad)   # Retorno el texto formateado a imprimir

person2 = Person2 ("Nebula", 36)        # creo una nueva instancia 'person2' de la clase 'Person2'
print (person2)



class Ropa:
    stock : dict = { 'nombre': [], 'material': [], 'cantidad': []} # Diccionario que contiene str de clave y lista de valor

    def __init__ (self, nombre):
        self.material = ""  # Si no lo inicializo aquí nunca se guarda como parte de una instancia de Ropa
        self.nombre = nombre

    def añadir_item (self, nombre, material, cantidad):
        Ropa.stock ['nombre'].append (nombre)
        Ropa.stock ['material'].append (material)  # Usar el material pasado como parámetro
        Ropa.stock ['cantidad'].append (cantidad)

    def stock_por_material(self, material):
        contador = 0
        for i, item in enumerate(Ropa.stock['material']):  
            # enumerate se utiliza para iterar sobre una secuencia mientras lleva un recuento del índice actual de los elementos
            if item == material:
                contador += Ropa.stock['cantidad'][i]  
                # Uso este índice i para acceder a la cantidad correcta y agregarla al contador.
            
        return contador
        
class Camiseta (Ropa):      # Creo dos subclases Camiseta y Vestido de la clase Ropa y los inicializo añadiendo el material
    def __init__(self, nombre):
        super().__init__(nombre)   # super() función que permite acceder a los métodos y atributos de la clase padre desde una subclase
        self.material = 'algodon'

class Vestido (Ropa):
    def __init__(self, nombre):
        super().__init__(nombre)
        self.material = 'algodon'

manga_corta = Camiseta ("manga corta")   # Creo dos instancias una de cada subclase y las inicializo con los nombres que es el 1º atributo
de_fiesta = Vestido ("de fiesta")

manga_corta.añadir_item(manga_corta.nombre, manga_corta.material, 4)
de_fiesta.añadir_item(de_fiesta.nombre, de_fiesta.material, 6)

stock_actual = manga_corta.stock_por_material("algodon")

print (f"Tenemos en stock de {manga_corta.nombre}, y {de_fiesta.nombre} en {manga_corta.material} la siguiente cantidad: {stock_actual}")
# No nos muestra el total por material independiente sino todo lo de algodon, usease 10

print()
''' DIFICULTAD EXTRA (opcional):
 * Implementa dos clases que representen las estructuras de Pila y Cola (estudiadas
 * en el ejercicio número 7 de la ruta de estudio)
 * - Deben poder inicializarse y disponer de operaciones para añadir, eliminar,
 *   retornar el número de elementos e imprimir todo su contenido.'''

print("Stack_pila:")
class Stack_pila ():   

    def __init__(self):
        self.stack =[]  #lista vacía

    def push_apliar (self, elemento):     # Todas las funciones tienen que recibirse a ellas mismas
        self.stack.append(elemento)

    def pop_desapilar (self):
        if len(self.stack) >0:            # Podría poner en vez del len, self.contar()
            return self.stack.pop()        # LIFO última en entrar primera en salir
        else:
            return None
        
    def contar (self):
        return len(self.stack)
    
    def imprimir (self):
        for i in reversed(self.stack):   # Si queremos que salga lo último añadido hay que darle la vuelta a la lista con reversed
            print (i)

instancia_stack = Stack_pila()          # Creo una instancia
instancia_stack.push_apliar (1)  
instancia_stack.push_apliar (2)  
instancia_stack.push_apliar (3)  
instancia_stack.imprimir()              # 3 2 1
print()
print(instancia_stack.contar())         # 3
print()
instancia_stack.pop_desapilar()         # 2
instancia_stack.imprimir()              # 1
print()
print(instancia_stack.pop_desapilar())  # 2
print(instancia_stack.pop_desapilar())  # 1
print(instancia_stack.pop_desapilar())  # None
print()
print(instancia_stack.contar())         # 0

print("Queue_cola:")
class Queue_cola ():   

    def __init__(self):
        self.queue =[]  #lista vacía

    def push_apliar (self, elemento):     # Todas las funciones tienen que recibirse a ellas mismas
        self.queue.append(elemento)

    def pop_desapilar (self):
        if len(self.queue) >0:            # Podría poner en vez del len, self.contar()
            return self.queue.pop(0)      # FIFO primera en entrar primera en salir así que le digo que la posición 0
        else:
            return None
        
    def contar (self):
        return len(self.queue)
    
    def imprimir (self):
        for i in self.queue:   
            print (i)

instancia_queue = Queue_cola()          # Creo una instancia
instancia_queue.push_apliar (1)  
instancia_queue.push_apliar (2)  
instancia_queue.push_apliar (3)  
instancia_queue.imprimir()              # 1 2 3
print()
print(instancia_queue.contar())         # 3
print()
instancia_queue.pop_desapilar()         # 2
instancia_queue.imprimir()              # 3
print()
print(instancia_queue.pop_desapilar())  # 2
print(instancia_queue.pop_desapilar())  # 3
print(instancia_queue.pop_desapilar())  # None
print()
print(instancia_queue.contar())         # 0