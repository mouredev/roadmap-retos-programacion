# Operadores Aritméticos:
a = 10
b = 3

suma = a + b
resta = a - b
multiplicacion = a * b
division = a / b
resto = a % b
division_entera = a // b
exponente = a ** b

print(suma, resta, multiplicacion, division, resto , division_entera, exponente)

# Operadores Lógicos:
p = True
q = False

y_logico = p and q
o_logico = p or q
negacion = not p

print(y_logico, o_logico, negacion)

# Operadores de Comparación:
x = 5
y = 10

igual = x == y
diferente = x != y
menor_que = x < y
mayor_que = x > y
menor_igual = x <= y
mayor_igual = x >= y

print(igual, diferente, menor_que, mayor_que, menor_igual, mayor_igual)

# Operadores de Asignación:
a = 5
b = 2

a += b
print(a)

a *= 3
print(a)

# Estructuras Condicionales:
x = 10

if x > 0:
    print("x es positivo")
elif x == 0:
    print("x es cero")
else:
    print("x es negativo")

# Bucle for:
for i in range(5):
    print(i)

# Bucle while:
n = 0

while n < 5:
    print(n)
    n += 1

# Estructuras de Control de Flujo usando break:
for i in range(10):
    if i == 5:
        break
    print(i)

# Estructuras de Control de Flujo usando continue
for i in range(5):
    if i == 2:
        continue
    print(i)


# DIFICULTAD EXTRA (opcional):
for num in range(10, 56):
    # Verificar si el número es par y no es el 16 ni múltiplo de 3
    if num % 2 == 0 and num != 16 and num % 3 != 0:
        print(num)
