class Persona:
    """Representa a una persona."""

    def __init__(self, nombre, edad):
        """Inicializa los atributos de la persona."""
        self.nombre = nombre  # Atributo de instancia: nombre
        self.edad = edad      # Atributo de instancia: edad

    def imprimir_datos(self):
        """Imprime los datos de la persona."""
        print(f"Nombre: {self.nombre}, Edad: {self.edad}")

# Crear una instancia de la clase Persona
persona1 = Persona("Alice", 30)

# Establecer y modificar atributos
persona1.nombre = "Alicia"  # Modificar el atributo nombre
persona1.profesion = "Ingeniera"  # Agregar un nuevo atributo

# Imprimir datos
persona1.imprimir_datos()  # Nombre: Alicia, Edad: 30

# Ejercicio

class Pila:
    """ Representa una pila (LIFO) """

    def __init__(self):
        """ Inicializa una pila vacia. """
        self.items = []

    def apilar (self, elemento):
        """ Apila un elemento en la pila. """
        self.items.append(elemento)

    def desapilar(self):
        """ Desapila y devuelve el ultimo elemento de la pila. """
        if not self.esta_vacia():
            return self.items.pop()
        else:
            raise IndexError("La pila esta vacia.")
        
    def esta_vacia(self):
        """ Verifica si la pila esta vacia. """
        return len(self.items) == 0
    
    def tamano(self):
        """ Devuelve el numero de elementos en la pila. """
        return len(self.items)
    
    def mostrar(self):
        """ Imprime los elementos de la pila. """
        print(self.items)

# Clase Cola (FIFO) - Implementacion similar a Pila, pero usando pop(0) para desencolar

# Ejemplo de uso
pila = Pila()
pila.apilar("A")
pila.apilar("B")
pila.apilar("C")
pila.mostrar() # ["A", "B", "C"]
print(pila.desapilar()) # C