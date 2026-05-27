# @Author Daniel Grande (Mhayhem)

# EJERCICIO:
# ¡La Casa del Dragón ha finalizado y no volverá hasta 2026! 
# ¿Alguien se entera de todas las relaciones de parentesco
# entre personajes que aparecen en la saga?
# Desarrolla un árbol genealógico para relacionarlos (o invéntalo).
# Requisitos:
# 1. Estará formado por personas con las siguientes propiedades:
#    - Identificador único (obligatorio)
#    - Nombre (obligatorio)
#    - Pareja (opcional)
#    - Hijos (opcional)
# 2. Una persona sólo puede tener una pareja (para simplificarlo).
# 3. Las relaciones deben validarse dentro de lo posible.
#    Ejemplo: Un hijo no puede tener tres padres.
# Acciones:
# 1. Crea un programa que permita crear y modificar el árbol.
#    - Añadir y eliminar personas
#    - Modificar pareja e hijos
# 2. Podrás imprimir el árbol (de la manera que consideres).
# 
# NOTA: Ten en cuenta que la complejidad puede ser alta si
# se implementan todas las posibles relaciones. Intenta marcar
# tus propias reglas y límites para que te resulte asumible.

class Person:
    def __init__(self, id: int, name: str, partner=None, children=None):
        self.id = id
        self.name = name.capitalize()
        self.partner = partner
        self.children = children if children is not None else []

    def set_partner(self, person):
        if self.partner:
            self.partner.partner = None
        self.partner = person
        if person:
            person.partner = self
        print("Registro de pareja completado.")

    def add_child(self, child):
        if child not in self.children:
            self.children.append(child)

    def delete_relantioship(self, person):
        if self.partner and person.id == self.partner.id:
            self.partner = None

        self.children = [child for child in self.children if child.id != person.id]

class FamilyTre:
    def __init__(self):
        self.people = {}
        self.next_id = 1

    def add_person(self):
        name = input("Introducir nombre:\n")
        person = Person(self.next_id, name)
        self.people[self.next_id] = person
        self.next_id += 1
        print(f"{person.name} ha sido registrado con ID: {person.id}.")
        
        return person

    def delete_person(self, id: int):
        if id in self.people:
            person = self.people[id]
            print(f"Eliminando a {person.name}")
            for per in self.people.values():
                if person in per.children:
                    per.children.remove(person)
            if person.partner:
                person.partner.partner = None
            del self.people[id]
        else:
            print("ID no encontrado.")

    def get_id(self):
        if self.people:
            id = int(input("Indique el ID de la persona."))
            return id
        else:
            print("No hay personas registradas.")
            return

    def get_person(self, id: int):
        if id in self.people:
            return self.people[id]
        else:
            print(f"ID: {id}: No encontrado.")
            return None

    def display_people(self):
        for index, value in self.people.items():
            print(f"{index}: {value.name}")

    def print_tree(self, person: object):
        partner_name = person.partner.name if person.partner else "Sin Pareja"
        
        if person.children:
            children_names = ', '.join([child.name for  child in person.children])
            child_name = f"Hijo(s): {children_names}"
            
        else:
            child_name = f"Hijo(s): Sin hijos."

        print(f"Nombre: {person.name} - Pareja: {partner_name}\n"
            f"{child_name}")

    def verify_not_partner(self, person: object):
        for per in self.people.values():
            if person == per.partner:
                return False
            return True

    def verify_partner_not_sibilis(self, person: object, person2: object):
        for per in self.people.values():
            if person in per.children:
                if person2 in per.children:
                    return False
        return True

    def verify_not_parents(self, person: object, person2: object):
        if person in person2.children or person2 in person.children:
            return False
        return True

    def verify_not_has_parents(self, person: object):
        parents = 0
        for per in self.people.values():
            if person in per.children:
                parents += 1
        if parents > 2:
            return False
        return True

def main():
    
    tree = FamilyTre()
    
    print("\n ######### ÁRBOL GENEALÓGICO #########\n")
    while True:
        print("\n1. Añadir persona.\n"
            "2. Eliminar persona\n"
            "3. Establecer pareja.\n"
            "4. Añadir hijo.\n"
            "5. Mostrar árbol.\n"
            "6. Salir.")
        
        option = int(input("Elegir una opción.\n"))
        try:
            match option:
                case 1:
                    person = tree.add_person()
                case 2:
                    tree.display_people()
                    index = int(input("Indique indice de la persona a elegir.\n"))
                    person = tree.get_person(index)
                    tree.delete_person(person.id)
                case 3:
                    tree.display_people()
                    index = int(input("Indique indice de la persona a elegir.\n"))
                    person = tree.get_person(index)
                    if person is None:
                        print("ERROR: ID no valido.")
                        continue
                    index2 = int(input("Indique indice de la persona que sera su compañera.\n"))
                    person2 = tree.get_person(index2)
                    if person2 is None:
                        print("ERROR: ID no valido.")
                        continue
                    elif person.id == person2.id:
                        print("ERROR: Son la misma persona.")
                        continue
                    single = tree.verify_not_partner(person2)
                    not_sibilis = tree.verify_partner_not_child(person, person2)
                    not_child = tree.verify_not_parents(person, person2)
                    if single:
                        if not_sibilis:
                            if not_child:
                                person.set_partner(person2)
                            else:
                                print(f"{person.name} y {person2.name} tienen relación padre e hijo.")
                        else:
                            print(f"{person2.name} y {person.name} son hermanos.")
                            continue
                    else:
                        print(f"{person2.name} ya tiene otra pareja.")
                        continue
                    
                case 4:
                    tree.display_people()
                    index = int(input("Indique indice de la persona a elegir.\n"))
                    person = tree.get_person(index)
                    while True:
                        index2 = int(input("Indique indice de la persona del hijo.\n"))
                        if person.id == index2:
                            print("ERROR: Son la misma persona.")
                            continue
                        person2 = tree.get_person(index2)
                        has_parents = tree.verify_not_has_parents(person2)
                        if has_parents:
                            person.add_child(person2)
                        else:
                            print("No puede tener mas de dos padres.")
                        again = input("¿Añadir otro hijo?\n").lower()
                        if again != "si":
                            break
                case 5:
                    tree.display_people()
                    index = int(input("Indique indice de la persona.\n"))
                    person = tree.get_person(index)
                    tree.print_tree(person)
                case 6:
                    print("Cerrando el programa.")
                    break
        except ValueError as e:
            print(f"ERROR: {e}; Solo se admiten números.")
        print("\n")

main()