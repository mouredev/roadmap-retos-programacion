"""
    EJERCICIO:
    Explora el concepto de clase y crea un ejemplo que implemente un inicializador,
    atributos y una función que los imprima (teniendo en cuenta las posibilidades
    de tu lenguaje).
    Una vez implementada, créala, establece sus parámetros, modifícalos e imprímelos
    utilizando su función.
"""

class Computadora:
    def __init__(self, marca, color, precio):
        self.marca = marca
        self.color = color
        self.precio = precio

    def ver_atributos(self):
        print(f"Carácterísticas de la computadora: {self.marca}, {self.color}, {self.precio}.")

# Creamos una instancia de la clase 'Computadora'
compu_ph = Computadora("HP", "Azul", 7999)

# Llamamos al método "ver_atributos"
compu_ph.ver_atributos()

# Cambiamos algunos atributos, por ejemplo, el color y precio.
compu_ph.color = "Rojo"
compu_ph.precio = 10000

# Volvemos a llamar el método para ver los cambios
compu_ph.ver_atributos()


"""
DIFICULTAD EXTRA (opcional):
Implementa dos clases que representen las estructuras de Pila y Cola (estudiadas
en el ejercicio número 7 de la ruta de estudio)
    - Deben poder inicializarse y disponer de operaciones para añadir, eliminar,
    retornar el número de elementos e imprimir todo su contenido.
"""

############################
# Clase Pila/Stack (LIFO) #
###########################

class Pila:
    def __init__(self):
        self.stack = []
    
    def insertar(self, element):
        self.stack.append(element) # Push

    def eliminar(self):
        if len(self.stack) > 0:
            self.stack.pop() # Pop
        else:
            Pila.vacio()

    def all_elements(self):
        if len(self.stack) > 0:
            print(f"La Pila tiene estos elementos: {self.stack}")
        else:
            Pila.vacio()

    def total_elements(self):
        if len(self.stack) > 0:
            print(f"Total de elementos de la Pila: {len(self.stack)}") 
        else:
            Pila.vacio()

    def vacio():
        print("Pila vacía")


# Creamos una instancia de la clase
pila1 = Pila()

# Usamos el método "insertar" para poner elementos en la pila (1, "uno", 2 y "dos" respectivamente)
pila1.insertar(1)
pila1.insertar("uno")
pila1.insertar(2)
pila1.insertar("dos")

# Usamos el método 'eliminar' para eliminar el último elemento de la pila
pila1.eliminar()

# Vemos los elementos con el que se quedó la pila y el total de este
pila1.total_elements() #Total
pila1.all_elements() #Elementos


# Creamos una función para manipular los valores de la pila ya instanciada
def clase_pila():
     while True:
        action = input("Elige una opción para manipular la pila: insertar/eliminar/ver/total/salir: ")
        if action == "insertar":
            insert = input("Escriba lo que desea insertar a la pila: ")
            pila1.insertar(insert)
        elif action == "eliminar":
            pila1.eliminar()
        elif action == "ver":
            pila1.all_elements()
        elif action == "total":
            pila1.total_elements()
        elif action == "salir":
            break
        else:
            pass

#clase_pila()

############################
# Clase Cola/Queue (FIFO) #
###########################

class Cola:
    def __init__(self):
        self.queue = []

    def insertar(self, element):
        self.queue.append(element) # Push

    def eliminar(self):
        if len(self.queue) > 0:
            self.queue.pop(0) # Pop
        else:
            Cola.vacio()

    def all_elements(self):
        if len(self.queue) > 0:
            print(f"La Cola tiene estos elementos: {self.queue}")
        else:
            Cola.vacio()

    def total_elements(self):
        if len(self.queue) > 0:
            print(f"Total de elementos de la Cola: {len(self.queue)}") 
        else:
           Cola.vacio()

    def vacio():
        print ("Cola vacío")


# Creamos una instancia de la clase Cola
cola1 = Cola()

# Usamos el método "insertar" para poner elementos en la cola (1, 2, 3 y 4 respectivamente)
cola1.insertar(1)
cola1.insertar(2)
cola1.insertar(3)
cola1.insertar(4)

# Usamos el método 'eliminar' para  eliminar el primer elemento de la Cola
pila1.eliminar()

# Vemos los elementos con el que se quedó la Cola y el total de este
cola1.total_elements() #Total
cola1.all_elements() #Elementos



# Creamos una función para manipular los valores de la Cola ya instanciada
def clase_cola():
     while True:
        action = input("Elige una opción para manipular la Cola: insertar/eliminar/ver/total/salir: ")
        if action == "insertar":
            insert = input("Escriba lo que desea insertar a la Cola: ")
            cola1.insertar(insert)
        elif action == "eliminar":
            cola1.eliminar()
        elif action == "ver":
            cola1.all_elements()
        elif action == "total":
            cola1.total_elements()
        elif action == "salir":
            break
        else:
            pass

clase_cola()