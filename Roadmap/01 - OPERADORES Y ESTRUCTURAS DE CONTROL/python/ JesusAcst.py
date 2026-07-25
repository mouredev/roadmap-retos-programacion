# Operadores arimeticos
print("Operadores Aritméticos:")
print(f"Suma: 13 + 7 = {13 + 7}")
print(f"Resta: 13 - 7 = {13 - 7}")
print(f"Multiplicación: 13 * 7 = {13 * 7}")
print(f"División: 13 / 7 = {13 / 7}")
print(f"División entera: 13 // 7 = {13 // 7}")
print(f"Módulo: 13 % 7 = {13 % 7}")
print(f"Potencia: 13 ** 7 = {13 ** 7}")

# Operadores de comparación
print("Operadores de Comparación:")
print(f"Igualdad: 13 == 7 es {13 == 7}")
print(f"Desigualdad: 13 != 7 es {13 != 7}")
print(f"Mayor que: 13 > 7 es {13 > 7}")
print(f"Menor que: 13 < 7 es {13 < 7}")
print(f"Mayopr o igual: 13 >= 7 es {13 >= 7}")
print(f"Menor o igual: 13 <= 7 es {13 <= 7}")

# Operadores de asignación
print("Operadores de Asignación:")
number = 13  # Asignación
print(f"Valor inicial: {number}")
number += 7  # Suma y asignación
print(f"Después de += 7: {number}")
number -= 7  # Resta y asignación
print(f"Después de -= 7: {number}")
number *= 7  # Multiplicación y asignación
print(f"Después de *= 7: {number}")
number /= 7  # División y asignación
print(f"Después de /= 7: {number}")
number //= 7  # División entera y asignación
print(f"Después de //= 7: {number}")
number %= 7  # Módulo y asignación
print(f"Después de %= 7: {number}")
number **= 7  # Exponente y asignación
print(f"Después de **= 7: {number}")

# Operadores de Identidad
print("Operadores de Identidad:")
new_number = 13  # Asignación   
print(f"number is new_number: {number is new_number}")
print(f"number is not new_number: {number is not new_number}")

# Operadores de Pertenencia
print("Operadores de Pertenencia:")
print(f"'Y' in 'Python' = {'y' in 'python'}") # verifica si la letra 'y' está presente en la palabra 'python', y devuelve True o False dependiendo del resultado
print(f"'B' not in 'Python' = {'b' not in 'python'}") # verifica si la letra 'b' no está presente en la palabra 'python', y devuelve True o False dependiendo del resultado

# Operadores de bit
print("Operadores de Bit:")
print(f"AND: 13 & 7 = {13 & 7}") # 13 en bit es 1101 y 7 en bit es 0111, el resultado es 0101 que es 5 en decimal
print(f"OR: 13 | 7 = {13 | 7}") # 13 en bit es 1101 y 7 en bit es 0111, el resultado es 1111 que es 15 en decimal
print(f"XOR: 13 ^ 7 = {13 ^ 7}") # 13 en bit es 1101 y 7 en bit es 0111, el resultado es 1010 que es 10 en decimal
print(f"NOT: ~ 13 = {~13}") # 13 en bit es 1101, el resultado es 0010 que es -14 en decimal (en complemento a dos)
print(f"Desplazamiento a la izquierda: 13 << 2 = {13 << 2}") # 13 en bit es 1101, el resultado es 110100 que es 52 en decimal
print(f"Desplazamiento a la derecha: 13 >> 2 = {13 >> 2}") # 13 en bit es 1101, el resultado es 11 que es 3 en decimal


"""
Estructuras de control:
- Condicionales: if, elif, else
- Iterativas: for, while
- Excepciones: try, except, finally
"""

# Condicionales
print("Condicionales:")
my_string = 'Python'
if my_string == 'Python':
    print("La cadena es Python")
elif my_string == 'Java':
    print("La cadena es Java")
else:
    print("La cadena no es Python ni Java")

# Iterativas
print("Iterativas")
for i in range(11):
     print(i)

i = 0
while i < 11:
    i += 1
    print(i)

# Manejo de Excepciones
print("Manejo de Excepciones:")
try:
    print(10 / 0)
except ZeroDivisionError:
    print("No se puede dividir por cero")
finally:
    print("Finalizó el manjeo de excepciones")

print("Dificultad extra:")
for i in range(10, 55):
    if i % 2 == 0 and i != 16 and i % 3 != 0: # Si i es par, no es 16 y no es múltiplo de 3, entonces se imprime
        print(i)
    
    
