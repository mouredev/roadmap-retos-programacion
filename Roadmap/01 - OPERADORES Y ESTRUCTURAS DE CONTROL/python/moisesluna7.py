"""
Operadores
"""

# Operadores aritméticos 
print(f"Suma: 10 + 3 = {10 + 3}")
print(f"Multiplicación: 10 * 3 = {10 * 3}")
print(f"Resta: 10 - 20 = {10 - 20}")
print(f"División: 10/20 = {10/20}")
print(f"Exponente: 10 ** 3 = {10 ** 3}")

# Operadores de comparación = dan como resultado si la operación es verdadera o falsa
print(f"Igualdad: 10 == 3 = {10 == 3}") # Esto es para igualdades Verdadero / Falso
print(f"Desigualdad: 10!=3 = {10 != 3}") # Esto es para desigualdades Verdadero / Falso
print(f"Mayor que: 5 > 10 = {5 > 10}")
print(f"Menor que: 5 < 10 = {5 < 10}")
print(f"Mayor o igual que: 5 >= 10 = {5>=10}")
print(f"Menor o igual que: 5 <= 10 = {5<=10}")

# Operadores lógicos 
print(f"AND: 10 + 3 = 13 and 5 - 1 = 4 es {10 + 4 == 13 and 5 - 1 == 4}") # AND te dice si todas las condiciones de una función son verdaderas 
print(f"OR: 10 + 3 = 13 and 5 - 1 = 4 es {10 + 4 == 13 or 5 - 1 == 4}") # OR te dice si aunque sea una de las condiciones es verdadera
print(f"NOT: 10 + 3 == 14 = {not 10 + 3 == 14}")

# Operadores de asignación
my_number = 12 # asignación de variable
print(my_number)
my_number += 20
print(my_number)
my_number -= 20
print(my_number)
my_number *= 20
print(my_number)
my_number /= 20
print(my_number)

# Operadores de identidad
my_new_number = my_number
print(f"my_new_number is my_number es {my_number is my_new_number}")
print(f"my_number is not my_new_number es {my_number is my_new_number}")

# Operadores de pertenencia
print(f"'u' in 'moure' = {'u' in 'moure'}")
print(f"'b' not in 'moure' = {'b' not in 'moure'}")

# Operadores de bit
a = 10 # 1010
b= 3 # 0011
print(f"AND: 10 & 3 = {10 & 3}") #0010
print(f"OR: 10 | 3 = {10 | 3}") #0010
print(f"XOR: 10 ^ 3 = {10 ^ 3}") #0010
print(f"NOT: ~10 = {~10}")
print(f"Desplazamiento a la derecha: 10 >> 2 = {10 >> 2}")

"""
Estructuras de control
"""

# Condicionales
my_string = "Moy" # Variable cualquiera
if my_string == "Moy":
    print("my_string es 'Moy'")
elif my_string == "Aarón": 
    print("my_string es 'Aarón'")
else: 
    print("my string no es 'Moy'")

# Iterativas
for k in range (11):
    print(k)

k = 0

while k <= 10:
    print(k)
    k += 1

# Manejo de excepciones: esto le dice a tu programa "Corre este comando pero si no funciona, no te rompas, solo intenta"
try:
    print(10 / 0)
except: 
    print("Se ha producido un error")

try: 
    print(10 / 1)
except: 
    print("Se ha producido un error")

# Ejercicio de dificultad extra: Crea un programa que imprima por consola todos los números comprendidos entre 10 y 55 (incluidos), pares, y que no son ni el 16 ni múltiplos de 3

for number in range(10, 56): # Para cada número de 10 hasta 55, haz algo. 
    if number % 2 == 0 and number != 16 and number % 3 != 0:
        print(number)

for number_1 in range(0, 101): 
    if number_1 % 3 == 0 and number_1 != 55 and number_1 % 2 != 0:
        print(number_1)
    
