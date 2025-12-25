#08
#Clases
class Perro: # La primera en mayuscula
    def __init__(self, nombre, raza): # Inicializador
        self.nombre = nombre
        self.raza = raza

    def ladrar(self):
        print(f"{self.nombre} está ladrando")

mi_perro = Perro("Max", "Labrador")
tu_perro = Perro("Luna", "Poodle")

mi_perro.ladrar()  # Max está ladrando
tu_perro.ladrar()  # Luna está ladrando

# Herencias
class Animal:
    def __init__(self, nombre):
        self.nombre = nombre

    def hablar(self):
        print("Este animal hace un sonido")

class Gato(Animal):
    def hablar(self):
        print(f"{self.nombre} dice miau")

mi_gato = Gato("Michi")
mi_gato.hablar()  # Michi dice miau


# Ejercicio
# Definición de la clase
class Persona:
    # Inicializador: se ejecuta al crear un nuevo objeto
    def __init__(self, nombre, edad):
        self.nombre = nombre  # atributo de instancia
        self.edad = edad      # atributo de instancia

    # Método: función dentro de la clase
    def mostrar_info(self):
        print(f"Nombre: {self.nombre}, Edad: {self.edad}")
    
    def cumplir_años(self):
        self.edad += 1

# Crear un objeto (instancia) de la clase Persona
persona1 = Persona("Brian", 24)

# Llamamos al método que imprime los datos
persona1.mostrar_info()  # 👉 Nombre: Brian, Edad: 24

# Modificamos los atributos directamente
persona1.nombre = "Andrés"
persona1.edad = 25

# Imprimimos de nuevo
persona1.mostrar_info()  # 👉 Nombre: Andrés, Edad: 25

persona1.cumplir_años()
persona1.mostrar_info()

""" * DIFICULTAD EXTRA (opcional):
 * Implementa dos clases que representen las estructuras de Pila y Cola (estudiadas
 * en el ejercicio número 7 de la ruta de estudio)
 * - Deben poder inicializarse y disponer de operaciones para añadir, eliminar,
 *   retornar el número de elementos e imprimir todo su contenido."""

class Pila:
    def __init__(self):
        self.list = []

    def add(self, dato):
        self.list.append(dato)
        pass
    def remove_pila(self):
        self.list.pop()

    def remove_cola(self):
        self.list.pop(0)
    
    def count_list(self):
        self.cuenta = len(self.list)
        print(f"\nHay {self.cuenta} elementos en la lista")
    
    def mostrar_info(self):
        print(f"\nLista: {self.list}")

mi_pila = Pila()
mi_pila.add(1)
mi_pila.add(2)
mi_pila.add(3)
mi_pila.add(4)

mi_pila.mostrar_info()
mi_pila.count_list()

mi_pila.remove_pila()

mi_pila.mostrar_info()
mi_pila.count_list()

mi_pila.remove_cola()

mi_pila.mostrar_info()
mi_pila.count_list()

mi_cola = Pila()
mi_cola.add(1)
mi_cola.add("A")
mi_cola.add("B")

mi_cola.mostrar_info()