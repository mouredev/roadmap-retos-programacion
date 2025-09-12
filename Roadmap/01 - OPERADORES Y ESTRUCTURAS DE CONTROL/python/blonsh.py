"""
Crear ejemplos de operadores
"""

## Operadores aritméticos
a = 10
b = 3

print("Suma:", a + b)            # 13
print("Resta:", a - b)          # 7
print("Multiplicación:", a * b) # 30
print("División:", a / b)       # 3.333...
print("Módulo:", a % b)         # 1
print("Exponente:", a ** b)     # 1000
print("División entera:", a // b) # 3

## Operadores de comparación
m = 5
n = 7

print("Igual a:", m == n)         # False
print("Distinto de:", m != n)     # True
print("Mayor que:", m > n)        # False
print("Menor que:", m < n)        # True
print("Mayor o igual:", m >= n)  # False
print("Menor o igual:", m <= n)  # True

##Operadores lógicos
x = True
y = False

print("AND:", x and y)     # False
print("OR:", x or y)       # True
print("NOT x:", not x)     # False

## Operadores de asignación
num = 5
print("Valor inicial:", num)    # 5

num += 2
print("Suma y asigna:", num)    # 7

num -= 1
print("Resta y asigna:", num)   # 6

num *= 3
print("Multiplica y asigna:", num) # 18

num /= 2
print("Divide y asigna:", num)  # 9.0

num %= 4
print("Módulo y asigna:", num)  # 1.0

num **= 3
print("Exponente y asigna:", num) # 1.0

num //= 2
print("División entera y asigna:", num) # 0.0

## Operadores de identidad
a = [1, 2, 3]
b = a
c = [1, 2, 3]

print("a es b:", a is b)     # True
print("a es c:", a is c)     # False
print("a no es c:", a is not c) # True

## Operadores de pertenencia
lista = [1, 2, 3, 4, 5]

print("2 en lista:", 2 in lista)       # True
print("10 en lista:", 10 in lista)     # False
print("10 no en lista:", 10 not in lista) # True

## Operadores de bit
a = 5   # en binario:  0101
b = 3   # en binario:  0011


print("a en binario:", bin(a))   # 0b101
print("b en binario:", bin(b))   # 0b11

# AND (y bit a bit)
print("AND (a & b):", a & b)     # 1  (0001)

# OR (o bit a bit)
print("OR (a | b):", a | b)      # 7  (0111)

# XOR (o exclusivo bit a bit)
print("XOR (a ^ b):", a ^ b)     # 6  (0110)

# NOT (negación bit a bit)
print("NOT (~a):", ~a)           # -6 (complemento a 2)

# Desplazamiento a la izquierda
print("a << 1:", a << 1)         # 10 (1010)

# Desplazamiento a la derecha
print("a >> 1:", a >> 1)         # 2  (0010)

## Estructuras de control

# Condicionales
calificacion = int(input("Ingresa tu calificación (0–100): "))

if calificacion >= 90:
    print("Excelente, obtuviste una A.")
elif calificacion >= 80:
    print("Muy bien, obtuviste una B.")
elif calificacion >= 70:
    print("Bien, obtuviste una C.")
elif calificacion >= 60:
    print("Pasaste, obtuviste una D.")
else:
    print("Reprobaste, obtuviste una F.")

## Iterativas

# Pedir calificaciones de 3 estudiantes
for i in range(3):
    calificacion = int(input(f"Ingrese la calificación del estudiante {i+1} (0–100): "))
    
    if calificacion >= 90:
        print("Excelente, obtuviste una A.")
    elif calificacion >= 80:
        print("Muy bien, obtuviste una B.")
    elif calificacion >= 70:
        print("Bien, obtuviste una C.")
    elif calificacion >= 60:
        print("Pasaste, obtuviste una D.")
    else:
        print("Reprobaste, obtuviste una F.")

# Pedir calificaciones hasta que el usuario escriba -1
while True:
    calificacion = int(input("Ingrese una calificación (0–100) o -1 para salir: "))
    
    if calificacion == -1:
        print("Fin del programa.")
        break
    
    if calificacion >= 90:
        print("Excelente, obtuviste una A.")
    elif calificacion >= 80:
        print("Muy bien, obtuviste una B.")
    elif calificacion >= 70:
        print("Bien, obtuviste una C.")
    elif calificacion >= 60:
        print("Pasaste, obtuviste una D.")
    else:
        print("Reprobaste, obtuviste una F.")

## Manejo de excepciones
try:
    x = int(input("Ingresa un número: "))
    resultado = 10 / x
    print("El resultado es:", resultado)

except ZeroDivisionError:
    print("Error: No puedes dividir entre cero.")

except ValueError:
    print("Error: Debes ingresar un número válido.")

else:
    print("Todo salió bien.")

finally:
    print("Esto se ejecuta siempre, ocurra o no un error.")

""""Extra"""
for num in range(10, 56):  # desde 10 hasta 55 inclusive
    if num % 2 == 0 and num != 16 and num % 3 != 0:
        print(num)
