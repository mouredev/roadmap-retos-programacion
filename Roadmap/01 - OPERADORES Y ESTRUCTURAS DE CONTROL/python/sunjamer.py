"""
operadores
"""

# operadores aritméticos

print(f"Suma 10 + 3 = {10 + 3}")
print(f"resta 8 - 4 = {8 - 4}")
print(f"multiplicar 2 * 10 = {2 * 10}")
print(f"división de 14 / 5 = {14 / 5}")
print(f"módulo de 14 / 5 = {14 % 5}")
print(f"exponente de 2 ** 5 = {2 ** 5}")
print(f"division entera 14 // 5 = {14 // 5}")

# operadores de comparación

print(f"igualdad 8 == 4 es {8 == 4}")
print(f"es diferente 14 != 5 = {14 != 5}")
print(f"es 14 > 5 {14 > 5}")
print(f"es 14 < 5 {14 < 5}")
print(f"es 14 >= 5 {14 >= 5}")
print(f"es 14 <= 5 {14 <= 5}")


# operadores logicos

print(f"AND es 7 + 5 = 12 and 9 - 6 == 3 {7 + 5 == 12 and 9 - 6 == 3}")
print(f"OR es 7 + 5 = 12 OR 9 - 6 == 4 {7 + 5 == 12 or 9 - 6 == 4}")
print(f"NOT 7 + 5 = 12 or 9 - 6 == 3 {not (9 + 6 == 3 or 7 + 5 == 12)}")

# operadores de asignación

my_variable = 33   # asignación de valor a variable
print(my_variable)
my_variable+=3
print(my_variable)
my_variable-=8
print(my_variable)
my_variable*=3
print(my_variable)
my_variable/=2
print(my_variable)
my_variable%=2
print(my_variable)
my_variable//=1
print(my_variable)

my_variable=0b01000
my_variable&=0b10101  # and
print(bin(my_variable))
my_variable|=0b01100 #or
print(bin(my_variable))
my_variable|=0b0101 
print(bin(my_variable))

# operadores de bit

var_a = 12  # 1100
var_b = 4 # 0100
print(f"AND: 12 & 4 = {12 & 4}")
print(f"OR: 12 & 4 = {12 | 4}")
print(f"XOR: 12 ^ 4 = {12 ^ 4}")
print(f"NOT: 12 ~ 4 = {12 ~ 4}")
print(f"Deslazamiento a la derecha 12 >> 4 = {12 >> 4}")
print(f"Deslazamiento a la izquierda 12 << 4 = {12 << 4}")

# operadores de identidad

my_variable = 25

my_new_varialble = my_variable
printf(f"my_variable is my_new_variable es {my_variable is my_new_variable}")
printf(f"my_variable is not my_new_variable es {my_variable is not my_new_variable}")

# operadores de pertenencia

printf(f"'p' en pedro = {'p' in pedro}")
printf(f"'p' no en pedro = {'p' not in pedro}")

# estructuras de control

mi_cadena = "sunjamer"
if mi_cadena == "sunjamer":
  print("mi_cadena és 'sunjamer'")
else:
  

# ejercicios

my_age = 46
my_weight = 70.3
my_complex_variable = 5j+1

print("Entra la base del triangulo")
base = int(input ())
print("Entra la altura del triangulo")
height = int(input())
area = 0.5*base*height
print(f"El area del triangulo es {area}")





