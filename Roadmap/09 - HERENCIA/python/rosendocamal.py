"""
 * EJERCICIO:
 * Explora el concepto de herencia según tu lenguaje. Crea un ejemplo que
 * implemente una superclase Animal y un par de subclases Perro y Gato,
 * junto con una función que sirva para imprimir el sonido que emite cada Animal.
 *
 * DIFICULTAD EXTRA (opcional):
 * Implementa la jerarquía de una empresa de desarrollo formada por Empleados que
 * pueden ser Gerentes, Gerentes de Proyectos o Programadores.
 * Cada empleado tiene un identificador y un nombre.
 * Dependiendo de su labor, tienen propiedades y funciones exclusivas de su
 * actividad, y almacenan los empleados a su cargo.
"""

class Animal():
    def __init__(self, sound: str) -> None:
        self.sound = sound

    def comunicarse(self) -> str:
        return self.sound
    
    def __str__(self) -> str:
        return "El animal hace ¡%s!" % self.sound

class Perro(Animal):
    def __init__(self, sound: str, name: str) -> None:
        super().__init__(sound)
        self.name = name

    def __str__(self) -> str:
        return "El perro %s hace ¡%s!" % (self.name, self.sound)

class Gato(Animal):
    def __init__(self, sound: str, name: str) -> None:
        super().__init__(sound)
        self.name = name

    def __str__(self) -> str:
        return "El gato %s hace ¡%s!" % (self.name, self.sound)

an_animal: Animal = Animal("Grr, grr")
print(an_animal); print(an_animal.comunicarse()); print()

a_dog: Perro = Perro("Gua, gua, gua", "Boby")
print(a_dog); print(a_dog.comunicarse()); print()

a_cat: Gato = Gato("Miau, mia, miau", "Kitty")
print(a_cat); print(a_cat.comunicarse()); print()

# EXTRA

class Empleado():
    def __init__(self, name: str, id: int, job: str, salary: float) -> None:
        self.name = name
        self.id_empleado = id
        self.job = job
        self.salary_base = salary

    def chambear(self) -> str:
        return "Se pone a laburar..."

    def __str__(self) -> str:
        return f"{self.id_empleado} - {self.name.upper()} - {self.job.upper()}"

class Gerente(Empleado):
    def __init__(self, name: str, id: int, job: str, salary: float) -> None:
        super().__init__(name, id, job, salary)
        self.under_employees = []

    def salario(self, goal_percentage: float) -> float:
        return self.salary_base * goal_percentage

    def subordinados(self, subordinado: Empleado) -> None:
        self.under_employees.append(subordinado)

    def ver_gente_a_cargo(self) -> str:
        gente: str = ""
        for employee in self.under_employees:
            gente += employee.__str__() + '\n'
        return gente

class Programador(Empleado):
    def __init__(self, name: str, id: int, job: str, salary: float) -> None:
        super().__init__(name, id, job, salary)

    def salario(self, hours_per_week: int) -> float:
        return self.salary_base * hours_per_week

gerente_gay = Gerente("Gary Guy Gay", 1001, "Gerente", 200000)
programadorA = Programador("Juan", 1010, "Frot-End Developer", 25000)
programadorB = Programador("Sebastián", 1011, "Back-End Developer", 25500)
programadorC = Programador("Gabriel", 1012, "FullStack Developer", 35000)

gerente_gay.subordinados(programadorA)
gerente_gay.subordinados(programadorB)
gerente_gay.subordinados(programadorC)

print(gerente_gay.salario(75))
print(gerente_gay.salary_base)
print(gerente_gay.under_employees)
print(gerente_gay)
print()

print(programadorA.chambear())
print(programadorB.chambear())
print(programadorC.chambear())
print(gerente_gay.chambear())
print()

print(programadorA.salario(45))
print(programadorB.salario(40))
print(programadorC.salario(85))
print()