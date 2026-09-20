# EJERCICIO:
# Explora el concepto de clase y crea un ejemplo que implemente un inicializador,
# atributos y una función que los imprima (teniendo en cuenta las posibilidades
# de tu lenguaje).
# Una vez implementada, créala, establece sus parámetros, modifícalos e imprímelos
# utilizando su función.

class Person:
    def __init__(self, nombres: str, apellidos: str, edad: int):
        self.__edad = edad
        self.__nombres = nombres
        self.__apellidos = apellidos
        self.__nombre_completo = f"{self.__nombres} {self.__apellidos}"

    def get_nombre_completo(self):
        return self.__nombre_completo

    def get_edad(self):
        return self.__edad

    def set_nombres(self, nombres: str):
        self.__nombres = nombres
        self.__nombre_completo = f"{self.__nombres} {self.__apellidos}"

    def set_apellidos(self, apellidos: str):
        self.__apellidos = apellidos
        self.__nombre_completo = f"{self.__nombres} {self.__apellidos}"

persona_1 = Person("Gabriel", "Halo", 25)
print(f"Nombre de Persona 1: {persona_1.get_nombre_completo()}")
print(f"Edad de Persona 1: {persona_1.get_edad()} años")

persona_2 = Person("Jane", "Doe", 30)
print(f"Nombre de Persona 2: {persona_2.get_nombre_completo()}")
print(f"Edad de Persona 2: {persona_2.get_edad()} años")

print("\nCambiando nombres y apellidos de Persona 1...")
persona_1.set_nombres('James Eduardo')
persona_1.set_apellidos('Valderrama Flores')
print(f"Nombre de Persona 1: {persona_1.get_nombre_completo()}")
print()

# DIFICULTAD EXTRA (opcional):
# Implementa dos clases que representen las estructuras de Pila y Cola (estudiadas
# en el ejercicio número 7 de la ruta de estudio)
# - Deben poder inicializarse y disponer de operaciones para añadir, eliminar,
#   retornar el número de elementos e imprimir todo su contenido.

class Pila:
    def __init__(self, elementos: list = []):
        self.__elementos = elementos

    def get_pila_length(self):
        return len(self.__elementos)

    def imprimir_pila(self):
        for i in self.__elementos[::-1]:
            print(i)

    def agregar(self, elemento):
        self.__elementos.append(elemento)

    def quitar(self):
        if self.get_pila_length() > 0:
            return self.__elementos.pop()
        else:
            None

class Cola:
    def __init__(self, elementos: list = []):
        self.__elementos = elementos

    def get_cola_length(self):
        return len(self.__elementos)

    def imprimir_cola(self):
        for i in self.__elementos:
            print(i)

    def agregar(self, elemento):
        self.__elementos.append(elemento)

    def quitar(self):
        if self.get_cola_length() > 0:
            return self.__elementos.pop(0)
        else:
            None

print("=== PILA DE LIBROS ===")
libros = ["Libro 1", "Libro 2", "Libro 3", "Libro 5"]

pila_libros = Pila(libros)
print("\nLibros en Pila: ")
pila_libros.imprimir_pila()
print(f"Total: {pila_libros.get_pila_length()}")

print("\nColocando Libro 4 entre Libro 3 y Libro 5...")
libro_quitado = pila_libros.quitar()
pila_libros.agregar("Libro 4")
if libro_quitado != None:
    pila_libros.agregar(libro_quitado)
print("\nLibros en Pila: ")
pila_libros.imprimir_pila()
print(f"Total: {pila_libros.get_pila_length()}")
print()

print("=== COLA DE TICKETS ===")
tickets = ["10001", "10002", "10003", "10004", "10005"]

cola_tickets = Cola()
print(f"\nTickets en Cola: {cola_tickets.get_cola_length()}")
print("Agregando tickets...")
for ticket in tickets:
    cola_tickets.agregar(ticket)

print("\nTickets en Cola:")
cola_tickets.imprimir_cola()
print(f"Total: {cola_tickets.get_cola_length()}")

tickets_atendidos = []
print("\nAtendiendo 3 tickets en módulo...")
tickets_atendidos.append(cola_tickets.quitar())
tickets_atendidos.append(cola_tickets.quitar())
tickets_atendidos.append(cola_tickets.quitar())
print(f"{len(tickets_atendidos)} tickets atendidos: {tickets_atendidos}")

print(f"\nTickets en Cola:")
cola_tickets.imprimir_cola()
print(f"Total: {cola_tickets.get_cola_length()}")

tickets_atendidos = []
print(f"\nAtendiendo 2 tickets en módulo...")
tickets_atendidos.append(cola_tickets.quitar())
tickets_atendidos.append(cola_tickets.quitar())
print(f"{len(tickets_atendidos)} tickets atendidos: {tickets_atendidos}")
print()

tickets_atendidos = []
tickets_atendidos.append(cola_tickets.quitar())
if None in tickets_atendidos:
    print("Error: Se intentó atender un ticket que no estaba en cola...")