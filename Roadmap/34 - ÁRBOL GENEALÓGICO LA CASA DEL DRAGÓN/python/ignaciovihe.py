"""
* EJERCICIO:
 * ¡La Casa del Dragón ha finalizado y no volverá hasta 2026! 
 * ¿Alguien se entera de todas las relaciones de parentesco
 * entre personajes que aparecen en la saga?
 * Desarrolla un árbol genealógico para relacionarlos (o invéntalo).
 * Requisitos:
 * 1. Estará formado por personas con las siguientes propiedades:
 *    - Identificador único (obligatorio)
 *    - Nombre (obligatorio)
 *    - Pareja (opcional)
 *    - Hijos (opcional)
 * 2. Una persona sólo puede tener una pareja (para simplificarlo).
 * 3. Las relaciones deben validarse dentro de lo posible.
 *    Ejemplo: Un hijo no puede tener tres padres.
 * Acciones:
 * 1. Crea un programa que permita crear y modificar el árbol.
 *    - Añadir y eliminar personas
 *    - Modificar pareja e hijos
 * 2. Podrás imprimir el árbol (de la manera que consideres).
 * 
 * NOTA: Ten en cuenta que la complejidad puede ser alta si
 * se implementan todas las posibles relaciones. Intenta marcar
 * tus propias reglas y límites para que te resulte asumible.
"""

from uuid import uuid4

class Person:
    def __init__(self, name: str):
        self.id = uuid4()
        self.name = name
        self.parents = []
        self.partner = None
        self.children = []


class Family:
    def __init__(self):
        self.members = {}

    def __getitem__(self, index):
        return self.members[index]
    
    def __setitem__(self, key, value):
        self.members[key] = value

    def __contains__(self, key):
        return key in self.members
    
    def __len__(self):
        return len(self.members)


class FamilyManager:
    def __init__(self, family: Family):
        self.family = family

    def add_person(self, person: Person):
        self.family[person.id] = person

    def add_partner(self, person: Person, partner: Person):
        if person.id in self.family and partner.id in self.family and not person.partner:
            person.partner = partner.id
            partner.partner = person.id
        else:
            print("Una de las personas no esta añadida a la familia, o ya tiene pareja.")

    def add_child(self, parent: Person, child: Person):
        if parent.id in self.family and child.id in self.family and parent.partner and not child.parents:
            parent.children.append(child)
            self.family[parent.partner].children.append(child)
            child.parents.append(parent)
            child.parents.append(parent.partner)


class FamilyPrinter:
    def __init__(self, family: Family):
        self.family = family

    def print_family_tree(self, root_person: Person, prefix: str = "", is_last: bool = True):
        pareja = ""
        if root_person.partner:
            pareja = f"-💍-{self.family[root_person.partner].name}"
        branch = "└─ " if is_last else "├─ "
        print(f"{prefix}{branch}{root_person.name}{pareja}")

        # Nuevo prefijo para hijos
        if is_last:
            new_prefix = prefix + "   "
        else:
            new_prefix = prefix + "│  "

        # Imprimir hijos
        num_children = len(root_person.children)
        for i, child in enumerate(root_person.children):
            is_last_child = (i == num_children - 1)
            self.print_family_tree(child, new_prefix, is_last_child)

def main():
    print()
    print()
    family = Family()
    family_manager = FamilyManager(family)
    family_printer = FamilyPrinter(family)

    p1 = Person("Jocelyn")
    p2 = Person("Aemon")
    family_manager.add_person(p1)
    family_manager.add_person(p2)
    family_manager.add_partner(p1, p2)

    p3 = Person("Rhaenys")
    family_manager.add_person(p3)
    family_manager.add_child(p1,p3)

    p4 = Person("Corlys")
    family_manager.add_person(p4)
    family_manager.add_partner(p3, p4)

    p5 = Person("Laena")
    p6 = Person("Laenor")
    family_manager.add_person(p5)
    family_manager.add_person(p6)
    family_manager.add_child(p3,p5)
    family_manager.add_child(p3,p6)


    p7 = Person("Baelon")
    p8 = Person("Alyssa")
    family_manager.add_person(p7)
    family_manager.add_person(p8)
    family_manager.add_partner(p7, p8)

    p9 = Person("Viserys I")
    p10 = Person("Daemon")
    family_manager.add_person(p9)
    family_manager.add_person(p10)
    family_manager.add_child(p7,p9)
    family_manager.add_child(p8,p10)

    p11 = Person("Aemma")
    family_manager.add_person(p11)
    family_manager.add_partner(p9, p11)

    p12 = Person("Rhaenyra")
    family_manager.add_person(p12)
    family_manager.add_child(p9,p12)
    family_manager.add_partner(p10, p12)

    p13 = Person("Aegon")
    p14 = Person("Viserys")
    family_manager.add_person(p13)
    family_manager.add_person(p14)
    family_manager.add_child(p12,p13)
    family_manager.add_child(p12,p14)

    family_printer.print_family_tree(p1)
    family_printer.print_family_tree(p7)

main()   
