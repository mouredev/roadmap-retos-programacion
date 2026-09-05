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

# ASIGNACIÓN POR VALOR

var1: int = 15; var2: str = '15'; var3: list = ['b', 'c', 'd', 'a']; var4:  dict = {}; print(var1, var2, var3, var4)

import copy
var0: list = copy.copy(var3)
print(var0)

lista: list[list[int]] = [[0], [1]]
print(lista)
lista2: list[list[int]] = copy.deepcopy(lista)
lista3: list[list[int]] = copy.copy(lista)
lista4: list[list[int]] = lista.copy()
lista[0].append(31); lista[1].append(32)
print(lista, lista2, lista3, lista4)
print()

# ASIGNACIÓN POR REFERENCIA

var5: int = var1
var5 += 1
print(var1, var5)
var1 += 1
print(var1, var5)

var6 = var3
print(var6, var3)
var3.append(var1)
print(var6, var3)
var6.append(var1)
print(var6, var3)
print(var0)
print()

# FUNCIONES

a, b, c = 15, 15, 15; d = a; e = d
def obtener_variable(var):
    a = var
    print("%s" % a)

obtener_variable(a)
obtener_variable(b)
obtener_variable(c)
obtener_variable(d)
obtener_variable(e)
print(a, b, c, d, e)

a = [[[], []],
     [[[[5]]]],
     []]

b = a.copy()

def obtener_variable(var):
    x = var

    x[0][0].append(15); x[0][1].append(16)
    x[1][0][0][0].append(17)
    x[2].append(18)

    return x

result = obtener_variable(a)
print(f"A: {a}\tB: {b}\tX: {result}".expandtabs(5))
result.append(19)
print(f"A: {a}\tB: {b}\tX: {result}".expandtabs(5))
result[0][0].append(20)
print(f"A: {a}\tB: {b}\tX: {result}".expandtabs(5))
print()

# EXTRA

original1, original2 = [1, 2, 3, 4, 5], [5, 4, 3, 2, 1]; copia1, copia2 = original1.copy(), copy.deepcopy(original2)

def funcion(var1, var2):
    x, y = sorted(var1), sorted(var2)
    print(f"var1: {original1}\tvar2: {original2}\nxvar1: {x}\tyvar2: {y}")
    return None

funcion(original1, original2)
funcion(copia1, copia2)

print("Original 1: {}, Original 2: {}\nCopia 1: {}, Copia 2: {}".format(original1, original2, copia1, copia2))