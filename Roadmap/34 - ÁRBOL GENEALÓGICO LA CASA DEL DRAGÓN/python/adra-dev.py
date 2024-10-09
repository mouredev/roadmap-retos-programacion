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

by adra-dev
"""

class Person:
    
    def __init__(self, id: int, name: str):
        self.id = id
        self.name = name 
        self.partner = None
        self.children = []
        self.has_parents = False


    def add_partner(self, partner):
        if self.partner is not None:
            print(f"{self.name} ya tiene una pareja: {self.partner.name}.")
        else:
            self.partner = partner
            partner.partner = self
            print(f"{self.name} es pareja de {partner.name}")

    def add_child(self, child):
        if child not in self.children:
            self.children.append(child)
            print(f"{self.name} ha tenido un hijo: {child.name}")
        else:
            print(f"{child.name} ya es hijo de {self.name}")


class FamilyTree:

    def __init__(self):
        self.people = {}

    def add_person(self, id, name):
        if id in self.people:
            print(f"La persona con ID:{id} ya existe.")
        else:
            person = Person(id, name)
            self.people[id] = person
            print(f"La perosna con nombre {name} [ID: {id}] ha sido agregada al arbol.")

    def remove_person(self, id):
        if id in self.people:
            person = self.people[id]
            del self.people[id]
            print(f"La persona con nombre {person.name} [ID: {id}] ha sido eliminada del arbol.")
        else:
            print(f"La persona con [ID: {id}] no existe en el arbol.")
        
    def set_partner(self, id1, id2):
        if id1 in self.people and id2 in self.people:
            person1 = self.people[id1]
            person2 = self.people[id2]
            person1.add_partner(person2)
        else:
            print("Algun ID no existe en el arbol.")

    def add_child(self, parent_id, child_id):
        if parent_id in self.people and child_id in self.people:
            if parent_id == child_id:
                print("Los ID no pueden ser iguales a la hora de asignar un hijo.")
            else:
                parent = self.people[parent_id]
                if parent.partner is None:
                    print(f"Se necesita una pareja para poder tener un hijo.")
                else:
                    child = self.people[child_id]
                    if child.has_parents:
                        print(f"{child.name} [ID: {id}] ya tiene padres")
                    else:
                        child.has_parents = True
                        parent.add_child(child)
                        parent.partner.add_child(child)
        else:
            print("Algun ID no existe en el arbol.")

    def pint_tree(self):

        visited = set()

        def print_person(person, level = 0):
            
            if person.id in visited:
                return
            
            visited.add(person.id)

            indent = "\t" * level

            print(f"{indent} - {person.name} [ID: {person.id}]")

            if person.partner:
                visited.add(person.partner.id)
                print(
                    f"{indent}   Pareja: {person.partner.name} [ID: {person.partner.id}]")

            if person.children:
                print(f"{indent}  Hijos:")
                for child in person.children:
                    print_person(child, level + 1)
        

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

tree.set_partner(7,8)


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

tree.pint_tree()