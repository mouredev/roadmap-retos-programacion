class Animal:

    def __init__(self,name):
        self.name = name  

    def sound(self):
        pass   



class Perro(Animal):

    def sound(self):

        print("Guau")       

class Gato(Animal):

    def sound(self):

        print("Miau")   


my_animal = Animal("Animal")
my_animal.sound()              
my_perro = Perro("Perro")
my_perro.sound()
my_gato = Gato("Gato")
my_gato.sound()




class Empresa:

    def __init__(self, id:int, name:str):

        self.id = id
        self.name = name
        self.empleados = []


    def emplear(self, empleados):
        self.empleados.append(empleados)
        

class Gerente(Empresa):

    def coordinar_proyectos(self):
        print(f"{self.name} esta coordinando los proyectos de la empresa")


class Gerente_Proyecto(Empresa):
    
    def __init__(self, id: int, name: str, proyecto:str):
        super().__init__(id, name)
        self.proyecto = proyecto

    def coordinar_proyecto(self):
        print(f"{self.name} esta coordinando su proyecto {self.proyecto}")

    def proyecto_ger(self):
        print(f"{self.name} esta coordinando el {self.proyecto}")   


class Programador(Empresa):

    def __init__(self, id: int, name: str, lenguaje:str):
        super().__init__(id, name)
        self.lenguaje = lenguaje

    def programar(self):
        print(f"{self.name} esta programando en {self.lenguaje}")

    def emplear(self, empleados):
        print(f"un programdor no tiene empleados a su cargo")   


my_gerente= Gerente(1, "Andres")
my_gerente_proyecto1= Gerente_Proyecto(2, "Jose", "Carrosdev" ) 
my_gerente_proyecto2= Gerente_Proyecto(3, "Carlos", "Motosdev")
my_programador= Programador(4, "Maykol" , "Python") 
my_programador2= Programador(5, "Abraham" , "Go") 
 
my_gerente.emplear(my_gerente_proyecto1)
my_gerente.emplear(my_gerente_proyecto2)

my_gerente_proyecto1.emplear(my_programador)
my_gerente_proyecto2.emplear(my_programador2)

my_programador.emplear(my_programador2)
my_programador.programar()

my_gerente_proyecto1.coordinar_proyecto()

my_gerente.coordinar_proyectos()
