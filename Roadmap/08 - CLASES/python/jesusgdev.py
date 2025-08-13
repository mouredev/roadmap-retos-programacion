'''
* EJERCICIO:
 * Explora el concepto de clase y crea un ejemplo que implemente un inicializador,
   atributos y una función que los imprima (teniendo en cuenta las posibilidades
   de tu lenguaje).
 * Una vez implementada, créala, establece sus parámetros, modifícalos e imprímelos
   utilizando su función.
  
 * DIFICULTAD EXTRA (opcional):
 * Implementa dos clases que representen las estructuras de Pila y Cola (estudiadas
   en el ejercicio número 7 de la ruta de estudio)
   - Deben poder inicializarse y disponer de operaciones para añadir, eliminar,
     retornar el número de elementos e imprimir todo su contenido.
 
'''

# 1. Crea la clase y el inicializador

# Voy a crear una clase como ejemplo que tenga como atributos el nombre y la edad
class Pet:
    # Atributo opcional que no es requerido al crear una instancia pero que podemos usar
    specie: str = None

    def __init__(self, name: str, age: int):
        self.name = name    # Guardamos el nombre como atributo
        self.age = age      # Guardamos la edad como atributo

# 2. Agrega una funcion para mostrar los datos

    # Creo un metodo para la clase mascota que imprima tanto el nombre como la edad
    def show_info(self):
        print(f"Nombre: {self.name}| Specie: {self.specie} | Edad: {self.age}")

# 3. Usa la clase(crea una mascota)
my_pet = Pet("Fawler", 17)

# 4. Llama a la funcion para mostrar la informacion
my_pet.show_info()

# Podemos agregar un atributo opcional a cualquier instancia y utilizarlo cuando se requiera
my_pet.specie = "Ave"  
my_pet.show_info() 

# 5. Modifica los atributos despues de crear el objeto
my_pet.name = "Zerk"
my_pet.age = 12
my_pet.specie = "Camaleon"
my_pet.show_info()

'''
Extra
'''

# 1. Implementacion de clases usando la estructura de datos pila

class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)
        print(f"Agregando {item} a la pila")

    def pop(self):
        if len(self.stack) == 0:
            print("La pila esta vacia")
        else:
            removido = self.stack.pop()
            print(f"\nDesapilando {removido} de la pila")

    def count(self):
        longitud = len(self.stack)
        print(f"\nLa pila tiene {longitud} elementos")

    def print(self):
        if len(self.stack) == 0:
            print("La pila esta vacia")
        else:
            print("\nImprimiendo la pila:")
            for elemento in reversed(self.stack):
                print(elemento)

my_stack = Stack()

my_stack.push(1)
my_stack.push(2)
my_stack.push(3)
my_stack.push(4)

my_stack.print()

my_stack.count()

my_stack.pop()

my_stack.print()

my_stack.count()


# 2. Implementacion de clases usando la estructura de datos cola

class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, item):
        self.queue.append(item)
        print(f"Agregando {item} a la cola")

    def dequeue(self):
        if len(self.queue) == 0:
            print("La cola esta vacia")
        else:
            removido = self.queue.pop(0)
            print(f"\nEl elemento {removido} a salido de la cola")

    def count(self):
        if len(self.queue) == 0:
            print("La cola esta vacia")
        else:
            print(f"La cola tiene {len(self.queue)} elementos")

    def print(self):
        if len(self.queue) == 0:
            print("La cola esta vacia")
        else:
            print("\nImprimiendo la cola:")
            for elementos in self.queue:
                print(elementos)

my_queue = Queue()

my_queue.enqueue(1)
my_queue.enqueue(2)
my_queue.enqueue(3)
my_queue.enqueue(4)

my_queue.print()

my_queue.count()

my_queue.dequeue()

my_queue.print()

