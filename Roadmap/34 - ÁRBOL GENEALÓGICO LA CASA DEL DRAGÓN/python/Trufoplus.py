class Person:
    def __init__(self, id, name):
        self.id = id
        self.name = name 
        self.couple = None
        self.childs = []

    def relationships(self, couple):
        if self.couple:
            print(f'{self.name} ya tiene una pareja: {self.couple.name}.')
        else:
            self.couple = couple
            couple.couple = self  # Asegura que la relación sea mutua

    def add_child(self, child):
        if child in self.childs:
            print(f'{self.name} ya tiene a {child.name} como hijo.')
        else:
            self.childs.append(child)
            
    def delete_child(self, child):
        if child in self.childs:
            self.childs.remove(child)
        else:
            print(f'{child.name} no es hijo de {self.name}.')

    def delete_couple(self):
        if self.couple:
            print(f'{self.name} se ha separado de {self.couple.name}.')
            self.couple.couple = None  # Rompe la relación mutua
            self.couple = None
        else:
            print(f'{self.name} no tiene ninguna pareja.')
    
    def print_tree(self, level=0):
        print(' ' * level * 4 + f"{self.name}")
        if self.couple:
            print(' ' * level * 4 + f"  Pareja: {self.couple.name}")
        if self.childs:
            print(' ' * level * 4 + f"  Hijos: ")
            for child in self.childs:
                child.print_tree(level + 1)   
            
def create_person(id, name):
    return Person(id, name)        

def establish_childs(father, mother, child):
    father.add_child(child)
    mother.add_child(child)



# Personas de la casa del dragon
aemon = create_person(2, 'Aemon Targaryen')
jocelyn = create_person(1, 'Jocelyn Baratheon')
rhaenys = create_person(3, 'Rhaenys Targaryen')
corlys = create_person(4, 'Corlys Velaryon')
loena = create_person(5, 'Loena Velaryon')
laenor = create_person(6, 'Laenor Velaryon')
daemon = create_person(7, 'Daemon Targaryen')
baela = create_person(8, 'Baela Targaryen')
rhaena = create_person(9, 'Rhaena Targaryen')
rhaenyra = create_person(10, 'Rhaenyra Targaryen')
jacaerys = create_person(11, 'jacaerys Velarion')
lucerys = create_person(12, 'Lucerys Velarion')
joffrey = create_person(13, 'Joffrey Velarion')


# Establecionda las relaciones
aemon.relationships(jocelyn)
establish_childs(aemon, jocelyn, rhaenys)

rhaenys.relationships(corlys)
establish_childs(corlys, rhaenys, loena)
establish_childs(corlys, rhaenys, laenor)

daemon.relationships(loena)
establish_childs(daemon, loena, baela)
establish_childs(daemon, loena, rhaena)

rhaenyra.relationships(laenor)
establish_childs(laenor, rhaenyra, jacaerys)
establish_childs(laenor, rhaenyra, lucerys)
establish_childs(laenor, rhaenyra, joffrey)


# Imprimir el árbol genealógico
aemon.print_tree()


