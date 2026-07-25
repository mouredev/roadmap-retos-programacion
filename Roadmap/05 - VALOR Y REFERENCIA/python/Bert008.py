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
# asignacion de variables por valor
a = 10
booleano = True
b = a
booleano2 = booleano
print("a = ", a)
print("b = ", b)
print("booleano = ", booleano)
print("booleano2 = ", booleano2)

# adignacion de variables por referencia, solo para estructuras en python
lista = [1, 2, 3, 4, 5]
a, b, c, d, e = lista
a = lista[0]
b = lista[1]
c = lista[2]
d = lista[3]
e = lista[4]

abcde = [a, b, c, d, e]
for i in abcde:
    print(i)

# asignacion por valores y referencias en funciones
def suma(x, y):
    return x + y

x = 2
y = 5

print("suma", suma(x, y))

def listas(lista):
    lista.append(len(lista) + 1)
    return lista

lista = [1, 2, 3, 4, 5]
print(listas(lista))

# dificultad extra

def xyyx(x, y):
    return y, x

x = 1
y = 2
print("valores originales ", (x, y))
print("valores cambiados: ", xyyx(x, y))

def referencias(ref1, ref2):
    ref1[:], ref2[:] = ref2[:], ref1[:]
    return ref1, ref2
x = [1, 2]
y = [3, 4]
print("original: ",x, y)
x, y = referencias(x, y)
print("Cambio: ", x, y)