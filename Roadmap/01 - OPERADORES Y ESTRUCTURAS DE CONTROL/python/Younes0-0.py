"""
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
"""

# Operaciones Aritméticos
print("Operaciones Aritmeticas")
print("Operacion de suma")
print("10 + 3 = ",10 + 3)
print("Operacion de resta")
print("10 - 3 = ",10 - 3)
print("Operacion de multiplicaión")
print("10 * 3 = ",10 * 3)
print("Operacion de división")
print("10 / 3 = ",10 / 3)
print("Operacion de residuo o resto")
print("10 % 3 = ",10 % 3)
print("Operacion de potencia")
print("10 ** 3 = ",10 ** 3)
print("Operacion de división entera")
print("10 // 3 = ",10 // 3)
print("-------------------------------------------")

# Operadores relacionales
print("Operadores Relacionales")
print("Mayor que")
print("10 > 3 = ",10 > 3)
print("Menor que")
print("10 < 3 = ",10 < 3)
print("Igual")
print("10 == 3 = ",10 == 3)
print("Mayor o igual")
print("10 >= 3 = ",10 >= 3)
print("Menor o igual")
print("10 <= 3 = ",10 <= 3)
print("Diferente")
print("10 != 3 = ",10 != 3)
print("-------------------------------------------")

# Operadores Bit a Bit
print("Operadores Bit a Bit")
print("Operacion de AND")
print("0b1101 & 0b1011 = ",bin(0b1101 & 0b1011))
print("Operacion de OR")
print("0b1101 | 0b1011 = ",bin(0b1101 | 0b1011))
print("Operacion de XOR")
print("0b1101 ^ 0b1011 = ",bin(0b1101 ^ 0b1011))
print("Operacion de NOT")
print("~0b1101 = ",bin(~0b1101))
print("Operacion de LEFT SHIFT")
print("10 << 3 = ",10 << 3)
print("Operacion de RIGHT SHIFT")
print("10 >> 3 = ",10 >> 3)
print("-------------------------------------------")    

# Operaciones de asignación
print("Operaciones de asignación")
print("Operacion de asignación")
diez = 10
print("10 = ",diez)
print("Operacion de suma")
diez = 10
diez += 3
print("10 += 3 = ",diez)
print("Operacion de resta")
diez = 10
diez -= 3
print("10 -= 3 = ",diez)
print("Operacion de multiplicaión")
diez = 10
diez *= 3
print("10 *= 3 = ",diez)
print("Operacion de división")
diez = 10
diez /= 3
print("10 /= 3 = ",diez)
print("Operacion de residuo o resto")
diez = 10
diez %= 3
print("10 %= 3 = ",diez)
print("Operacion de potencia")
diez = 10
diez **= 3
print("10 **= 3 = ",diez)
print("Operacion de división entera")
diez = 10
diez //= 3
print("10 //= 3 = ",diez)
print("Operacion AND de bits")
diez = 0b1101
diez &= 0b1011
print("0b1101 &= 0b1011 = ",bin(diez))
print("Operacion OR de bits")
diez = 0b1101
diez |= 0b1011
print("0b1101 |= 0b1011 = ",bin(diez))
print("Operacion XOR de bits")
diez = 0b1101
diez ^= 0b1011
print("0b1101 ^= 0b1011 = ",bin(diez))
print("Operacion LEFT SHIFT de bits")
diez = 0b1101
diez <<= 0b1011
print("0b1101 <<= 0b1011 = ",bin(diez))
print("Operacion RIGHT SHIFT de bits")
diez = 0b1011
diez >>= 0b1011
print("0b1011 >>= 0b1011 = ",bin(diez))
print("-------------------------------------------")

# Operaciones lógicas
print("Operaciones lógicas")
verdad = True
falso = False
print("Operacion AND")
print("verdad y verdad = ",verdad and verdad)
print("verdad y falso = ",verdad and falso)
print("falso y verdad = ",falso and verdad)
print("falso y falso = ",falso and falso)
print("Operacion OR")
print("verdad o verdad = ",verdad or verdad)
print("verdad o falso = ",verdad or falso)
print("falso o verdad = ",falso or verdad)
print("falso o falso = ",falso or falso)
print("Operacion NOT")
print("not verdad = ",not verdad)
print("not falso = ",not falso)
print("-------------------------------------------")

# Operaciones de identidad
print("Operaciones de identidad")
print("10 is 10 = ",10 is 10)
print("10 is not 10 = ",10 is not 10)
print("-------------------------------------------")

# Operaciones de pertenencia
print("Operaciones de pertenencia")
print("10 in [1,2,3,4,5] = ",10 in [1,2,3,4,5])
print("10 not in [1,2,3,4,5] = ",10 not in [1,2,3,4,5])
print("-------------------------------------------")

