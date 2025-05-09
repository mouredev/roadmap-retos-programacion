"""
 EJERCICIO:
 ¡La Casa del Dragón ha finalizado y no volverá hasta 2026! 
 ¿Alguien se entera de todas las relaciones de parentesco
 entre personajes que aparecen en la saga?
 Desarrolla un árbol genealógico para relacionarlos (o invéntalo).
 Requisitos:
 1. Estará formado por personas con las siguientes propiedades:
    - Identificador único (obligatorio)
    - Nombre (obligatorio)
    - Pareja (opcional)
    - Hijos (opcional)
 2. Una persona sólo puede tener una pareja (para simplificarlo).
 3. Las relaciones deben validarse dentro de lo posible.
    Ejemplo: Un hijo no puede tener tres padres.
 Acciones:
 1. Crea un programa que permita crear y modificar el árbol.
    - Añadir y eliminar personas
    - Modificar pareja e hijos
 2. Podrás imprimir el árbol (de la manera que consideres).
 
 NOTA: Ten en cuenta que la complejidad puede ser alta si
 se implementan todas las posibles relaciones. Intenta marcar
 tus propias reglas y límites para que te resulte asumible.
"""
from typing import Literal


class Relationship:

    def __init__(self, relation: Literal["single", "spouse", "parent", "child"]):
        self.relation = []
        self.add_relation(relation)

    def add_relation(self, relation: Literal["single", "spouse", "parent", "child"]):
        self.relation.append(relation)

    def drop_relation(self, relation: Literal["single", "spouse", "parent", "child"]):
        self.relation.remove(relation)


class Person(Relationship):

    id = 0
    people = []

    def __init__(self, name: str, gender: Literal["F", "M"]):
        super().__init__("single")
        self.name = name.title()
        self.gender = gender
        self.spouse = None
        self.parents = []
        self.children = []
        self.id = self.set_id()
        Person.people.append(self)

    @classmethod
    def set_id(cls):
        cls.id += 1
        return cls.id

    @classmethod
    def get_people(cls):
        def sort_people(p):
            return p.get_name()

        cls.people.sort(key=sort_people)
        return cls.people

    def get_id(self):
        return self.id

    def get_name(self):
        return self.name

    def get_parent(self):
        return self.parents

    def get_children(self):
        return self.children

    def is_maried(self):
        return self.spouse

    def get_relations(self):
        return self.relation

    def set_spouse(self, spouse):
        if "spouse" in self.get_relations():
            return False
        self.spouse = spouse
        self.drop_relation("single")
        self.add_relation("spouse")
        return True

    def set_parents(self, parents):

        def restrictions():
            if self in parents:
                print(f"No se puede ser padre de uno mismo")
                return True
            if self.parents:
                print(f"Ya tiene padres")
                return True
            if parents.__len__() > 1:
                if parents[0] == parents[1]:
                    print(f"Ambos padres NO pueden ser la misma persona.")
                    return True
                if parents[0] != parents[1].is_maried():
                    print(f"Los padres NO estan casados.")
                    return True
            return False

        if restrictions():
            return False

        self.parents.append(parents[0])
        if self not in parents[0].get_children():
            parents[0].set_children([self])
        if parents.__len__() > 1:
            self.parents.append(parents[1])
            if self not in parents[1].get_children():
                parents[1].set_children([self])
        if "child" not in self.get_relations():
            self.add_relation("child")
        return True

    def set_children(self, children):
        for child in children:
            if child not in self.get_children():
                self.children.append(child)
                if "child" not in child.get_relations():
                    child.add_relation("child")
        if "parent" not in self.get_relations():
            self.add_relation("parent")


def are_siblings(person1: Person, person2: Person):

    for parent in person1.get_parent():
        if person2 in parent.get_children():
            return True

    for parent in person2.get_parent():
        if person1 in parent.get_children():
            return True

    return False


def get_married(person1: Person, person2: Person):

    if person1 == person2:
        print(f"No se puede casar consigo mismo")
    else:
        p1_married = person1.is_maried()
        p2_married = person2.is_maried()
        siblings = are_siblings(person1, person2)
        p1_son = person1 in person2.get_children()
        p2_son = person1 in person1.get_children()
        p1_parent = person1 in person2.get_parent()
        p2_parent = person1 in person1.get_parent()
        if any([p1_married, p2_married]):
            print(f"No se pueden casar: bigamia")
        elif any([siblings, p1_son, p2_son, p1_parent, p2_parent]):
            print(f"No se pueden casar: consanguinidad")
        else:
            person1.set_spouse(person2)
            person2.set_spouse(person1)


def menu():
    option = -1

    print("\n\tElegir una persona para mostrar el árbol genealógico\n")
    for index, person in enumerate(Person.get_people()):
        print(f"\t{index + 1} - {person.get_name()}")
    print(f"\t0 - Salir")
    while option < 0 or option > Person.get_people().__len__():
        option = input(f"\n\tIngrese una opción [1 - {Person.get_people().__len__()} | 0 para salir]: ")
        if not option.isnumeric():
            option = -1
        else:
            option = int(option)
    return Person.get_people()[option - 1] if option > 0 else None


