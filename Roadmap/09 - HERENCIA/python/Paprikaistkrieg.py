#HERENCIA y POLIMORFISMO

"""
La herencia es un concepto fundamental en la programación orientada a objetos (OOP) que
permite a una clase (llamada clase hija o subclase) heredar atributos y métodos de otra clase (llamada clase padre o superclase).
Esto promueve la reutilización del código y facilita la creación de jerarquías de clases.

El polimorfismo, por otro lado, es la capacidad de diferentes clases para ser tratadas como instancias de una clase común.
Esto significa que una función o método puede operar en objetos de diferentes clases,
siempre que esas clases implementen los mismos métodos o interfaces.
El polimorfismo permite que el mismo código funcione con diferentes tipos de objetos,
lo que mejora la flexibilidad y la extensibilidad del software.

Aquí tienes un ejemplo básico de herencia y polimorfismo en Python:
"""
class Animal:  # Clase padre o superclase
    def __init__(self, name :str):
        self.name = name

    def hacer_sonido(self):  # Método que será sobrescrito por las subclases
        raise NotImplementedError("Subclase debe implementar este método")
        # Esta excepción indica que las subclases deben proporcionar su propia implementación
        # si intentan llamar a este método directamente desde la clase padre.
        # Esto es útil para definir una interfaz común que todas las subclases deben seguir.
        # Si no se implementa en la subclase, se lanzará esta excepción.
        # Esto es una forma de asegurar que las subclases implementen este método.
        # También se puede usar la palabra clave 'pass' si no se desea lanzar una excepción.
        # pass  # Si no se desea lanzar una excepción, se puede usar 'pass' para indicar que el método no hace nada.
        # Sin embargo, lanzar NotImplementedError es una práctica común para indicar que el método debe ser implementado por las subclases.
        # Esto es especialmente útil en clases base o abstractas donde se espera que las subclases proporcionen una implementación específica.
            # raise NotImplementedError("Subclase debe implementar este método")
    
    
    class Animal:
        def hablar(self):
            print("Hace un sonido")

class Perro(Animal):
    def hablar(self):
        print("Ladra")

class Gato(Animal):
    def hablar(self):
        print("Maulla")


# Uso del polimorfismo
def hacer_hablar(animal: Animal): # Función que acepta un objeto de tipo Animal
    animal.hablar()  # Llama al método hablar del objeto animal

hacer_hablar(Perro("Kuky"))  # Imprime: Ladra
hacer_hablar(Gato("Wildson"))   # Imprime: Maulla


     # Llama al método hablar del objeto animal, que puede ser de cualquier subclase de Animal
    # Esto demuestra el polimorfismo, ya que el mismo método puede comportarse de manera diferente según el tipo de objeto
    # que se le pase (Perro, Gato, etc.).
    # La función hacer_hablar puede aceptar cualquier objeto que sea una instancia de Animal o sus subclases
    # y llamar al método hablar, sin importar la implementación específica de cada subclase.
    # Esto permite que el mismo código funcione con diferentes tipos de objetos,
    # mejorando la flexibilidad y la extensibilidad del software.
    # Esto es especialmente útil en situaciones donde se desea tratar diferentes tipos de objetos de manera uniforme,
    # siempre que implementen la misma interfaz o métodos.
    # En este caso, cualquier objeto que sea una instancia de Animal o sus subclases
    # puede ser pasado a la función hacer_hablar y se llamará al método hablar correspondiente.
    # Esto es un ejemplo de polimorfismo en acción.
    
#XtraJ

class Empleado:
    def __init__(self,id: int, nombre: str):
        self.id = id
        self.nombre = nombre
        self.empleados = []  # Lista para almacenar empleados a cargo

    def agregar_empleados(self, empleados):
        self.empleados.extend([empleados])  # Agrega varios empleados a la lista de empleados a cargo

    def print_empleados(self):
        for empleado in self.empleados:
            print(empleado.nombre)  # Imprime los nombres de los empleados a cargo


class Gerente(Empleado): #Gerente hereda de Empleado
  def coordinar_proyectos(self):
    print(f"El gerente {self.nombre} está coordinando proyectos de la empresa.")

class Gerente_de_proyectos(Empleado): #Gerente_de_proyectos hereda de Gerente
  def __init__(self,id: int, nombre: str, proyecto: str):
        super().__init__(id, nombre)
        self.proyecto = proyecto

  def coordinar_proyectos(self):
      print(f"El gerente de proyectos {self.nombre} está coordinando el {self.proyecto}.")

class programador(Empleado): #Programador hereda de Empleados
  def __init__(self,id: int, nombre: str, lenguaje: str):
        super().__init__(id, nombre,)
        self.lenguaje = lenguaje
  def programar(self):
      print(f"El programador {self.nombre} está programando en {self.lenguaje}.")

  def agregar_empleados(self, empleados): #Los programadores no pueden tener empleados a cargo
      for empleado in empleados:
          print(
                f"Los programadores no pueden tener empleados a cargo. {empleado} no se agregó.")
# Crear instancias de las clases
gerente = Gerente(1, "Charly")
gerente.coordinar_proyectos()  # El gerente Charly está coordinando proyectos.

gerente_de_proyectos = Gerente_de_proyectos(2, "Ana", "Proyecto X")
gerente_de_proyectos.coordinar_proyectos()  # El gerente de proyectos Ana está coordinando el Proyecto X.
gerente_de_proyectos2 = Gerente_de_proyectos(3, "Luis", "Proyecto Y")
gerente_de_proyectos2.coordinar_proyectos()  # El gerente de proyectos Luis está coordinando el Proyecto Y.
programador1 = programador(4, "Ivan", "Python")
programador1.programar()  # El programador Ivan está programando en Python.
programador2 = programador(5, "Maria", "JavaScript")
programador2.programar()  # El programador Maria está programando en JavaScript.
programador3 = programador(6, "Pedro", "C++")
programador3.programar()  # El programador Pedro está programando en C++.
programador3.agregar_empleados(["Pedro"])  # Los programadores no pueden tener empleados a cargo. Pedro no se agregó.

gerente.agregar_empleados(gerente_de_proyectos) # Agrega Ana a la lista de empleados a cargo de Charly
gerente.agregar_empleados(gerente_de_proyectos2) # Agrega Luis a la lista de empleados a cargo de Charly
"""
aqui estamos agregando a los gerentes de proyectos a la lista de empleados a cargo del gerente
"""

gerente_de_proyectos.agregar_empleados(programador1) # Agrega Ivan a la lista de empleados a cargo de Ana
gerente_de_proyectos.agregar_empleados(programador2) # Agrega Maria a la lista de empleados a cargo de Ana
"""
aqui estamos agregando a los programadores a la lista de empleados a cargo del gerente de proyectos
"""

print(f"Empleados a cargo de {gerente.nombre}:")
gerente.print_empleados()  # Imprime los empleados a cargo de Charly

# En este ejemplo, tenemos una clase base Empleado y tres subclases: Gerente, Gerente_de_proyectos y Programador.
# Cada subclase hereda atributos y métodos de la clase base Empleado.
# Además, cada subclase puede tener sus propios métodos y atributos específicos.
# La función coordinar_proyectos en las subclases Gerente y Gerente_de_proyectos demuestra el polimorfismo,
# ya que el mismo método se comporta de manera diferente según la subclase que lo implemente.
# La clase Programador también tiene su propio método programar.
# Además, la clase Programador sobrescribe el método agregar_empleados para evitar que los programadores tengan empleados a cargo.
# Esto muestra cómo la herencia y el polimorfismo pueden ser utilizados para crear una jerarquía de clases con comportamientos específicos.
            