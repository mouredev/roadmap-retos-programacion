""" 
/*
 * EJERCICIO:
 * - Muestra ejemplos de asignación de variables "por valor" y "por referencia", según
 *   su tipo de dato.
 * - Muestra ejemplos de funciones con variables que se les pasan "por valor" y 
 *   "por referencia", y cómo se comportan en cada caso en el momento de ser modificadas.
 * (Entender estos conceptos es algo esencial en la gran mayoría de lenguajes)
 */
"""
""" 
    Paso por valor: Se crea una copia local de la variable dentro de la función.
    Paso por referencia: Se maneja directamente la variable, los cambios realizados dentro de la función le afectarán también fuera.

    Los tipos simples se pasan por valor: Enteros, flotantes, cadenas, lógicos...
    Los tipos compuestos se pasan por referencia: Listas, diccionarios, conjuntos...

"""

# Paso por valor
a = 5
b = 10
print(f'a={a}')
print(f'b={b}')
print(f'La direccion de memoria de a = {id(a)}')
print(f'La direccion de memoria de b = {id(b)}')
b = a 
print(f'Valor de b luego de igualar a "a" = {b}')
print(f'La direccion de memoria de a = {id(a)}')
print(f'La direccion de memoria de b luego de igualar a "a" = {id(b)}')
a += 2
print(f'Valor de a luego de sumar 2 = {a}')
print(f'La direccion de memoria de a luego de sumar 2 = {id(a)}')
print(f'Valor de b luego de sumar 2 a "a" = {b}')
print(f'La direccion de memoria de b luego de sumar 2 a "a" = {id(b)}')

b += 3
print(f'Valor de b luego de sumar 3 = {b}')
print(f'La direccion de memoria de b luego de sumar 3 = {id(b)}')
print()
# Paso por referencia
list_a = [1,2,3]
list_b = [2,3,4]
print(f'Lista a = {list_a}')
print(f'Lista b = {list_b}')
print(f'Direccion de memoria de lista a = {id(list_a)}')
print(f'Direccion de memoria de lista b = {id(list_b)}')

list_b = list_a
print(f'Lista b = {list_b}')
print(f'Direccion de memoria de lista b luego de igualarla a lista a = {id(list_b)}')

list_a.append(4)
print(f'Lista b luego de agregar valor a lista a = {list_b}')
print(f'Direccion de memoria de lista b luego agregar valor a lista a = {id(list_b)}')

list_b.append(5)
print(f'Lista b luego de agregar valor a lista b = {list_b}')
print(f'Direccion de memoria de lista b luego agregar valor a lista b = {id(list_b)}')
print(f'Lista a luego de agregar valor a lista a y b = {list_a}')
print(f'Direccion de memoria de lista a luego agregar valor a lista a y b = {id(list_a)}')

# Funciones con paso por valor
def square_number(number: int):
    number **= 2
    print(f'El numero elevado al cuadrado es: {number}')

number = 5
print(f'Antes de la funcion: {number}')
square_number(number)
print(f'Despues de la funcion: {number}')

# Funciones con paso referencia
def insert_element(my_list: list):
    my_list.append(5)
    my_list_2 = my_list
    print(f'Lista original luego de agregar elemento: {my_list}')
    my_list_2.append(3)
    print(f'Segunda lista luego de agregar elemento: {my_list_2}')
    
my_list = [9]
insert_element(my_list)
print(f'Lista luego de la funcion: {my_list}')

# Paso por referencia, sin cambiar valor original
def insert_element_copy(my_list: list):
    print('Prueba funcion copiando lista, sin modificar la original')
    my_list.append(5)
    my_list_2 = my_list
    print(f'Lista original luego de agregar elemento: {my_list}')
    my_list_2.append(3)
    print(f'Segunda lista luego de agregar elemento: {my_list_2}')
    
my_list = [9]
insert_element_copy(my_list[:]) # Envio una copia de la lista
print(f'Lista luego de la funcion: {my_list}')

"""
 * DIFICULTAD EXTRA (opcional):
 * Crea dos programas que reciban dos parámetros (cada uno) definidos como variables anteriormente.
 * - Cada programa recibe, en un caso, dos parámetros por valor, y en otro caso, por referencia.
 *   Estos parámetros los intercambia entre ellos en su interior, los retorna, y su retorno
 *   se asigna a dos variables diferentes a las originales. A continuación, imprime el valor de las
 *   variables originales y las nuevas, comprobando que se ha invertido su valor en las segundas.
 *   Comprueba también que se ha conservado el valor original en las primeras.
"""
def change_values(a: int,b: int):
    a,b = b,a
    return a,b

a = 1
b = 2 
c,d = change_values(a,b)
print(f'a = {a}, b = {b}, c = {c}, d = {d}')

def change_value_reference(list_a: int, list_b: int):
    list_a, list_b = list_b, list_a
    return list_a, list_b

list_a = [1,2,3]
list_b = [4,5,6]

list_c, list_d = change_value_reference(list_a,list_b)
print(f'lista a = {list_a}, lista b = {list_b}, lista c = {list_c}, lista d = {list_d}')