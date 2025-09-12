# 9 Herencia

# Ejercicio

# Superclase Animal
class Animal:
    def __init__(self, nombre: str, raza: str, edad: int, sonido_emitido: str):
        self.nombre = nombre
        self.raza = raza
        self.edad = edad
        self.sonido_emitido = sonido_emitido

    def sonido(self):
        print(f"{self.sonido_emitido}.")

    def jugar(self):
        pass

# Subclase Perro que hereda de Animal


class Perro(Animal):
    def __init__(self, nombre: str, raza: str, edad: int, sonido_emitido: str, tamaño: str, objeto: str):
        super().__init__(nombre, raza, edad, sonido_emitido)
        self.tamaño = tamaño
        self.objeto = objeto

    def ladrar(self):
        print(f"{self.nombre} dice ", end='')
        self.sonido()  # Llamada al método sonido de la superclase Animal

    def jugar(self):
        return f"{self.nombre} juega con la {self.objeto}."

# Subclase Gato que hereda de Animal


class Gato(Animal):
    def maullar(self):
        print(f"{self.nombre} dice ", end='')
        self.sonido()

    def jugar(self):
        return f"{self.nombre} juega con un ovillo de lana."

# Polimorfismo


def mostrar_juego(animal: Animal):
    print(animal.jugar())


# Instancia de la clase Perro
mi_perro = Perro("Rex", "Labrador", 5, "Guau", "Grande", "Pelota")

# Llamar al método ladrar
mi_perro.ladrar()

# Instancia de la clase Gato
mi_gato = Gato("Tom", "Persa", 2, "Miau")

# Llamar al método ladrar
mi_gato.maullar()

# Acceder a los atributos
print("Nombre:", mi_gato.nombre)
print("Raza:", mi_gato.raza)
print("Edad:", mi_gato.edad)
print("Sonido emitido:", mi_gato.sonido_emitido)
mostrar_juego(mi_perro)
mostrar_juego(mi_gato)


# Dificultad Extra

class Empleado:
    def __init__(self, id: int, nombre: str):
        self.id = id
        self.nombre = nombre
        self.cargo = ""
        self.area = ""
        self.proyecto = ""
        self.empleados_a_cargo = []

    def asignar_cargo(self, cargo):
        self.cargo = cargo

    def asignar_area(self, area):
        self.area = area

    def asignar_proyecto(self, proyecto):
        self.proyecto = proyecto

    def asignar_empleado(self, empleado: 'Empleado'):
        self.empleados_a_cargo.append(empleado)

    def empleados(self):
        for emp in self.empleados_a_cargo:
            print(emp.nombre)


# Subclase Gerente
class Gerente(Empleado):
    def coordinar(self):
        print(f"{self.nombre} coordina los proyectos de la empresa")

    def asignar_area(self, area):
        print(f"{self.nombre} coordina todas las areas.")

# Subclase GerenteProyectos


class GerenteProyectos(Empleado):
    def coordinar(self):
        print(f"{self.nombre} coordina el proyecto {self.proyecto}.")

# Subclase Programador


class Programador(Empleado):
    def __init__(self, id: int, nombre: str, lenguaje: str):
        super().__init__(id, nombre)
        self.lenguaje = lenguaje

    def asignar_empleado(self, empleado: Empleado):
        pass


# Instancia
gerente = Gerente(1, "Juan")
gerente.asignar_cargo("Gerente de Desarrollo")
gerente.asignar_area("Desarrollo")

gerente_proyecto = GerenteProyectos(2, "María")
gerente_proyecto.asignar_area("Desarrollo")
gerente_proyecto.asignar_cargo("Gerente de BD")
gerente_proyecto.asignar_proyecto("Implementación de base de datos")

programador1 = Programador(3, "Pedro", "Python")
programador1.asignar_area("Desarrollo")
programador1.asignar_proyecto("Implementación de base de datos")
programador1.asignar_cargo("Programador")
programador2 = Programador(4, "Lucía", "Java")
programador2.asignar_area("Desarrollo")
programador2.asignar_cargo("Programador")
programador3 = Programador(4, "Pablo", "Cobol")
programador3.asignar_area("Desarrollo")
programador3.asignar_cargo("Programador")


gerente.asignar_empleado(gerente_proyecto)
gerente_proyecto.asignar_empleado(programador1)
gerente_proyecto.asignar_empleado(programador2)
gerente_proyecto.asignar_empleado(programador3)
programador1.asignar_empleado(programador2)


# Uso
print("Empleados de gerente:")
gerente.empleados()

print("Empleados de gerente de proyectos:")
gerente_proyecto.empleados()

print(programador1.empleados_a_cargo)
print(programador1.lenguaje)
print(programador2.lenguaje)

gerente.coordinar()
gerente_proyecto.coordinar()
