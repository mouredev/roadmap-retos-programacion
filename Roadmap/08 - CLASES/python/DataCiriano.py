"""
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
"""

class Animal():
    def __init__(self, nombre:str, especie:str, raza:str, edad:int, sexo:str, color:str):
        self.nombre = nombre
        self.especie = especie
        self.raza = raza
        self.edad = edad
        self.sexo = sexo
        self.color = color
        
    def caracteristicas(self):
        print(f"{self.nombre.capitalize()} es un {self.especie} de raza {self.raza}.")
        print(f"Tiene {self.edad} años de edad, es {self.sexo} y es de color {self.color}.")
        
    def modificar_atributos(self, nuevo_nombre=None, nueva_edad=None, nuevo_color=None):
        if nuevo_nombre is not None:
            self.nombre = nuevo_nombre
        if nueva_edad is not None:
            self.edad = nueva_edad
        if nuevo_color is not None:
            self.color = nuevo_color
        
        
        
#Crear instancia de clase          
snoopy = Animal("snoopy", "perro", "beagle", 10, "macho", "tricolor")
snoopy.caracteristicas()
#Modificar los atributos de la calse 'Snoopy'
snoopy.modificar_atributos("Snoopyus", 12, "negro con blanco")
snoopy.caracteristicas()

#Crear instancia de clase
felix = Animal("felix", "gato", "común", 5, "macho", "blanco y negro")
felix.caracteristicas()
#Modificar los atributos de la clase 'Felix el gato'
felix.modificar_atributos("felix el gato", 7, "negro" )
felix.caracteristicas()


#-----EXTRA-----

#Clase que simula un pila de libros

class PilaLibros:
    
    def __init__(self):
        self.pila = []
    
    def añadir(self, libro):
        self.libro = libro
        self.pila.append(self.libro)
    
    def eliminar(self):
        try:
            libro_eliminado = self.pila.pop()
            print(f"Se elimino el libro {libro_eliminado}")
        except IndexError:
            print("No se puedo eliminar ningún libro ya que la Pila está vacía.")
    
    def elementos(self):
        print(f"La pila contiene un total de {len(self.pila)} libros.")
    
    def imprimir(self):
        print(f"Estos son los libros almacenados en la pila: {self.pila}")
    
#Crear instancia de clase
cuentos = PilaLibros()

#Uso de los métodos de la clase
cuentos.añadir("Blancanieves y los 7 enanitos")
cuentos.añadir("Perter Pan")

cuentos.elementos()

cuentos.imprimir()

cuentos.eliminar()
cuentos.eliminar()
cuentos.eliminar() #Arroja el mensaje de error de que la Pila está vacía.



#Clase que simula una cola de clientes que realizan pedidos en una cafetería y son atendidos en orden de llegada

class ColaClientes:
    
    def __init__(self):
        self.cola = []
        
    def añadir(self, nombre_cliente,):
        self.nombre_cliente = nombre_cliente
        self.cola.append(self.nombre_cliente)
    
    def eliminar(self):
        try:
            pedido_eliminado = self.cola.pop(0)
            print(f"Se eliminó el pedido {pedido_eliminado}")
        except IndexError:
            print("No se puedo eliminar ningún pedido ya que la Cola está vacía.")
    
    def elementos(self):
        print(f"La cola contiene un total de {len(self.cola)} pedidos.")
    
    def imprimir(self):
        print(f"Estos son los pedidos en curso: {self.cola}")
        
        
#Crear instancia de clase para simular una cola de clientes que realizan pedidos en una cafetería en prden de llegada
pedidos = ColaClientes()

#Uso de los métodos de la clase
pedidos.añadir("Juan Rodríguez - Café con leche sin lactosa")
pedidos.añadir("Ana García - Café con leche + tarta chocolate")
pedidos.añadir("Luís Perez - Bodadillo jamón serrano")
pedidos.añadir("Esther Coronado - Zumo naranja + sandwich huevo")

pedidos.elementos()

pedidos.imprimir()

pedidos.eliminar()

pedidos.imprimir()

pedidos.eliminar()
pedidos.eliminar()
pedidos.eliminar()
pedidos.eliminar() #Arroja el mensaje de error de que la Cola está vacía.

