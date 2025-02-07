'''
EJERCICIO:
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
 '''

class Animal:
    def __init__(self, name: str):
        self.name = name

    def sound(self):
        pass
    def __repr__(self):
        return str(self.__dict__)

class Perro(Animal):
    def __init__(self, name: str, age: int, race:str):
        super().__init__(name)
        self.race = race
        self.age = age

    def sound(self):
        print('Guau')
    
class Gato(Animal):
    def __init__(self, name: str, age: int, race: str):
        super().__init__(name)
        self.race = race
        self.age = age

    def sound(self):
        print('Miau')


def print_sound(animal: Animal):
    animal.sound()

animal = Animal('Fede')
perro = Perro('Firulais', 5, 'Pastor Aleman')
gato = Gato('Garfield', 3, 'Siames')

print(animal.name)
print_sound(perro)
print_sound(gato)
print(perro.name)
print(gato)


'''
 * DIFICULTAD EXTRA (opcional):
 * Implementa la jerarquía de una empresa de desarrollo formada por Empleados que pueden ser Gerentes, Gerentes de Proyectos o Programadores.
 * Cada empleado tiene un identificador y un nombre.
 * Dependiendo de su labor, tienen propiedades y funciones exclusivas de su actividad, y almacenan los empleados a su cargo.
 '''

class Empleado:
    def __init__(self, id: int, name: str):
        self.id = id
        self.name = name
        self.employees = []
    def __repr__(self):
        return str(self.__dict__)
    def add(self, employee):
        self.employees.append(employee)

    def print_employees(self):
        for employee in self.employees:
            print(f'los empleados de {employee.name} son: {employee}')


class Gerente(Empleado):
    def __init__(self, id: int, name: str, area: str):
        super().__init__(id, name)
        self.area = area

    def coordinate_areas(self):
        print(f'{self.name} esta coordinando las areas {self.area}')

class Ger_Proyectos(Empleado):
    def __init__(self, id: int, name: str, project: str):
        super().__init__(id, name)
        self.project = project

    def coordinate_project(self):
        print(f'{self.name} esta coordinando el proyecto {self.project}')

class Programador(Empleado):
    def __init__(self, id: int, name: str, languages: list):
        super().__init__(id, name)
        self.languages = languages

    def print_languages(self):
        print(f'{self.name} sabe los siguientes lenguajes: {self.languages}')
    def add(self, employee):
        print(f'Un programador no tiene empleados a su cargo. {employee.name} no se añadirá.')

p1 = Programador(1, 'Adolfo', ['Python', 'Java', 'C++'])
p2 = Programador(2, 'Pedro', ['Rust', 'Javascript', 'Basic'])
p3 = Programador(3, 'Juan', ['C#', 'Ruby', 'Go'])
p4 = Programador(4, 'Maria', ['PHP', 'Swift', 'Kotlin'])
g = Gerente(3, 'Juan', 'Gerencia')
proj1 = Ger_Proyectos(4, 'Maria', 'Proyecto 1')
proj2 = Ger_Proyectos(5, 'Carlos', 'Proyecto 2')
print(p1.name)
print(p2.name)
print(g.name)
print(proj1.name)
p1.print_languages()
g.coordinate_areas()
proj1.coordinate_project()
print(p1)
print(p2)
print(g)
print(proj1)
proj1.add(p1)
proj1.add(p2)
proj2.add(p3)
g.add(proj1)
g.add(proj2) 

g.print_employees()
proj1.print_employees()
proj2.print_employees()


'''
 * DIFICULTAD EXTRA (opcional):
 * Implementa dos clases que representen las estructuras de Pila y Cola (estudiadas
 * en el ejercicio número 7 de la ruta de estudio)
 * - Deben poder inicializarse y disponer de operaciones para añadir, eliminar, retornar el número de elementos e imprimir todo su contenido.
 '''
