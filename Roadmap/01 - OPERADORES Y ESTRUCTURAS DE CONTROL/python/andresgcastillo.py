# Operadores aritméticos
suma = 5 + 3
resta = 5 - 3
multiplicacion = 5 * 3
division = 5 / 3
modulo = 5 % 3
exponente = 5 ** 3
division_entera = 5 // 3

print("Operadores aritméticos:", suma, resta, multiplicacion, division, modulo, exponente, division_entera)

# Operadores de comparación
igual = 5 == 3
no_igual = 5 != 3
mayor_que = 5 > 3
menor_que = 5 < 3
mayor_o_igual_que = 5 >= 3
menor_o_igual_que = 5 <= 3

print("Operadores de comparación:", igual, no_igual, mayor_que, menor_que, mayor_o_igual_que, menor_o_igual_que)

# Operadores lógicos
and_logico = True and False
or_logico = True or False
not_logico = not True

print("Operadores lógicos:", and_logico, or_logico, not_logico)

# Operadores de asignación
a = 5
a += 3
a -= 3
a *= 3
a /= 3
a %= 3
a **= 3
a //= 3

print("Operadores de asignación:", a)

# Operadores de identidad
a = 5
b = a
es = a is b
no_es = a is not b

print("Operadores de identidad:", es, no_es)

# Operadores de pertenencia
lista = [1, 2, 3, 4, 5]
pertenece = 3 in lista
no_pertenece = 6 not in lista

print("Operadores de pertenencia:", pertenece, no_pertenece)

# Operadores de bits
and_bits = 5 & 3
or_bits = 5 | 3
not_bits = ~5
xor_bits = 5 ^ 3
desplazamiento_derecha = 5 >> 3
desplazamiento_izquierda = 5 << 3

print("Operadores de bits:", and_bits, or_bits, not_bits, xor_bits, desplazamiento_derecha, desplazamiento_izquierda)

# Estructuras de control
# Condicionales
if 5 > 3:
    print("5 es mayor que 3")
else:
    print("5 no es mayor que 3")

# Iterativas
for i in range(5):
    print(i)

i = 0
while i < 5:
    print(i)
    i += 1

# Excepciones
try:
    print(5 / 0)
except ZeroDivisionError:
    print("No se puede dividir por cero")

#Dificultad Extra
# Recorremos el rango de números del 10 al 55 (incluidos)
for i in range(10, 56):
    # Comprobamos si el número es par, no es 16 y no es múltiplo de 3
    if i % 2 == 0 and i != 16 and i % 3 != 0:
        print(i)