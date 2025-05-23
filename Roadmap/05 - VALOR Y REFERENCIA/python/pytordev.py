##EJERCICIO:
##- Muestra ejemplos de asignación de variables "por valor" y "por referencia", según su tipo de dato.
# Por valor
a = 1
b = a
b = 2
print(a)  # Salida: 1
print(b)  # Salida: 2

# Por referencia
lista1 = [1, 2, 3]
lista2 = lista1
lista2.append(4)
print(lista1)  # Salida: [1, 2, 3, 4]
print(lista2)  # Salida: [1, 2, 3, 4]
lista3 = lista1.copy()
lista3.append(5)
print(lista1)  # Salida: [1, 2, 3, 4]
print(lista3)  # Salida: [1, 2, 3, 4, 5]

##- Muestra ejemplos de funciones con variables que se les pasan "por valor" y "por referencia", y cómo se comportan en cada caso en el momento de ser modificadas.

# funcion con parametros por valor. No se modifica el valor original
x = 5
print(x)  # Salida: 5


def mod_by_value(x):
    x = 10
    return x


print(mod_by_value(x))  # Salida: 10

# funcion con parametros por referencia. Se modifica el valor original
lista4 = [1, 2, 3]
print(lista4)  # Salida: [1, 2, 3]


def mod_by_reference(lista):
    lista = lista4
    lista.append(4)
    return lista


print(mod_by_reference([]))  # Salida: [1, 2, 3, 4]
print(lista4)  # Salida: [1, 2, 3, 4]


"""
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
# Programa 1
a = 10
b = 20


def swap_values(x, y):
    x2, y2 = y, x
    print(x, y)
    print(x2, y2)
    return x2, y2


swap_values(a, b)

# Programa 2
list_a = [15]
list_b = [25]


def swap_references(a: list, b: list):
    a2, b2 = b.copy(), a.copy()
    print(list_a, list_b)
    print(a2, b2)
    return a2, b2


swap_references(list_a, list_b)
