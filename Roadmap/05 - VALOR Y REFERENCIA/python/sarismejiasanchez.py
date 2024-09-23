# #05 VALOR Y REFERENCIA

"""
* - Muestra ejemplos de asignación de variables "por valor" y "por referencia", según
*   su tipo de dato.
"""

# PASO POR VALOR
# Variables inmutables (se comportan como si fueran "por valor")
# Los tipos de datos inmutables en Python incluyen int, float, bool, str, tuple. 
# Si modificas una variable de un tipo inmutable, se crea un nuevo objeto en memoria.

print("PASO POR VALOR")
# Variables inmutables (int, str)
a = 10
b = a   # Apunta al mismo valor que a

b = 20  # Se crea un nuevo valor, b apunta a otro lugar en memoria

print(a)    # 10 (a no ha cambiado)
print(b)    # 20 (b tiene un nuevo valor)

# PASO POR REFERENCIA
# Variables mutables (se comportan como si fueran "por referencia")
# Los tipos de datos mutables incluyen list, dict, set. Modificar una variable mutable afecta # a todas las referencias que apuntan a ese objeto.

print("PASO POR REFERENCIA")
# Variables mutables (listas)
x = [1, 2, 3]
y = x  # y apunta al mismo espacio en memoria de x

y.append(4)  # Modifica la lista a la que ambos apuntan

print(x)  # Output: [1, 2, 3, 4] (x ha cambiado)
print(y)  # Output: [1, 2, 3, 4] (y también ha cambiado)
        

"""
* - Muestra ejemplos de funciones con variables que se les pasan "por valor" y 
*   "por referencia", y cómo se comportan en cada caso en el momento de ser modificadas.
* (Entender estos conceptos es algo esencial en la gran mayoría de lenguajes)
*
"""

# Función con inmutables (se comportan como si fueran "por valor")
# Cuando pasas un tipo inmutable a una función, cualquier modificación dentro de la función no # afectará al valor original fuera de la función.

print("\nFunciones: Paso por Valor vs Referencia")

print("PASO POR VALOR")

def modificar_numero(n):
    n = 100  # Se asigna un nuevo valor a n
    print(f"Valor dentro de la función: {n}")   # # Valor dentro de la función: 100

numero = 10
modificar_numero(numero)
print(f"Valor fuera de la función: {numero}")   # Valor fuera de la función: 10

# Función con mutables (se comportan como si fueran "por referencia")
# Cuando pasas un tipo mutable a una función, las modificaciones dentro de la función 
# afectarán al objeto original.

print("PASO POR REFERENCIA")

def modificar_lista(lista):
    lista.append(100)  # Modifica la lista original

mi_lista = [1, 2, 3]
modificar_lista(mi_lista)
print(mi_lista)     # [1, 2, 3, 100] (la lista ha sido modificada)


"""
* DIFICULTAD EXTRA (opcional):
* Crea dos programas que reciban dos parámetros (cada uno) definidos como variables anteriormente.
* - Cada programa recibe, en un caso, dos parámetros por valor, y en otro caso, por referencia.
*   Estos parámetros los intercambia entre ellos en su interior, los retorna, y su retorno
*   se asigna a dos variables diferentes a las originales. A continuación, imprime el valor de las
*   variables originales y las nuevas, comprobando que se ha invertido su valor en las segundas.
*   Comprueba también que se ha conservado el valor original en las primeras.
*/

"""