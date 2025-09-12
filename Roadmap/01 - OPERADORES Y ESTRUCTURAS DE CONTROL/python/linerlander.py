"""
Operadores
"""
#Operadores arimético
print(f'Suma: 10 + 3 = {10 + 3}') # Suma
print(f'Resta: 10 - 3 = {10 - 3}') #Resta
print(f'Multiplicación: 10 * 3 = {10 * 3}') # Multiplicación
print(f'División: 10 / 3 = {10 / 3}') # División
print(f'Modulo: 10 % 3 = {10 % 3}') # Modulo
print(f'Exponente: 10 ** 3 = {10 ** 3}') # Exponente
print(f'División: 10 // 3 = {10 // 3}') # División Entera

#Operadores de comparación
print(f'Igualdad: 10 == 3: {10 == 3}') # Igualdad
print(f'Desigualdad: 10 == 3: {10 != 3}') # Desigualdad
print(f'Mayor que: 10 > 3: {10 > 3}') # Mayor
print(f'Menor que: 10 < 3: {10 == 3}') # Menor
print(f'Mayor o igual que: 10 > 3: {10 >= 3}') # Mayor igual que
print(f'Menor o igual que: 10 < 3: {10 <= 3}') # Menor igual que

#Operadores lógicos
print(f'AND &&: 10 + 3 == 13 and 5 -1 == 4 es {10 + 3 == 13 and 5 -1 == 4}') # Operador and
print(f'OR ||: 10 + 3 == 13 or 5 -1 == 4 es {10 + 3 == 14 or 5 -1 == 4}') # Operador or
print(f'NOT !: 10 + 3 == 14 {not 10 + 3 == 14}') # Operador not

#Operadores de Asignación
my_number = 11 # Operador de asignación
print(my_number)
my_number += 1 # Suma y asignación
print(my_number)
my_number -= 1 # Resta y asignación
print(my_number)
my_number *= 2 # Multiplicación y asignación
print(my_number)
my_number /= 2 # División y asignación
print(my_number)
my_number %= 2 # Modulo y asignación
print(my_number)
my_number %= 2 # Modulo y asignación
print(my_number)
my_number **= 1 # Exponente y asignación
print(my_number)
my_number //= 1 # División entera y asignación
print(my_number)

#Operadores de indentidad

my_new_number = my_number
print(f'my_number is my_new_number es {my_number is my_new_number}') # Compara dirección de memoria
print(f'my_number is my_new_number es {my_number is not my_new_number}') # Negar la comparación de dirección de memoria

#Operadores de pertenencia
print(f'"u" in "more" = {"u" in "liner"}') # Comparar un dato este dentro de otro
print(f'"u" in "more" = {"b" not in "liner"}') # Negar Comparar un dato este dentro de otro

#Operadores de bit
a = 10 # 1010
b = 3 # 0011

print(f'AND: 10 & 3 {10 & 3}') # 0010
print(f'OR: 10 | 3 {10 | 3}') # 1011
print(f'XOR: 10 ^ 3 {10 ^ 3}') # 1001
print(f'NOT: ~10  {~10}')
print(f'Desplazamiento ala derecha: 10 >> 2 {10 >> 2}') # 1010 --> 0101 --> 0010
print(f'Desplazamiento ala izquierda: 10 << 2 {10 << 2}') # 101000 <-- 1010

'''
Estructruras de control
'''

#Condicionales
my_string = 'LinerDev'

if my_string == "LinerDev":
    print("My_string es 'LinerDev'")
elif my_string == "LanderDev":
    print("my_string no es 'LanderDev'")
else:
    print("my_string no es 'LinerDev'")

#Iterativas
for i in range(11):
    print(i)
i = 0
while i <= 10:
    print(i) 
    i += 1

#Manejo de excepciones
try:
    print(10/0)
except:
    print('Se ha producido un error')

finally:
    print('Ha finalizado el manejo de excepciones')

### Dificultada Extra ###

x = 10
while x <= 55:
    if x % 2 == 0 and x != 16 and x % 3 != 0:
        print(x)
        x += 1
    else:
        x += 1

for number in range(10,56):
    if number % 2 == 0 and number != 16 and number % 3 != 0:
        print(number)
