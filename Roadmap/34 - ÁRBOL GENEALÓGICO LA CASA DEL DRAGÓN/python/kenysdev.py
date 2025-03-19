# ╔═════════════════════════════════════╗
# ║ Autor:  Kenys Alvarado              ║
# ║ GitHub: https: github.com/Kenysdev  ║
# ║ 2024 -  Python                      ║
# ╚═════════════════════════════════════╝

# -------------------------------------------
# #34 ÁRBOL GENEALÓGICO DE LA CASA DEL DRAGÓN
# -------------------------------------------
#  * ¡La Casa del Dragón ha finalizado y no volverá hasta 2026!
#  * ¿Alguien se entera de todas las relaciones de parentesco
#  * entre personajes que aparecen en la saga?
#  * Desarrolla un árbol genealógico para relacionarlos (o invéntalo).
#  * Requisitos:
#  * 1. Estará formado por personas con las siguientes propiedades:
#  *    - id_entificador único (obligatorio)
#  *    - Nombre (obligatorio)
#  *    - Pareja (opcional)
#  *    - Hijos (opcional)
#  * 2. Una persona sólo puede tener una pareja (para simplificarlo).
#  * 3. Las relaciones deben valid_arse dentro de lo posible.
#  *    Ejemplo: Un hijo no puede tener tres padres.
#  * Acciones:
#  * 1. Crea un programa que permita crear y modificar el árbol.
#  *    - Añadir y eliminar personas
#  *    - Modificar pareja e hijos
#  * 2. Podrás imprimir el árbol (de la manera que consid_eres).
#  *
#  * NOTA: Ten en cuenta que la complejid_ad puede ser alta si
#  * se implementan todas las posibles relaciones. Intenta marcar
#  * tus propias reglas y límites para que te resulte asumible.

# NOTE: Here is the 'people.json' file with the data if you want to test it:
#       https://pastebin.com/29kWWgPU
#       Just paste it into the base folder where file.py is located.

import json
from typing import List, Optional, Dict, Tuple

# ________________________
class Input:
    def input_str(self, msg: str) -> str:
        while True:
            txt: str = input(msg)
            if len(txt) > 0:
                return txt
            
            print("\n❌ This field cannot be empty.")

    def input_int(self, msg: str) -> int:
        while True:
            txt: str = self.input_str(msg)
            if txt.isdigit():
                return int(txt)
            print("\n❌ Enter an integer.")

# ________________________
class Person:
    def __init__(self, id: int, name: str):
        self.id = id
        self.name = name
        self.parents: List[int] = []
        self.partners: List[int] = []
        self.children: Dict[int, List[int]] = {}
        self.deleted: bool = False

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "parents": self.parents,
            "partners": self.partners,
            "children": self.children,
            "deleted": self.deleted
        }

    @classmethod
    def from_dict(cls, data: dict):
        person = cls(data['id'], data['name'])
        person.parents = data.get('parents', [])
        person.partners = data.get('partners', [])
        person.children = {int(k): v for k, v in data.get('children', {}).items()}
        person.deleted = data.get('deleted', False)
        return person

    def __repr__(self) -> str:
        return f"Person(id={self.id}, name='{self.name}')"

