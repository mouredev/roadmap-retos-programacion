""" 
Operadores
"""
#Operadores aritmeticos
print(f"suma: 10 + 3 = {10 + 3}")
print(f"resta: 10 - 3 = {10 - 3}")
print(f"multiplicacion : 10 * 3 = {10 * 3}")
print(f"division : 10 / 3 = {10 / 3}")
print(f"modulo : 10 % 3 = {10 % 3}")
print(f"exponente: 10 ** 3 = {10 ** 3}")
print(f"division entera: 10 + 3 = {10 // 3}")

#operadores de comparacion

print(f"igualdad: 10 == 3 = {10 == 3}")
print(f"desigualdad: 10 != 3 = {10 != 3}")
print(f"mayor que: 10 > 3 = {10 > 3}")
print(f"menor que: 10 < 3 = {10 < 3}")
print(f"menor igual que: 10 >= 3 = {10 >= 10}")
print(f"mayor igual que: 10 <= 3 = {10 <= 3}")

#Operadores Logicos
print(f"AND && : 10 + 3 == 13 and 5 - 1 == 4 es {10 + 3 == 13 and 5 - 1 == 4} ")
print(f"OR || : 10 + 3 == 13 or 5 - 1 == 4 es {10 + 3 == 13 or 5 - 1 == 4} ")
print(f"NOT ! : not 10 + 3 == 14 es {not 10 + 3 == 14} ")

#Operadores de asignacion
my_number = 11
print(my_number)
my_number += 1
print(my_number)
my_number -= 1
print(my_number)
my_number *= 2
print(my_number)
my_number /= 2
print(my_number)
my_number **= 2
print(my_number)
my_number //= 2
print(my_number)
my_number %= 2
print(my_number)

#Operador de identidad
my_new_number = my_number
print(f"my_number is my_new_number es: {my_number is my_new_number}")
print(f"my_number is not my_new_number es: {my_number is not my_new_number}")

#Operadores de pertenencia
print(f"'a' in 'martin' = {'a' in 'martin'}")
print(f"'x' not in 'martin' = {'a' in 'martin'}")

#Operadores de bit
a = 10 #1010
b = 3 #0011
print(f"AND: 10 & 3 = {10 & 3}")
print(f"OR: 10 | 3 = {10 | 3}")
print(f"XOR: 10 ^ 3 = {10 ^ 3}")
print(f"NOT: 10 ~ 3 = {~10}")
print(f"Desplaza a la derecha: 10 >> 2 = {10 >> 2}")
print(f"Desplaza a la izquierda: 10 << 2 = {10 << 2}")

"""
Estructuras de control
"""
#Condicionales

my_sting = "martin"

if my_sting == "martin":
    print("my_sting es : 'martin'")
elif my_sting == "maca":
    print("my_string es 'maca'")
else:
    print("my_string no es 'martin' ni 'maca")

# Interactivas
    
for i in range(22):
    print(i)

i = 0
while i <= 10:
    print(i)
    i += 1
    
# Manejo de excepciones


try:
    print(10/0)
except:
    print("tiene un error") 
finally:
    print("finaliza el manejo de excepciones")
    
"""
Extra
"""
for number in range (10, 56):
    if number % 2 == 0 and number !=16 and number %3 != 0:
        print(number)



