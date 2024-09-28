def print_section(name: str, lines_from_top: int = 0) -> None:
    [print() for i in range(lines_from_top)]

    print(f"{'*' * 14} {name} {'*' * 14}")
    print("-" * 60)


def print_sub_section(title: str) -> None:
    print(f"\n** {title} **")


# ************** Operadores **************
print_section("Operadores")


# ** Operadores Aritméticos **
print_sub_section("Operadores Aritméticos")
# Suma
print(f"10 + 4 = {10 + 4}")
# Resta
print(f"10 - 4 = {10 - 4}")
# Multiplicación
print(f"10 * 4 = {10 * 4}")
# División
print(f"28 / 7 = {28 / 7}")
# Módulo
print(f"5 % 2 = {5 % 2}")
# División entera
"""
La división entera redondea cerca de cero solo
cuando los números son positivos.
"""
print(f"10 // 3 = {10 // 3}")
print(f"10 // -3 = {10 // -3}")
# Potencia
print(f"4**2 = {4**2}")


#  ** Operadores Lógicos **
print_sub_section("Operadores Lógicos")
"""
Se pueden usar tanto True y False como los números 0 y 1,
siendo 0: False y 1: True
"""
# and
print(f"True and False = {True and False}")
print(f"0 and 1 = {0 and 1}")
# or
print(f"True or False = {True or False}")
print(f"1 or 0 = {1 or 0}")
# not
print(f"not True = {not True}")
print(f"not 1 = {not 1}")


# ** Operadores de Comparación **
print_sub_section("Operadores de Comparación")
# Menor que
print(f"4 < 8 = {4 < 8}")
# Mayor que
print(f"4 > 8 = {4 > 8}")
# Igual
print(f"4 == 8 = {4 == 8}")
# Mayor o igual
print(f"4 >= 8 = {4 >= 8}")
# Menor o igual
print(f"4 <= 8 = {4 <= 8}")
# Distinto
print(f"4 != 8 = {4 != 8}")


# ** Operadores de Concatenación **
print_sub_section("Operadores de Concatenación")
print(f"'ab' + 'cd' = '{'ab' + 'cd'}'")


# ** Operadores de Bits **
print_sub_section("Operadores de Bits")
# and
print(f"10 & 4 = {10 & 4}")
# or
print(f"10 | 4 = {10 | 4}")
# not
print(f"~10 = {~10}")
# xor
print(f"10 ^ 4 = {10 ^ 4}")
# Desplazamiento a izquierda
print(f"10 << 4 = {10 << 4}")
# Desplazamiento a derecha
print(f"10 >> 4 = {10 >> 4}")


# ** Operadores de Asignación **
print_sub_section("Operadores de Asignación")
x = 4
print(f"x = 4   = {4}")
print(f"x += 4   = {x + 4}")
print(f"x -= 4   = {x - 4}")
print(f"x *= 4   = {x * 4}")
print(f"x /= 4   = {x / 4}")
print(f"x %= 4   = {x % 4}")
print(f"x //= 4   = {x // 4}")
print(f"x **= 4   = {x ** 4}")
print(f"x &= 4   = {x & 4}")
print(f"x |= 4   = {x | 4}")
print(f"x ^= 4   = {x ^ 4}")
print(f"x <<= 4   = {x << 4}")
print(f"x >>= 4   = {x >> 4}")


# ** Operadores de Identidad **
print_sub_section("Operadores de Identidad")
print(f"True is False = {True is False}")
print(f"True is not False = {True is not False}")


# ** Operadores de Pertenencia **
print_sub_section("Operadores de Pertenencia")
print(f"4 in [3, 4, 5] = {4 in [3, 4, 5]}")
print(f"4 not in [3, 4, 5] = {4 not in [3, 4, 5]}")


# ************** Estructuras de Control **************
print_section("Estructuras de Control", lines_from_top=2)


# ** Condicionales **
print_sub_section("Condicionales")
x = -5
if x >= 5:
    print("x es mayor o igual que 5")
elif x > 0:
    print("x es mayor que 0 y menor que cinco")
else:
    print("x es menor o igual que 0")


# ** Excepciones **
print_sub_section("Excepciones")
try:
    4 + "5"
except TypeError:
    print("No se puede sumar un int y un string")
else:
    print("Ejecutado sin problemas")
finally:
    print("Acabando sin importar si huvo algún problema")


#  ** Iterativas **
print_sub_section("Iterativas")
c = 1
while c > 0:
    print(f"c es igual a {c}")
    c -= 1

# EXTRA
nums = []
print("\nEjercicio extra:")
for i in range(10, 55):
    if i % 2 == 0:
        if i != 16:
            if i % 3 != 0:
                nums.append(i)
print(nums)
