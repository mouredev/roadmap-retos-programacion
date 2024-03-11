"""
 * EJERCICIO:
 * Explora el concepto de herencia según tu lenguaje. Crea un ejemplo que
 * implemente una superclase Animal y un par de subclases Perro y Gato,
 * junto con una función que sirva para imprimir el sonido que emite cada Animal.
"""

from __future__ import annotations

import uuid
from abc import ABC, abstractmethod
from typing import List, Optional, Union


class Animal(ABC):
    def __init__(self, name: str) -> None:
        self.name = name

    @abstractmethod
    def make_sound(self):
        pass


class Perro(Animal):

    def make_sound(self):
        print('Guauuu')


class Gato(Animal):
    def make_sound(self):
        print('Miauu')


firulais = Perro('Firulais')
mishi = Gato('Mishi')

firulais.make_sound()
mishi.make_sound()


"""
 * DIFICULTAD EXTRA (opcional):
 * Implementa la jerarquía de una empresa de desarrollo formada por Empleados que
 * pueden ser Gerentes, Gerentes de Proyectos o Programadores.
 * Cada empleado tiene un identificador y un nombre.
 * Dependiendo de su labor, tienen propiedades y funciones exclusivas de su
 * actividad, y almacenan los empleados a su cargo.
"""


class Employee(ABC):

    def __init__(self, name: str, salary: float, leader: Optional[Employee] = None) -> None:
        self.id = uuid.uuid4()
        self.name = name
        self.salary = salary
        self.leader = leader
        self.direct_reports: List[Employee] = []

        if leader:
            leader.add_direct_report(self)

    def __str__(self) -> str:
        string = '\n'.join(
            (
                f'ID: {self.id}',
                f'Nombre: {self.name}',
                f'Salario: {self.salary:_}',
                f'Líder: {self.get_leader_name()}',
                f'Reportes Directos: {self.get_direct_reports_names()}',
                f'Ejecutando: {self.execute()}',
            )
        )
        return string

    def add_direct_report(self, employee: Employee) -> None:
        self.direct_reports.append(employee)

    def get_direct_reports_names(self) -> List[str]:
        return [employee.name for employee in self.direct_reports]

    def get_leader_name(self) -> Union[str, None]:
        if self.leader and isinstance(self.leader, Employee):
            return self.leader.name
        return None

    @abstractmethod
    def execute(self) -> str:
        pass


class Manager(Employee):
    def execute(self):
        return 'Definiendo estrategía para que la compañía crezca...'


class Projectmanager(Employee):

    def __init__(
        self, name: str, salary: float, project: str, leader: Optional[Employee] = None
    ) -> None:
        super().__init__(name, salary, leader)
        self.project = project

    def execute(self):
        return f'Liderando y supervisando el proyecto: {self.project}'


class Developer(Employee):
    def __init__(self, name: str, salary: float, leader: Optional[Projectmanager] = None) -> None:
        super().__init__(name, salary, leader)
        if leader and isinstance(leader, Projectmanager):
            self.project = leader.project
        else:
            self.project = 'sin proyecto'

    def execute(self):
        return f'Desarrollando en el proyecto: {self.leader.project}'


manager = Manager('Juan David', 35_000_000)

project_manager_1 = Projectmanager('Esteban', 13_000_000, 'Incentivos', manager)
project_manager_2 = Projectmanager('Santiago', 12_500_000, 'Algoritmo', manager)

developer_1 = Developer('Daniel', 8_000_000, project_manager_1)
developer_2 = Developer('Julian', 8_500_000, project_manager_1)
developer_3 = Developer('Felipe', 8_000_000, project_manager_1)
developer_4 = Developer('Duván', 9_000_000, project_manager_2)
developer_5 = Developer('Brais', 11_000_000, project_manager_2)

print(manager)
print('-' * 25)
print(project_manager_1)
print('-' * 25)
print(project_manager_2)
print('-' * 25)
print(developer_5)
