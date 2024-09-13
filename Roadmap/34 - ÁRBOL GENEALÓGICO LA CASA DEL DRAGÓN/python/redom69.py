"""
/*
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
 */
 """

class Person:
    def __init__(self, id, name, couple=None, children=None):
        self.id = id
        self.name = name
        self.couple = couple
        self.children = children if children is not None else []

    def add_child(self, child):
        self.children.append(child)

    def modify_couple(self, couple):
        self.couple = couple

    def __repr__(self):
        couple_name = self.couple.name if self.couple else "None"
        return f"Person(id={self.id}, name={self.name}, couple={couple_name}, children={len(self.children)})"

class FamilyTree:
    def __init__(self, person):
        self.root = person
        self.people = {person.id: person}

    def add_person(self, person):
        if person.id not in self.people:
            self.people[person.id] = person
        else:
            print(f"La persona con ID {person.id} ya existe en el árbol genealógico.")

    def delete_person(self, person_id):
        if person_id in self.people:
            del self.people[person_id]
        else:
            print(f"No se encontró ninguna persona con ID {person_id}.")

    def edit_person(self, id, name=None, couple=None, children=None):
        if id in self.people:
            person = self.people[id]
            if name:
                person.name = name
            if couple:
                person.modify_couple(couple)
            if children is not None:
                person.children = children if isinstance(children, list) else []
        else:
            print(f"No se encontró ninguna persona con ID {id}.")

    def display_tree(self, person=None, level=0):
        if person is None:
            person = self.root

        indent = " " * (level * 4)
        couple_name = f" & {person.couple.name}" if person.couple else ""
        print(f"{indent}{person.name}{couple_name}")

        if person.children:
            for child in person.children:
                self.display_tree(child, level + 1)

    def __repr__(self):
        return f"FamilyTree(root={self.root.name}, total_people={len(self.people)})"

def main():

    jaehaerys = Person(id=1, name="Jaehaerys I Targaryen")
    alysanne = Person(id=2, name="Alysanne Targaryen")

    baelon = Person(id=3, name="Baelon Targaryen")
    alyssa = Person(id=4, name="Alyssa Targaryen")

    viserys = Person(id=5, name="Viserys I Targaryen")
    aemma = Person(id=6, name="Aemma Arryn")

    daemon = Person(id=7, name="Daemon Targaryen")
    rhea = Person(id=8, name="Rhea Royce")
    laena = Person(id=9, name="Laena Velaryon")
    rhaenyra = Person(id=10, name="Rhaenyra Targaryen")

    alicent = Person(id=11, name="Alicent Hightower")
    aegon_ii = Person(id=12, name="Aegon II Targaryen")
    helaena = Person(id=13, name="Helaena Targaryen")
    aemond = Person(id=14, name="Aemond Targaryen")
    daeron = Person(id=15, name="Daeron Targaryen")

    jaehaerys.couple = alysanne
    baelon.couple = alyssa
    baelon.children = [viserys, daemon]
    viserys.couple = aemma
    viserys.children = [rhaenyra]
    daemon.couple = rhea  
    daemon.children = []  

    daemon.couple = laena
    baela = Person(id=16, name="Baela Targaryen")
    rhaena = Person(id=17, name="Rhaena Targaryen")
    daemon.children = [baela, rhaena]

    rhaenyra.couple = daemon

    viserys.couple = alicent
    viserys.children += [aegon_ii, helaena, aemond, daeron] 

    family_tree = FamilyTree(viserys)
    family_tree.add_person(jaehaerys)
    family_tree.add_person(alysanne)
    family_tree.add_person(baelon)
    family_tree.add_person(alyssa)
    family_tree.add_person(daemon)
    family_tree.add_person(rhea)
    family_tree.add_person(laena)
    family_tree.add_person(rhaenyra)
    family_tree.add_person(alicent)
    family_tree.add_person(aegon_ii)
    family_tree.add_person(helaena)
    family_tree.add_person(aemond)
    family_tree.add_person(daeron)
    family_tree.add_person(baela)
    family_tree.add_person(rhaena)

    family_tree.display_tree()



if __name__ == "__main__":
    main()