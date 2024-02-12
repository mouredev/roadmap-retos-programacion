# Operadores Aritméticos

a = 10
b = 1

adicion = a + b
subtraccion = a - b
multiplicacion = a * b
division = a / b
modulo = a % b
potencia = a ** b

op_ar = f"""
Operadores Aritméticos
-----------------------
adicion = {adicion}
subtraccion = {subtraccion}
multiplicacion = {multiplicacion}
division = {division}
modulo = {modulo}
potencia = {potencia}
"""

print(op_ar)

# Operadores Relacionales

igualdad = (a == b)
desigualdad = (a != b)
mayor_que = (a > b)
menor_que = (a < b)
mayor_o_igual_que = (a >= b)
menor_o_igual_que = (a <= b)

op_rl = f"""
Operadores Relacionales
-----------------------
igualdad = {igualdad}
desigualdad = {desigualdad}
mayor_que = {mayor_que}
menor_que = {menor_que}
mayor_o_igual_que = {mayor_o_igual_que}
menor_o_igual_que = {menor_o_igual_que}
"""

print(op_rl)

# Operadores de Asignación

print('''
Operadores de Asignación
-----------------------''')
x = 5
print(x)
# Operador de asignación simple
x = 10
print(x)
# Operador de asignación con suma
x += 3
print(x)
# Operador de asignación con resta
x -= 2
print(x)
# Operador de asignación con multiplicación
x *= 4
print(x)
# Operador de asignación con división
x /= 2
print(x)
# Operador de asignación con módulo
x %= 3
print(x)
# Operador de asignación con exponenciación
x **= 2
print(x)

# Operadores Lógicos

var_and = True and False  # Devuelve True si ambos operandos son True
var_or = True or False  # Devuelve True si alguno de los operandos es True
var_not = not True  # Devuelve True si alguno de los operandos False

op_lg = f"""
Operadores Lógicos
-----------------------
var_and = {var_and}
var_or = {var_or}
var_not = {var_not}
"""

print(op_lg)

# Operadores de Pertenencia

var_in = 1 in [1, 2, 3, 4]
var_not_in = 1 not in [1, 2, 3, 4]

op_pr = f"""
Operadores de Pertenencia
-----------------------
var_in = {var_in}
var_not_in = {var_not_in}
"""

print(op_pr)

# Operadores de identidad

var_is = 1 is int
var_is_not = 1 is not int

op_id = f"""
Operadores de identidad
-----------------------
var_is = {var_is}
var_is_not = {var_is_not}
"""

print(op_id)

# DIFICULTAD EXTRA (opcional):


def programa_1():
    numeros = [num for num in range(10, 56)
               if num != 16 and num % 3 != 0 and num % 2 == 0]
    print(numeros)


programa_1()
