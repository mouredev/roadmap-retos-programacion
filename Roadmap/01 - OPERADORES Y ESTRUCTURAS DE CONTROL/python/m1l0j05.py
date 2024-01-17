# Operadores Aritméticos:
# 1. `+` (suma)
# 2. `-` (resta)
# 3. `*` (multiplicación)
# 4. `/` (división)
# 5. `%` (módulo - devuelve el resto de una división)
# 6. `**` (exponente)
# 7. `//` (división entera -  devuelve el cociente de la división redondeado hacia abajo al entero más cercano)

a = 10
b = 3

addition = a + b
subtraction = a - b
multiplication = a * b
division = a / b
modulo = a % b
exponent = a ** b
integer_division = a // b

print('\nOPERADORES ARITMETICOS\n')
print(addition)
print(subtraction)
print(multiplication)
print(division)
print(modulo)
print(exponent)
print(integer_division)


# Operadores de Asignación:
# 1. `=` (asignación)
# 2. `+=` (suma y asigna)
# 3. `-=` (resta y asigna)
# 4. `*=` (multiplica y asigna)
# 5. `/=` (divide y asigna)
# 6. `%=` (módulo y asigna)
# 7. `**=` (exponente y asigna)
# 8. `//=` (división entera y asigna)
# 9. `&=` (AND bit a bit y asigna) -> Este operador realiza un AND bit a bit entre dos variables y luego asigna el resultado a la variable de la izquierda. Ejemplo: x &= y es equivalente a x = x & y.
# 10. `|=` (OR bit a bit y asigna) -> Realiza un OR bit a bit entre dos variables y asigna el resultado a la variable de la izquierda. Ejemplo: x |= y es equivalente a x = x | y.
# 11. `^=` (XOR bit a bit y asigna) -> Ejecuta un XOR bit a bit entre dos variables y asigna el resultado a la variable de la izquierda. Ejemplo: x ^= y es equivalente a x = x ^ y.
# 12. `>>=` (desplaza a la derecha y asigna) -> Desplaza los bits de la variable de la izquierda a la derecha por el número de posiciones indicadas por la variable de la derecha y luego asigna el resultado. Ejemplo: x >>= y es equivalente a x = x >> y.
# 13. `<<=` (desplaza a la izquierda y asigna) -> Desplaza los bits de la variable de la izquierda a la izquierda por el número de posiciones indicadas por la variable de la derecha y luego asigna el resultado. Ejemplo: x <<= y es equivalente a x = x << y.

# Los operadores de asignación del 9 al 13 en Python son operadores 
# compuestos que combinan una operación bit a bit con una asignación.

print('\nOPERADORES DE ASIGNACION\n')

c = 5
c += 2  # c es ahora 7
c -= 1  # c es ahora 6
c *= 2  # c es ahora 12
c /= 4  # c es ahora 3.0
c %= 3  # c es ahora 0.0
c **= 2 # c es ahora 0.0
c //= 2 # c es ahora 0.0

# Inicialización de variables
x = 4  # 100 en binario
y = 3  # 011 en binario

# Operador &= (AND bit a bit y asigna)
x_and_assign = x  # Copiamos x para no modificar el original
x_and_assign &= y # Equivalente a x_and_assign = x_and_assign & y
# x_and_assign es ahora 0 (000 en binario)

# Operador |= (OR bit a bit y asigna)
x_or_assign = x  # Copiamos x para no modificar el original
x_or_assign |= y # Equivalente a x_or_assign = x_or_assign | y
# x_or_assign es ahora 7 (111 en binario)

# Operador ^= (XOR bit a bit y asigna)
x_xor_assign = x  # Copiamos x para no modificar el original
x_xor_assign ^= y # Equivalente a x_xor_assign = x_xor_assign ^ y
# x_xor_assign es ahora 7 (111 en binario)

# Operador >>= (desplaza a la derecha y asigna)
x_shr_assign = x  # Copiamos x para no modificar el original
x_shr_assign >>= 1 # Equivalente a x_shr_assign = x_shr_assign >> 1
# x_shr_assign es ahora 2 (010 en binario)

# Operador <<= (desplaza a la izquierda y asigna)
x_shl_assign = x  # Copiamos x para no modificar el original
x_shl_assign <<= 1 # Equivalente a x_shl_assign = x_shl_assign << 1
# x_shl_assign es ahora 8 (1000 en binario)

