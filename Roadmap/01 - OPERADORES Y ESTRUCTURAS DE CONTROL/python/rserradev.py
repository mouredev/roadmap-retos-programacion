# Ejemplos con todos los tipos de operadores del lenguaje
x = 5
y = 5

# Aritmeticos
addition = x + y
print(addition)

subtraction = x - y
print(subtraction)

multiplication = x * y
print(multiplication)

division = x / y
print(division)

modulus = x % y
print(modulus)

exponentiation = x ** y
print(exponentiation)

floorDivision = x // y
print(floorDivision)

# Asignación
x = 10
x += 3
x -= 3
x *= 3
x /= 3
x %= 3
print(x := 3)

# Comparación
x = 20
y = 20

print(x == y)	
print(x != y)	
print(x > y)
print(x < y)
print(x >= y)	
print(x <= y)

# Logicos
x = 30
y = 30

print(x < 5 and x < 10)
print(x < 5 or x < 10)
print(not(x < 5 and x < 10))

# Identidad

x = 1
y = "1"

print(x is y)
print(x is not y)

# BitWise (binary)

x = 99
y = 10

print(x & y)
print(x | y)
print(x ^ y)
print(x >> y)
print(x << y)

# Ejercicio opcional
x = 10
y = 56

for i in range(x, y):
    if (i % 3 != 0) and (i % 2 == 0) and (i != 16):
        print("numero " + str(i))
    elif (i == 55):
        print("numero " + str(i))
    else:
        print("no es multiplo de 3, no es numero par ni tampoco es el numero 16")