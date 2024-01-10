# Operadores Aritméticos
a = 5
b = 2
print("Suma:", a + b)
print("Resta:", a - b)
print("Multiplicación:", a * b)
print("División:", a / b)
print("Módulo:", a % b)
print("Incremento:", a + 1)
print("Decremento:", b - 1)

# Operadores de Comparación
x = 10
y = "10"
print("Igualdad:", x == y)
print("Igualdad ", x == int(y))
print("Desigualdad:", a != b)
print("Mayor que:", a > b)
print("Menor que o igual:", a <= b)

# Operadores Lógicos
p = True
q = False
print("AND lógico:", p and q)
print("OR lógico:", p or q)
print("NOT lógico:", not p)

# Operadores de Asignación
c = 3
c += 2
print("Asignación con adición:", c)

# Operadores de Identidad
print("Identidad:", x == 10)
print("Identidad:", y == 10)

# Operadores de Pertenencia
arreglo = [1, 2, 3]
print("Pertenece al arreglo:", 2 in arreglo)

# Operadores de Bits
num1 = 5  # Representación binaria: 0101
num2 = 3  # Representación binaria: 0011
print("AND a nivel de bits:", num1 & num2)  # Resultado: 0001 (1 en binario)
print("OR a nivel de bits:", num1 | num2)  # Resultado: 0111 (7 en binario)
print("Desplazamiento a la izquierda:", num1 << 1)  # Resultado: 1010 (10 en binario)
print("Desplazamiento a la derecha:", num1 >> 1)  # Resultado: 0010 (2 en binario)

# Estructuras de Control
# Condicionales
edad = 18
if 18 <= edad <= 125:
    print("Eres mayor de edad")
elif edad < 18:
    print("Eres menor de edad")
else:
    print("Edad no válida")

# Excepciones
try:
    resultado = 10 / 0
    print("Resultado:", resultado)
except ZeroDivisionError as error:
    print("Error:", error)
finally:
    print("Finalizado el bloque try-catch")

# Programa
for i in range(10, 56):
    if i % 2 == 0 and i != 16 and i % 3 != 0:
        print(i)