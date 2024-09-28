# #05 VALOR Y REFERENCIA
#### Dificultad: Fácil | Publicación: 29/01/24 | Corrección: 05/02/24

## Ejercicio

"""
 * EJERCICIO:
 * - Muestra ejemplos de asignación de variables "por valor" y "por referencia", según
 *   su tipo de dato.
 * - Muestra ejemplos de funciones con variables que se les pasan "por valor" y 
 *   "por referencia", y cómo se comportan en cada caso en el momento de ser modificadas.
"""

# Ejemplos de asignación de variables "por valor" y "por referencia"
# por valor
c = 34

# por referencia, asignamos una variable a otra y ambas apuntan al mismo objeto.
a = [45,420,23]
b = a
b.append(79)
print(f"b original: {b}")
print(f"a original: {a}")
a.append(99) #modificamos a
print(f"b final: {b}") # b sigue referenciando a "a" y los cambios de "a" afectan a "b"


# ejemplo de función con variable que se le pasan por referencia
def doble(numero):
    return numero * 2

print(doble(5))


"""
 * DIFICULTAD EXTRA (opcional):
 * Crea dos programas que reciban dos parámetros (cada uno) definidos como variables anteriormente.
 * - Cada programa recibe, en un caso, dos parámetros por valor, y en otro caso, por referencia.
 *   Estos parámetros los intercambia entre ellos en su interior, los retorna, y su retorno
 *   se asigna a dos variables diferentes a las originales.
 *   A continuación, imprime el valor de las
 *   variables originales y las nuevas, comprobando que se ha invertido su valor en las segundas.
 *   Comprueba también que se ha conservado el valor original en las primeras.
"""

def test1 (param1, param2):
    param1, param2 = param2, param1
    return param1, param2


param1 = 5
param2 = 10
print(f"Variables originales: {param1} y {param2}")

print(f"Variables nuevas: {test1(param1, param2)}")
print(f"Las variables conservan su valor: {param1} y {param2}")