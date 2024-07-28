""" /*
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
 */ """

# Tipo de datos valor
entero = 10
otro = 5
suma = entero + otro
print(entero)
print(otro)
print(suma)

# Tipo de dato referencia
lista = [1, 2, 5, 10]
otra = [3, 4, 8, 6, 7]
print(lista)
print(otra)
lista.append(otra)
print(lista)

# Paso por valor
def valor(numero):
    numero += 5

num = 2
valor(num)
print(num)

def por_valor(cadena):
    cadena = cadena.split(" ")

cadena = "Mi cadena"
por_valor(cadena)
print(cadena)

# Paso por referencia
def referencia(lista):
    for i, _ in enumerate(lista):
        lista[i] += 5

lista = [0, 1, 2, 3, 4, 5]
referencia(lista)
print(lista)