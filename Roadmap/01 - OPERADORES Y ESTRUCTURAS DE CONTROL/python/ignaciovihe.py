"""
Operadores
"""
#Operadores aritmeticos
print(f"10 + 4 = {10 + 4}")
print(f"10 - 4 = {10 - 4}")
print(f"10 * 4 = {10 * 4}")
print(f"10 / 4 = {10 / 4}")
print(f"10 ** 4 = {10 ** 4}")
print(f"10 % 4 = {10 % 4}")
print(f"10 // 4 = {10 // 4}")

#Operedores de comparación
print(f"Igualdad: 10 == 4 es: {10 == 4}")
print(f"Mayor que: 10 > 4 es: {10 > 4}")
print(f"Menor que: 10 < 4 es: {10 < 4}")
print(f"Mayor o igual que: 10 >= 4 es: {10 >= 4}")
print(f"Menor o igual que: 10 <= 10 es: {10 <= 10}")
print(f"Desigualdad: 10 != 4 es: {10 != 4}")

#Operadores de asignación
my_number = 4 #Asignacion
print(f"my_number = {my_number}")
my_number += 2 #Suma y asignación
print(f"my_number = {my_number}")
my_number -= 3 #Resta y asignación
print(f"my_number = {my_number}")
my_number *= 2 #Multiplicación y asignación
print(f"my_number = {my_number}")
my_number /= 2 #División y asignación
print(f"my_number = {my_number}")
my_number **= 2 #Exponente y asignación
print(f"my_number = {my_number}")
my_number %= 2 #Modulo y asignación
print(f"my_number = {my_number}")
my_number //= 2 #División entera y asignación
print(f"my_number = {my_number}")

#Operadores logicos
print(f"AND : 10 > 0 and 3 < 1 es: {10 > 0 and 3 < 1}")
print(f"OR : 10 > 0 or 3 < 1 es: {10 > 0 or 3 < 1}")
print(f"NOT 10 > 0 es: {not 10 > 0}")


#Operadores de identidad
my_number = 1
my_other_number = 1
#Para números pequeños, Python reutiliza los mismos objetos de memoria, por eso devuelve True
print(f"my_other_number is my_number es: {my_other_number is my_number}")
my_other_number = my_number
print(f"my_other_number is my_number es: {my_other_number is my_number}")
my_other_number = 3000
print(f"my_other_number is my_number es: {my_other_number is my_number}")
my_other_number = my_number
print(f"my_other_number is my_number es: {my_other_number is my_number}")
print(f"my_other_number is not my_number es: {my_other_number is not my_number}")


#Operadores de pertenencia
print(f"IN: 'a' in 'Hola, Python!' es: {'a' in 'Hola, Python!'}")
print(f"IN: 'u' in 'Hola, Python!' es: {'u' in 'Hola, Python!'}")
print(f"IN: 'u' not in 'Hola, Python!' es: {'u' not in 'Hola, Python!'}")

#Operadores de bits
a= 10 # 1010
b= 5  # 0101
print(f"AND: 10 & 5 = {10 & 5}")  # Ambos bits son '1' -- 0000
print(f"OR: 10 | 5 = {10 | 5}")  # Al menos 1 de los dos bits es '1' - 1111
print(f"XOR: 10 ^ 5 = {10 ^ 5}")  # Ambos bits son diferentes - 1111
print(f"NOT: ~10 = {~10}") # Invierte los bits 00001010 -> 11110101. En decimal es -(x+1)
print(f"Desplazamiento a la derecha: 10 >> 2 = {10 >> 3}")  # 0001
print(f"Desplazamiento a la izquierda: 10 << 2 = {10 << 3}")  # 1010000


"""
Estructuras de control
"""

#Condicionales
#IF
edad = 21
if edad < 18:
    print("Tarifa reducida por minoria de edad")
elif edad < 65:
    print("Tarifa normal")
else:
    print("Tarifa reducida por mayor de 65")

# MATCH - CASE

dia = "sabado"

match dia:
    case "lunes":
        print("Primer dia de la semana")
    case "viernes":
        print("Último día laborable")
    case "sabado" | "domingo":
        print("Fin de semana")
    case _:
        print("Dia normal")


#Iterativas

for num in range(11):
    print(num)

i = 0
while i < 11:
    print(i)
    i += 1

#Manejo de excepciones

a, b = 3, "4"
try:
    print(f"{a}/{b} = {int(a)/int(b)}")
except ZeroDivisionError as error:
    print(error)
except ValueError as error:
    print(error)

"""
Extra
Crea un programa que imprima por consola todos los números comprendidos
entre 10 y 55 (incluidos), pares, y que no son ni el 16 ni múltiplos de 3.
"""
for i in range(10,56,2):
    if (i % 3) and i != 16:
        print(i)