# ________________________
class People(Input):
    def __init__(self, filename: str = "people.json") -> None:
        self._people: List[Person] = []
        self._filename = filename
        self.load_from_json()

    def get_people(self) -> List[Person]:
        return self._people

    def load_from_json(self) -> None:
        try:
            with open(self._filename, "r") as f:
                data = json.load(f)
                self._people = []
                for person_data in data:
                    person = Person.from_dict(person_data)
                    self._people.append(person)
                    
                print(f"✅ The file '{self._filename}' has been successfully loaded.")
        except Exception:
            print(
                f"⚠️ The file '{self._filename}' not found. Starting with an empty list."
            )
            self._people = []
            self._people.append(Person(id=0, name="unknown"))

    def save_to_json(self) -> None:
        try:
            data = [person.to_dict() for person in self._people]
            with open(self._filename, "w") as f:
                json.dump(data, f, indent=2)
            print(f"✅ Data saved successfully to {self._filename}")
        except Exception as e:
            print(
                f"❌ An error occurred while saving to '{self._filename}': {e}. Data may not have been saved."
            )

    def print_people(self) -> None:
        print(f"{'_' * 32}\n|{'id'.center(4)}|{'Name'.center(25)}|\n{'_' * 32}")
        for person in self._people:
            if not person.deleted:
                print(
                    f"|{str(person.id).center(4)}|{str(person.name).center(25):<25}|"
                )
            # optional:
            # else:
            #    print(f"id: {person.id:<4}, This person was deleted.")
        print("_" * 32)

    def get_person_by_id_(self, id_: int) -> Optional[Person]:
        if 0 <= id_ < len(self._people):
            return self._people[id_]
        else:
            print("❌ id not found.")
            return None

    def add_person(self) -> None:
        print("Add Person or 'x' to Exit")
        name = self.input_str("Name: ")
        if name.lower() == "x":
            print("Exit")
            return

        new_id = max([person.id for person in self._people], default=-1) + 1
        new_person = Person(id=new_id, name=name)
        self._people.append(new_person)
        print(f"✅ Added: {new_person}")
        self.save_to_json()

    def remove_person(self) -> None:
        self.print_people()
        print("\nPerson ID to mark as deleted or a letter to exit.")
        id_: str = self.input_str("ID: ")
        if not id_.isdigit():
            print("Exit")
            return

        person = self.get_person_by_id_(int(id_))
        if not person:
            return

        if person.partners or person.parents:
            print("❌ You cannot delete a person who is linked to parents or partners.")
            return

        person.deleted = True
        print(f"✅ '{person.name}' is marked as deleted.")
        self.save_to_json()

    def __len__(self) -> int:
        return len(self._people)

# ________________________
class Partners(People):
    def __add(self, partners: list, id_person: int):
        print("Select Partner ID")
        id_partner: int = self.input_int("ID: ")
        partner = self.get_person_by_id_(id_partner)
        if not partner or partner.deleted:
            print("❌ ID not found or the person is deleted.")
            return

        if id_partner in partners:
            print("❌ This partner is already added.")
            return

        partners.append(id_partner)
        partner.partners.append(id_person)

        print("✅ Partner successfully added.")
        self.save_to_json()

    def __remove(self, partners: list, id_person: int):
        print("Select Partner ID to Delete")
        id_: int = self.input_int("ID: ")
        if id_ not in partners:
            print("❌ ID not found.")
            return

        partner = self.get_person_by_id_(id_)
        if not partner:
            print("❌ Partner not found.")
            return

        if partner.children:
            print("❌ Cannot delete a partner who has children.")
            return

        partners.remove(id_)
        partner.partners.remove(id_person)

        print("✅ Partner deleted")
        self.save_to_json()

    def __options(self, partners: list, id_person: int):
        print("\n1. Add partner | 2. Remove partner | 3. Exit")
        option: int = self.input_int("\nOption: ")

        if option == 1:
            self.__add(partners, id_person)

        elif option == 2:
            self.__remove(partners, id_person)

        elif option == 3:
            return

        else:
            print("❌ Invalid option.")

    def edit_partners(self):
        self.print_people()
        print("\nPerson ID to edit partners or a letter to exit.")
        id_s: str = self.input_str("ID: ")
        if not id_s.isdigit():
            print("Exit")
            return

        id_: int = int(id_s)
        person = self.get_person_by_id_(id_)
        if not person or person.deleted:
            print("❌ ID not found or the person is deleted.")
            return

        print(f"You selected '{person.name}'")
        partners = person.partners

        if partners:
            print("Partners:")
            for id_p in partners:
                partner = self.get_person_by_id_(id_p)
                if partner:
                    print(f"ID: {partner.id} -> {partner.name}")
        else:
            print("🚫 This person has no partners.")

        self.__options(partners, id_)

