#operadores aritmeticos y asignacion

#suma
print("SUMA")
suma = 10 + 15
print(suma)
suma += 10
print(f"Suma + 10 = {suma}")

#resta
print("\nRESTA")
resta = 15 - 10
print(resta)
resta -= 5
print(f"Resta - 5 = {resta}")

#multiplicacion
print("\nMULTIPLICACION")
mult = 5 * 2
print(mult)
mult *= 2
print(f"mult x 2 = {mult}")

#division
print("\nDIVISION")
div = 20 / 2
print(div)
div /= 10
print(f"div / 10 = {div}")

#modulo
print("\nMODULO")
mod = 10 % 2
print(mod)
mod %= 1
print(f"mod % 1 = {mod}")

#exponente
print("\nEXPONENTE")
exp = 2 ** 2
print(exp)
exp **= 2
print(f"exp ** 2 = {exp}")

#cociente
print("\nCOCIENTE")
coc = 100 // 2
print(coc)
coc //= 2
print(f"coc // 2 = {coc}")

#operadores logicos

#and
print("\nAND")
print("True and False = ", True and False)
#or
print("\nOR")
print("True or True = ", True or True)
#not
print("\nNOT")
print("not True = ", not True)

#operadores de comparación

#identico
print("\nIDENTICO")
print("1 == 2 = ", 1 == 2)
#distinto
print("\nDISTINTO")
print("1 != 2 = ", 1 != 2)
#mayor
print("\nMAYOR QUE")
print("1 > 2 = ", 1 > 2)
#menor
print("\nMENOR QUE")
print("1 < 2 = ", 1 < 2)
#mayor o igual
print("\nMAYOR O IGUAL")
print("1 >= 2 = ", 1 >= 2)
#menor o igual
print("\nMENOR O IGUAL")
print("1 <= 2 = ", 1 <= 2)

# Definición de variables
a = 'Hola'
b = 'Hola'
c = [0, 1, 2]
d = [0, 1, 2]

# Operador is
print("\nIS")
print(f"a is b: {a is b}")  # True
print(f"id(a) == id(b): {id(a) == id(b)}")  # True

print(f"c is d: {c is d}")  # False (hace referencia al id, y son listas diferentes aunque con el mismo contenido)
print(f"id(c) == id(d): {id(c) == id(d)}")  # False (muestra que son objetos diferentes)

# Operador is not
print("\nIS NOT")
print(f"a is not b: {a is not b}")  # False (son el mismo objeto)
print(f"c is not b: {c is not b}")  # True (son diferentes tipos de objetos)

# Definición de la lista
x = [1, 2, 3, 4]

# Operador in
print(f"1 in x: {1 in x}")  # True (1 está en la lista x)
print(f"123 in x: {123 in x}")  # False (123 no está en la lista x)

# Operador not in
print(f"1 not in x: {1 not in x}")  # False (1 está en la lista x, así que no es verdad que no esté)
print(f"123 not in x: {123 not in x}")  # True (123 no está en la lista x, así que es verdad que no esté)

# Definición de variables
a = 10  # 1010 en binario
b = 4   # 0100 en binario

# Operador AND (&)
print("\nAND")
result = a & b
print(f"{a} & {b} = {result} (binario: {bin(result)})")
# Operador OR (|)
print("\nOR")
result = a | b
print(f"{a} | {b} = {result} (binario: {bin(result)})")
# Operador XOR (^)
print("\nXOR")
result = a ^ b
print(f"{a} ^ {b} = {result} (binario: {bin(result)})")
# Operador NOT (~)
print("\nNOT")
result = ~a
print(f"~{a} = {result} (binario: {bin(result)})")
# Desplazamiento a la izquierda (<<)
print("\nDESP. IZQ.")
result = a << 2
print(f"{a} << 2 = {result} (binario: {bin(result)})")
# Desplazamiento a la derecha (>>)
print("\nDESP. DER.")
result = a >> 2
print(f"{a} >> 2 = {result} (binario: {bin(result)})")

print("ESTRUCTURAS DE CONTROL")
#IF
print("IF")
if 1 < 2:
    print("1 < 2")
else:
    print("1 > 2")

#ITERATIVAS (FOR)
print("FOR")
for i in range(10):
    print(i)

    print("ESTRUCTURAS DE CONTROL")

# IF
print("IF")
if 1 < 2:
    print("1 < 2")
else:
    print("1 > 2")

# ITERATIVAS (FOR)
print("FOR")
for i in range(10):
    print(i)

# EXCEPCIONES
print("EXCEPCIONES")
try:
    resultado = 10 / 0
except ZeroDivisionError as e:
    print(f"Ocurrió una excepción: {e}")
finally:
    print("Esto se ejecuta siempre, haya o no una excepción")

print("El programa continúa ejecutándose después de manejar la excepción")

''' * DIFICULTAD EXTRA (opcional):
 * Crea un programa que imprima por consola todos los números comprendidos
 * entre 10 y 55 (incluidos), pares, y que no son ni el 16 ni múltiplos de 3.'''

for i in range(10, 51):
    if (i % 2 == 0) and (i != 16) and (i % 3 != 0):
        print(i)