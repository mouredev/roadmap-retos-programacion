# /*
#  * EJERCICIO:
#  * Explora el concepto de clase y crea un ejemplo que implemente un inicializador,
#  * atributos y una función que los imprima (teniendo en cuenta las posibilidades
#  * de tu lenguaje).
#  * Una vez implementada, créala, establece sus parámetros, modifícalos e imprímelos
#  * utilizando su función.
#  */

# CLASE -> Es un tipo de estructura de datos en la cual podemos definir un conjunto de atributos y métodos privados o no
# de una instancia de esa clase.Por así decirlo es como una plantilla con la que podemos crear objetos/instancias independientes
# de esa misma clase.


class Humano():
    """Plantilla para crear instancias/objetos de humanos independientes"""
    # Método constructor interno de la clase. Cada vez que se cree una instancia nueva se ejecuta de forma automática
    def __init__(self,name,username,age):
        # ATRIBUTOS con lo que se inicializa cualquier instancia
        self.nombre = name
        self.apellido = username
        self.edad= age
    

    def saludar(self):
        print(f"Hola soy {self.nombre.capitalize()} {self.apellido.capitalize()} y tengo {self.edad} años.")


    def update(self,new_name,new_username,new_age):
        """Este método lo vamos a usar para actualizar los datos de los objetos de las clase Humano"""
        self.nombre = new_name
        self.apellido = new_username
        self.edad = new_age


# CASO DE USO
humano1 = Humano("night","blockchain","26")
humano1.saludar()
humano1.update("pepe","blanco",18)
humano1.saludar()


#  *
#  * DIFICULTAD EXTRA (opcional):
#  * Implementa dos clases que representen las estructuras de Pila y Cola (estudiadas
#  * en el ejercicio número 7 de la ruta de estudio)
#  * - Deben poder inicializarse y disponer de operaciones para añadir, eliminar,
#  *   retornar el número de elementos e imprimir todo su contenido.
#  * 

class Stack():

    def __init__(self,name_stack):
        self.name_stack = name_stack
        self.contenido_stack = []

    def add(self,num:int):
        """Método para agregar elementos a la pila según el método LIFO. También conocido como PUSH"""
        self.contenido_stack.append(num)

    def remove(self):
        """Método eliminar el último elemento agregado a la pila.También conocido como POP"""
        self.contenido_stack.pop()


    def show_stack(self):
        """Método para mostrar el estado de la pila"""
        print(f"{self.contenido_stack}")
    

# Caso de uso STACK
stack1 = Stack("Stack1")

stack1.add(1)
stack1.add(2)
stack1.add(3)

stack1.show_stack()

stack1.remove()
stack1.remove()

stack1.show_stack()


class Queue():

    def __init__(self,name_queue):
        self.name_queue = name_queue
        self.contenido_queue= []

    def add(self,num:int):
        """Método para agregar elementos a la cola según el método FIFO. También conocido como PUSH"""
        self.contenido_queue.append(num)

    def remove(self):
        """Método eliminar el primer elemento de la cola.También conocido como POP"""
        self.contenido_queue.pop(0)


    def show_cola(self):
        """Método para mostrar el estado de la cola"""
        print(f"{self.contenido_queue}")

# Caso de uso QUEUE
cola1 = Queue("qu1")

cola1.add(1)
cola1.add(2)
cola1.add(3)

cola1.show_cola()

cola1.remove()
cola1.remove()

cola1.show_cola()