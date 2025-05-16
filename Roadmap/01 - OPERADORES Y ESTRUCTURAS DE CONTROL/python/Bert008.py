'''
/*
 * EJERCICIO:
 * - Crea ejemplos utilizando todos los tipos de operadores de tu lenguaje:
 *   Aritméticos, lógicos, de comparación, asignación, identidad, pertenencia, bits...
 *   (Ten en cuenta que cada lenguaje puede poseer unos diferentes)
 * - Utilizando las operaciones con operadores que tú quieras, crea ejemplos
 *   que representen todos los tipos de estructuras de control que existan
 *   en tu lenguaje:
 *   Condicionales, iterativas, excepciones...
 * - Debes hacer print por consola del resultado de todos los ejemplos.
 *
 * DIFICULTAD EXTRA (opcional):
 * Crea un programa que imprima por consola todos los números comprendidos
 * entre 10 y 55 (incluidos), pares, y que no son ni el 16 ni múltiplos de 3.
 *
 * Seguro que al revisar detenidamente las posibilidades has descubierto algo nuevo.
 */
'''
x = 2
y = 4
print("x = ", 2)
print("y = ", 4)
print("------------------------------------------------")
print("Operadores aritmeticos")
print("Suma (x + y) = ", x + y)
print("Resta (x - y) = ", x - y)
print("Multiplicacion (x * y) = ", x * y)
print("Divicion (y / x) = ", y/x)
print("Esponente (y ** x) = ", y ** x)
print("Modulo (y % x) = ", y % x)
print("Cociente (x // y) = ", x // y)
print("------------------------------------------------")
print("Operadores logicos")
print("True and True: ", True and True)
print("False and False: ", False and False)
print("True and False: ", True and False)
print("False and True: ", False and True)

print("True or True: ", True or True)
print("False or False: ", False or False)
print("True or False: ", True or False)
print("False or True: ", False or True)

print("Not False: ", not False)
print("Not True: ", not True)
print("------------------------------------------------")
print("Operadores de comparacion")
print("Es igual que (x == y): ", x == y)
print("No es igual que (x != y): ", x != y)
print("Es mayor que (x > y): ", x > y)
print("Es menor que (x < y): ", x < y)
print("Es mayor o igual que (x >= y): ", x >= y)
print("Es menor o igual que (x <= y): ", x <= y)
print("------------------------------------------------")
print("Operadores de asignacion")
x = y
a = 10; a += x
b = 10; b -= x
c = 10; c *= x
d = 10; d /= x
e = 10; e **= x
f = 10; f %= x
g = 10; g //= x
h = 10; h &= x
i = 10; i <<= x
j = 10; j >>= x
print("a += x: ")
print("b -= x: ")
print("c *= x: ")
print("d /= x: ")
print("e **= x: ")
print("f %= x: ", f)
print("g //= x: ", g)
print("h &= x: ", h)
print("i <<= x: ", i)
print("j >>= x: ", j)
print("------------------------------------------------")
print("Operadores de identidad y pertenencia")
lista = [1, 2, 3, 4, 5]
lista2 = [1, 2, 3, 4, 5]
print("x is y: ", x is y)
print("x is not y", x is not y)
print("lista == lista2: ", lista == lista2)
print("lista is lista2: ", lista is lista2)
print("lista is not lista2: ", lista is not lista2)
# las listas no se identifican de una como otra ya que aunque contienen los mismo atributos, de acuerdo con python estos dos son dos objetos disnintos.
print("1 in lista: ", 1 in lista) # 1 se encuentra dentro de lista
print("1 not in lista: ", 1 not in lista) # 1 si esta en la lista
print("6 not in lista: ", 6 not in lista) # 6 si esta en la lista
print("------------------------------------------------")
print("Operadores de bits")
print("Bitwise")
#x = bin(2)
#y = bin(10)
print("Or x | y = ", (x | y))
print("And x & y = ", x & y)
print("Not ~(x): ", ~(x))
print("Xor x ^ y = ", x ^ y)
print("Desplazamiento a la derecha x << y: ", x << y)
print("Desplazamiento a la izquierda x >> y: ", x >> y)

'''
* DIFICULTAD EXTRA (opcional):
 * Crea un programa que imprima por consola todos los números comprendidos
 * entre 10 y 55 (incluidos), pares, y que no son ni el 16 ni múltiplos de 3.
'''
print("-------------------------------------------------------------")
print("Dificultad extra")
for i in range(10, 56, 2):
    if i != 16 and i % 3 != 0:
        print(i)