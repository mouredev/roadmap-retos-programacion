### HERENCIA ###

class Animal:
    def __init__(self,tipo,name,grupo):
        self.tipo = tipo
        self.name = name
        self.grupo = grupo
    def caracteristicas(self):
        print(f"El animal es de tipo: {self.tipo}, es un/a {self.name} y pertenece al grupo de {self.grupo}")

class Perro(Animal):
    def sonido(self):
        print("El perro hace: Guau-Guau")

class Gato(Animal):
    def sonido(self):
        print("El gato hace: Miau-Miau")


my_animal = Animal ("Salvaje", "Ballena","Mamifero")

my_animal.caracteristicas() 

my_dog = Perro ("Domestico", "Perro" , "Mamifero")

my_dog.caracteristicas()

my_dog.sonido()

my_cat = Gato ("Domestico", "Gato", "Mamifero")

my_cat.caracteristicas()

my_cat.sonido()

## *********EXTRA********** ##

class Empleado:
    def __init__(self, id , name) :
     self.id = id
     self.name = name
     self.empleados = []
    def add(self,empleado):
        self.empleados.append(empleado)
    def print_empleados(self):
        for empleado in self.empleados:
            print(empleado.name)

    


class Programador(Empleado):
    def __init__(self, id , name , language) :
     super().__init__(id,name)
     self.language = language
    def funciones (self) :
        print (f"El programador {self.name} programa en {self.language} y tiene las siguientes funciones: ")
        print("Desarrollo de aplicaciones moviles y web \nAcatar las instrucciones del Gerente de proyectos.")
    def add(self,empleado:Empleado):
        print(f"Un programador no tiene trabajadores a su cargo. {empleado.name} no se agregará")



class GerenteProyectos(Empleado):

    def funciones (self) :
        print (f"El Gerente de Proyectos {self.name} tiene las siguientes funciones: ")
        print("Coordinar y definir actividades para el desarollo del proyecto asignado \nAsignar tareas a los programadores a su cargo")

class Gerente(Empleado):
    def funciones (self) :
        print (f"El Gerente {self.name} tiene las siguientes funciones: ")
        print("Establecer los requerimientos del cliente \nAcatar los lineamientos del proyecto por parte del CEO y del cliente \nAsignar el proyecto al gerente del proyecto")


p_1 = Programador(1,"Julio Cesar Torres","Kotlin")

p_1.funciones()

m1_manager = Gerente(1,"Francisco Gutierrez")
m2_manager = GerenteProyectos(1,"Laura Jimenez")

m1_manager.add(m2_manager)

m1_manager.print_empleados()