# OPERADORES

# Operadores aritméticos
print("-Operadores aritméticos-")
x = 15
y = 5

sum = x + y
print(f"Suma: 15 + 5 = {sum}")

sub = x - y
print(f"Resta: 15 - 5 = {sub}")

mul = x * y
print(f"Multiplicación: 15 * 5 = {mul}")

div = x / y
print(f"División: 15 / 5 = {div}")

module = x % y == 0
print(f"Módulo: 15 % 5 = {module}")

exponent = x ** y
print(f"Exponente: 15 ** 5 = {exponent}")

div_int = x // y
print(f"División entera: 15 // 5 = {div_int}")


# Operadores de comparación
print("-Operadores de comparación-")

equal = x == y
print(f"Igualdad: 15 == 5 es {equal}")

unequal = x != y
print(f"Desigual: 15 != 5 es {unequal}")

greaterThan = x > y
print(f"Mayor que: 15 > 5 es {greaterThan}")

lessThan = x < y
print(f"Menor que: 15 < 5 es {lessThan}")

greaterEqualThan = x >= y
print(f"Mayor o igual: 15 >= 5 es {greaterEqualThan}")

lessEqualThan = x <= y
print(f"Menor o igual: 15 <= 5 es {lessEqualThan}")


# Operadores lógicos
print("-Operadores lógicos-")
print(f"AND && : True and True = {True and True}")
print(f"OR || : True or False = {True or False}")
print(f"NOT ! : not True = {not True}")

# Operadores de asignación
print("-Operadores de asignación-")
my_int = 15  # Asignamos un valor
print(my_int)
my_int += 1  
print(f"Suma y asignación: {my_int}")
my_int -= 1  
print(f"Resta y asignación: {my_int}")
my_int *= 2  
print(f"Multiplicación y asignación: {my_int}")
my_int /= 2  
print(f"División y asignación: {my_int}")
my_int %= 2 
print(f"Módulo y asignación: {my_int}")
my_int **= 1  
print(f"Exponente y asignación: {my_int}")
my_int //= 1  
print(f"División entera y asignación: {my_int}")

# Operadores de identidad
print("-Operadores de identidad-")
print(f"x is y = {y is x}")
print(f"x is y = {y is not x}")

# Operadores de pertenencia
print("-Operadores de pertenencia-")
print(f"'z' in 'zetared' = {'z' in 'zetared'}")
print(f"'v' not in 'zetared' = {'v' not in 'zetared'}")

# Operadores de bit
print("-Operadores de bit-")
x = 15 # 1111
y = 5 # 0101
print(f"AND: x & y = {x & y}")  
print(f"OR: x | y = {x | y}")  
print(f"XOR: x ^ y = {x ^ y}")  
print(f"NOT: ~x = {~x}")
print(f"Desplazamiento a la derecha: x >> 1 = {x >> 1}")  
print(f"Desplazamiento a la izquierda: x << 1 = {x << 1}")  


# ESTRUCTURAS DE CONTROL
print("-Estructuras de control-")
# Condicionales
my_str = "Zeta"

if my_str == "ZetaRed":
    print("my_str es 'ZetaRed'")
elif my_str == "Zeta":
    print("my_str es 'Zeta'")
else:
    print("my_str no es 'ZetaRed' ni 'Zeta'")

# Iterativas
print("-Iterativas-")
for i in range(15):
    print(i)

i = 0

while i <= 15:
    print(i)
    i += 1

# Manejo de expepciones

try:
    print(15 / 0)
except:
    print("Error")
finally:
    print("Manejo de excepciones finalizadas")

# EJERCICIO EXTRA
#  * DIFICULTAD EXTRA (opcional):
#  * Crea un programa que imprima por consola todos los números comprendidos
#  * entre 10 y 55 (incluidos), pares, y que no son ni el 16 ni múltiplos de 3.

for num in range(10, 56):
    if num % 2 == 0 and num != 16 and num % 3 != 0:
        print(num)