# Resultados
print("AND bit a bit y asigna (x &= y):", x_and_assign)
print("OR bit a bit y asigna (x |= y):", x_or_assign)
print("XOR bit a bit y asigna (x ^= y):", x_xor_assign)
print("Desplaza a la derecha y asigna (x >>= 1):", x_shr_assign)
print("Desplaza a la izquierda y asigna (x <<= 1):", x_shl_assign)


# Operadores de Comparación:
# 1. `==` (igual a)
# 2. `!=` (diferente de)
# 3. `>` (mayor que)
# 4. `<` (menor que)
# 5. `>=` (mayor o igual que)
# 6. `<=` (menor o igual que)


print('\nOPERADORES DE COMPARACION\n')

d = 5
e = 10

equals = d == e # False
different = d != e # True
greater_than = d > e # False
less_than = d < e # True
greater_equal = d >= e # False
less_equal = d <= e # True

print(equals)
print(different)
print(greater_than)
print(less_than)
print(greater_equal)
print(less_equal)


# Operadores Lógicos:
# 1. `and` (y lógico)
# 2. `or` (o lógico)
# 3. `not` (no lógico)

print('\nOPERADORES LOGICOS\n')

f = True
g = False

and_logical = f and g # False
or_logical = f or g # True
not_logical = not f # False

print(and_logical)
print(or_logical)
print(not_logical)

# Operadores de Identidad:
# 1. `is` (es)
# 2. `is not` (no es)

print('\nOPERADORES DE IDENTIDAD\n')

h = [1, 2, 3]
i = [1, 2, 3]
j = h

it_is = h is j     # True
its_not = h is i  # False

print(it_is)
print(its_not)

# Operadores de Membresía:
# 1. `in` (en)
# 2. `not in` (no en)

print('\nOPERADORES DE IDENTIDAD\n')

k = 3

its_in = k in h   # True
its_not_in = k not in i # False

print(its_in)
print(its_not_in)

# Operadores Bit a Bit:
# 1. `&` (AND)
# 2. `|` (OR)
# 3. `^` (XOR)
# 4. `~` (NOT)
# 5. `<<` (desplazamiento a la izquierda)
# 6. `>>` (desplazamiento a la derecha)

print('\nOPERADORES BIT A BIT\n')

l = 6  # 110 en binario
m = 2  # 010 en binario

and_bit = l & m  # 010 -> 2
or_bit = l | m   # 110 -> 6
xor_bit = l ^ m  # 100 -> 4
not_bit = ~l     # -011 -> -7
desp_left = l << m # 11000 -> 24
desp_rigth = l >> m # 001 -> 1

print(and_bit)
print(or_bit)
print(xor_bit)
print(not_bit)
print(desp_left)
print(desp_rigth)

# Estructuras de Control Condicionales
# Ejemplo de if, elif, else
number = 10
if number > 15:
    print("The number is greater than 15")
elif number == 10:
    print("The number is 10")
else:
    print("The number is less than 15 and not 10")

# Estructuras de Control de Bucles
# Ejemplo de for
names = ["Ana", "Juan", "Carlos"]
for name in names:
    print(f"Hello, {name}")

# Ejemplo de while
counter = 5
while counter > 0:
    print(f"Counter: {counter}")
    counter -= 1

# Ejemplo de break
for i in range(1, 10):
    if i == 5:
        break
    print(i)

# Ejemplo de continue
for i in range(1, 10):
    if i % 2 == 0:
        continue
    print(i)

# Estructuras de Control para Manejar Excepciones
# Ejemplo de try, except, else, finally
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Division by zero")
else:
    print("Division performed correctly")
finally:
    print("This block is always executed")

# Ejercicio Extra:

print('\n[+] Ejercicio extra:\n')

def number_checker(start :int, end :int, exception :int) -> list:
    verified_numbers = []
    for number in range(start, end + 1):
        if number % 2 == 0 and number % 3 != 0 and number != exception:
            verified_numbers.append(number)

    return verified_numbers

start_range = 10
end_range = 55
excluded_number = 16

result = number_checker(start_range, end_range, excluded_number)

print(result)



