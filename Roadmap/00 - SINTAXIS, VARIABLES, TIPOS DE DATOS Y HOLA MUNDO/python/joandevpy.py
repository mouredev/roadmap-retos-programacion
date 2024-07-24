
# Operadores aritméticos

print("Operadores aritméticos:")
print(f"Suma: 10 + 3 = {10 + 3}")
print(f"Resta: 10 - 3 = {10 - 3}")
print(f"Multiplicación: 10 * 3 = {10 * 3}")
print(f"División: 10 / 3 = {10 / 3}")
print(f"División entera: 10 // 3 = {10 // 3}")
print(f"Modulo: 10 % 3 = {10 % 3}")
print(f"Exponencial: 10 ** 3 = {10 ** 3}")

""" 
Operadores de comparación-
Pueden ser con variables__|
"""
print("\nOperadores de comparación:")
print(f"Igual 10 == 3 : {10 == 3}")
print(f"Desigual 10 != 3 : {10 != 3}")
print(f"Maypr que 10 > 3 : {10 > 3}")
print(f"Menor que 10 < 3 : {10 < 3}")
print(f"Mayor o igual que 10 >= 10 : {10 >= 10}")
print(f"Menor o igual que 10 <= 3 : {10 <= 3}")

# Operadores lógicos
print("\nOperadores lógicos:")
print(f"10 > 5 and 3 < 5 : {10 > 5 and 3 < 5}")
print(f"3 > 5 or || 3 < 2 : {10 > 5 or 3 < 2}")
print(f"not(10 > 5) : {not 10 > 5}")

# Operadores de asignación
my_number = 11

print("\nOperadores de asignación:")
print(f"my_number es {my_number}")
my_number += 5
print(f"my_number += 5: {my_number}") # Suma y Asignacion
my_number -= 2
print(f"my_number -= 2: {my_number}") # Resta y Asignacion
my_number *= 3
print(f"my_number *= 3: {my_number}") # Multiplicar y Asignacion
my_number /= 4
print(f"my_number /= 4: {my_number}") # Divide y Asignacion
my_number //= 2
print(f"my_number //= 2: {my_number}") # Divide entera y Asignacion
my_number %= 3
print(f"my_number %= 3: {my_number}") # Modulo y Asignacion
my_number **= 2
print(f"my_number **= 2: {my_number}") # Exponencial y Asignacion

# Operadores de identidad
print("\nOperadores de identidad:")
my_new_number = my_number
print(f"my_number is my_new_number : {my_number is my_new_number}")
print(f"my_number is not my_new_number : {my_number is not my_new_number}")


# Operadores de pertenencia
print("\nOperadores de pertenencia:")
print(f"'a' in 'joandevpy' : {'a' in 'joandevpy'}")
print(f"'a' not in 'joandevpy' : {'a' not in 'joandevpy'}")


# Operadores de bits
print("\nOperadores de bits:")
c = 10  # 1010
d = 3   # 0011
print(f"c & d : {c & d}")  # AND bit a bit
print(f"c | d : {c | d}")  # OR bit a bit
print(f"c ^ d : {c ^ d}")  # XOR bit a bit
print(f"~c : {~c}")        # NOT bit a bit
print(f"c << 1 : {c << 2}") # Desplazamiento a la izquierda
print(f"c >> 1 : {c >> 1}") # Desplazamiento a la derecha


"""
Estructuras de control
"""

# Condicionales

print("\nCondicionales:")

my_string = "joandevpyy"

if my_string == "joandevpy":
    print("my_string es joandevpy")
elif my_string == "Joan":
   print("my_string es Joan")
else:
    print("my_string no es joandevpy ni Joan")

# Bucles for o Iterativas
print("\nBucles for o iterativas:")
for i in range(11): # el ultimo numero no se imprime seria hasta el 10
    print(i)

# Bucles while siempre se ejecuta mientras sea True (Bucle Infinito)
print("\nBucles while:")
i = 0
while i < 5:
    print(f"Contador en {i}")
    i += 1

# Excepciones
print("\nExcepciones:")
try:
    resultado = 10 / 0
    print(f"El resultados es: {resultado}")
except ZeroDivisionError:
    print("Error: División por cero")
finally:
    print("Ha finalizado el manejo de excepciones")    


# Dificultad extra
print("\nNúmeros entre 10 y 55, pares, que no son ni el 16 ni múltiplos de 3:")
for number in range(10, 56):
    if number % 2 == 0 and number != 16 and number % 3 != 0:
        print(number)
