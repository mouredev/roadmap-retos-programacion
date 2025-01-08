"""
Operadores
"""

# Operadores aritmeticos

print(f"Suma: 100 + 50 = {100 + 50}")
print(f"Resta: 100 - 50 = {100 - 50}")
print(f"Multiplicacion: 10 * 5 = {10 * 5}")
print(f"Division: 12 / 3 = {12 / 3}")
print(f"Modulo: 16 % 3 = {16 % 3}")
print(f"Potencia: 12 ** 3 = {12 ** 3}")
print(f"Division Entera: 18 // 5 = {18 // 5}")

# Operadores relacionales

print(f"Mayor que(>): 10 > 5 = {10 > 5}")
print(f"Menor que(<): 10 < 5 = {10 < 5}")
print(f"Igual a: (==): {100 == 100}")
print(f"Mayor o igual que(>=): {75 >= 50}")
print(f"Menor o igual que(<=): {50 <= 75}")
print(f"Diferente(!=): {0 != 1}")

# Operadores Bit

print(f"AND(&): 2 & 3 = {2 & 3}")
print(f"OR(|): 2 | 3 = {2 | 3}")
print(f"XOR(^) 2 ^ 3 = {2 ^ 3}")
print(f"NOT(~) ~2 = {~2}")
print(f"Desplazamiento derecha bit(>>): 2 >> b = {2 >> 3}")
print(f"Desplazamiento izquierda bit(>>): 2 << b = {2 << 3}")

# Operadores de asignacion

my_var = 10 # Asignacion
print(my_var)

my_var += 5 # Suma y asignacion
print(my_var)

my_var -= 5 # Resta y asignacion
print(my_var)

my_var *= 3 # Multiplicacion y asignacion
print(my_var)

my_var /= 2 # Division y asignacion
print(my_var)

my_var %= 4 # Modulo y asignacion
print(my_var)

my_var **= 3 # Potencia y asignacion
print(my_var)

my_var //= 4 # Division entera y asignacion
print(my_var)

my_new_var = 50
my_new_var &= 18 # AND bit y asignacion
print(my_new_var)

my_new_var |= 3 # OR bit y asignacion
print(my_new_var)

my_new_var ^= 3 # XOR bit y asignacion
print(my_new_var)

my_new_var >>= 3 # Desplazamiento derecha bit y asignacion
print(my_new_var)

my_new_var <<= 3 # Desplazamiento izquierda bit y asignacion
print(my_new_var)

# Operadores Logicos

print(f"AND(and): 5 > 2 and 10 < 20 = {5 > 2 and 10 < 20}")
print(f"OR(or): 5 > 2 or 10 > 20 = {5 > 2 or 10 > 20}")
print(f"NOT(not): not(5 < 2) = {not(5 < 2)}")

# Operadores de pertenencia

a = [1, 2, 3, 4, 5]

print(3 in a)
print(12 not in a)
print(15 in a)

b = "Hello World"

print("World" in b)
print("code" not in b)

# Operadores de identidad

a = 3
b = 3
c = 4

print(a is b)
print(a is not c)
print(b is c)