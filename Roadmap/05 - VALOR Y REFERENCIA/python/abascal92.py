'''
/*
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
 */
'''

# Asignación de variables por valor (números, strings, booleanos)
a = 1
b = 2
b = a
print(a, b) # 1 1

c = "hola"
d = "adios"
d = c
print(c, d) # hola hola

# Asignación de variables por referencia (listas, diccionarios, objetos)
e = [1, 2, 3]
f = [4, 5, 6]
e = f
print(e, f) # [1, 2, 3] [1, 2, 3]

g = {"a": 1, "b": 2}
h = {"c": 3, "d": 4}
g = h
print(g, h) # {'a': 1, 'b': 2} {'a': 1, 'b': 2}

# Funciones con variables por valor
num = 1
def por_valor(x):
    x = 2
    return x
print(por_valor(num)) # 2

# Funciones con variables por referencia
num = [1, 2, 3]
def por_referencia(x):
    x[0] = 2
    return x
print(por_referencia(num)) # [2, 2, 3]


# DIFICULTADO EXTRA
# Por valor
def por_valor(x, y): # Se intercambian los valores de x e y
    x, y = y, x
    return x, y
num1 = 1
num2 = 2
num3, num4 = por_valor(num1, num2)
print(f"Valor original de num1: {num1}, valor original de num2: {num2}") 
print(f"Valor de num1: {num3}, valor de num2: {num4}") # 2 1

# Por referencia
def por_referencia(x, y): # Se intercambian los valores de x e y
    x[0], y[0] = y[0], x[0]
    return x, y
num4 = [1, 2, 3]
num5 = [4, 5, 6]
print(f"Valor original de num4: {num4}, valor original de num5: {num5}")
num6, num7 = por_referencia(num4, num5)
print(f"Valor de num4: {num6}, valor de num5: {num7}") # [4, 2, 3] [1, 5, 6]
