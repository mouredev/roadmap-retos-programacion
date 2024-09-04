# 01 - OPERADORES Y ESTRUCTURAS DE CONTROL

# - Crea ejemplos utilizando todos los tipos de operadores de tu lenguaje:
#   Aritméticos, lógicos, de comparación, asignación, identidad, pertenencia, bits...
#   (Ten en cuenta que cada lenguaje puede poseer unos diferentes)
# - Utilizando las operaciones con operadores que tú quieras, crea ejemplos
#   que representen todos los tipos de estructuras de control que existan
#   en tu lenguaje:
#   Condicionales, iterativas, excepciones...
# - Debes hacer print por consola del resultado de todos los ejemplos.

'''
Operadores
'''

#      Aritméticos
print(" ARITMETICAS")
print(f"Suma: 1 + 2 = {1 + 2}")
print(f"Resta: 1 - 2 = {1 - 2}")
print(f"Multiplicación: 1 * 2 = {1 * 2}")
print(f"División: 1 / 2 = {1 / 2}")
print(f"Módulo: 1 % 3 = {1 % 3}")
print(f"Exponente: 1 ** 3 = {1 ** 3}")
print(f"División entera: 1 // 3 = {1 // 3}")

#     Lógicos
print("\n LOGICAS")
print(f"AND: (10 + 3 == 13) and (5 - 1 == 4) es {(10 + 3 == 13) and (5 - 1 == 4)}")
print(f"OR: (10 + 3 == 13) or (5 - 1 == 3) es {(10 + 3 == 13) or (5 - 1 == 3)}")
print(f"NOT: not (10 + 3 == 13) es {not (10 + 3 == 13)}")

#    Comparación
print("\n COMPARACIÓN")
print(f"Igualdad: 10 == 3 es {10 == 3}")
print(f"Desigualdad: 10 != 3 es {10 != 3}")
print(f"Mayor que: 3 > 10 es {3 > 10}")
print(f"Mayor o igual: 10 <= 10 es {10 <= 10}")
print(f"Menor que: 3 < 10 es {3 < 10}")
print(f"Menor o igual: 3 <= 10 es {3 <= 10}")

#    Asignación
print("\n ASIGNACION")
my_number = 11 #asignación
print(my_number)
my_number += 1 #suma y asignación
print(my_number)
my_number -= 1 #resta y asignación
print(my_number)
my_number *= 2 #multiplicación y asignación
print(my_number)
my_number /= 2 #división y asignación
print(my_number)
my_number %= 2 #módulo y asignación 
print(my_number)
my_number **= 3 #exponente y asignación
print(my_number)
my_number //= 2 #división entera y asignación
print(my_number)

#    Operadores de identidad
print("\n IDENTIDAD")
my_new_number = my_number
print(f"my_number is my_new_number es {my_number is my_new_number}")
print(f"my_number is not my_new_number es {my_number is not my_new_number}")

#    Operadores de pertenencia
print("\n PERTENENCIA")
print(f"'u' in 'Guillesese' = {'u' in 'Guillesese'}")
print(f"'b' not in 'Guillesese' = {'b' not in 'Guillesese'}")

#    Operadores de bit
print("\n BIT")
a = 10 # 1010 
b = 3  # 0011
print(f"AND: 10 & 3 = {10 & 3}") #0010
print(f"OR: 10 | 3 = {10 | 3}") #1011
print(f"XOR: 10 ^ 3 = {10 ^ 3}") #1001
print(f"NOT: ~10 = {~10}")
print(f"Desplazamiento dcha: 10 >> 2 = {10 >> 2}") # 0010
print(f"Desplazamiento izda: 10 << 2 = {10 << 2}") #10100

'''
Estructuras de control 
'''

#     Condicionales
print("\n CONDICIONALES")
my_string = "sese"
if my_string == "guille": 
    print("my_string es 'guille'")
elif my_string == 'sese':
    print("my_string es 'sese'")
else:   
    print("my_string no es ni 'guille' ni 'sese'")

#   Iterativas
print("\n ITERATIVAS")
for i in range(10): 
    print (i)

i = 0
while i<=10: 
    print (i)
    i += 1

print("\n EXCEPCIONES")
try:
    print(10/0)
except:
    print("Error de división por 0")
finally:
    print("Fin del manejo de excepciones")

#DIFICULTAD EXTRA (opcional):
#  Crea un programa que imprima por consola todos los números comprendidos
#  entre 10 y 55 (incluidos), pares, y que no son ni el 16 ni múltiplos de 3.

for number in range(10,56): 
    if (number % 2 == 0) and (number != 16) and (number % 3 != 0):
        print(number)

    