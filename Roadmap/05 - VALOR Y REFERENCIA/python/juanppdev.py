"""
* - Muestra ejemplos de asignación de variables "por valor" y "por referencia", según
 *   su tipo de dato.
 * - Muestra ejemplos de funciones con variables que se les pasan "por valor" y 
 *   "por referencia", y cómo se comportan en cada caso en el momento de ser modificadas.
"""

# Asignación de variables "por valor" (int, float, str, tuple)
numero = 5
numero_copia = numero
numero_copia += 1
print("numero:", numero)  # Salida: 5
print("numero_copia:", numero_copia)  # Salida: 6

cadena = "Hola"
cadena_copia = cadena
cadena_copia += " Mundo"
print("cadena:", cadena)  # Salida: Hola
print("cadena_copia:", cadena_copia)  # Salida: Hola Mundo

tupla = (1, 2, 3)
tupla_copia = tupla
tupla_copia += (4, 5)
print("tupla:", tupla)  # Salida: (1, 2, 3)
print("tupla_copia:", tupla_copia)  # Salida: (1, 2, 3, 4, 5)

# Asignación de variables "por referencia" (list, dict, set)
lista = [1, 2, 3]
lista_referencia = lista
lista_referencia.append(4)
print("lista:", lista)  # Salida: [1, 2, 3, 4]
print("lista_referencia:", lista_referencia)  # Salida: [1, 2, 3, 4]

diccionario = {"a": 1, "b": 2}
diccionario_referencia = diccionario
diccionario_referencia["c"] = 3
print("diccionario:", diccionario)  # Salida: {'a': 1, 'b': 2, 'c': 3}
print("diccionario_referencia:", diccionario_referencia)  # Salida: {'a': 1, 'b': 2, 'c': 3}

conjunto = {1, 2, 3}
conjunto_referencia = conjunto
conjunto_referencia.add(4)
print("conjunto:", conjunto)  # Salida: {1, 2, 3, 4}
print("conjunto_referencia:", conjunto_referencia)  # Salida: {1, 2, 3, 4}

# EJERCICIO EXTRA
"""
    Crea dos programas que reciban dos parámetros (cada uno) definidos como variables anteriormente.
 * - Cada programa recibe, en un caso, dos parámetros por valor, y en otro caso, por referencia.
 *   Estos parámetros los intercambia entre ellos en su interior, los retorna, y su retorno
 *   se asigna a dos variables diferentes a las originales. A continuación, imprime el valor de las
 *   variables originales y las nuevas, comprobando que se ha invertido su valor en las segundas.
 *   Comprueba también que se ha conservado el valor original en las primeras.
"""

# Por valor
def swap_by_value(x, y):
    # Swap the values of x and y
    x, y = y, x
    # Return the swapped values
    return x, y

# Define two variables with integer values
a = 5
b = 10
# Call the swap_by_value function and assign the returned values to new variables
c, d = swap_by_value(a, b)
# Print the original and new variables
print("Por valor:")
print("Original variables: a =", a, ", b =", b)
print("New variables: c =", c, ", d =", d)

# Por referencia
def swap_by_reference(lst):
    # Swap the first and second elements of the list
    lst[0], lst[1] = lst[1], lst[0]
    # Return the modified list
    return lst

# Define two variables with list values
e = [5, 10]
f = [15, 20]
# Call the swap_by_reference function and assign the returned value to a new variable
g = swap_by_reference([e, f])
# Print the original and new variables
print("Por referencia:")
print("Original variables: e =", e, ", f =", f)
print("New variables: g =", g)