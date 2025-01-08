"""
------------------
VALOR Y REFERENCIA
------------------
EJERCICIO:
- Muestra ejemplos de asignación de variables "por valor" y "por referencia", según
  su tipo de dato.
- Muestra ejemplos de funciones con variables que se les pasan "por valor" y 
  "por referencia", y cómo se comportan en cada caso en el momento de ser modificadas.
(Entender estos conceptos es algo esencial en la gran mayoría de lenguajes)

DIFICULTAD EXTRA (opcional):
Crea dos programas que reciban dos parámetros (cada uno) definidos como
variables anteriormente.
- Cada programa recibe, en un caso, dos parámetros por valor, y en otro caso, por referencia.
  Estos parámetros los intercambia entre ellos en su interior, los retorna, y su retorno
  se asigna a dos variables diferentes a las originales. A continuación, imprime
  el valor de las variables originales y las nuevas, comprobando que se ha invertido
  su valor en las segundas.
  Comprueba también que se ha conservado el valor original en las primeras.
"""

# Ejercicio

# Asignación de variable por valor

def fun_one(number: int):
    number *= 5

n = 10
fun_one(n)
print(n)

my_int_a = 20 # Otro ejemplo
my_int_b = my_int_a
my_int_b = 30
print(my_int_a)
print(my_int_b)

# Asignación de variable por referencia

def fun_two(my_list: list):
    for i, n in enumerate(my_list):
        my_list[i] *= 2

l = [1, 2, 3]

fun_two(l)
print(l)

my_list_a = [10, 20] # Otro ejemplo
my_list_b = my_list_a
my_list_b.append(30)
print(my_list_a)
print(my_list_b)

# Ejercicio Extra

value_one = 1
value_two = 2

def my_fun(value_a: int, value_b: int):
    temp = value_a
    value_a = value_b
    value_b = temp
    return value_a, value_b

print("\nAsignación por valor:")
value_three, value_four = (my_fun(value_one, value_two))
print(f"Originales: {value_one}, {value_two}")
print(f"Nuevos: {value_three}, {value_four}")

value_ref_one = [10, 20]
value_ref_two = [30, 40]

def my_other_fun(value_a: list, value_b: list):
    temp = value_a
    value_a = value_b
    value_b = temp
    value_a.append(50)
    value_b.append(30)
    return value_a, value_b

print("\nAsignación por referencia:")
value_three, value_four = my_other_fun(value_ref_one, value_ref_two)
print(f"Originales: {value_ref_one}, {value_ref_two}")
print(f"Nuevos: {value_three}, {value_four}")