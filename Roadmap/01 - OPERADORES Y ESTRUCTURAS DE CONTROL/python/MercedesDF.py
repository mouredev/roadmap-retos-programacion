# Operadores Aritméticos
a = 10
b = 3
print("Suma:", a + b)  # Suma
print("Resta:", a - b)  # Resta
print("Multiplicación:", a * b)  # Multiplicación
print("División:", a / b)  # División (flotante)
print("División entera:", a // b)  # División entera
print("Módulo:", a % b)  # Residuo
print("Potencia:", a ** b)  # Potencia
print("")
# Operadores Lógicos
x = True
y = False
print("Lógico AND:", x and y)  # AND
print("Lógico OR:", x or y)  # OR
print("Lógico NOT x:", not x)  # NOT
print("Lógico NOT y:", not y)  # NOT
print("")
# Operadores de Comparación
print("Igualdad:", a == b)  # Igualdad
print("Diferente:", a != b)  # Diferencia
print("Mayor que:", a > b)  # Mayor que
print("Menor que:", a < b)  # Menor que
print("Mayor o igual que:", a >= b)  # Mayor o igual que
print("Menor o igual que:", a <= b)  # Menor o igual que
print("")
# Operadores de Asignación
c = 5
c += 2  # c = c + 2
print("Asignación (+=):", c)
c *= 3  # c = c * 3
print("Asignación (*=):", c)
print("")
# Operadores de Identidad
print("¿a es b?", a is b)  # Verifica si a y b son el mismo objeto
print("¿a no es b?", a is not b)  # Verifica si no lo son
print("")
# Operadores de Pertenencia
lista = [1, 2, 3, 4, 5]
print("¿2 en lista?", 2 in lista)  # Verifica si el 2 está en la lista
print("¿6 no en lista?", 6 not in lista)  # Verifica si el 6 no está en la lista
print("")
# Operadores de Bits
num = 6  # 110 en binario
print("AND de bits:", num & 3)  # AND a nivel de bits (110 & 011 = 010 = 2)
print("OR de bits:", num | 3)  # OR a nivel de bits (110 | 011 = 111 = 7)
print("XOR de bits:", num ^ 3)  # XOR a nivel de bits (110 ^ 011 = 101 = 5)
print("Desplazamiento a la izquierda:", num << 1)  # Desplazar bits a la izquierda (110 << 1 = 1100 = 12)
print("Desplazamiento a la derecha:", num >> 1)  # Desplazar bits a la derecha (110 >> 1 = 11 = 3)
print("")
# Ejemplos de estructuras de control
# Condicionales
if a > b:
    print("a es mayor que b")
elif a == b:
    print("a es igual a b")
else:
    print("a es menor que b")
print("")
# Bucle for
for i in range(5):
    print(f"Iteración {i} en el bucle for")
print("")
# Bucle while
contador = 0
while contador < 3:
    print(f"Iteración {contador} en el bucle while")
    contador += 1
print("")
# Manejo de excepciones
try:
    resultado = a / 0  # Error de división por cero
except ZeroDivisionError:
    print("Error: División por cero")
print("")
# Desafío extra: imprimir los números entre 10 y 55, pares, que no sean 16 ni múltiplos de 3
for num in range(10, 56):
    if num % 2 == 0 and num != 16 and num % 3 != 0:
        print(num)
