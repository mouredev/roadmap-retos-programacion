#34 { Retos para Programadores } ÁRBOL GENEALÓGICO DE LA CASA DEL DRAGÓN 

# Bibliography reference:
# I use GPT as a reference and sometimes to correct or generate proper comments.

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
 *    - Modificar pareja e hijo
 * 2. Podrás imprimir el árbol (de la manera que consideres).
 * 
 * NOTA: Ten en cuenta que la complejidad puede ser alta si
 * se implementan todas las posibles relaciones. Intenta marcar
 * tus propias reglas y límites para que te resulte asumible.

"""


"""   Arbol Genealógico

Rey Viserys I Targaryen:
    Título: Rey de los Siete Reinos.
    Esposas:
        Aemma Arryn (madre de Rhaenyra y Aegon II).
        Alicent Hightower (madre de Aegon III, Aemond y otros).
    Hijos:
        Con Aemma Arryn:
            Rhaenyra Targaryen (heredera al trono).
            Aegon II Targaryen (rival de Rhaenyra).
        Con Alicent Hightower:
            Aegon III Targaryen.
            Aemond Targaryen.
        Otros hijos (como Daeron Targaryen).
Rhaenyra Targaryen:
    Título: Princesa de Dragonstone, heredera al trono.
    Esposo: Laenor Velaryon (hijo de Corlys Velaryon y Rhaenys Targaryen).
    Hijos: Joffrey Velaryon. Lucerys Velaryon. Jorah Velaryon.
Aegon II Targaryen:
    Título: Rey de los Siete Reinos (rival de Rhaenyra).
    Hijos: No se menciona que Aegon II tenga hijos legítimos en la serie.
Alicent Hightower:
    Título: Reina consorte.
    Hijos: Aegon III Targaryen. Aemond Targaryen. Daeron Targaryen (en algunas versiones de la historia).
    Familia: Proviene de la influyente Casa Hightower, que juega un papel importante en la política de Westeros.
Aemond Targaryen:
    Título: Príncipe de la Casa Targaryen.
    Hermanos: Aegon III y Daeron Targaryen.
Laenor Velaryon:
    Título: Príncipe de la Casa Velaryon.
    Esposa: Rhaenyra Targaryen.
    Hijos: Joffrey, Lucerys y Jorah Velaryon (aunque su paternidad es cuestionada). """

log = print

class Person:
    def __init__(self, id, name, mother='', father='', partners=None, childrens=None):
        self.id = id
        self.name = name
        self.mother = mother
        self.father = father
        self.partners = self.set_partners(partners)
        self.childrens = self.set_childrens(childrens)

    def set_partners(self, partners):
        if partners is None:
            return []  # Return an empty list if no partners are provided
        if isinstance(partners, list):
            return partners.copy()
        else:
            return [partners]

    def set_childrens(self, childrens):
        if childrens is None:
            return []  # Return an empty list if no children are provided
        if isinstance(childrens, list):
            return childrens.copy()
        else:
            return [childrens]

    def get_partners(self):
        return self.partners if self.partners else f"there's no partners for {self.name}"

    def get_childrens(self):
        return self.childrens if self.childrens else f"there's no childrens for {self.name}"


class GenealogyTree:
    def __init__(self, persons=None):
        if persons is None:
            persons = []
        self.persons = persons

    def add_person(self, person):
        if any(p.id == person.id for p in self.persons):
            print(f"The {person.name} is already added")
            return
        self.persons.append(person)

    def delete_person(self, person_id):
        index = next((i for i, p in enumerate(self.persons) if p.id == person_id), -1)
        if index == -1:
            print(f"The person with id {person_id} isn't already added")
            return
        self.persons.pop(index)

    def show_tree(self):
        for p in self.persons:
            print(f"ID: {p.id}, Name: {p.name}, Mother: {p.mother}, Father: {p.father}, "
                  f"Partners: {p.get_partners()}, Childrens: {p.get_childrens()}")


# Creating instances of Person
king = Person(1, 'Rey Viserys I Targaryen', '', '', ['Aemma Arryn', 'Alicent Hightower'],
              ['Rhaenyra Targaryen', 'Aegon II Targaryen', 'Aegon III Targaryen', 'Aemond Targaryen', 'Daeron Targaryen'])
princess = Person(2, 'Rhaenyra Targaryen', 'Aemma Arryn', 'Rey Viserys I Targaryen', ['Laenor Velaryon'],
                  ['Joffrey Velaryon', 'Lucerys Velaryon', 'Jorah Velaryon'])
king_aegon_ii = Person(3, 'Aegon II Targaryen', 'Aemma Arryn', 'Rey Viserys I Targaryen')
queen = Person(4, 'Alicent Hightower', '', '', ['Rey Viserys I Targaryen'],
               ['Aegon III Targaryen', 'Aemond Targaryen', 'Daeron Targaryen'])
prince_aemond = Person(5, 'Aemond Targaryen', '', '', [], [])
prince_laenor = Person(6, 'Laenor Velaryon', '', '', ['Rhaenyra Targaryen'],
                       ['Joffrey Velaryon', 'Lucerys Velaryon', 'Jorah Velaryon'])

# Creating the genealogy tree
dragon_house_tree = GenealogyTree([king, princess, king_aegon_ii, queen, prince_aemond, prince_laenor])

# Displaying the genealogy

# Displaying the genealogy tree
dragon_house_tree.show_tree()

# output:
"""   
ID: 1, Name: Rey Viserys I Targaryen, Mother: , Father: , Partners: ['Aemma Arryn', 'Alicent Hightower'], Childrens: ['Rhaenyra Targaryen', 'Aegon II Targaryen', 'Aegon III Targaryen', 'Aemond Targaryen', 'Daeron Targaryen']
ID: 2, Name: Rhaenyra Targaryen, Mother: Aemma Arryn, Father: Rey Viserys I Targaryen, Partners: ['Laenor Velaryon'], Childrens: ['Joffrey Velaryon', 'Lucerys Velaryon', 'Jorah Velaryon']
ID: 3, Name: Aegon II Targaryen, Mother: Aemma Arryn, Father: Rey Viserys I Targaryen, Partners: there's no partners for Aegon II Targaryen, Childrens: there's no childrens for Aegon II Targaryen
ID: 4, Name: Alicent Hightower, Mother: , Father: , Partners: ['Rey Viserys I Targaryen'], Childrens: ['Aegon III Targaryen', 'Aemond Targaryen', 'Daeron Targaryen']
ID: 5, Name: Aemond Targaryen, Mother: , Father: , Partners: there's no partners for Aemond Targaryen, Childrens: there's no childrens for Aemond Targaryen
ID: 6, Name: Laenor Velaryon, Mother: , Father: , Partners: ['Rhaenyra Targaryen'], Childrens: ['Joffrey Velaryon', 'Lucerys Velaryon', 'Jorah Velaryon']

"""