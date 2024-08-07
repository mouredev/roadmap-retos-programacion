"""
EJERCICIO:
 * Explora el concepto de clase y crea un ejemplo que implemente un inicializador,
 * atributos y una función que los imprima (teniendo en cuenta las posibilidades
 * de tu lenguaje).
 * Una vez implementada, créala, establece sus parámetros, modifícalos e imprímelos
 * utilizando su función.
"""
# Clase Persona con atributo
class Persona:
    def __init__(self, nombre, apellido):  # Inicializador o constructor
        self.nombre = nombre
        self.apellido = apellido

    def imprimir(self):
        print("Nombre: ", self.nombre)
        print("Apellido: ", self.apellido)

persona1 = Persona("John", "Doe")
print("\nPersona 1:\n")
persona1.imprimir()

# Modificar los datos de persona
persona2 = Persona("Jane", "Smith")
print("\n\nPersona 2:\n")
persona2.nombre = "Michael"
persona2.apellido = "Jackson"
persona2.imprimir()
# Crear una subclase llamada Estudiante que herede de la clase Persona
# y agregue un nuevo atributo, estudiante_id. Implementar el método imprimir para mostrar este dato adicional.


class Estudiante(Persona):
    def __init__(self, nombre, apellido, curso):
        super().__init__(nombre, apellido)
        self.curso = curso

    def imprimir_estudiante(self):
        print("Curso: ", self.curso)


estudiante1 = Estudiante("Ana", "Rodríguez", 3)
print("\nEstudiante 1:\n")
estudiante1.imprimir()
estudiante1.imprimir_estudiante()

# Probar el acceso a los atributos privados (no recomendado pero se puede hacer)
print("\nAccediendo directamente al atributo 'curso' del estudiante 1:\n")
print("Curso: ", estudiante1.curso)

"""
DIFICULTAD EXTRA (opcional):
 * Implementa dos clases que representen las estructuras de Pila y Cola 
 * - Deben poder inicializarse y disponer de operaciones para añadir, eliminar,
 *   retornar el número de elementos e imprimir todo su contenido.
"""

class Pila:
    def __init__(self):
        self.elementos = []

    def push(self, elemento):
        self.elementos.append(elemento)

    def pop(self):
        if not self.esta_vacia():
            return self.elementos.pop()
        else:
            raise Exception("La pila está vacía")

    def esta_vacia(self):
        return len(self.elementos) == 0

    def tamaño(self):
        return len(self.elementos)

    def imprimir(self):
        print(self.elementos)


class Cola:
    def __init__(self):
        self.elementos = []

    def encolar(self, elemento):
        self.elementos.append(elemento)

    def desencolar(self):
        if not self.esta_vacia():
            return self.elementos.pop(0)
        else:
            raise Exception("La cola está vacía")

    def esta_vacia(self):
        return len(self.elementos) == 0

    def tamaño(self):
        return len(self.elementos)

    def imprimir(self):
        print(self.elementos)


# Ejemplo de uso
pila = Pila()
pila.push(1)
pila.push(2)
pila.push(3)
pila.imprimir()  # [1, 2, 3]
print(pila.tamaño())  # 3
print(pila.pop())  # 3
print(pila.tamaño())  # 2

cola = Cola()
cola.encolar(1)
cola.encolar(2)
cola.encolar(3)
cola.imprimir()  # [1, 2, 3]
print(cola.tamaño())  # 3
print(cola.desencolar())  # 1
print(cola.tamaño())  # 2