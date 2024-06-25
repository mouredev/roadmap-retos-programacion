"""
 * EJERCICIO:
 * - Muestra ejemplos de asignación de variables "por valor" y "por referencia", según
 *   su tipo de dato.
 * - Muestra ejemplos de funciones con variables que se les pasan "por valor" y 
 *   "por referencia", y cómo se comportan en cada caso en el momento de ser modificadas.
 * (Entender estos conceptos es algo esencial en la gran mayoría de lenguajes)
 *
 * DIFICULTAD EXTRA (opcional):
 * Crea dos programas que reciban dos parámetros (cada uno) definidos como variables anteriormente.
 * - Cada programa recibe, en un caso, dos parámetros por valor, y en otro caso, por referencia.
 *   Estos parámetros los intercambia entre ellos en su interior, los retorna, y su retorno
 *   se asigna a dos variables diferentes a las originales. A continuación, imprime el valor de las
 *   variables originales y las nuevas, comprobando que se ha invertido su valor en las segundas.
 *   Comprueba también que se ha conservado el valor original en las primeras.
"""

# Asignación por valor

number_a = 11
number_b = number_a
print("number_a:", number_a)  # 11
print("number_b:", number_b)  # 11
number_b = 7
print("number_a:", number_a)  # 11
print("number_b:", number_b)  # 7

# Asignación por referencia

list_a = [1, 2, 3, 4]
list_b = list_a
print("list_a:", list_a)  # [1, 2, 3, 4]
print("list_b:", list_b)  # [1, 2, 3, 4]
list_b.append(5)
print("list_a:", list_a)  # [1, 2, 3, 4, 5]
print("list_b:", list_b)  # [1, 2, 3, 4, 5]


# Funciones por valor


def print_double(number: int) -> None:
    number *= 2
    print(number)


my_number = 2
print_double(my_number)  # 4
print(my_number)  # 2


# Funciones por referencia


def print_append_number(arr: list, num: int) -> None:
    arr.append(num)
    print("List inside function:", arr)


my_arr = [1, 2, 3, 4]
print_append_number(my_arr, 5)  # [1, 2, 3, 4, 5]
print("List outside function:", my_arr)  # [1, 2, 3, 4, 5]


"""
 * DIFICULTAD EXTRA (opcional):
 * Crea dos programas que reciban dos parámetros (cada uno) definidos como variables anteriormente.
 * - Cada programa recibe, en un caso, dos parámetros por valor, y en otro caso, por referencia.
 *   Estos parámetros los intercambia entre ellos en su interior, los retorna, y su retorno
 *   se asigna a dos variables diferentes a las originales. A continuación, imprime el valor de las
 *   variables originales y las nuevas, comprobando que se ha invertido su valor en las segundas.
 *   Comprueba también que se ha conservado el valor original en las primeras.
"""


def exchange_by_value(val_one: int, val_two: int) -> tuple[int]:
    val_one, val_two = val_two, val_one
    return val_one, val_two


first_value = 11
second_value = 7
val_1, val_2 = exchange_by_value(first_value, second_value)
print(f"\n1.1. Before function: {first_value}    After function: {val_1}")
# 1.1. Before function: 11    After function: 7
print(f"1.2. Before function: {second_value}     After function: {val_2}")
# 1.2. Before function: 7     After function: 11


def exchange_by_reference(arr_one: list, arr_two: list) -> tuple[list]:
    arr_one, arr_two = [*arr_two], [*arr_one]
    return arr_one, arr_two


first_list = [1, 2, 3, 4]
second_list = [9, 8, 7, 6]
list_1, list_2 = exchange_by_reference(first_list, second_list)
print(f"\n2.1 Before function: {first_list}    After function: {list_1}")
# 2.1 Before function: [1, 2, 3, 4]    After function: [9, 8, 7, 6]
print(f"2.2 Before function: {second_list}    After function: {list_2}")
# 2.2 Before function: [9, 8, 7, 6]    After function: [1, 2, 3, 4]
