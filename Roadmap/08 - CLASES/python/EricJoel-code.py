## Clases

# Concepto: Una clase es una plantilla para crear objetos, que encapsula datos y comportamientos relacionados.

class Persona:
    
    apellido = None  # Atributo de clase compartido por todas las instancias
    
    def __init__(self, nombre, edad, ciudad):
        self.nombre = nombre
        self.edad = edad
        self.ciudad = ciudad
        
    def imprimir_info(self):
        print(f"Nombre: {self.nombre}, Apellido: {self.apellido} Edad: {self.edad}, Ciudad: {self.ciudad}")
        
# Crear instancias de la clase Persona
persona1 = Persona("Alice", 30, "New York")
persona1.imprimir_info()
persona1.apellido = "Smith" 
persona1.imprimir_info()

persona2 = Persona("Bob", 25, "Los Angeles")
persona2.imprimir_info()
persona2.edad = 26 
persona2.imprimir_info()


##Extra

"""Implementa dos clases que representen las estructuras de Pila y Cola. 
Deben poder inicializarse y disponer de operaciones para añadir, eliminar,
retornar el número de elementos e imprimir todo su contenido."""

#Pila/Stacks/LIFO (Last In, First Out)

class Pila:
    def __init__(self):
        self.elementos = []
        
    def agregar(self, elemento):
        self.elementos.append(elemento)
    
    def eliminar(self):
        if self.tamaño() > 0:
            return self.elementos.pop()
        return None
    
    def tamaño(self):
        return len(self.elementos)
    
    def imprimir(self):
        for elemento in reversed(self.elementos):
            print(elemento)
            
mi_pilas = Pila()
mi_pilas.agregar(1)
mi_pilas.agregar(2)
mi_pilas.agregar(3)
mi_pilas.imprimir()
print(mi_pilas.tamaño())
mi_pilas.eliminar()
mi_pilas.eliminar()
mi_pilas.eliminar()
mi_pilas.eliminar()
mi_pilas.eliminar()
mi_pilas.imprimir()
print(mi_pilas.tamaño())

#Cola/Queues/PIFO (First In, First Out)

class Cola:
    def __init__(self):
        self.elementos = []
        
    def agregar(self, elemento):
        self.elementos.append(elemento)
        
    def eliminar(self):
        if self.tamaño() > 0:
            return self.elementos.pop(0)
        return None
    
    def tamaño(self):
        return len(self.elementos)
    
    def imprimir(self):
        for elemento in self.elementos:
            print(elemento)
            
mi_colas = Cola()
mi_colas.agregar(10)
mi_colas.agregar(20)
mi_colas.agregar(30)
mi_colas.imprimir()
print(mi_colas.tamaño())
mi_colas.eliminar()
mi_colas.eliminar()
mi_colas.eliminar()
mi_colas.eliminar()
mi_colas.eliminar()
mi_colas.eliminar()
mi_colas.eliminar()
mi_colas.imprimir()
print(mi_colas.tamaño())