# Operadores Aritmeticos

print(f"""Los operadores aritmeticos son:
    Suma: 3 + 2,
    Resta: 5 - 2,
    Multiplicacion: 3 * 2,
    Division: 10 / 2,
    Modulo: 10 % 3,
    Exponente: 2 ** 3,
    Division Entera: 10 // 3
""")


# Operadores de comparacion

print(f"""Los operadores de comparacion son los siguientes:
    Igual a: 3 == 3
    Diferente de: 3 != 2
    Mayor que: 5 > 3
    Menor que: 3 < 5
    Mayor o igual que: 5 >= 3
    Menor o igual que: 5 <= 3
""")


# Operadores logicos

print(f"""Los operadores logicos son:
    and: True and False -> False 
    or: True or False -> True
    not: not True -> False
""")


# Operadores de Asignacion

print(f"""Los operadores de asignacion son:
    Asignacion basica: x = 5
    Suma y asigna: x += 3
    Resta y asigna: x -= 2
    Multiplica y asigna: x *= 2
    Divide y asigna: x /= 2
    Modulo y asigna: x %= 3
    Exponente y asigna: x **= 2
    Division entera y asigna: x //= 2 
""")


# Operadores de Identidad

print(f"""Los operadores de identidad son:
    Es: x is y -> Devuelve True si ambos objetos son iguales
    No es: x is not y -> Devuelve True si ambos objetos no son iguales
""")


# Operadores de pertenencia

print(f"""Los operadores de identidad son:
    En: 3 in [1, 2, 3] -> Devuelve True si el valor está en la secuencia
    En no: 4 not in [1, 2, 3] -> Devuelve True si el valor no está en la secuencia
""")

# Extra:
print(f"""Crea un programa que imprima por consola todos los números comprendidos
dentre 10 y 55 (incluidos), pares, y que no son ni el 16 ni múltiplos de 3.""")

for num in range(10, 56):
    if num % 2 == 0 and num != 16 and num % 3 != 0:
        print(num)