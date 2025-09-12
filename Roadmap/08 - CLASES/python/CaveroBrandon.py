"""EJERCICIO:
- Explora el concepto de clase y crea un ejemplo que implemente un inicializador, atributos y una función que los imprima (teniendo en cuenta las posibilidades de tu lenguaje).
- Una vez implementada, créala, establece sus parámetros, modifícalos e imprímelos utilizando su función.
"""


class Doctor:
    office = '101'

    def __init__(self, specialty, name, age):
        self.specialty = specialty
        self.name = name
        self.age = age

    def show_psychology_doctor(self):
        return (f"Psychology doctor's information:\n"
                f"Name: {self.name}\n"
                f"Age: {self.age}")

    def show_doctor(self):
        return (f"**************************************\n"
                f"{self.specialty} doctor's information:\n"
                f"Name: {self.name}\n"
                f"Age: {self.age}\n"
                f"Office: {self.office}")


def menu():
    print('**************************************\n'
          'Select the specialty: \n'
          '1. Psychology\n'
          '2. Traumatology\n'
          '3. Exit')
    try:
        option = int(input('Option: '))
        if option == 1:
            name = input('Name: ')
            age = input('Age: ')
            if age.isdigit():
                psychology_doctor = Doctor(specialty='Psychology',
                                           name=name,
                                           age=age)
                print(psychology_doctor.show_doctor())
            else:
                print('Try again, enter a correct value')
            menu()
        elif option == 2:
            name = input('Name: ')
            age = input('Age: ')
            if age.isdigit():
                traumatology_doctor = Doctor(specialty='Traumatology',
                                           name=name,
                                           age=age)
                print(traumatology_doctor.show_doctor())
            else:
                print('Try again, enter a correct value')
            menu()
        elif option == 3:
            pass
        else:
            print('Enter a correct option')
            menu()
    except ValueError:
        print('Enter a valid option')
        menu()


"""
DIFICULTAD EXTRA (opcional):
Implementa dos clases que representen las estructuras de Pila y Cola (estudiadas en el ejercicio número 7 de la ruta de estudio)
- Deben poder inicializarse y disponer de operaciones para añadir, eliminar, retornar el número de elementos e imprimir todo su contenido."""


def menu_stack():
    print('**************************************\n'
          'MENU FOR STACK: \n'
          '1. Append a value\n'
          '2. Remove a value\n'
          '3. Count elements\n'
          '4. Print all content\n'
          '5. Exit')
    try:
        option = int(input('Option: '))
        if option == 1:
            value = input('Enter the value: ')
            new_list.element_append(value)
            menu_stack()
        elif option == 2:
            new_list.remove_element()
            menu_stack()
        elif option == 3:
            print(f'The quantity of elements is: {new_list.element_count()}')
            menu_stack()
        elif option == 4:
            new_list.print_all()
            menu_stack()
        elif option == 5:
            pass
        else:
            print('Enter a correct option')
            menu_stack()
    except ValueError:
        print('Enter a valid option')
        menu_stack()


def menu_queue():
    print('**************************************\n'
          'MENU FOR QUEUE: \n'
          '1. Append a value\n'
          '2. Remove a value\n'
          '3. Count elements\n'
          '4. Print all content\n'
          '5. Exit')
    try:
        option = int(input('Option: '))
        if option == 1:
            value = input('Enter the value: ')
            new_queue.element_append(value)
            menu_queue()
        elif option == 2:
            new_queue.remove_element()
            menu_queue()
        elif option == 3:
            print(f'The quantity of elements is: {new_queue.element_count()}')
            menu_queue()
        elif option == 4:
            new_queue.print_all()
            menu_queue()
        elif option == 5:
            pass
        else:
            print('Enter a correct option')
            menu_queue()
    except ValueError:
        print('Enter a valid option')
        menu_queue()


class Stack:
    def __init__(self):
        self.stack = list()

    def element_append(self, element):
        self.stack.append(element)
        print(f'The list is {self.stack}')

    def remove_element(self):
        if len(self.stack) == 0:
            print('The list is empty, add at least one value first')
            return
        else:
            try:
                print(f'The current list is: {self.stack}')
                position_to_remove = int(input('Which position you want to remove: '))
                self.stack.pop(position_to_remove)
                print(f'The list after removing the element is: {self.stack}')
            except IndexError:
                print('The position does not exist, please try again')
                new_list.remove_element()
            except ValueError:
                print('Select a correct position')
                new_list.remove_element()

    def element_count(self):
        return len(self.stack)

    def print_all(self):
        copy_list = self.stack.copy()
        print('**** Recovering the information LIFO ****')
        print(f'The list is: {self.stack}')
        while len(copy_list) != 0:
            removed_value = copy_list.pop()
            print(f'The value recovered is \'{removed_value}\', the list is now: {copy_list}')


class Queue:
    def __init__(self):
        self.queue = list()

    def element_append(self, element):
        self.queue.append(element)
        print(f'The list is {self.queue}')

    def remove_element(self):
        if len(self.queue) == 0:
            print('The list is empty, add at least one value first')
            return
        else:
            try:
                print(f'The current list is: {self.queue}')
                position_to_remove = int(input('Which position you want to remove: '))
                self.queue.pop(position_to_remove)
                print(f'The list after removing the element is: {self.queue}')
            except IndexError:
                print('The position does not exist, please try again')
                new_queue.remove_element()
            except ValueError:
                print('Select a correct position')
                new_queue.remove_element()

    def element_count(self):
        return len(self.queue)

    def print_all(self):
        copy_list = self.queue.copy()
        print('**** Recovering the information FIFO ****')
        print(f'The list is: {self.queue}')
        while len(copy_list) != 0:
            removed_value = copy_list.pop(0)
            print(f'The value recovered is \'{removed_value}\', the list is now: {copy_list}')


new_list = Stack()
new_queue = Queue()

menu()
menu_stack()
menu_queue()
