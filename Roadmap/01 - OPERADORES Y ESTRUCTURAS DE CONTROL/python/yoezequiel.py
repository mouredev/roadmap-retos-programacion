# Operadores aritméticos
num1 = 10
num2 = 5
print("Operadores aritméticos:")
print("Suma:", num1 + num2)
print("Resta:", num1 - num2)
print("Multiplicación:", num1 * num2)
print("División:", num1 / num2)
print("Módulo:", num1 % num2)
print("Exponente:", num1**num2)
print("División entera:", num1 // num2)

# Operadores de comparación
a = 10
b = 20
print("Operadores de comparación:")
print("Igualdad:", a == b)
print("Desigualdad:", a != b)
print("Mayor que:", a > b)
print("Menor que:", a < b)
print("Mayor o igual que:", a >= b)
print("Menor o igual que:", a <= b)

# Operadores lógicos
x = True
y = False
print("Operadores lógicos:")
print("AND:", x and y)
print("OR:", x or y)
print("NOT:", not x)

# Operadores de asignación
c = 5
print("Operadores de asignación:")
c += 3
print("Suma y asignación:", c)
c -= 2
print("Resta y asignación:", c)
c *= 4
print("Multiplicación y asignación:", c)
c /= 2
print("División y asignación:", c)

# Operadores de identidad
list1 = [1, 2, 3]
list2 = [1, 2, 3]
print("Operadores de identidad:")
print("is:", list1 is list2)
print("is not:", list1 is not list2)

# Operadores de pertenencia
print("Operadores de pertenencia:")
print("in:", 2 in list1)
print("not in:", 4 not in list1)

# Operadores a nivel de bits
num3 = 7
num4 = 3
print("Operadores a nivel de bits:")
print("AND a nivel de bits:", num3 & num4)
print("OR a nivel de bits:", num3 | num4)
print("XOR a nivel de bits:", num3 ^ num4)
print("Desplazamiento a la derecha:", num3 >> 1)
print("Desplazamiento a la izquierda:", num4 << 1)

# Estructuras de control
print("Estructuras de control:")
# Condicionales
if a > b:
    print("a es mayor que b")
elif a == b:
    print("a es igual a b")
else:
    print("a es menor que b")

# Iterativas
print("Bucle while:")
count = 0
while count < 5:
    print(count, end=" ")
    count += 1

print("Bucle for:")
for i in range(1, 6):
    print(i, end=" ")

# Excepciones
print("Manejo de excepciones:")
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Error: División por cero")

# Programa extra (DIFICULTAD EXTRA)
print("Números entre 10 y 55, pares, no 16 ni múltiplos de 3:")
for num in range(10, 56):
    if num % 2 == 0 and num != 16 and num % 3 != 0:
        print(num, end=" ")
