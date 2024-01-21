# Operadores Aritmeticos
print(34 + 78)  # Suma
print(43 - 19)  # Resta
print(27 * 8)  # Producto
print(112 / 14)  # División
print(103 % 7)  # Modulo
print(12**6)  # Potencia
print(18 // 5)  # División con resultado entero


# Operadores Lógicos
x, y = True, False
print(x and y)  # True and False => False
print(x or y)  # True or False => True
print(not y)  # Valor opuesto de False => True


# Operadores de Pertenencia
lst = [1, 3, 9, 17, 22, 187, 99]
print(22 in lst)  # True
print(112 in lst)  # False
print(456 not in lst)  # True
print(99 not in lst)  # False


# Operadores de Identidad
a, b = "Python", "JavaScript"
print(a is b)  # False
print(a is not b)  # True


# Operadorees de Comparación
print(10 > 8)  # True
print(19 < 11)  # False
print(15 >= 15)  # True
print(58 <= 26)  # False
print(29 == 30)  # False
print(44 != 88)  # True


# Operadores a nivel de Bits
print(3 | 7)  # 7
print(3 ^ 7)  # 4
print(3 & 7)  # 3
print(3 << 7)  # 384
print(3 >> 7)  # 0
print(~7)  # -8


# Operadores de Asignación
m, n = 24, 4
m += n  # m = m + n
m -= n  # m = m - n
m *= n  # m = m * n
m /= n  # m = m / n
m %= n  # m = m % n
m //= n  # m = m // n
m **= n  # m = m ** n
m = int(m)
m |= n  # m = m | n
m ^= n  # m = m ^ n
m &= n  # m = m & n
m <<= n  # m = m << n
m >>= n  # m = m >> n


# Estructuras de Control Condicionales
# if-elif-else
if 4 >= 3 >= 1 and True is not False:
    print("Primer cuatrimestre")
elif 8 >= 7 >= 5 and 1 in [2, 6, 8, 1]:
    print("Segundo cuatrimestre")
elif 12 >= 10 >= 9 and not False:
    print("Tercer cuatrimestre")
else:
    print("Valores incorrectos")


# Estructuras de Control Iterativas
# for
for i in range(0, 30):
    if i % 2 == 1:
        print(i, end=" ")


# while
print()
resul = 50
while resul >= 20:
    resul -= 7
print(f"El resultado es: {resul}")


# Estructuras de Control para Manejo de Excepciones
# exception
v1, v2 = 45, "Hola Mundo"
try:
    v1 += v2
except TypeError:
    print("Error: no se puede sumar un tipo de dato int con uno str")


# Crea un programa que imprima por consola todos los números comprendidos entre 10 y 55 (incluidos), pares, y que no son ni el 16 ni múltiplos de 3.
print([i for i in range(10, 56) if i % 2 == 0 and i != 16 and i % 3 != 0])
