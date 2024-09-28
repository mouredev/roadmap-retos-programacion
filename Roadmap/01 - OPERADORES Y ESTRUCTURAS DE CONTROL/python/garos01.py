# Operciones aritmeticas
a = 5
b = 3
suma = a + b
resta = a - b
multiplicacion = a * b
division = a / b
modulo = a % b
potencia = a**b

print(suma, resta, multiplicacion, division, modulo, potencia)


# Operadores de comparación
igual = a == b
diferente = a != b
mayor_que = a > b
menor_que = a < b

# Operadores lógicos
and_logico = (a > b) and (a < 20)
or_logico = (a < b) or (b > 0)
not_logico = not (a == b)

print(igual, diferente, mayor_que, menor_que, and_logico, or_logico, not_logico)


# Operadores de asignacion
a = 5
a += 3  # equivalente a: a = a + 3
print(a)


lista_1 = [1, 2, 3]
lista_2 = [1, 2, 3]

# Operadores de identidad
identidad = lista_1 is lista_2
no_identidad = lista_1 is not lista_2

# Operadores de pertenencia
pertenece = 1 in lista_1
no_pertenece = 4 not in lista_1

print(identidad, no_identidad, pertenece, no_pertenece)


# Operadores a nivel de bits
a = 5
b = 3

bitwise_and = a & b
bitwise_or = a | b
bitwise_xor = a ^ b
bitwise_not_a = ~a
left_shift = a << 1
right_shift = a >> 1

print(bitwise_and, bitwise_or, bitwise_xor, bitwise_not_a, left_shift, right_shift)

# Estructuras de control
# Condicionales
edad = 18

if edad >= 18:
    print("Eres mayor de edad")
else:
    print("Eres menor de edad")

# Iterativas
for i in range(5):
    print(i)

while edad < 21:
    print("Eres menor de 21 años")
    edad += 1

# Excepciones
try:
    resultado = 10 / 0
except ZeroDivisionError:
    print("Error: División por cero")
finally:
    print("Este bloque se ejecuta siempre")

# Ejercicio extra

lista_a = []

for i in range(10, 55):
    if i % 2 == 0:
        lista_a.append(i)
        if i % 3 == 0:
            lista_a.remove(i)
        elif i == 16:
            lista_a.remove(i)

print(lista_a)
