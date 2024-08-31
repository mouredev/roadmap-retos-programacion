class Animal:
    #Creamos el método constructor de la clase y el atributo del sonido
    def __init__(self, nombre):
        self.nombre = nombre
        self.sonido = "Sonido que realiza un animal"
    
    def realizar_sonido(self):
        print(self.sonido)

#Creamos las subclases Perro y Gato que heredaran de la clase Animal
class Perro(Animal):

    def __init__(self, nombre):
        super().__init__(nombre)
    
    #Cambiamos el resultado del método realizar_sonido que hace la clase Perro respecto a la clase Animal
    def realizar_sonido(self):
        print("Guau")

class Gato(Animal):

    def __init__(self, nombre):
        super().__init__(nombre)

    #Cambiamos el resultado del método realizar_sonido que hace la clase Gato respecto a la clase Animal
    def realizar_sonido(self):
        print("Miau")

mi_perro = Perro("Willie")
mi_perro.realizar_sonido()

mi_gato = Gato("Lebron")
mi_gato.realizar_sonido()


#EXTRA
class Empleados:

    def __init__(self, identificador, nombre):
        self.identificador = identificador
        self.nombre = nombre
        self.empleados = []

    def add(self, empleado):
        self.empleados.append(empleado)

    def mostrar_empleados(self):
        print("\nLos empleados a su cargo son:")
        for empleado in self.empleados:
            print(empleado.nombre)

class Gerente(Empleados):

    def __init__(self, identificador, nombre):
        super().__init__(identificador, nombre)

    def coordinar_proyectos(self):
        print(f"{self.nombre} esta coordinado los proyectos")

class GerenteDeProyectos(Empleados):

    def __init__(self, identificador, nombre):
        super().__init__(identificador, nombre)

    def coordinar_proyecto(self):
        print(f"{self.nombre} está gestionando su proyecto")

class Programadores(Empleados):

    def __init__(self, identificador, nombre, lenguaje):
        super().__init__(identificador, nombre)
        self.lenguaje = lenguaje


    def codigo(self):
        print(f"{self.nombre} está programando la app en {self.lenguaje}")

    def add(self):
        print(f"Los programadores no tienen empleados a su cargo.")

mi_gerente = Gerente(1, "Manuel")
mi_gerente_proyecto = GerenteDeProyectos(2, "Lucia")
mi_programador1 = Programadores(3, "Mario", "Python")
mi_programador2 = Programadores(4, "Marcial", "C#")
mi_programador3 = Programadores(5, "Rosa", "Python")
mi_programador4 = Programadores(6, "Nuria", "Java")

mi_gerente.add(mi_gerente_proyecto)
mi_gerente_proyecto.add(mi_programador1)
mi_gerente_proyecto.add(mi_programador2)
mi_gerente_proyecto.add(mi_programador3)
mi_gerente_proyecto.add(mi_programador4)
mi_programador1.codigo()
mi_programador2.codigo()
mi_programador3.codigo()
mi_programador4.codigo()

mi_gerente.mostrar_empleados()
mi_gerente_proyecto.mostrar_empleados()