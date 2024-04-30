"""
/*
 * EJERCICIO:
 * Explora el concepto de clase y crea un ejemplo que implemente un inicializador,
 * atributos y una función que los imprima (teniendo en cuenta las posibilidades
 * de tu lenguaje).
 * Una vez implementada, créala, establece sus parámetros, modifícalos e imprímelos
 * utilizando su función.
 *
 * DIFICULTAD EXTRA (opcional):
 * Implementa dos clases que representen las estructuras de Pila y Cola (estudiadas
 * en el ejercicio número 7 de la ruta de estudio)
 * - Deben poder inicializarse y disponer de operaciones para añadir, eliminar,
 *   retornar el número de elementos e imprimir todo su contenido.
 * 
 */
"""
class Person:
        
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

    def get_name(self):
        return self.name

    def perso_info(self):
        print(f"Mi nombre es: {self.name} y mi apellido es: {self.surname}")
    
my_person = Person("Nicolle", "Ramirez")
my_person.perso_info()

my_person = Person("Matheo", "ramirez")
my_person.perso_info()

class Pila:
    def __init__(self):
        self.my_class_pila = []
    
    def is_empty(self):
        return len(self.my_class_pila) == 0
    
    def agregar_elemento(self, elemento):
        self.my_class_pila.append(elemento)
    
    def eliminar_elemento(self):
        if not self.is_empty():
            self.my_class_pila.pop()
    
    def imprimir_elemento(self):
        for n in reversed(self.my_class_pila):
            print(n)

my_pila = Pila()
my_pila.agregar_elemento("python") 
my_pila.agregar_elemento("fastapi")
my_pila.agregar_elemento("github")
my_pila.imprimir_elemento()
my_pila.eliminar_elemento()
my_pila.imprimir_elemento()

class Cola:
    def __init__(self):
        self.my_class_cola = []
    
    def is_empty(self):
        return len(self.my_class_cola) == 0
    
    def agregar_elemento(self, elemento):
        self.my_class_cola.append(elemento)
    
    def eliminar_elemento(self):
        if not self.is_empty():
            self.my_class_cola.pop(0)
    
    def imprimir_elemento(self):
        for n in self.my_class_cola:
            print(n)


queue = Cola()
queue.agregar_elemento("retos") 
queue.agregar_elemento("programacion")
queue.agregar_elemento("logica")
queue.imprimir_elemento()
queue.eliminar_elemento()
queue.imprimir_elemento()
