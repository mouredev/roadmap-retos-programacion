"""
Operadores
"""

# Operadores aritmeticos

print(f"Suma: 10 + 3 = {10 + 3}")

print(f"Resta: 10 - 3 = {10 - 3}")

print(f"Multiplicacion: 10 * 3 = {10 * 3}")

print(f"Division: 10 / 3 = {10 / 3}")

print(f"Modulo: 10 % 3 = {10 % 3}")

print(f"Exponencial: 10 ** 3 = {10 ** 3}")

#Operadores de comparacion

print(f"Igualdad: 10 == 3 es {10 == 3}")

print(f"Desigualdad: 10 != 3 es {10 != 3}")

print(f"Mayor que: 10 > 3 es {10 > 3}")

print(f"Menor que: 10 < 3 es {10 < 3}")

print(f"Mayor o igual que: 10 >= 3 es {10 >= 10}")

print(f"Menor o igual que: 10 <= 3 es {10 <= 3}")

print(f"Menor o igual que: 10 <= 3 es {10 <= 3}")

#Operadores logicos

print(f"AND &&: 10 + 3 == 13 and 5 - 1 == 4 es {10 + 3 == 13 and 5 - 1 == 4}")

print(f"OR ||: 10 + 3 == 14 or 5 - 1 == 4 es {10 + 3 == 14 or 5 - 1 == 4}")

print(f"NOT !: not 10 + 3 == 14 es {not 10 + 3 == 14}")

#Operadores de asignacion

my_number = 11 #asignacion
print(my_number)

my_number += 1 # suma y asignacion
print(my_number)

my_number -= 1 # resta y asignacion
print(my_number)

my_number *= 1 # multiplicacion y asignacion
print(my_number)

my_number /= 1 # division y asignacion
print(my_number)

my_number %= 1 # modulo y asignacion
print(my_number)

my_number **= 1 # exponente y asignacion
print(my_number)

my_number //= 1 # division entera y asignacion
print(my_number)

#Operadores de identidad

my_new_number = my_number

print(f"my_number is my_new_number es {my_number is my_new_number}")

print(f"my_number is not my_new_number es {my_number is not my_new_number}")

#Operadores de pertenencia

print(f"'u' in 'mouse' ={'u' in 'mouse'}")

print(f"'b not in 'mouse' ={'b' not in 'mouse'}")

#Operadores de bit

a = 10 # 1010
b = 3 # 0011

print(f"AND: 10 & 3 = {10 & 3}") # 0010

print(f"OR: 10 | 3 = {10 | 3}") # 1011

print(f"XOR: 10 ^ 3 = {10 ^ 3}") # 1001

print(f"NOT: ~10 = {~10}")

print(f"DESPLAZAMIENTO  A LA DERECHA: 10 >> 2 = {10 >> 2}") # 0010

print(f"DESPLAZAMIENTO  A LA IZQUIERDA: 10 << 2 = {10 << 2}") # 101000

"""
Estructuras de control
"""

# Condicionales

my_string = "VictorRivero"

if my_string == "VictorRivero":
    print("my_string es: 'VictorRivero'")
elif my_string == "Juan":
    print("my_string es Juan")
else:
    print("my_string no es 'VictorRivero'")

#Iternativas 

for i in range(11):
    print(i)

i = 0 

while i <= 10:
    print(i)
    i += 1

#Manejo de excepciones

try: 
    print(10 / 0)
except:
    print("Se ha producido un error")
finally:
    print("Ha finalizado el manejo de excepciones")

"""
Extra
"""

for number in range(10, 56):
    if number % 2 == 0 and number != 16 and number %3 != 0:
        print(number)
