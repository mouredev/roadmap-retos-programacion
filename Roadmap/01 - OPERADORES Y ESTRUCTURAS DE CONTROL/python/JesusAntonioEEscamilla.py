# #01 - Python -> Jesus Antonio Escamilla

"""
EJERCIÓ
"""

"""
Operaciones
"""
'''
ARITMÉTICA
'''
print(f"Suma: 3 + 5 = {3 + 5}")
print(f"Resta: 6 - 4 = {6 - 4}")
print(f"Multiplicación: 5 * 2 = {5 * 2}")
print(f"Division: 10 / 1 = {10 / 1}")
print(f"Division Entera: 10 // 2= {10 // 2}")
print(f"Modulo: 8 % 2 = {8 % 2}")
print(f"Exponente: 4 ** 2 = {4 ** 2}")

'''
ASIGNACIÓN
'''
number = 5
print(f"Asignación {number}")
number += 2
print(f"Asignación y Suma {number}")
number -= 1
print(f"Asignación y Resta {number}")
number *= 7
print(f"Asignación y Multiplicación {number}")
number /= 3
print(f"Asignación y Division {number}")
number //= 3
print(f"Asignación y Division Entera {number}")
number %= 6
print(f"Asignación y Modulo {number}")
number **= 3
print(f"Asignación y Exponente {number}")

'''
COMPARACIÓN
'''
print(f"Igualdad: 10 == 3 -> {10 == 3}")
print(f"Distinto: 2 != 1 -> {2 != 1}")
print(f"Mayor que: 5 > 4 -> {5 > 4}")
print(f"Menor que: 8 < 11 -> {8 < 11}")
print(f"Mayor que o igual: 7 >= 6 -> {7 >= 6}")
print(f"Menor que o igual: 9 <= 4 -> {9 <= 4}")

'''
LÓGICOS
'''
print(f"AND - &&: 10 == 10 and 5 == 6 {10 == 10 and 5 == 6}")
print(f"OR - ||: 7 == 3 or 3 == 3 {7 == 3 or 3 == 3}")
print(f"NOT - !: not 2 == 4 {not 2 == 4}")

'''
IDENTIDAD
'''
new_number = number
print(f"new_number is number: {new_number is number}")
print(f"new_number is not number: {new_number is not number}")

'''
BITS
'''
a = 10  # 1010 en binario
b = 4   # 0100 en binario

print(f"AND: a & b: {a & b}")
print(f"OR: a | b: {a | b}")
print(f"XOR: a ^ b: {a ^ b}")
print(f"NOT: a & b: {~a}")
print(f"Desplazamiento a la izquierda: a & b: {a << b}")
print(f"Desplazamiento a la derecha: a & b: {a >> b}")


"""
Estructura de Control
"""
'''
IF-ELIF-ELSE
'''
x = 10
if x > 0:
    print("Es positivo")
elif x == 0:
    print("Es cero")
else:
    print("Es Negativo")

'''
FOR
'''
frutas = ["Manzana", "Pera", "Cereza"]
for fruta in frutas:
    print(fruta)
    
for i in range(5):
    print(i)


'''
WHILE
'''
i = 0
while i < 5:
    print(i)
    i += 1


'''
TRY-EXCEPT-FINALLY
'''
try:
    resultado = 10/0
except:
    print("No se puede dividir entre 0")
finally:
    print("Fin del bloque try-except")


"""
EXTRA
"""
for num in range(10, 56):
    if num % 2 == 0 and num != 16 and num % 3 != 0:
        print(num)