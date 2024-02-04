"""
 * EJERCICIO:
 * - Muestra ejemplos de asignación de variables "por valor" y "por referencia", según
 *   su tipo de dato.
 * - Muestra ejemplos de funciones con variables que se les pasan "por valor" y 
 *   "por referencia", y cómo se comportan en cada caso en el momento de ser modificadas.
 * (Entender estos conceptos es algo esencial en la gran mayoría de lenguajes)
"""

from typing import List, Union

# Por valor (inmutables)
number = 42
string = "Hola mundo!"
boolean = True

# Por referencia (mutables)
my_list = [1, 2, 3]
my_dict = {"Nombre": "Juan", "Apellido": "Herrera"}


# Función con parametros "por valor"
def elevate_value(value: Union[int, float], n: Union[int, float]):
    value **= n
    print(value)


print(number)
elevate_value(number, 2)
print(number)


# Función con parametros "por valor"
def elevate_values(container: List[Union[int, float]], n: Union[int, float]):
    for index, value in enumerate(container):
        container[index] = value**n

    print(container)


print(my_list)
elevate_values(my_list, 2)
print(my_list)

print("-----------------------------------------")

"""
 * DIFICULTAD EXTRA (opcional):
 * Crea dos programas que reciban dos parámetros (cada uno) definidos como variables anteriormente.
 * - Cada programa recibe, en un caso, dos parámetros por valor, y en otro caso, por referencia.
 *   Estos parámetros los intercambia entre ellos en su interior, los retorna, y su retorno
 *   se asigna a dos variables diferentes a las originales. A continuación, imprime el valor de las
 *   variables originales y las nuevas, comprobando que se ha invertido su valor en las segundas.
 *   Comprueba también que se ha conservado el valor original en las primeras.
"""


def are_values_equal(original_1, original_2, new_1, new_2):
    return original_1 == new_1 and original_2 == new_2


def swap_by_value(param_1, param_2):
    param_1, param_2 = param_2, param_1
    return param_1, param_2


value_1 = "Juan"
value_2 = "David"

print(value_1, value_2)
value_3, value_4 = swap_by_value(value_1, value_2)
print(value_1, value_2)
print(value_3, value_4)
print(
    "El valor de las variables originales fue invertido:",
    are_values_equal(value_1, value_2, value_3, value_4),
)
print("---------------------------")


def swap_by_reference(param_1, param_2):
    if len(param_1) == len(param_2):
        for index in range(len(param_1)):
            param_1[index], param_2[index] = param_2[index], param_1[index]
    return param_1, param_2


value_1 = ["Juan", "David"]
value_2 = ["Herrera", "Parra"]

print(value_1, value_2)
value_3, value_4 = swap_by_reference(value_1, value_2)
print(value_1, value_2)
print(value_3, value_4)
print(
    "El valor de las variables originales fue invertido:",
    are_values_equal(value_1, value_2, value_3, value_4),
)
