""" #09 HERENCIA Y POLIMORFISMO """

from abc import ABC, abstractmethod

# ----------------- EJERCICIO ------------------------


class Animal:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
        patas = 4

    def caminar(self):
        print("Caminando")

    def correr(self):
        print("Corriendo")


class Perro(Animal):
    def __init__(self, nombre, edad):
        super().__init__(nombre, edad)

    def ladrar(self):
        print(f"{self.nombre} está ladrando: Guau!")


class Gato(Animal):
    def __init__(self, nombre, edad):
        super().__init__(nombre, edad)

    def mauyar(self):
        print(f"{self.nombre} está mauyando: Miau!")


perro = Perro("Cucho", 5)
perro.ladrar()

gato = Gato("Minino", 1)
gato.mauyar()

# ----------------- EJERCICIO ADICIONAL --------------

# Clase Empleado (Padre)


class Employee:
    """ Clase Empleado (Clase Padre) """

    def __init__(self, name, identificator):
        """ Constructor """
        self.name = name
        self.id = identificator

    @property
    @abstractmethod
    def working(self):
        pass

    @abstractmethod
    def having_a_break(self):
        pass


# Clase Gerente


class Manager(Employee):
    """ Clase Gerente """

    def __init__(self, name, identificator):
        super().__init__(name, identificator)
        self.employees = []
        self.employees_num = 0

    def lead(self):
        """ Lidera """
        print(f"{self.name} esta dirigiendo")

    def working(self):
        """ Trabajando """
        print("Trabajando")

    def having_a_break(self):
        """ Tomando un descanso """
        print("Tomando un descanso")

    def my_employees(self, employee):
        self.employees.append(employee)

    def count_my_employees(self):
        self.employees_num = len(self.employees)
        print(self.employees_num)


# Clase Gerente de Proyectos


class ProyectManager(Manager):
    """ Clase Gerente de Proyectos """

    def __init__(self, name, identificator):
        """ Constructor """
        super().__init__(name, identificator)
        self.employees = []
        self.employees_num = 0

    def ask_for_work(self):
        """ Pregunta como vamos """
        print(f"{self.name} pregunta como vas")

    def working(self):
        """ Trabajando """
        print("Trabajando")

    def having_a_break(self):
        """ Tomando un descanso """
        print("Tomando un descanso")

    def my_employees(self, employee):
        self.employees.append(employee)

    def count_my_employees(self):
        self.employees_num = len(self.employees)
        print(self.employees_num)


# Clase Programador


class Developer(Employee):
    """ Clase Programador """

    def __init__(self, name, identificator):
        """ Constructor """
        super().__init__(name, identificator)

    def coding(self):
        """ Tirando codigo """
        print(f"{self.name} está programando")

    def debugging(self):
        """ Corrigiendo codigo """
        print(f"{self.name} está depurando su código")

    def crying(self):
        """ Frustrado """
        print(f"{self.name} está llorando por que no compila")

    def working(self):
        """ Trabajando """
        print("Trabajando")

    def having_a_break(self):
        """ Tomando un descanso """
        print("Tomando un descanso")


gerente = Manager("Ruben", 1)
gerente_proyectos = ProyectManager("Enrique", 2)
programador = Developer("Allan", 3)
programador2 = Developer("Francisco", 4)

gerente_proyectos.my_employees([programador, programador2])
gerente.my_employees(gerente_proyectos)

gerente.count_my_employees()
gerente.lead()
gerente_proyectos.ask_for_work()
programador.crying()
programador2.coding()
