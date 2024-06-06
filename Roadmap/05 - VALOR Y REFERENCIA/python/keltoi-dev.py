"""
* EJERCICIO:
* - Muestra ejemplos de asignación de variables "por valor" y "por referencia", según
*   su tipo de dato.
* - Muestra ejemplos de funciones con variables que se les pasan "por valor" y 
*   "por referencia", y cómo se comportan en cada caso en el momento de ser modificadas.
* (Entender estos conceptos es algo esencial en la gran mayoría de lenguajes)
"""

# Asignacion por valor
x = 100
y = x
y = 10
print(id(x))
print(id(y))

print(x, y)
print("Al ser inmutables apuntan a distintos id a pesar que se igualaron")

# Asignacion por referencia
l1 = [1, 2, 3, 4]
l2 = l1
l2.append(5)

print(id(l1))
print(id(l2))

print(l1, l2)
print("Al ser mutables apuntan al mismo id desde que se igualaron")


# Paso a funciones por valor
def valor(num):
    num += 10
    print("La variable dentro de la funcion:", num)
    print(id(num))


valor(x)
print("La variable fuera de la funcion:", x)
print(id(x))


# Paso a funciones por referencia
def referencia(lista):
    lista.pop()
    print("La variable dentro de la funcion:", lista)
    print(id(lista))


referencia(l1)
print("La variable fuera de la funcion:", l1)
print(id(l1))


"""
* DIFICULTAD EXTRA (opcional):
* Crea dos programas que reciban dos parámetros (cada uno) definidos como variables anteriormente.
* - Cada programa recibe, en un caso, dos parámetros por valor, y en otro caso, por referencia.
*   Estos parámetros los intercambia entre ellos en su interior, los retorna, y su retorno
*   se asigna a dos variables diferentes a las originales. A continuación, imprime el valor de las
*   variables originales y las nuevas, comprobando que se ha invertido su valor en las segundas.
*   Comprueba también que se ha conservado el valor original en las primeras.
"""


# Funcion con parametros por valor
def prog_valor(num1, num2):
    num2, num1 = num1, num2
    return num1, num2


original1 = 10
original2 = 100
nuevo1, nuevo2 = prog_valor(original1, original2)

print(f"El primer valor original es {original1} y el segundo {original2}")
print(f"El primer valor nuevo es {nuevo1} y el segundo {nuevo2}")


# Funcion con parametros por referencia
def prog_referencia(l_orig1, l_orig2):
    l_orig2, l_orig1 = l_orig1, l_orig2
    return l_orig1, l_orig2


l_orig1 = [1, 2, 3]
l_orig2 = [4, 5, 6]

l_nueva1, l_nueva2 = prog_referencia(l_orig1, l_orig2)

print(f"El primer valor original es {l_orig1} y el segundo {l_orig2}")
print(f"El primer valor nuevo es {l_nueva1} y el segundo {l_nueva2}")
