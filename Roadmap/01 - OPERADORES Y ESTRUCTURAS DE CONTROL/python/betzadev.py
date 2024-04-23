print('\n--- OPERADORES Y ESTRUCTURAS DE CONTROL 🐍 ---')

while True:
    try:
        num1 = int(input("Ingrese el primer número: "))
        num2 = int(input("Ingrese el segundo número: "))
        break
    except ValueError:
        print("Por favor, ingrese números válidos.")
result = 0

print('\n🔷Operadores lógicos o booleanos')

x = True
y = False
resultado_and = x and y
resultado_or = x or y
resultado_not = not x
print(f"AND: {resultado_and}, OR: {resultado_or}, NOT: {resultado_not}")


print('\n🔷Operadores de comparación')

print(f"Igualdad: {num1} == {num2} es {num1 == num2}")
print(f"Desigualdad: {num1} != {num2} es {num1 != num2}")
print(f"Mayor que: {num1} > {num2} es {num1 > num2}")
print(f"Menor que: {num1} < {num2} es {num1 < num2}")
print(f"Mayor o igual que: {num1} >= {num1} es {num1 >= num1}")
print(f"Menor o igual que: {num1} <= {num2} es {num1 <= num2}")

print('\n🔷Operadores aritméticos')

# Operador suma (+)
result = num1 + num2
print(f"La suma de {num1} + {num2} es {result}")

# Operador resta (-)
result = num1 - num2
print(f"La resta de {num1} - {num2} es {result}")

# Operador multiplicación (*)
result = num1 * num2
print(f"La multiplicación de {num1} * {num2} es {result}")

# Operador división (/)
result = num1 / num2
print(f"La división de {num1} / {num2} es {result}")

# Operador módulo (%)
result = num1 % num2
print(f"El resto de la división de {num1} / {num2} es {result}")

print('\n🔷Operadores a nivel de bits')

num = 10
complemento = ~num
print(f"Complemento de {num}: {complemento}")

a = 5  # Representación binaria: 0101
b = 3  # Representación binaria: 0011
resultado_and = a & b
print(f"AND entre {a} y {b}: {resultado_and}")

x = 12  # Representación binaria: 1100
y = 6   # Representación binaria: 0110
resultado_or = x | y
print(f"OR entre {x} y {y}: {resultado_or}")

p = 9   # Representación binaria: 1001
q = 6   # Representación binaria: 0110
resultado_xor = p ^ q
print(f"XOR entre {p} y {q}: {resultado_xor}")

num_binario = 10  # Representación binaria: 1010
desplazamiento_izquierda = num_binario << 2
desplazamiento_derecha = num_binario >> 1
print(f"Desplazamiento izquierda: {desplazamiento_izquierda}, Desplazamiento derecha: {desplazamiento_derecha}")

num_rotacion = 15  # Representación binaria: 1111
rotacion_izquierda = (num_rotacion << 2) | (num_rotacion >> 2)
print(f"Rotación izquierda: {rotacion_izquierda}")


print('\n🔷Operadores de asignación')

x = 10
x += 5
x -= 3
x *= 2
print(f"Valor final de x: {x}")


print('\n🔷Operadores de identidad y pertenencia')

lista1 = [1, 2, 3]
lista2 = [1, 2, 3]
es_mismo_objeto = lista1 is lista2
esta_en_lista = 2 in lista1
print(f"Mismo objeto: {es_mismo_objeto}, Está en lista: {esta_en_lista}")


print('\n--- ESTRUCTURAS DE CONTROL ---')

print('\n🔷Condicionales (if-elif-else)')

edad = 18
if edad < 18:
    print("Eres menor de edad")
elif edad == 18:
    print("Tienes 18 años")
else:
    print("Eres mayor de edad")
    
print('\n🔷Iterativas (for y while)')
    
# Ciclo for
for i in range(5):
    print(f"Valor de i: {i}")

# Ciclo while
contador = 0
while contador < 3:
    print(f"Contador: {contador}")
    contador += 1


print('\n🔷Manejo de excepciones')

try:
    print(3 / 0)
except:
    print("Se ha producido un error")
finally:
    print("Ha finalizado el manejo de excepciones")


print('\n🔷EJERCICIO EXTRA:')
""" 
Crea un programa que imprima por consola todos los números comprendidos entre 10 y 55 (incluidos), pares, y
que no son ni el 16 ni múltiplos de 3.
"""
for number in range(10, 56):
    if number % 2 == 0 and number != 16 and number % 3 != 0:
        print(number)