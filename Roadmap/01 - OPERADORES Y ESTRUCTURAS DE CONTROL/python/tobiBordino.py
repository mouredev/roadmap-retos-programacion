"""
Operadores
"""

# Operadores aritméticos
print("--- Operadores aritméticos ---")
print(f"Suma: 10 + 3 = {10 + 3}")
print(f"Resta: 10 - 3 = {10 - 3}")
print(f"Multiplicación: 10 * 3 = {10 * 3}")
print(f"División: 10 / 3 = {10 / 3}")
print(f"División entera: 10 // 3 = {10 // 3}")
print(f"Residuo: 10 % 3 = {10 % 3}")
print(f"Exponente: 10^3 = {10 ** 3}")

# Operadores de comparación
print("--- Operadores de comparación ---")
print(f"Igual que: 10 == 3 = {10 == 3}")
print(f"Diferente que: 10 != 3 = {10 != 3}")
print(f"Mayor que: 10 > 3 = {10 > 3}")
print(f"Menor que: 10 < 3 = {10 < 3}")
print(f"Mayor o igual que: 10 >= 10 = {10 >= 10}")
print(f"Menor o igual que: 10 <= 3 = {10 <= 3}")

# Operadores lógicos
print("--- Operadores lógicos ---")
print(f"AND &&: True and False = {True and False}")
print(f"OR ||: True or False = {True or False}")
print(f"NOT !: not True = {not True}")

# Operadores de asignación
print("--- Operadores de asignación ---")
x = 10
print(f"x = {x}")
x += 1
print(f"x += 1 = {x}")
x -= 1
print(f"x -= 1 = {x}")
x *= 1
print(f"x *= 1 = {x}")
x /= 1
print(f"x /= 1 = {x}")
x %= 1
print(f"x %= 1 = {x}")
x //= 1
print(f"x //= 1 = {x}")
x **= 1
print(f"x **= 1 = {x}")

# Operadores de identidad
print("--- Operadores de identidad ---")
x = 10
y = 10
print(f"x = {x}")
print(f"y = {y}")
print(f"x is y = {x is y}")
print(f"x is not y = {x is not y}")

# Operadores de pertenencia
print("--- Operadores de pertenencia ---")
x = 3
y = 10
lista = [1, 2, 3, 4, 5]
print(f"x = {x}")
print(f"y = {y}")
print(f"lista = {lista}")
print(f"x in lista = {x in lista}")
print(f"y not in lista = {y not in lista}")

# Operadores de bits
print("--- Operadores de bits ---")
x = 10 # 1010
y = 3 # 0011
print(f"x = {x}")
print(f"y = {y}")
print(f"AND: x & y = {x & y}") # 0010
print(f"OR: x | y = {x | y}") # 1011
print(f"XOR: x ^ y = {x ^ y}") # 1001 "1" si los bits son diferentes, 0 si son iguales
print(f"NOT: ~x = {~x}") # 0101
print(f"DESPLAZAMIENTO A LA IZQUIERDA: x << 2 = {x << 2}") # 101000
print(f"DESPLAZAMIENTO A LA DERECHA: x >> 2 = {x >> 2}") # 10

# Estructuras de control
print("--- Estructuras de control ---")
# if
print("--- if ---")
x = 10
y = 3
if x > y:
    print(f"{x} es mayor que {y}")
elif x == y:
    print(f"{x} es igual que {y}")
else:
    print(f"{x} es menor que {y}")

# Estructura iterativa
# for
print("--- for ---")
lista = [1, 2, 3, 4, 5]
for i in lista:
    print(i)

# while
print("--- while ---")
i = 0
while i <= 5:
    print(i)
    i += 1

# Manejo de excepciones
print("--- Manejo de excepciones ---")
try:
    x = 10
    y = 0
    print(x / y)
except ZeroDivisionError:
    print("No se puede dividir entre cero")
except TypeError:
    print("No se puede dividir entre cero")
except:
    print("Error desconocido")
finally:
    print("Finalmente")

# Sección extra (realizar un programa)
# Programa que imprima por consola todos los números entre el 10 y el 55 incluido pero que sean sólo los pares. 
    #Excepto el número 16.
    #Expecto los múltiplos de 3.
print("--- Programa ---")
for number in range(10, 56):
    if number % 2 == 0 and number != 16 and number % 3 != 0:
        print(number)