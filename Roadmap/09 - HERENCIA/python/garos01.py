# Herencia


class Animal:
    def __init__(self, nombre):
        self.nombre = nombre

    def hacer_sonido(self):
        pass


class Perro(Animal):
    def hacer_sonido(self):
        return "Guau"


class Gato(Animal):
    def hacer_sonido(self):
        return "Miau"


def imprimir_sonido(animal):
    tipo_animal = type(animal).__name__
    print(f"{animal.nombre} mi {tipo_animal} hace: {animal.hacer_sonido()}")


mi_perro = Perro("Buddy")
mi_gato = Gato("Whiskers")

imprimir_sonido(mi_perro)
imprimir_sonido(mi_gato)

# Ejercicio extra


class Empleado:
    def __init__(self, identificador, nombre):
        self.identificador = identificador
        self.nombre = nombre

    def realizar_tarea(self):
        pass


class Gerente(Empleado):
    def __init__(self, identificador, nombre, departamento):
        super().__init__(identificador, nombre)
        self.departamento = departamento
        self.empleados_a_cargo = []

    def asignar_tarea(self, tarea):
        print(f"El gerente {self.nombre} asigna la tarea: {tarea}")

    def realizar_tarea(self):
        print(f"El gerente {self.nombre} está gestionando el departamento.")


class GerenteProyecto(Gerente):
    def __init__(self, identificador, nombre, departamento, proyecto):
        super().__init__(identificador, nombre, departamento)
        self.proyecto = proyecto

    def realizar_tarea(self):
        print(
            f"El gerente de proyecto {self.nombre} está supervisando el proyecto {self.proyecto}."
        )


class Programador(Empleado):
    def __init__(self, identificador, nombre, lenguaje):
        super().__init__(identificador, nombre)
        self.lenguaje = lenguaje

    def codificar(self):
        print(f"El programador {self.nombre} está codificando en {self.lenguaje}.")

    def realizar_tarea(self):
        self.codificar()


gerente_jefe = Gerente(1, "Ana", "Desarrollo")
gerente_proyecto1 = GerenteProyecto(2, "Carlos", "Desarrollo", "ProyectoX")
gerente_proyecto2 = GerenteProyecto(3, "Diana", "Desarrollo", "ProyectoY")
gerente_proyecto3 = GerenteProyecto(4, "Eduardo", "QA", "ProyectoZ")
programador1 = Programador(5, "Fernando", "Python")
programador2 = Programador(6, "Gabriela", "Java")
programador3 = Programador(7, "Hugo", "C++")
programador4 = Programador(8, "Isabel", "JavaScript")
programador5 = Programador(9, "Javier", "Ruby")
programador6 = Programador(10, "Karen", "Swift")

gerente_jefe.empleados_a_cargo.extend(
    [
        gerente_proyecto1,
        gerente_proyecto2,
        gerente_proyecto3,
        programador1,
        programador2,
        programador3,
        programador4,
        programador5,
        programador6,
    ]
)

gerente_jefe.asignar_tarea("Planificación anual")
for empleado in gerente_jefe.empleados_a_cargo:
    empleado.realizar_tarea()
