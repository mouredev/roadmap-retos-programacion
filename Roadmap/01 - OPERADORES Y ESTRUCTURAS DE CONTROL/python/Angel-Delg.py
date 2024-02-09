# Operadores Aritméticos
num1 = 10
num2 = 5
suma = num1 + num2
resta = num1 - num2
multiplicacion = num1 * num2
division = num1 / num2
modulo = num1 % num2
potencia = num1 ** num2

print("Operadores Aritméticos:")
print("Suma:", suma)
print("Resta:", resta)
print("Multiplicación:", multiplicacion)
print("División:", division)
print("Módulo:", modulo)
print("Potencia:", potencia)

# Operadores de Comparación
igual = (num1 == num2)
diferente = (num1 != num2)
mayor_que = (num1 > num2)
menor_que = (num1 < num2)
mayor_o_igual = (num1 >= num2)
menor_o_igual = (num1 <= num2)

print("\nOperadores de Comparación:")
print("Igual:", igual)
print("Diferente:", diferente)
print("Mayor que:", mayor_que)
print("Menor que:", menor_que)
print("Mayor o igual:", mayor_o_igual)
print("Menor o igual:", menor_o_igual)

# Operadores Lógicos
and_op = (num1 > 0) and (num2 < 0)
or_op = (num1 > 0) or (num2 < 0)
not_op = not (num1 > 0)

print("\nOperadores Lógicos:")
print("AND:", and_op)
print("OR:", or_op)
print("NOT:", not_op)

# Operadores de Asignación
a = 5
a += 2  # Equivalente a: a = a + 2
b = 10
b *= 3  # Equivalente a: b = b * 3

print("\nOperadores de Asignación:")
print("a:", a)
print("b:", b)

# Estructuras de Control - Condicionales
if num1 > num2:
    print("\nCondicionales:")
    print("num1 es mayor que num2")
elif num1 == num2:
    print("num1 es igual a num2")
else:
    print("num1 es menor que num2")

# Estructuras de Control - Iterativas
print("\nIterativas:")
for i in range(10, 56):
    if i % 2 == 0 and i != 16 and i % 3 != 0:
        print(i, end=" ")

# Estructuras de Control - Excepciones
try:
    resultado = num1 / 0
except ZeroDivisionError:
    print("\n\nExcepciones:")
    print("Error: División por cero")