def load_generations():
    # Primera generación
    tito = Person("Tito", "M")
    livia = Person("Livia", "F")
    chacho = Person("Chacho", "M")
    tina = Person("Tina", "F")
    romula = Person("Romula", "F")

    get_married(tito, livia)
    get_married(chacho, tina)

    # Segunda generación
    turula = Person("Turula", "F")
    pepe = Person("Pepe", "M")
    papo = Person("Papo", "M")
    pipa = Person("Pipa", "F")
    soto = Person("Soto", "M")
    rema = Person("Rema", "F")
    roma = Person("Roma", "F")

    for child in [turula, pepe, papo]:
        child.set_parents([tito, livia])

    for child in [pipa, soto]:
        child.set_parents([chacho, tina])

    for child in [rema, roma]:
        child.set_parents([romula])

    get_married(turula, soto)
    get_married(pepe, pipa)
    get_married(papo, roma)

    # Tercera generación
    tita = Person("Tita", "F")
    sita = Person("Sita", "F")
    pipo = Person("Pipo", "M")
    pepa = Person("Pepa", "F")
    chino = Person("Chino", "M")
    ramo = Person("Ramo", "M")
    rima = Person("Rima", "F")

    for child in [tita, sita]:
        child.set_parents([turula, soto])

    for child in [pipo, pepa, chino]:
        child.set_parents([pepe, pipa])

    for child in [ramo, rima]:
        child.set_parents([rema])

    get_married(tita, ramo)
    get_married(pipo, rima)

    # Cuarta generación
    paco = Person("Paco", "M")
    chicho = Person("Chicho", "M")
    chona = Person("Chona", "F")
    chano = Person("Chano", "M")
    rama = Person("Rama", "F")

    paco.set_parents([tita, ramo])

    for child in [chicho, chona, chano]:
        child.set_parents([pipo, rima])

    rama.set_parents([sita])

    # Quinta generación
    pico = Person("Pico", "M")

    pico.set_parents([paco])


def show_tree(person: Person, level: int = 0, iteration: int = 0, tree=None):
    if tree is None:
        tree = {0: [], 1: [], 2: []}
    message = ""
    for relationship in person.get_relations():
        match relationship, level:
            case "child", 0:
                parents = []
                siblings = []
                for parent in person.get_parent():
                    parents.append(parent.get_name())
                    show_tree(parent, 1, iteration + 1, tree)
                for sibling in person.get_parent()[0].get_children():
                    if person != sibling:
                        siblings.append(sibling.get_name())
                message = f"\t{person.get_name()} es {'hijo' if person.gender == 'M' else 'hija'} de " + f"{', '.join(parents)}"
                if siblings:
                    message += f"\n\t{person.get_name()} es {'hermano' if person.gender == 'M' else 'hermana'} de " + f"{', '.join(siblings)}"
                if message not in tree[level]:
                    tree[level].append(message)
            case "spouse", 0:
                message = f"\t{person.get_name()} está {'casado' if person.gender == 'M' else 'casada'} con {person.spouse.get_name()}"
                if message not in tree[level]:
                    tree[level].append(message)
            case "parent", 0:
                children = []
                for child in person.get_children():
                    children.append(child.get_name())
                    show_tree(child, 2, iteration + 1, tree)
                message = f"\t{person.get_name()} es {'padre' if person.gender == 'M' else 'madre'} de " + f"{', '.join(children)}"
                if message not in tree[level]:
                    tree[level].append(message)
            case "single", 0:
                message = f"\t{person.get_name()} es {'soltero' if person.gender == 'M' else 'soltera'}"
                if message not in tree[level]:
                    tree[level].append(message)
            case "child", 1:
                parents = []
                for parent in person.get_parent():
                    parents.append(parent.get_name())
                    show_tree(parent, 1, iteration + 1, tree)
                message = f"\t{'-' * 5 * iteration + '> '}{person.get_name()} es {'hijo' if person.gender == 'M' else 'hija'} de " + f"{', '.join(parents)}"
                if message not in tree[level]:
                    tree[level].append(message)
            case "parent", 2:
                children = []
                for child in person.get_children():
                    children.append(child.get_name())
                    show_tree(child, 2, iteration + 1, tree)
                message = f"\t{'-' * 5 * iteration + '> '}{person.get_name()} es {'padre' if person.gender == 'M' else 'madre'} de " + f"{', '.join(children)}"
                if message not in tree[level]:
                    tree[level].append(message)
        # tree[level].append(message)
    return tree


load_generations()
while True:
    person = menu()
    if not person:
        break
    tree = show_tree(person)
    tree[2].sort(reverse=True)
    print(f"\n\t## Árbol  {'#' * 30}\n")
    for level in (1, 0, 2):
        for msg in tree[level]:
            print(msg)
    print(f"\n\t{'#' * 40}")
