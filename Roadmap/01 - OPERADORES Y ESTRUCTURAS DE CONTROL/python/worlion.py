# Operadores aritméticos
print(1 + 1) # Suma 


# Operadores de comparación
print(1 >= 1) # mayor que

# Operadores de asignación
a = 1

# Operadores lógicos
print(True and False)

# Operadores de identidad
print(5 is 3)

# Operadores de pertenencia
print(5 in [1, 2, 3, 4, 5])

# Operadores de bits
print(5 & 3)

# Estructura condicional (if-else)
x = 10
if x > 5:
    print("x is greater than 5")
else:
    print("x is less than or equal to 5")

# Estructura iterativa (for loop)
for i in range(1, 6):
    print(i)

# Estructura de excepción (try-except)
try:
    result = 10 / 0
    print(result)
except ZeroDivisionError:
    print("Cannot divide by zero")

# DIFICULTAD EXTRA (opcional):
# Estructura iterativa con condiciones adicionales
for i in range(10, 55, 2):
    if(i != 16 and i % 3 != 0):
        print(i)