# ________________________
class Children(People):
    def __init__(self, filename: str = "people.json") -> None:
        super().__init__(filename)
        self.__id_parent: int
        self.__children: dict
        self.__id_child: int
        self.__parents: list
        self.__id_partner: int

    def __select_partner(self, partners: list) -> Optional[int]:
        print("Partners:")
        for id_p in partners:
            partner = self.get_person_by_id_(id_p)
            if partner:
                print(f"ID: {partner.id} -> {partner.name}")

        print("Select the ID of the partner with whom you have the child.")
        id_partner: int = self.input_int("ID: ")
        partner = self.get_person_by_id_(id_partner)
        if id_partner not in partners or not partner or partner.deleted:
            print("❌ ID not found or the person is deleted.")
            return

        return id_partner

    def __update_child_parent(self) -> Optional[int]:
        id_partner: int = self.__id_partner
        print("Select Child ID")
        id_child: int = self.input_int("ID: ")
        child = self.get_person_by_id_(id_child)
        if not child:
            print("❌ ID not found.")
            return

        if child.parents:
            print("❌ This person already has parents.")
            return

        if id_partner in self.__children:
            if id_child not in self.__children[id_partner]:
                self.__children[id_partner].append(id_child)
        else:
            self.__children[id_partner] = [id_child]

        parent = self.get_person_by_id_(self.__id_parent)
        if parent:
            parent.children = self.__children

        child.parents = [self.__id_parent, id_partner]

        return id_child

    def __update_child_partner(self, partner: Person) -> None:
        if self.__id_parent in partner.children:
            if self.__id_child not in partner.children[self.__id_parent]:
                partner.children[self.__id_parent].append(self.__id_child)
        else:
            partner.children[self.__id_parent] = [self.__id_child]

    def __add(self) -> None:
        id_parent: int = self.__id_parent
        parent = self.get_person_by_id_(id_parent)
        if not parent:
            print("❌ Parent not found.")
            return

        partners = parent.partners
        if not partners:
            print("❌ This person does not have a partner with whom to have children.")
            return

        id_partner = self.__select_partner(partners)
        if not id_partner:
            return

        partner = self.get_person_by_id_(id_partner)
        if not partner:
            print("❌ Partner not found.")
            return

        self.__id_partner = id_partner
        id_child = self.__update_child_parent()
        if id_child is None:
            return

        self.__id_child = id_child
        self.__update_child_partner(partner)

        print("✅ Child successfully added.")
        self.save_to_json()

    def __remove_and_update(self, id_parent: int, id_partner: int) -> None:
        parent = self.get_person_by_id_(id_parent)
        if not parent:
            print("❌ Parent not found.")
            return

        children_with_partner = parent.children.get(id_partner, [])
        if self.__id_child in children_with_partner:
            children_with_partner.remove(self.__id_child)
            if not children_with_partner:
                del parent.children[id_partner]
            else:
                parent.children[id_partner] = children_with_partner

        child = self.get_person_by_id_(self.__id_child)
        if child:
            child.parents.remove(id_parent)

        print("✅ Child deleted")
        self.save_to_json()

    def __remove(self) -> None:
        print("Select Child ID to Delete")
        self.__id_child = self.input_int("ID: ")
        child = self.get_person_by_id_(self.__id_child)
        if not child:
            print("❌ Child not found.")
            return

        parents = child.parents
        if len(parents) != 2:
            print("❌ Child does not have two parents.")
            return

        self.__parents = parents
        id_p1, id_p2 = parents
        self.__remove_and_update(id_p1, id_p2)
        self.__remove_and_update(id_p2, id_p1)

    def __options(self) -> None:
        print("\n1. Add child | 2. Remove child | 3. Exit")
        option: int = self.input_int("\nOption: ")

        if option == 1:
            self.__add()

        elif option == 2:
            self.__remove()

        elif option == 3:
            return

        else:
            print("❌ Invalid option.")

    def edit_children(self) -> None:
        self.print_people()
        print("\nPerson ID to edit Children or a letter to exit.")
        id_s: str = self.input_str("ID: ")
        if not id_s.isdigit():
            print("Exit")
            return

        id_: int = int(id_s)
        parent = self.get_person_by_id_(id_)
        if not parent or parent.deleted:
            print("❌ ID not found or the person is deleted.")
            return

        print(f"You selected '{parent.name}'")
        children = parent.children
        if children:
            print("Children:")
            for partner_id, child_ids in children.items():
                partner = self.get_person_by_id_(partner_id)
                partner_name = partner.name if partner else "Unknown"
                print(f"With ID: {partner_id} -> '{partner_name}':")
                for child_id in child_ids:
                    child = self.get_person_by_id_(child_id)
                    child_name = child.name if child else "Unknown"
                    print(f"    ID: {child_id} -> '{child_name}'")
        else:
            print("🚫 This person has no children.")

        self.__id_parent = id_
        self.__children = children
        self.__options()

