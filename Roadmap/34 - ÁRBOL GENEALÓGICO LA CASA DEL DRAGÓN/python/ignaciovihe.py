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

# Contiene la informacion de cada mienbro.
class Person:

    _id_counter = 1 # Se utiliza para crear el id. Se podria usar uuid4 pero serian ids mas complejos.
    
    def __init__(self, name: str):
        self.id = Person._id_counter
        Person._id_counter += 1
        self.name = name
        self.parents = []
        self.partners = {} # Para implementar varias parejas he diseñado un dicccionario con {id_pareja:[hijos]}


class Family: # Esta clase es como un diccionario que une cada id de persona con su objeto Persona. Para poder hacer busquedas rapidas.
    def __init__(self):
        self.members = {}

    def __getitem__(self, index):# permite obtener un item sin tener que acceder a family.members[i]-> simplemente family[i]
        return self.members[index]
    
    def __setitem__(self, key, value):# lo mismo para setear un valor
        self.members[key] = value

    def __contains__(self, key):# para poder usar in family directamente (no in family.members)
        return key in self.members
    
    def __len__(self):
        return len(self.members)# para obtener len fa family directamente.


# Esta clase se encarga de gestionar las personas y añadir relaciones en family.
class FamilyManager:
    def __init__(self, family: Family):
        self.family = family

    def add_person(self, person: Person):
        self.family[person.id] = person

    def add_partner(self, person: Person, partner: Person):
        if person.id in self.family and partner.id in self.family:
            if partner.id not in person.partners:
                person.partners[partner.id] = []
                partner.partners[person.id] =[]
            else:
                print("Ya esta registrada la pareja.")
        else:
            print("Una de las personas no esta añadida a la familia.")

    def add_child(self, parent: Person, partner: Person, child: Person):
        if parent.id in self.family and partner.id in self.family and child.id in self.family:
            if partner.id in parent.partners and not child.parents:
                parent.partners[partner.id].append(child)
                partner.partners[parent.id].append(child)
                child.parents.append(parent)
                child.parents.append(partner)
            else:
                print("Las personas pasadas no son pareja, o el hijo ya tiene padres.")
        else:
            print("El padre, madre o el hijo no estan añadidas a la familia")


# Se encarga de imprimir el arbol familiar a partir de una raiz de forma recursiva.
# Lo he diseñado para que imprime todas las parejas de cada miembro y sus hijos.
#Aunque se repita alguna persona. Con el id se puede ver si se refiere a la misma.
class FamilyPrinter:
    def __init__(self, family: Family):
        self.family = family

    def print_family_tree(self, root: Person, prefix: str = "", is_last: bool = True):

        branch = "└─ " if is_last else "├─ "
        print(f"{prefix}{branch}{root.name}[id={root.id}]")

        if is_last:
            prefix_partner = prefix + "   "
        else:
            prefix_partner = prefix + "│  "

        partners = root.partners.keys()
        for i , id_partner in enumerate(partners):
            is_last_partner = i == len(partners) - 1
            branch_partner = "└─ " if is_last_partner else "├─ "
            print(f"{prefix_partner}{branch_partner}💍- {self.family[id_partner].name}[id={self.family[id_partner].id}]")

            if is_last_partner:
                prefix_child = prefix_partner + "   "
            else:
                prefix_child = prefix_partner + "│  "

            children = root.partners[id_partner]
            for i, child in enumerate(children):
                is_last_child = i == len(children) - 1
                self.print_family_tree(child, prefix_child, is_last_child)


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
    family_manager.add_child(p1, p2, p3)

    p4 = Person("Corlys")
    family_manager.add_person(p4)
    family_manager.add_partner(p3, p4)

    p5 = Person("Laena Velaryon")
    p6 = Person("Laenor Velaryon")
    family_manager.add_person(p5)
    family_manager.add_person(p6)
    family_manager.add_child(p3, p4, p5)
    family_manager.add_child(p3, p4, p6)


    p7 = Person("Baelon")
    p8 = Person("Alyssa")
    family_manager.add_person(p7)
    family_manager.add_person(p8)
    family_manager.add_partner(p7, p8)

    p9 = Person("Viserys I")
    p10 = Person("Daemon")
    family_manager.add_person(p9)
    family_manager.add_person(p10)
    family_manager.add_child(p7, p8, p9)
    family_manager.add_child(p8, p7, p10)

    family_manager.add_partner(p10, p5)

    p11 = Person("Aemma Arryn")
    family_manager.add_person(p11)
    family_manager.add_partner(p9, p11)

    p12 = Person("Alicent Hightower")
    family_manager.add_person(p12)
    family_manager.add_partner(p9, p12)
    p20 = Person("Aegon II")
    p21 = Person("Helaena")
    p22 = Person("Aemond")
    family_manager.add_person(p20)
    family_manager.add_person(p21)
    family_manager.add_person(p22)
    family_manager.add_child(p9, p12, p20)
    family_manager.add_child(p9, p12, p21)
    family_manager.add_child(p9, p12, p22)


    p13 = Person("Rhaenyra")
    family_manager.add_person(p13)
    family_manager.add_child(p9, p11, p13)
    family_manager.add_partner(p13, p6)

    p15 = Person("Jacaerys")
    p16 = Person("Lucerys")
    p17 = Person("Joffrey")
    family_manager.add_person(p15)
    family_manager.add_person(p16)
    family_manager.add_person(p17)
    family_manager.add_child(p13, p6, p15)
    family_manager.add_child(p13, p6, p16)
    family_manager.add_child(p13, p6, p17)

    family_manager.add_partner(p10, p13)
    p18 = Person("Aegon III")
    p19 = Person("Viserys II")
    family_manager.add_person(p18)
    family_manager.add_person(p19)
    family_manager.add_child(p10, p13, p18)
    family_manager.add_child(p10, p13, p19)
    
    
    p24 = Person("Aegon")
    p25 = Person("Viserys")
    family_manager.add_person(p24)
    family_manager.add_person(p25)
    
    family_manager.add_child(p10 ,p5, p24)
    family_manager.add_child(p10 ,p5, p25)

    family_printer.print_family_tree(p1)
    family_printer.print_family_tree(p7)

main()   
