#Herencia

class Animal:
    def __init__(self, type, age) -> None:
        self.type = type
        self.age = age

class Perro(Animal):
    def sonido(self):
        print("Guau")

class Gato(Animal):
    def sonido(self):
        print("Miau")

perro = Perro("Mamifero",7)
gato = Gato("Mamifero",5)

perro.sonido()
gato.sonido()

#Dificultad Extra
print("Dificultad Extra"+ "\n")

class Empleado:
    def __init__(self,id,nombre) -> None:
        self.id = id
        self.nombre = nombre

    def __str__(self) -> str:
        return "Empleado id: " + str(self.id) + " " + self.nombre
    
class Gerente(Empleado):
    def __init__(self, id, nombre,departamento,proyectos) -> None:
        super().__init__(id, nombre)
        self.departamento = departamento
        self.list_proyectos = proyectos

    def list_gerente_proyectos(self) -> str:
        proyectos = ""
        for elem in self.list_proyectos:
            proyectos = proyectos + str(elem) + "\n"
        return proyectos

    def __str__(self) -> str:
        proyectos = self.list_gerente_proyectos()
        return "*Gerente " + super().__str__() + " " + self.departamento + "\n" + proyectos
    
class Gerente_Proyectos(Empleado):
    def __init__(self, id, nombre,proyecto,programadores) -> None:
        super().__init__(id, nombre)
        self.proyecto = proyecto
        self.list_programadores = programadores
    
    def list_programmers(self) -> str:
        programmes = ""
        for elem in self.list_programadores:
            programmes = programmes + str(elem) + "\n"
        return programmes

    def __str__(self) -> str:
        return "-Gerente Proyectos " + super().__str__() + " " + self.proyecto + "\n" + self.list_programmers()

class Programadores(Empleado):
    def __init__(self, id, nombre, language_program) -> None:
        super().__init__(id, nombre)
        self.language_program = language_program
    def __str__(self) -> str:
        return " ".join(["--Programador",super().__str__(),"lenguaje",self.language_program])


programador1 = Programadores(6,"program1","JavaScript")
programador2 = Programadores(7,"program2","JavaScript")
programador3 = Programadores(8,"program3","React")
programador4 = Programadores(9,"program4","React")
programador5 = Programadores(10,"program5","Java")

gerente_pro1 = Gerente_Proyectos(3,"GPro1","Proyecto1",[programador1,programador2])
gerente_pro2 = Gerente_Proyectos(4,"GPro2","Proyecto2",[programador3])
gerente_pro3 = Gerente_Proyectos(5,"GPro3","Proyecto3",[programador1,programador2,programador4,programador5])

gerente1 = Gerente(1,"Gerente1","I+D",[gerente_pro1,gerente_pro2])
gerente2 = Gerente(2,"Gerente2","Finance",[gerente_pro3])

print(gerente1)
print(gerente2)