# ________________________
class Tree(People):
    def __filtered_grandparents(self) -> Tuple[List[Person], List[Person]]:
        grandparents = []
        no_partner = []

        for person in self.get_people():
            if (
                not person.parents
                and not person.deleted
                and person.name != "unknown"
            ):
                partners = person.partners
                if not partners:
                    no_partner.append(person)
                    continue

                has_grandparent_partner = False
                for partner_id in partners:
                    partner = self.get_person_by_id_(partner_id)
                    if partner and partner in grandparents:
                        has_grandparent_partner = True
                        break

                if not has_grandparent_partner:
                    grandparents.append(person)

        return grandparents, no_partner

    def __print_child(self, children: list, px: str, is_last: bool, is_root: bool) -> None:
        for j, child_id in enumerate(children):
            is_last_child = j == len(children) - 1
            new_prefix = px
            if not is_root:
                new_prefix = px[:-4] + ("    " if is_last else "│   ")

            self.__print_family(
                child_id,
                new_prefix + ("└── " if is_last_child else "├── "),
                is_last_child,
                False,
            )

    def __print_parents(self, id_: int, partners: list, px: str, is_last: bool, is_root: bool) -> None:
        for partner_id in partners:
            partner = self.get_person_by_id_(partner_id)
            if partner:
                print(f"{px}💑 With: {partner.name} (ID: {partner.id})")
                children = partner.children.get(id_, [])
                if children:
                    self.__print_child(children, px, is_last, is_root)
                else:
                    print(f"{px}└── 🚫 Without children")

    def __print_family(self, id_: int, px="", is_last=False, is_root=True) -> None:
        person = self.get_person_by_id_(id_)
        if not person:
            return

        print(f"{px}🙂 {person.name} (ID: {person.id})")

        partners = person.partners
        if isinstance(partners, list) and partners:
            if not is_root:
                px = px[:-4] + ("    " if is_last else "│   ")

            self.__print_parents(id_, partners, px, is_last, is_root)
            if not is_last:
                print(px)

    def print_tree(self): 
        grandparents, no_partner = self.__filtered_grandparents()

        if not grandparents and not no_partner:
            print("⚠️ No users are registered.")
            return

        if no_partner:
            print("__________\nParents unknown, without descendants and without a partner:")
            for p in no_partner:
                print(f"😐 {p.name}")

        print()      
        for i, person in enumerate(grandparents):
            print(f"__________\nFamily #{i+1}")
            self.__print_family(person.id)

# ________________________
class Program(Tree, Partners, Children):
    MENU = """
---------------------------------------------
| 1. Add person     | 4. Edit children      |  
| 2. Remove person  | 5. Print tree         |
| 3. edit partners  | 6. Salir              |
---------------------------------------------"""

    def run(self):
        # self.test()
        while True:
            print(Program.MENU)
            option: int = self.input_int("\nOption: ")
            match option:
                case 1:
                    self.add_person()
                case 2:
                    self.remove_person()
                case 3:
                    self.edit_partners()
                case 4:
                    self.edit_children()
                case 5:
                    self.print_tree()
                case 6:
                    print("Bye")
                    break
                case _:
                    print("❌ Invalid option.")

# ________________________
if __name__ == "__main__":
    _program = Program()
    _program.run()

