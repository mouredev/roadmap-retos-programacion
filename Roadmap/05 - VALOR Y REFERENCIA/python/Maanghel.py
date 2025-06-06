"""
EJERCICIO:
- Muestra ejemplos de asignación de variables "por valor" y "por referencia", según
    su tipo de dato.
- Muestra ejemplos de funciones con variables que se les pasan "por valor" y 
    "por referencia", y cómo se comportan en cada caso en el momento de ser modificadas.
(Entender estos conceptos es algo esencial en la gran mayoría de lenguajes)

DIFICULTAD EXTRA (opcional):
Crea dos programas que reciban dos parámetros (cada uno) definidos como variables anteriormente.
- Cada programa recibe, en un caso, dos parámetros por valor, y en otro caso, por referencia.
    parámetros los intercambia entre ellos en su interior, los retorna, y su retorno
    se asigna a dos variables diferentes a las originales. A continuación, imprime el valor de las
    variables originales y las nuevas, comprobando que se ha invertido su valor en las segundas.
    Comprueba también que se ha conservado el valor original en las primeras.
"""

# asignacion "por valor", los tipos de datos primitivos en Python se asignan por valor
my_int = 10
my_string = "Hola"
my_float = 3.14
my_bool = True
my_copy_int = my_int
my_copy_string = my_string
my_copy_float = my_float
my_copy_bool = my_bool

# asignacion "por referencia, los tipos de datos compuestos en Python se asignan por referencia"
my_list = [1, 2, 3]
my_dict = {"a": 1, "b": 2}
my_set = {1, 2, 3}
my_list_ref = my_list
my_dict_ref = my_dict
my_set_ref = my_set

# Funciones con datos por valor
def modify_value(value):
    value += 10
    return value

# Funciones con datos por referencia
def modify_reference(ref):
    ref.append(4)
    return ref

# Prueba de funciones con datos por valor
print("Antes de modificar por valor:")
print(f"my_copy_int: {my_copy_int}")
my_copy_int = modify_value(my_copy_int)
print("Después de modificar por valor:")
print(f"my_copy_int: {my_copy_int}")

# Prueba de funciones con datos por referencia
print("\nAntes de modificar por referencia:")
print(f"my_list_ref: {my_list_ref}")
my_list_ref = modify_reference(my_list_ref)
print("Después de modificar por referencia:")
print(f"my_list_ref: {my_list_ref}")

# EXTRA

# Función para intercambiar valores por valor
def swap_by_value(copy_a, copy_b):
    """
    Intercambia los valores de dos variables primitivas (por valor).
    No afecta las variables originales fuera de la función.
    """
    copy_a, copy_b = copy_b, copy_a
    return copy_a, copy_b

# Función para intercambiar valores por referencia
def swap_by_reference(ref_a, ref_b):
    """
    Intercambia los primeros elementos de dos listas (por referencia).
    Afecta las listas originales fuera de la función.
    """
    ref_a[0], ref_b[0] = ref_b[0], ref_a[0]
    return ref_a, ref_b

# Intercambio de valores por valor
first_num = 1
second_num = 2
new_first_num, new_second_num = swap_by_value(first_num, second_num)
print("\nVariables originales:")
print(f"{first_num}\n{second_num}")
print("Nuevas variables:")
print(f"{new_first_num}\n{new_second_num}")

# Intercambio de valores por referencia
first_list = [1, 2]
second_list = [3, 4]
new_first_list, new_second_list = swap_by_reference(first_list, second_list)
print("\nVariables originales:")
print(f"{first_list}\n{second_list}")
print("Nuevas variables:")
print(f"{new_first_list}\n{new_second_list}")