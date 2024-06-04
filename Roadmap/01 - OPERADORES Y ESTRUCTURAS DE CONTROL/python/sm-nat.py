# OPERADORES ARITMETICOS

suma = 2 + 2
print(suma)

resta = 5 - 2
print(resta)

multiplicacion = 5 * 5
print(multiplicacion)

division = 10 / 2
print(division)

division_entera = 32 // 4 # devuelve el numero entero del cociente
print(division_entera)

modulo = 5 % 3 # Devuelve el resto de la división del primer operando por el segundo
print(modulo)

exponencial = 5 ** 2
print(exponencial)

#OPERADORES DE COMPARACIÓN

x = 5
y = 10

#igual
print(x == y) #falso
print(x == 5) #verdadero

#distinto
print(x != y) #verdadero
print(x != 5) #falso

#mayor que
print(x > y) #falso
print(x > 4) #verdadero

#menor que
print(x < y) #verdadero
print(x < 4) #falso

#mayor o igual que
print(x >= y) #falso
print(x >= 4) #verdadero, es mayor

#menor o igual
print(x <= y) #verdadero, es menor
print(x <= 4) #falso, es mayor

#OPERADORES DE ASIGNACIÓN

#asiganción
n = 33 
print(n)

#asignacion suma
n += 5 
print(n) 

#asignacion resta
n -= 5
print(n) 

#asignacion multiplicacion
n *= 5
print(n)

#asignacion division
n /= 5
print(n)

#asignacion division entera
n //= 5
print(n)

#asignacion exponencial
n **= 5
print(n)

#asignacion modulo
n %= 5
print(n)

#OPERADORES LÓGICOS

#and
print(True and True) #verdadero
print(True and False) #falso

#or
print(True or True) #verdadero
print(True or False) #verdadero

# not
print(not True) #falso
print(not False) #verdadero

#OPERADORES DE BIT

# Definición de variables
a = 5  # 0101 en binario
b = 3  # 0011 en binario

# AND a nivel de bits
resultado_and = a & b
print("a & b =", resultado_and)  # 0101 & 0011 = 0001 (1 en decimal)

# OR a nivel de bits
resultado_or = a | b
print("a | b =", resultado_or)  # 0101 | 0011 = 0111 (7 en decimal)

# XOR a nivel de bits
resultado_xor = a ^ b
print("a ^ b =", resultado_xor)  # 0101 ^ 0011 = 0110 (6 en decimal)

# NOT a nivel de bits
resultado_not = ~a
print("~a =", resultado_not)  # ~0101 = 1010 (en complemento a dos, esto representa -6)

# Desplazamiento a la izquierda
resultado_shift_left = a << 1
print("a << 1 =", resultado_shift_left)  # 0101 << 1 = 1010 (10 en decimal)

# Desplazamiento a la derecha
resultado_shift_right = a >> 1
print("a >> 1 =", resultado_shift_right)  # 0101 >> 1 = 0010 (2 en decimal)

