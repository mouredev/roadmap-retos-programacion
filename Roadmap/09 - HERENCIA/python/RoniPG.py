#Roni
"""
EJERCICIO:
Explora el concepto de herencia según tu lenguaje. Crea un ejemplo que
implemente una superclase Animal y un par de subclases Perro y Gato,
junto con una función que sirva para imprimir el sonido que emite cada Animal.
"""
class Animal : # Superclase
    def __init__(self) -> None:
          pass
    def sonidoAnimal(self) :
        print("Soy un animal que emite sonido")
        
class Perro(Animal) : # --> Subclase
    def __init__(self) -> None:
        pass
    def sonidoAnimal(self) :
        print("Soy un perro y ladro")
        
class Gato (Animal) : # --> Subclase
    def __init__(self) -> None:
        pass
    def sonidoAnimal(self) :
        print("Soy un gato y maúllo")

# Instaciamos los objetos
an = Animal() # --> Objeto Animal
an.sonidoAnimal() # --> Llamamos a la función
perro = Perro() # --> Objeto Perro
perro.sonidoAnimal() # --> Llamamos a la función sobrescrita
gato = Gato() # --> Objeto Gato
gato.sonidoAnimal() # --> Llamamos a la función sobrescrita
"""
DIFICULTAD EXTRA (opcional):
Implementa la jerarquía de una empresa de desarrollo formada por Empleados que
pueden ser Gerentes, Gerentes de Proyectos o Programadores.
Cada empleado tiene un identificador y un nombre.
Dependiendo de su labor, tienen propiedades y funciones exclusivas de su
actividad, y almacenan los empleados a su cargo.
"""
#Instaciamos los objetos
class Empleado : # --> Superclase
    #Atributos heredables
    identificador :int
    nombre : str
    def __init__(self,identificador : int, nombre : str) -> None:
        self.identificador=identificador
        self.nombre=nombre
class Gerente (Empleado) : # --> Subclase
    #Atributos propios
    cargo : str
    g_p_d : list # --> Lista de empleados
    def __init__(self, identificador: int, nombre: str) -> None:
        super().__init__(identificador, nombre)
        self.g_p_d=list()
        self.cargo="Gerente"
    #Metodos propios
    def asignarEmpleado(self, gdp) :
        self.g_p_d.append(gdp)
    def soy(self) :
        print(f"Soy: {self.nombre}\nMi cargo es: {self.cargo}")
        for gdp in self.g_p_d:
           print(f"Tengo a cargo a: {gdp.nombre}")
class Gerente_de_Proyecto (Empleado) : # --> Subclase
    # Atributos propios
    cargo : str
    programadores : list # --> Lista de empleados
    def __init__(self, identificador: int, nombre: str) -> None:
        super().__init__(identificador, nombre)
        self.programadores= list()
        self.cargo="Gerente de Proyecto"
    # Metodos propios
    def asignarEmpleado(self, pgr ) :
        self.programadores.append(pgr) 
    def asignarEncargado(self, ger:Gerente) :
        ger.asignarEmpleado(self)
    def soy(self) :
        print(f"Soy: {self.nombre}\nMi cargo es: {self.cargo}")   
        for pgr in self.programadores:
            print(f"Tengo a cargo a: {pgr.nombre}")
class Programador (Empleado) : # --> Subclase
    # Atributos propios
    cargo :str
    def __init__(self, identificador: int, nombre: str) -> None:
        super().__init__(identificador, nombre)
        self.cargo="Programador"
    # Metodos propios
    def asignarEncargado(self, gdp:Gerente_de_Proyecto) :
        gdp.asignarEmpleado(self)
    def soy(self) :
        print(f"Soy: {self.nombre}\nMi cargo es: {self.cargo}")
ger1 = Gerente(0, "A") # --> Objeto Gerente
ger2 = Gerente(1, "B") # --> Objeto Gerente
gdp1 = Gerente_de_Proyecto(3, "C") # --> Objeto Gerente de Proyecto       
gdp2 = Gerente_de_Proyecto(4, "D") # --> Objeto Gerente de Proyecto       
pgr1 = Programador(5, "E") # --> Objeto Programador
pgr2 = Programador(6, "F") #--> Objeto Programador
# Le asignamos un empleado(Gerente de proyecto) al Gerente
ger1.asignarEmpleado(gdp1)
ger1.soy() # --> Llamamos a la función propia del Gerente
# Le asignamos un Encargado(Gerente) al Gerente de proyecto
gdp2.asignarEncargado(ger2)
ger2.soy() #--> Llamamos a la función propia del Gerente
# Le asignamos un empleado(Programador) al Gerente de proyecto
gdp1.asignarEmpleado(pgr1)
gdp1.soy() # --> Llamamos a la función propia del Gerente de proyecto de proyecto sobrescrita     
# Le asignamos un Encargado(Gerente de proyecto) al Programador
pgr2.asignarEncargado(gdp2)
gdp2.soy() #--> Llamamos a la función propia del Gerente de proyecto de proyecto sobrescrita     
pgr1.soy() # --> Llamamos a la función propia del Programador de proyecto sobrescrita
pgr2.soy() # --> Llamamos a la función propia del Programador de proyecto sobrescrita
