# 34 - Arbol Genealogico de la casa del dragon

class Person():

    def __init__(self, id: int, name: str):
        self.id = id
        self.name = name
        self.partner = None
        self.children = []
        self.has_parents = False
        self.father = None
        self.mother = None

    def add_partner(self, partner):
        if self.partner is not None:
            print(f"{self.name} ya tiene pareja ({self.partner.name})")
        elif partner.partner is not None:
            print(f"{partner.name} ya tiene pareja ({partner.partner.name})")
        else:
            self.partner = partner
            partner.partner = self
            print(f"{self.name} es pareja de {self.partner.name}")

    def add_child(self, child):
        if child not in self.children:
            self.children.append(child)
            print(f"{self.name} ha tenido un hijo: {child.name}")
        else:    
            print(f"{child.name} ya esta registrado como hijo de {self.name}")

    def add_parent(self, father, mother):
        if father is None and mother is None:
            self.father = father
            self.mother = mother
            self.has_parents = True
        # else:
        #     print(f"{self.name} ya tiene padres añadidos: {self.father}, {self.mother}")

class FamilyTree():

    def __init__(self):
        self.people = {}

    def add_person(self,id, name):
        if id in self.people:
            print(f"Ya se encuentra una persona con ID:{id}")
        elif name in self.people.values():
            print(f"Ya se encuentra una persona con el nombre: {name}")
        else:
            person = Person(id, name)
            self.people[id] = person
            print(f"La persona de nombre: {name} con ID: {id} ha sido añadida a la lista")
        
    def remove_person(self, id):
        if id in self.people:
            person = self.people[id]
            del self.people[id]
            print(f"La persona: {person.name} con ID:{id} ha sido removido del arbol familiar")
        else:
            print(f"No existe una persona con ID:{id}")

    def set_partner(self, id_1, id_2):
        if id_1 in self.people and id_2 in self.people:
            person_1 = self.people[id_1]
            person_2 = self.people[id_2]
            person_1.add_partner(person_2)
        else:
            print("Alguno de los ID no se encuentran en la lista")
        

    def add_child(self, id_parent, id_child):
        if id_parent in self.people and id_child in self.people:
            if id_parent == id_child:
                print("No pueden tener el mismo ID")
            else:
                parent = self.people[id_parent]
                if parent.partner is None:
                    print(f"{parent.name} debe tener pareja para tener un hijo")
                else:
                    child = self.people[id_child]
                    if child.has_parents:
                        print(
                            f"ID: {child.id} ya tiene padres!")
                    else:
                        parent.add_child(child)
                        parent.partner.add_child(child)
                        child.add_parent(parent, parent.partner)
        else:
            print("Alguno de los ID no se encuentran en la lista")

    def print_tree(self):

        visited = set()

        def print_person(person: Person, level =0):

            if person.id in visited:
                return
            
            visited.add(person.id)

            indent = " "*4*level

            print(f"{indent}-{person.name} [ID]: {person.id}")

            if person.partner:
                visited.add(person.partner.id)
                print(
                    f"{indent} Pareja: {person.partner.name} [ID]: {person.partner.id}"
                )
            
            if person.children:
                print(f"{indent} Hijos:")
                for child in person.children:
                    print_person(child, level+1)
        
        for person in self.people.values():
            is_child = person.has_parents
            if not is_child:
                print_person(person)

tree = FamilyTree()


tree.add_person(1, "Jocelyn")
tree.add_person(2, "Aemon")

tree.set_partner(1, 2)

tree.add_person(3, "Rhaenys")

tree.add_child(1, 3)

tree.add_person(4, "Corlys")

tree.set_partner(3, 4)

tree.add_person(5, "Laena")
tree.add_person(6, "Laenor")

tree.add_child(3, 5)
tree.add_child(3, 6)

tree.add_person(7, "Baelon")
tree.add_person(8, "Alyssa")

tree.set_partner(7, 8)

tree.add_person(9, "Viserys I")
tree.add_person(10, "Daemon")

tree.add_child(7, 9)
tree.add_child(8, 10)

tree.add_person(11, "Aemma")

tree.set_partner(9, 11)

tree.add_person(12, "Rhaenyra")

tree.add_child(9, 12)

tree.set_partner(10, 12)

tree.add_person(13, "Aegon")
tree.add_person(14, "Viserys")

tree.add_child(12, 13)
tree.add_child(12, 14)

tree.print_tree()
