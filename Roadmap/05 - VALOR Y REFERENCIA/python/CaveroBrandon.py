"""
- Muestra ejemplos de asignación de variables "por valor" y "por referencia", según su tipo de dato.
- Muestra ejemplos de funciones con variables que se les pasan "por valor" y "por referencia",
 y cómo se comportan en cada caso en el momento de ser modificadas
"""


def assigning_by_value():
    print('**** Assigning by value ****')
    message = 'Hello'
    greetings = message
    message = 'New message'

    print('Message:', message)
    print('Greetings:', greetings)
    print('Greetings is not affected by the change in message because both values are assigned by value')


def assigning_by_reference():
    print('\n**** Assigning by reference ****')
    list_numbers = [1, 2, 3]
    second_list_numbers = list_numbers
    list_numbers.append(4)

    print('List_numbers:', list_numbers)
    print('Second_list_numbers:', second_list_numbers)
    print('Both list are affected by the change in the first list because the value is assigned by reference')


def function_with_argument_assigned_by_value(value1):
    print('\n**** Function with assignment by value ****')
    print("Value previous to modification:", value1)
    value1 = 42
    print("Value after the modification, in the function:", value1)


def function_with_argument_assigned_by_reference(list1):
    print('\n**** Function with assignment by reference ****')
    print("List previous to modification:", list1)
    list1.append(4)
    print("List after the modification, in the function:", list1)


def function_that_exchanges_values_by_value(value1, value2):
    new_value_1 = value2
    new_value_2 = value1

    return new_value_1, new_value_2


def function_that_exchanges_values_by_reference(list1, list2):
    temp_list = list1
    new_list_1 = list2
    new_list_2 = temp_list

    return new_list_1, new_list_2


assigning_by_value()
assigning_by_reference()

number = 10
function_with_argument_assigned_by_value(number)
print("Original value after executing the function:", number)

number_list = [1, 2, 3]
function_with_argument_assigned_by_reference(number_list)
print("Original list after executing the function:", number_list)


""" * DIFICULTAD EXTRA (opcional):
- Crea dos programas que reciban dos parámetros (cada uno) definidos como variables anteriormente.
- Cada programa recibe, en un caso, dos parámetros por valor, y en otro caso, por referencia.
- Estos parámetros los intercambia entre ellos en su interior, los retorna, y su retorno se asigna a dos variables diferentes a las originales. 
A continuación, imprime el valor de las variables originales y las nuevas, comprobando que se ha invertido su valor en las segundas. 
- Comprueba también que se ha conservado el valor original en las primeras.
"""

value1 = 10
value2 = 20

new_value_1, new_value_2 = function_that_exchanges_values_by_value(value1, value2)
print(f"\nThe original values are: value_1 = {value1} and value_2 = {value2}")
print(f"The exchanged values are value_1 = {new_value_1} and value_2 = {new_value_2}")


list1 = [1, 2, 3, 4]
list2 = [5, 6, 7]
new_list_1, new_list_2 = function_that_exchanges_values_by_reference(list1, list2)
print(f"\nThe original list are: list_1 = {list1} and value_2 = {list2}")
print(f"The exchanged values are list_1 = {new_list_1} and value_2 = {new_list_2}")
