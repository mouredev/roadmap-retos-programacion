
"""  * EJERCICIO:
 * - Muestra ejemplos de asignación de variables "por valor" y "por referencia", según
 *   su tipo de dato.
 * - Muestra ejemplos de funciones con variables que se les pasan "por valor" y 
 *   "por referencia", y cómo se comportan en cada caso en el momento de ser modificadas.
 * (Entender estos conceptos es algo esencial en la gran mayoría de lenguajes)
 * """

# Asignación por valor (enteros son inmutables)
mi_entero_a = 5
mi_entero_b = mi_entero_a
mi_entero_b = 10
print(mi_entero_a) # imprime 5
print(mi_entero_b) # imprime 10

# Asignación por referencia (listas son mutables)
mi_lista_a = [3, 7, 44]
mi_lista_b = mi_lista_a
mi_lista_b.append(99)
print(f"Lista A: {mi_lista_a}") # imprime [3, 7, 44, 99]
print(f"Lista B: {mi_lista_b}") # imprime [3, 7, 44, 99]

# funciones con datos por valor
def funcion_entero(mi_entero: int):
    mi_entero = 15
    print(f"Dentro de la función: {mi_entero}") # imprime 15

mi_entero_c = 5
funcion_entero(mi_entero_c)
print(f"Fuera de la función: {mi_entero_c}") # imprime 5

# funciones con datos por referencia
def funcion_lista(mi_lista: list):
    mi_lista.append(88)
    print(f"Dentro de la función: {mi_lista}") # imprime la lista con 88 añadido

mi_lista_c = [1, 2, 3]
funcion_lista(mi_lista_c)
print(f"Fuera de la función: {mi_lista_c}") # imprime la lista con 88 añadido

"""  
 * DIFICULTAD EXTRA (opcional):
 * Crea dos programas que reciban dos parámetros (cada uno) definidos como
 * variables anteriormente.
 * - Cada programa recibe, en un caso, dos parámetros por valor, y en otro caso, por referencia.
 *   Estos parámetros los intercambia entre ellos en su interior, los retorna, y su retorno
 *   se asigna a dos variables diferentes a las originales. A continuación, imprime
 *   el valor de las variables originales y las nuevas, comprobando que se ha invertido
 *   su valor en las segundas.
 *   Comprueba también que se ha conservado el valor original en las primeras.
 */ """

 # defino la función para intercambiar valores por valor
def intercambiar_por_valor(a: int, b: int) -> tuple:
    return b, a

def intercambiar_por_referencia(lista1: list, lista2: list) -> tuple:
    lista1[:], lista2[:] = lista2[:], lista1[:]
    return lista1, lista2

lista_d = [10, 20]
lista_e = [30, 40]

print(f"Valores originales: {mi_entero_a, mi_entero_b}")
print(f"Valores invertidos por valor: {intercambiar_por_valor(mi_entero_a, mi_entero_b)}")
print(f"Listas originales: {lista_d, lista_e}")
print(f"Listas invertidas por referencia: {intercambiar_por_referencia(lista_d, lista_e)}")

print(f"Listas originales: {lista_d, lista_e}") # compruebo que las originales han cambiado
