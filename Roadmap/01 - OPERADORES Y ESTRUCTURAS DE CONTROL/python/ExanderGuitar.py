# Operadores aritméticos
# Suma
x = 20
y = 5
suma = x + y
print(suma)

# Resta
resta = x - y
print(resta)

# Multiplicación
multiplicacion = x * y
print(multiplicacion)

# División
division = x / y
print(division)

# Módulo
modulo = x % y
print(modulo)

# Potencia
potencia = x ** y
print(potencia)

# División con resultado entero
divsion_entera = x // y
print(divsion_entera)

# Operaciones relacionales
# Mayor que
mayor = x > y
print(mayor)

# Menor que
menor = x < y
print(menor)

# Mayor o igual que
mayor_igual = x >= y
print(mayor_igual)

# Menor o igual que
menor_igual = x <= y
print(menor_igual)

# Igual que
igual = x == y
print(igual)

# No igual
no_igual = x != y
print(no_igual)

# Operadores lógicos
# Operador AND
operador_and = 5 > 10 and 3 < 5
print(operador_and)

# Operador OR
operador_or = 5 > 10 or 3 < 5
print(operador_or)

# Operador NOT
operador_not = not 5 > 10
print(operador_not)

# Operadores bit a bit
a = 0b0001
b = 0b0101

## Operador and
print(a & b)

## Operador or
print(a | b)

## Operador xor
print(a ^ b)

## Operador not
print(~b)

## Operador desplazamiento a la derecha
print(a >> b)

## Operador desplazamiento a la izquierda
print(a << b)

# Controles de flujo
## Sentencia if
if (5 > 3):
    print("Funciona")

if (3 < 1):
    print("Aqui no")
else:
    print("Aqui sí")

if (5 == 8):
    print("Mmmm")
elif(2 == 2):
    print("Yeah")
else:
    print("Hola?")

if True:
    pass

## Bucle for
for i in range(0, 5):
    print(i)

for i in "Python":
    print(i)

## Bucle while
j = 0
while (j < 5):
    print(j)
    j += 1

# Ejercicio extra
for i in range(10, 56):
    if(i % 2 == 0):
        if(i != 16 and i % 3 != 0):
            print(i)
