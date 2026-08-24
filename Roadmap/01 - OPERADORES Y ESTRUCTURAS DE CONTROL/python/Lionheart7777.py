"""
Operadores
"""

print(f"Suma: 10 + 3 = {10+3}")
print(f"resta: 10 - 3 = {10-3}")
print(f"Multi: 10 * 3 = {10*3}")
print(f"División: 10 / 3 = {10/3}")
print(f"Modulo : 10 % 3 = {10%3}")
print(f"Exponente : 10 ** 3 = {10 ** 3}")
print(f"División entera : 10 // 3 = {10 // 3}")


# operadores de comparación
print(f"igualdad: 10 == 3 = {10 ==3}")
print(f"Desigualdad: 10 != 3 = {10 != 3}")
print(f"Mayor que: 10 > 3 = {10 > 3}")
print(f"Menor que: 10 < 3 = {10 < 3}")
print(f"Mayor o igual que: 10 >= 3 = {10 >= 3}")
print(f"Menor o igual que: 10 <= 3 = {10 <= 3}")

# operadores lógicos
print(f"AND && : 10 + 3 == 13 and 5-1==4 es {10+3==13 and 5-1==4} ")
print(f"OR !! : 10 + 3 == 14 or 5-1==4  es {10+3 == 14 or 5-1==4}")
print(f"NOT : 10 + 3 == 14 es {not 10+3==14} ")

# operadores de asignación
my_number = 11 # asignacion
print(my_number)
my_number +=1 # suma y asignación
print(my_number)
my_number -=1 # resta y asignación
print(my_number)
my_number *=2 # multipl y asignación
print(my_number)
my_number /=2 # división y asignación
print(my_number)
my_number %=2 # módulo y asign
print(my_number)
my_number **=2 # exponente y asig
print(my_number)
my_number //=1 # división entera y asig
print(my_number)

#operadores de identidad
my_new_number = my_number
print(f"my_number is my_new_number es {my_number is my_new_number}")
print(f"my_number is not my_new_number es {my_number is not my_new_number}")

# operadores de pertenencia
print(f" 'u' in 'mouredev = {'u' in 'mouredev'}")
print(f" 'b' in 'mouredev = {'b' in 'mouredev'}")

# Operadores de bit
a = 10 # 1010
b = 3  # 0011
print(f"AND: 10 & 3 = {10 & 3}") # 0010
print(f"OR: 10 | 3 = {10 | 3}") # 1011
print(f"XOR: 10 ^ 3 = {10 ^ 3}") # 1001
print(f"NOT: ~10  3 = {~10}")
print(f"desplazamiento a la derecha : 10 >> 2 = {10 >> 2}") # 0010
print(f"Desplazamiento a la izquierda : 10 << 2 = {10 <<2}") # 101000

"""
Estructuras de Control
"""

# Condicionales

my_string = 'Lionheart'

if my_string == 'Lionheart' :
    print("my string es 'Lionheart'")
elif my_string == "Gatu":
    print("my string es 'Gatu'")
else:
    print("my string NO es 'Lionheart NI 'Gatu'")

    # Iterativas

for i in range(11):
        print(i)

i = 0
while i <= 10 :
    print(i)
    i +=1

# Manejo de excepciones
try:
    print(10/1)
except:
     print("se ha producido un error")
finally:
     print("ha finalizado el manejo de excepciones")

     """
 EXTRA
     """
for number in range(10,56):
     if number % 2 == 0 and number != 16 and number % 3 != 0 :
        print(number)
          