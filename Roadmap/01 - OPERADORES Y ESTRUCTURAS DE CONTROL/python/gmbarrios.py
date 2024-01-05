# Crea ejemplos utilizando todos los tipos de operadores de tu lenguaje: aritméticos, lógicos, de comparación, asignación, identidad, pertenencia, bits...

# 1. Aritméticos
a = 8
b = 3

suma = a + b
resta = a - b
multiplicación = a * b
division = a / b
division_entera = a // b
modulo = a % b
exponente = a ** b

print(f"Suma: {suma}")
print(f"Resta: {resta}")
print(f"Multiplicacion: {multiplicación}")
print(f"Division: {division}")
print(f"Division entera: {division_entera}")
print(f"Modulo: {modulo}")
print(f"Exponente: {exponente}")


# 2. De comparación
c = 10
d = 15

mayor_que = d > c
menor_que = c < d
mayor_igual = c >= d
menor_igual = d <= c
igual = c == d
no_igual = c != d

print(f"Mayor que: {mayor_que}")
print(f"Menor que: {menor_que}")
print(f"Mayor o igual que: {mayor_igual}")
print(f"Menor o igual que: {menor_igual}")
print(f"Igual: {igual}")
print(f"No es igual: {no_igual}")


# 3. Lógicos
x = True
y = False

and_result = x and y
or_result = x or y
not_result = not x

print(f"AND: {and_result}")
print(f"OR: {or_result}")
print(f"NOT: {not_result}")


# 4. Asignación
e = 10
e += 2
e -= 2
e *= 2
e /= 3
e //= 3
e %= 3
e **= 2

print(f"Asignación de 'e' tomando el ultimo valor: {e}")


# 5. Identidad
f = [1, 2, 3, 4, 5]
g = [6, 7, 8, 9]
h = f

identidad = f is g
identidad2 = f is h
identidad3 = g is not h
print(identidad)
print(identidad2)
print(identidad3)


# 6. Pertenencia
mi_lista = [1, 2, 3, 4, 5, 6]

pertenencia = 3 in mi_lista
pertenencia2 = 9 not in mi_lista
pertenencia3 = 1 not in mi_lista

print(pertenencia)
print(pertenencia2)
print(pertenencia3)


# 7. Bits
a = 2
b = 5

bitwise_and = a & b
bitwise_or = a | b
bitwise_xor = a ^ b
bitwise_not = ~a
bitwise_left_shift = a << 2
bitwise_right_shift = a >> 1

print(f"Bitwise AND: {bitwise_and}")
print(f"Bitwise OR: {bitwise_or}")
print(f"Bitwise XOR: {bitwise_xor}")
print(f"Bitwise NOT: {bitwise_not}")
print(f"Bitwise Left Shift: {bitwise_left_shift}")
print(f"Bitwise Right Shift: {bitwise_right_shift}")


# Utilizando las operaciones con operadores que quieras, crea ejemplos que representen todos los tipos de estructuras de control que existan en tu lenguaje: condicionales, iterativas, excepciones...

# Condicionales
a = 15

if a > 20:
    print(f"{a} es mayor que 20")
elif a == 20:
    print(f"{a} es igual a 20")
else:
    print(f"{a} es menor que 20")


# Iterativas
for sequence in range(10):
    print(sequence)

number = 5
while number < 10 and number > 1:
    print(number)
    number += 1


# Excepciones
try:
    result = 5 / 0
except ZeroDivisionError:
    print("No puede dividirse por cero")
finally:
    print("Este bloque siempre se ejecutará")

# DIFICULTAD EXTRA (opcional):
# Crea un programa que imprima por consola todos los números comprendidos entre 10 y 55 (incluidos), pares, y que no son ni el 16 ni múltiplos de 3.

for number in range(10, 56):
    if number % 2 == 0 and number != 16 and number % 3 != 0:
        print(number)