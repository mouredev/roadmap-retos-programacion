#! /bin/python3.12

# Autor: Héctor Adán
# GitHub: https://github.com/hectorio23

class Person:
    def __init__(self, id, name, partner=None):
        self.id = id  
        self.name = name 
        self.partner = partner  
        self.children = []  

    def add_child(self, child):
        if len(child.parents()) < 2:
            self.children.append(child)
        else:
            raise ValueError(f"{child.name} already has two parents.")

    def set_partner(self, partner):
        if self.partner is None:
            self.partner = partner
            partner.partner = self
        else:
            raise ValueError(f"{self.name} is already partnered with {self.partner.name}.")

    def parents(self):
        # Get the parents by finding people who have this person as a child
        return [p for p in Person.instances if self in p.children]

    @staticmethod
    def display_tree(person, level=0):
        if person.partner:
            print("  " * level + person.partner.name)

        print("  " * level + person.name)
        for child in person.children:
            Person.display_tree(child, level + 1)


# Sample usage examples
Person.instances = []
alice = Person(1, "Andrea")
bob = Person(2, "Adán")
alice.set_partner(bob)
child = Person(3, "Alejandro")
alice.add_child(child)
child.add_child(Person(4, "María"))
Person.display_tree(alice)

