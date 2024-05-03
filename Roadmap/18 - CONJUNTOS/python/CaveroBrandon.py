"""Utilizando tu lenguaje crea un conjunto de datos y realiza las siguientes
operaciones (debes utilizar una estructura que las soporte):
- Añade un elemento al final.
- Añade un elemento al principio.
- Añade varios elementos en bloque al final.
- Añade varios elementos en bloque en una posición concreta.
- Elimina un elemento en una posición concreta.
- Actualiza el valor de un elemento en una posición concreta.
- Comprueba si un elemento está en un conjunto."""


class DataCollection:
    def __init__(self):
        self.my_list = list()

    def show_list(self):
        print(self.my_list)

    def add_an_element_to_the_end(self, element):
        self.my_list.append(element)
        self.show_list()

    def add_an_element_to_the_beginning(self, element):
        self.my_list.insert(0, element)
        self.show_list()

    def add_multiple_elements_to_the_end(self, *args):
        elements_to_add = list(args)
        self.my_list.extend(elements_to_add)
        self.show_list()

    def add_multiple_elements_to_the_beginning(self, *args):
        elements_to_add = list(args)
        self.my_list[:0] = elements_to_add
        self.show_list()

    def add_multiple_elements_to_a_given_position(self, position: int, *args):
        elements_to_add = list(args)
        self.my_list[position:position] = elements_to_add
        self.show_list()

    def remove_elements_from_a_given_position(self, position: int):
        self.my_list.pop(position)
        self.show_list()

    def update_element_given_a_position(self, position: int, new_value):
        self.my_list[position] = new_value
        self.show_list()

    def verify_that_an_element_is_available(self, element) -> bool:
        if element not in self.my_list:
            return False
        return True

    def convert_list_to_a_set(self):
        my_set = set(self.my_list)
        print(my_set)

    def remove_all_content(self):
        self.my_list = []
        self.show_list()

"""DIFICULTAD EXTRA (opcional): 
Muestra ejemplos de las siguientes operaciones con conjuntos:
- Unión.
- Intersección.
- Diferencia.
- Diferencia simétrica."""


def set_union():
    set_a = {1, 2, 3, 4}
    set_b = {2, 3, 4, 5}
    set_result = set_a | set_b
    print(f'{set_a} Union {set_b} = {set_result}')


def set_intersection():
    set_a = {1, 2, 3, 4}
    set_b = {2, 3, 4, 5}
    set_result = set_a & set_b
    print(f'{set_a} Intersection {set_b} = {set_result}')


def set_difference():
    set_a = {1, 2, 3, 4}
    set_b = {2, 3, 4, 5}
    set_result = set_a - set_b
    print(f'{set_a} Difference {set_b} = {set_result}')


def set_symmetric_difference():
    set_a = {1, 2, 3, 4}
    set_b = {2, 3, 4, 5}
    set_result = set_a ^ set_b
    print(f'{set_a} Symmetric Difference {set_b} = {set_result}')


my_collection = DataCollection()

my_collection.add_an_element_to_the_end(100)
my_collection.add_an_element_to_the_beginning(2)
my_collection.add_multiple_elements_to_the_end(10, 20, 30)
my_collection.add_multiple_elements_to_the_beginning(1, 2, 3)
my_collection.add_multiple_elements_to_a_given_position(2, 11, 22, 33)
my_collection.remove_elements_from_a_given_position(3)
my_collection.update_element_given_a_position(3, 'x')
print(my_collection.verify_that_an_element_is_available('x'))
my_collection.convert_list_to_a_set()

print('\n**** EXTRA ****')
set_union()
set_intersection()
set_difference()
set_symmetric_difference()
