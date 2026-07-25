# Operadores en Python

#Aritmeticos

print(f"Suma 8 + 9 = {8+9}")
print(f"Resta 18 - 7 = {18-7}")
print(f"Multiplicacion 6 * 5 = {6*5}")
print(f"Division 10 / 3 = {10/3}")
print(f"Modular 10 % 3 = {10%3}")
print(f"Exponente 10 ** 3 = {10**3}")
print(f"Division entera 10//3 = {10//3}")

#Comparacion

print(f"Igualdad 5 = 5 {5==5}")
print(f"Desigualdad 5 != 5 {5!=5}")
print(f"Mayor que 5 > 5 {5>5}")
print(f"Mayor o igual que 5 >= 5 {5 >= 5}")
print(f"Menor que 5 < 5 {5 < 5}")
print(f"Menor o igual que 5 <= 5 {5 <= 5}")

#Logicos

print(f"AND &&: 5 + 2 == 7 and 9 - 8 == 1 es {5 + 2 == 7 and 9 - 8 == 1}")
print(f"OR ||: 5 + 2 == 7 or 9 - 8 == 3 es {5 + 2 == 7 or 9 - 8 == 3}")
print(f"NOT !: !6 + 8 == 14  es {not 6 + 8 == 14 }")

#Asignacion

my_number = 16
print(my_number)
my_number += 2
print(my_number)
my_number -= 4
print(my_number)
my_number *= 2
print(my_number)
my_number /= 4
print(my_number)
my_number **= 2
print(my_number)
my_number %= 2
print(my_number)
my_number //= 4
print(my_number)


#Identidad 

my_new_number = my_number
print(f"My new number is my number es {my_new_number is my_number}")
print(f"My new number is not my number es {my_new_number is not my_number}")

#Pertenencia 

print(f"'s' in 'steven' {'s' in 'steven'}")
print(f"'f' in 'steven' {'f' in 'steven'}")
print(f"'s' not in 'steven' {'s' not in 'steven'}")

#Bit

a = 10 # 1010
b = 5  # 0101

print(f"AND: 10 & 5 = {10 & 5}") #0000
print(f"OR: 10 | 5 = {10 | 5}") #1111
print(f"XOR: 10 ^ 5 = {10 ^ 5}") #1111
print(f"NOT: ~10 = {~10}")
print(f"Desplazamiento a la derecha 10 >> 1 = {10 >> 1}") #0101
print(f"Desplazamiento a la izquierda 10 << 1 = {10 << 1}") #101000


"""
Estructuras de control
"""

#Condicionales

my_str= "SNaoj"

if my_str == "SNaoj":
    print("my_str es 'SNaoj'")
elif my_str == "Mouredev":
    print("my_str es 'Mouredev'")
else: 
    print("my_str no es 'Snaoj' ni 'Mouredev")

#Iterativas

for i in range (11):
    print(i)

i = 0
while i <= 10:
    print(i)
    i += 2

# Manejo de excepciones
try:
    print(50 / 2)
except:
    print("Se ha producido un error")
finally:
    print("Ha finalizado el manejo de excepciones")


#Extra

for number in range (10, 56):
    if number % 2 == 0 and number != 16 and number % 3 != 0:
        print(number)
        