"""
Ejercicio

"""

class Animal:

    def __init__(self) -> None:
        pass

    def sonido():
        pass

class Perro(Animal):

    def sonido(self):
        print("Guaau")

class Gato(Animal):

    def sonido(self):
        print("Miauu")


perro= Perro()
gato= Gato()

def sonido_de_aimal(ani:Animal):
    ani.sonido()

sonido_de_aimal(perro)
sonido_de_aimal(gato)


"""
Extra

"""

#Empleado

class Empleado:

    def __init__(self, id:int, nombre:str) :
        self.id=id
        self.nombre= nombre
        self.empl_a_cargo=[]

    def agregar_empleado(self, empleado):
        
        self.empl_a_cargo.append(empleado)

    def a_cargo(self):
        for emp in self.empl_a_cargo:
            print(emp.nombre)

    
#Gerente

class Gerente(Empleado):
     
     def proyectos(self):
        print(f"{self.nombre} está coordinando todos los proyectos")

class GerenteDeProyectos(Empleado):

    def __init__(self, id:int, nombre:str, proyecto:str):
        super().__init__(id, nombre)
        self.proyecto= proyecto

    def proyect(self):
        print(f"{self.nombre} está coordinando su proyecto")

#Programador

class Programador(Empleado):

    def __init__(self, id:int, nombre:str, lenguje:str):
        super().__init__(id, nombre)
        self.lenguje= lenguje


    def lenguaje (self):
        print(f"{self.nombre} está programando en {self.lenguje}")

    def agregar_empleado(self, emp: Empleado):
        print(f"Un programador no tiene empleados a cargo {emp.nombre} no se agregara")


my_manager = Gerente(1, "Masip")
my_project_manager = GerenteDeProyectos(2, "Ariel", "Proyecto 1")
my_project_manager2 = GerenteDeProyectos(3, "Diego", "Proyecto 2")
my_programmer = Programador(4, "Ciro", "Swift")
my_programmer2 = Programador(5, "Amadeo", "Cobol")
my_programmer3 = Programador(6, "Sil", "Dart")
my_programmer4 = Programador(7, "Ramona", "Python")

my_manager.agregar_empleado(my_project_manager)
my_manager.agregar_empleado(my_project_manager2)

my_project_manager.agregar_empleado(my_programmer)
my_project_manager.agregar_empleado(my_programmer2)
my_project_manager2.agregar_empleado(my_programmer3)
my_project_manager2.agregar_empleado(my_programmer4)

my_programmer.agregar_empleado(my_programmer2)

my_programmer.lenguaje()
my_project_manager.proyect()
my_manager.proyectos()
my_manager.a_cargo()
my_project_manager.a_cargo()
my_programmer.a_cargo()
