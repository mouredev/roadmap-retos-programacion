# 05 VALOR Y REFERENCIA

'''
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
'''

# Tipos de dato por valor

my_int_a = 10
my_int_b = my_int_a
# my_int_b = 20
# my_int_a = 30
print(my_int_a)
print(my_int_b)

# Tipos de dato por referencia

my_list_a = [10, 20]
my_list_b = my_list_a
my_list_b.append(30)
print(my_list_a)
print(my_list_b)

# Para que no suceda
my_list_a = [10, 20]
my_list_b = my_list_a.copy()
my_list_b.append(30)
print(my_list_a)
print(my_list_b)

'''
Funciones
'''

# Funciones datos por valor

my_int_c = 10

def my_int_func(my_int: int):
    my_int = 20
    print(my_int)

my_int_func(my_int_c)
print(my_int_c)

# Funciones datos por valor

my_list_c = [10, 20]

def my_list_func(my_list: list):
    my_list.append(30)
    print(my_list)

my_list_func(my_list_c)
print(my_list_c)

'''
-------
*Extra*
-------
'''

# Por valor
a_int = 10
b_int = 20

def changed(val_a: int, val_b: int):
    temp = val_a
    val_a = val_b
    val_b = temp
    return val_a, val_b

c_int, d_int = changed(a_int, b_int)
print(f'Originales: {a_int}-{b_int} <-> Cambiadas {c_int}-{d_int}')

# Por referencia

a_list = [10, 20]
b_list = [30, 40]

def changed(val_a: list, val_b: list):
    temp = val_a
    val_a = val_b
    val_b = temp
    return val_a, val_b

c_list, d_list = changed(a_list, b_list)
print(f'Originales: {a_list}-{b_list} <-> Cambiadas {c_list}-{d_list}')