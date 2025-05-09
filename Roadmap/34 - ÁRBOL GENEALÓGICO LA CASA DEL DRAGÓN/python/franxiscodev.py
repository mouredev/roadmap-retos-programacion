'''
Arbol genealógico de la casa del dragón
'''


class Person:
    def __init__(self, id: int, name: str):
        self.id = id
        self.name = name
        self.partner = None
        self.children = []

    def add_partner(self, partner):
        if self.partner is not None:
            print(f"Esta persona ya tiene pareja: {self.partner.name}")
        else:
            self.partner = partner
            partner.partner = self  # no es una relación unilateral
            print(f"{self.name} es pareja de {partner.name} y viceversa")

    def add_child(self, child):
        if self.partner == None:
            print("No puedes tener hijos sin pareja.")
        elif child not in self.children:
            self.children.append(child)
            self.partner.children.append(child)  # hijo de ambos
            print(
                f"{self.name} ha tenido un hijo: {child.name} junto a su pareja {self.partner.name}")
        else:
            print(f"{self.name} ya tiene un hijo: {child.name}")


class FamilyTree:
    def __init__(self):
        self.people = {}

    def add_person(self, id: int, name: str):
        if id not in self.people:
            person = Person(id, name)
            self.people[id] = person
            print(f"La persona {name} con ID:{id} se agregó al árbol.")
        else:
            print(f"El ID: {id} ya existe.")

    def remove_person(self, id: int):
        if id in self.people:
            person = self.people[id]
            del self.people[id]
            print(f"Se eliminó el ID: {id} de la persona {person.name}.")
        else:
            print(f"Persona con ID: {id} no existe.")

    def set_partner(self, id: int, partner_id: int):
        if id in self.people and partner_id in self.people:
            person = self.people[id]
            partner = self.people[partner_id]
            person.add_partner(partner)
        else:
            print(
                f"Una de las personas no existe. ID: {id} o ID: {partner_id}")

    def set_child(self, parent_id: int, child_id: int):
        if parent_id == child_id:
            print("No puedes ser padre de ti mismo.")
        elif parent_id in self.people and child_id in self.people:
            parent = self.people[parent_id]
            child = self.people[child_id]
            parent.add_child(child)
        else:
            print(
                f"Una de las personas no existe. ID: {parent_id} o ID: {child_id}")

    def print_tree(self):
        for person in self.people.values():
            print(
                f"ID: {person.id}, Name: {person.name}, Partner: {person.partner.name if person.partner else 'None'}, Children: {[child.name for child in person.children]}")


tree = FamilyTree()
tree.add_person(1, "Alicia")
tree.add_person(2, "Bob")
tree.add_person(3, "Charlie")

tree.set_partner(1, 3)  # Alicia es pareja de Charlie
tree.set_child(1, 2)    # Alicia es madre de Bob
# tree.set_child(3, 2)    # Charlie es padre de Bob, no es necesario lo fuerzo por ser pareja de ... que ya tiene un hijo
tree.set_child(3, 3)    # No puedes ser padre de ti mismo.

tree.print_tree()
