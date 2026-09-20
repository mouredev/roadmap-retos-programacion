## OPERADORES ARITMÉTICOS 
a = 10
b = 3
print("OPERACIONES ARITMÉTICAS CON DOS NÚMEROS")
print(f"a = {a}, b = {b}")
print(f"Suma a+b: {a+b}")
print(f"Resta a-b: {a-b} ")
print(f"Multiplicación a*b: {a*b}")
print(f"Cociente división a/b: {a/b}")
print(f"Cociente entero división a/b: {a//b}")
print(f"Resto división a/b: {a%b}")
print(f"Potenciación a**b: {a**b}")
print()

## OPERADORES DE COMPARACIÓN 
a = 6
b= 11
print("OPERACIONES DE COMPARACIÓN CON DOS NÚMEROS")
print(f"a = {a}, b = {b}")
print(f"a = b: {a == b}")
print(f"a != b: {a != b}")
print(f"a > b: {a > b}")
print(f"a >= b: {a >= b}")
print(f"a < b: {a < b}")
print(f"a <= b: {a <= b}")
print()

## OPERADORES LÓGICOS 
print("OPERACIONES LÓGICAS CON CONDICIONES VERDADERO/FALSO")
a = 3
b = 2
print(f"a = {a}, b = {b}")
print(f"Ejemplo AND: a > b y a < b: {a > b and a < b}")
print(f"Ejemplo OR: a > b o a < b: {a > b or a < b}")
print(f"Ejemplo NOT: not a > b: {not a > b}")
print()

## OPERADORES BINARIOS
print("OPERACIONES BINARIAS")
a = 0b1011
b = 0b0110
print(f"a = {a:04b}, b = {b:04b}")
print(f"AND a & b: {a & b:04b}")
print(f"OR a | b: {a | b:04b}")
print(f"XOR a ^ b: {a ^ b:04b}")
print(f"NOT ~a: {~a:04b}") # Realmente hace en formato entero x = -(x+1)
print(f"NOT & 1111 ~a: {~a & 0b1111:04b}") # De esta forma se muestra la pura inversión de bits
print(f"Desplazamiento a la izq. a << 1: {a << 1:04b}")
print(f"Desplazamiento a la der. a >> 1: {a >> 1:04b}")
print()
# Nota: los operadores binarios se pueden usar también sobre números enteros

## OPERADORES DE ASIGNACIÓN
print("OPERACIONES DE ASIGNACIÓN")
a = 15
print(f"Asignación: a = {a}")
a += 1
print(f"Suma y Asignación a += 1: a = {a}")
a -= 2
print(f"Resta y Asignación a -= 2: a = {a}")
a *= 3
print(f"Producto y Asignación a *= 3: a = {a}")
a /= 4
print(f"División y Asingación a /= 4: a = {a}")
a //= 2
print(f"División entera y Asignación a //= 2: a = {a}")
a %= 3
print(f"Resto División y Asingación a %= 3: a = {a}")
a **= 2
print(f"Potenciación y Asingación a ** 2: a = {a}")
print()

## OPERADORES DE IDENTIDAD
print("OPERACIONES DE IDENTIDAD")
a = "257"
b = "257"
print(f"a es b: {a is b}")
print(f"a no es b: {a is not b}")
print()
# En este caso a y b dan lo mismo porque python debe estar
# aplicando reutilizaciones para optimizar

## OPERADORES DE INCLUSIÓN
print("OPERADORES DE INCLUSIÓN")
print(f"H está en Hola Mundo: {"H" in "Hola Mundo"}")
print(f"h está en Hola Mundo: {"h" in "Hola Mundo"}")
print(f"X no está en Hola Mundo: {"X" not in "Hola Mundo"}")
print()

## ESTRUCTUTRAS DE CONTROL

print("ESTRUCTURAS CONDICIONALES")
a = 0
b = -20
print(f"a = {a}, b = {b}")
print("Condicional if, elif, else comparando a y b")
if a > b:
    print("Ejecuto sentencia en if porque a > b")
elif a < b:
    print("Ejecuto sentencia en elif porque a < b")
else:
    print("Ejecuto sentencia en else porque a = b")
print()

print("BUCLES")
a = 0
b = 10
print(f"a = {a}, b = {b}")
print("Bucle while suma 1 a variable hasta que a = b")
while a != b:
    a +=1
    print(f"a = {a}")
a = 0
print("Lo mismo con bucle for")
for i in range(b):
    a +=1
    print(f"a = {a}")
print()

print("MANEJO DE EXCEPCIONES")
a = 10
b = 0
print(f"a = {a}, b = {b}")
print("Dividir a/b")
try:
    print(a/b)
except:
    print("No se ha podido realizar la operación")