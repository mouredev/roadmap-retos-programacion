# HERENCIA Y POLIMORFISMO

# HERENCIA
class Animal:
    def __init__(self, nombre, edad) -> None:
        self.nombre = nombre
        self.edad = edad

class Perro(Animal):
    def hace_sonido(self) -> None:
        print(f"{self.nombre} de {self.edad} años hace Guau!")

class Gato(Animal):
    def hace_sonido(self) -> None:
        print(f"{self.nombre} de {self.edad} años hace Miau!\n")


perro = Perro("Firulais", 4)
gato = Gato("Manchas", 3)

perro.hace_sonido()
gato.hace_sonido()


# EJERCICIO - DIFICULTAD EXTRA

# EMPRESA DE DESAROLLO
class Empleado:
    def __init__(self, id: int, nombre: str) -> None:
        self.id = id
        self.nombre = nombre
        self.empleados = []

    def agregar_empleado(self, empleado) -> None:
        self.empleados.append(empleado)

    def mostrar_empleados(self) -> None:
        print({f"Id: {empleado.id}, Nombre: {empleado.nombre}" for empleado in self.empleados})

class Gerente(Empleado):
    def __init__(self, id: int, nombre: str, departamento: str) -> None:
        super().__init__(id, nombre)
        self.departamento = departamento

    def cargo_departamento(self):
        print(f"El gerente {self.nombre} tiene a cargo el departamento de {self.departamento}")

class GerenteProyecto(Empleado):
    def __init__(self, id: int, nombre: str, proyecto: str) -> None:
        super().__init__(id, nombre)
        self.proyecto = proyecto
        self.equipo_proyecto = []

    def cargo_proyecto(self) -> None:
        print(f"El gerente de proyecto {self.nombre} tiene a cargo el proyecto de {self.proyecto}")

    def add_developer(self, empleado: Empleado) -> None:
        self.equipo_proyecto.append(empleado.nombre)

    def show_developers(self) -> None:
        print(f"El gerente de proyecto {self.nombre} tiene a cargo a los desarrolladores: {', '.join([i for i in self.equipo_proyecto])}\n")

class Programador(Empleado):
    def __init__(self, id: int, nombre: str, lenguajes: list[str]) -> None:
        super().__init__(id, nombre)
        self.lenguaje = lenguajes

    def lenguajes(self) -> None:
        print(f"El programador {self.nombre} desarrolla en {", ".join([i for i in self.lenguaje])}")


gerente = Gerente(1, "Juan", "Ventas")
gerente2 = Gerente(2, "Andres", "Diseño y Publicidad")

gerente_proyecto = GerenteProyecto(3, "Sergio", "Desarrollo Aplicación Móvil")
gerente_proyecto2 = GerenteProyecto(4, "Javier", "E-Commerce")

programador = Programador(5, "Marco Antonio", ["Python", "C++", "Java"])
programador2 = Programador(6, "Pablo", ["C#", "Rust", "JavaScript"])


gerente.agregar_empleado(gerente)
gerente.agregar_empleado(gerente2)
gerente.cargo_departamento()
gerente2.cargo_departamento()

gerente_proyecto.agregar_empleado(gerente_proyecto)
gerente_proyecto.agregar_empleado(gerente_proyecto2)

gerente_proyecto.add_developer(programador)
gerente_proyecto.add_developer(programador2)

gerente_proyecto.cargo_proyecto()
gerente_proyecto2.cargo_proyecto()
gerente_proyecto.show_developers()

programador.agregar_empleado(programador)
programador.agregar_empleado(programador2)
programador.lenguajes()
programador2.lenguajes()

print()
gerente.mostrar_empleados()
gerente_proyecto.mostrar_empleados()
programador.mostrar_empleados()