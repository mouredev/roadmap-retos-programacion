# #01 OPERADORES Y ESTRUCTURAS DE CONTROL

"""

EJERCICIOS:

"""

# Operador de concatenación de cadenas

str_1 = 'Hello'
str_2 = 'World'

concatenacion = str_1 + ' ' + str_2
concatenacion_2 = 'Hello ' + 'World'

print(concatenacion)
print(concatenacion_2)


# Operadores lógicos

t = True
f = False

# Si uno de los dos es falso, el resultado será falso.
resultado_and = f'El resultado de (t and f) es {t and f}'

# Si uno de los dos es verdadero el resultado será verdadero.
resultado_or = f'El resultado de (t or f) es {t or f}'

# Niega el resultado obtenido
resultado_not = f'El resultado de (not t) es {not t}'


# Operadores de comparación

number1 = 10
number2 = 5
number3 = 10

resultado_1 = number1 > number2  # True, de lo contrario retorna False.
resultado_2 = number1 < number2   # False
resultado_3 = number1 >= number3  # True
resultado_4 = number1 <= number2  # False
resultado_5 = number1 != number2  # True
resultado_6 = number1 == number2  # False


# Operadores aritméticos

print(f'la suma de number1 con number2 es: {number1 + number2}')
print(f'la resta de number1 con number2 es: {number1 - number2}')
print(f'la multiplicación de number1 con number2 es: {number1 * number2}')
print(f'la división de number1 con number2 es: {number1 / number2}')
print(f'la potencia de number1 a la number2 es: {number1 ** number2}')
print(f'El módulo de number1 por number2 es: {number1 % number2}')
