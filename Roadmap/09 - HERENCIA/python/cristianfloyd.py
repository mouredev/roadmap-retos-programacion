# EJERCICIO:
# Explora el concepto de herencia según tu lenguaje. Crea un ejemplo que
# implemente una superclase Animal y un par de subclases Perro y Gato,
# junto con una función que sirva para imprimir el sonido que emite cada Animal.


class Animal:
    def __init__(self, nombre, raza=None):
        self.nombre = nombre
        self.raza = raza

    def hacer_sonido(self):
        raise NotImplementedError("Subclase debe implementar este método")

    def __str__(self):
        return (
            f"Nombre: {self.nombre}, Raza: {self.raza if self.raza else 'Desconocida'}"
        )


class Perro(Animal):
    def __init__(self, nombre, raza=None):
        super().__init__(nombre, raza)

    def hacer_sonido(self):
        print(f"{self.nombre}: Guau!")


class Gato(Animal):
    def __init__(self, nombre, raza=None):
        super().__init__(nombre, raza)

    def hacer_sonido(self):
        print(f"{self.nombre}: Miau!")


laica = Perro("Laika", "Husky Siberiano")
michi = Gato("Michi", "Siames")

laica.hacer_sonido()
michi.hacer_sonido()

print(laica)


#
# DIFICULTAD EXTRA (opcional):
# Implementa la jerarquía de una empresa de desarrollo formada por Empleados que
# pueden ser Gerentes, Gerentes de Proyectos o Programadores.
# Cada empleado tiene un identificador y un nombre.
# Dependiendo de su labor, tienen propiedades y funciones exclusivas de su
# actividad, y almacenan los empleados a su cargo.


class Empleado:
    def __init__(self, id, nombre, empleados_a_cargo=None):
        self.id = id
        self.nombre = nombre
        self.empleados_a_cargo = (
            empleados_a_cargo if empleados_a_cargo is not None else []
        )
        print(f"Empleado creado: {self.nombre} (ID: {self.id})")

    def trabajar(self):
        print(f"{self.nombre} está ejecutando las tareas asignadas.")

    def add(self, empleado):
        self.empleados_a_cargo.append(empleado)


class Gerente(Empleado):
    def __init__(self, id, nombre):
        super().__init__(id, nombre)

    def agregar_empleado(self, empleado):
        self.empleados_a_cargo.append(empleado)
        print(f"{empleado.nombre} ha sido agregado a los empleados de {self.nombre}.")

    def mostrar_empleados(self):
        print(f"Empleados a cargo de {self.nombre}:")
        for emp in self.empleados_a_cargo:
            print(f"- {emp.nombre} (ID: {emp.id})")

    def quitar_empleado(self, empleado):
        if empleado in self.empleados_a_cargo:
            self.empleados_a_cargo.remove(empleado)

    def coordinar_proyectos(self):
        print(f"{self.nombre} está coordinando todos los proyectos de la empresa.")

    def trabajar(self):
        return self.coordinar_proyectos()


class GerenteDeProyectos(Empleado):
    def __init__(self, id, nombre, proyecto):
        super().__init__(id, nombre)
        self.proyecto = proyecto

    def coordinar_proyecto(self):
        print(f"{self.nombre} está coordinando el proyecto: {self.proyecto}")
        print("Con los programadores asignados al proyecto:")
        print(", ".join([emp.nombre for emp in self.empleados_a_cargo]))

    def trabajar(self):
        return self.coordinar_proyecto()


class Programador(Empleado):
    def __init__(self, id, nombre: str, lenguaje):
        super().__init__(id, nombre)
        self.lenguaje = lenguaje

    def programar(self):
        print(f"{self.nombre} está programando en {self.lenguaje}.")

    def trabajar(self):
        return self.programar()


manager = Gerente(1, "Ana")
pm1 = GerenteDeProyectos(2, "Luis", "Proyecto X")
dev1 = Programador(3, "Cristian", "Python")

manager.agregar_empleado(pm1)
pm1.add(dev1)
manager.mostrar_empleados()
pm1.coordinar_proyecto()
dev1.programar()

pm2 = GerenteDeProyectos(4, "Sofía", "Proyecto Y")
dev2 = Programador(5, "Miguel", "JavaScript")
dev3 = Programador(6, "Lucía", "Java")

manager.agregar_empleado(pm2)
manager.mostrar_empleados()

pm2.add(dev2)
pm2.add(dev3)
pm2.coordinar_proyecto()
dev2.programar()
dev3.programar()
