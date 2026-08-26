# 01 Operadores y estructuras de control.

# operadores aritmeticos ( +, -, *, /, %, //, ** ).
print("Ejemplos de operadores aritmeticos\n")
numero_1 = 10
numero_2 = 2
numero_3 = 3
numero_4 = 4
numero_5 = 6


print("El resultado de sumar 5 + 3 es:", 5 + 3)

print("El resultado de restar 6 - 4 es: ", numero_5 - numero_4)

print(f"El resultado de multiplicar {numero_2} * {numero_3} es: ", numero_2 * numero_3)

resultado_division = numero_1 / numero_2
print(f"El resultado de la division {numero_1} / {numero_2} es: ", resultado_division)

print(f"El modulo o residuo de dividir {numero_1} entre {numero_2} es: ", numero_1 % numero_2)

print("El resultado de la division entera (redondeada) 20 // 3 es: ", 20 // 3)

print(f"El resultado de elevar exponencialmente {numero_3} a la {numero_4} (en matematicas[{numero_3}^{numero_4}]) (en python [{numero_3}**{numero_4}]) es: ", numero_3 ** numero_4)

print(f"\n{'*' * 50}")


# operadores logicos (and, or, not).
print("Ejemplos de operadores logicos")
valor1 = 1
valor2 = 0

if valor1 and valor2:
    print("verdadero")
else:
    print("falso porque valor2 es 0")

if valor1 or valor2:
    print("verdadero porque al menos valor1 es 1")
else:
    print("falso")

if not valor1:
    print("verdadero")
else:
    print("falso porque valor1 es 1. se invierte el valor.")

print(f"\n{'*' * 50}")


# operadores de comparacion (==, !=, >, <, >=, <=).
print("Ejemplos de operadores de comparacion")
if valor1 == valor2:
    print("son iguales")
else:
    print("falso porque son diferentes")

if valor1 != valor2:
    print("son diferentes")
else:
    print("falso porque son iguales")

if valor1 > valor2:
    print("valor1 es mayor que valor2")
else:
    print("falso")

if valor1 < valor2:
    print("verdadero")
else:
    print("falso porque valor1 es mayor que valor2")

if valor1 >= valor2:
    print("valor1 es mayor o igual que valor2")
else:
    print("falso")

if valor1 <= valor2:
    print("verdadero porque valor2 es 0 osea menor que valor1")
else:
    print("falso")

print(f"\n{'*' * 50}")

# operadores de asignacion (=, +=, -=, *=, /=, %=, //=, **=, &=, |=, ^=, >>=, <<=).
print("Ejemplos de operadores de asignacion")
asignacion_simple = 10
print(f"se le asigna el valor de {asignacion_simple} a la variable con el operador '='")

asignacion_simple += 5 # se le suma 5 a la variable asignacion_simple, ahora vale 15
print("se le suman 5 al valor anterior con el operador '+='. ahora la variable vale: ", asignacion_simple)

asignacion_simple -= 3 # se le resta 3 a la variable asignacion_simple, ahora vale 12
print("se le restan 3 al valor anterior con el operador '-='. ahora vale: ", asignacion_simple)

asignacion_simple *= 2 # se le multiplica por 2 a la variable ahora vale 24
print("el valor anterior se multiplica por 2 con el operador '*='. el resultado es: ", asignacion_simple)

asignacion_simple /= 4 # se le divide entre 4 a la variable ahora vale 6
print("el valor anterior se divide entre 4 con el operador '/='. con este operador se crea un resultado con punto decimal cuyo resultado es: ", asignacion_simple)

asignacion_simple %= 4 # se le aplica el modulo 4 a la variable ahora vale 2
print("el modulo o residuo de dividir el valor actual de la variable: 6.0 entre 4 con el operador '%=', es: ", asignacion_simple)

asignacion_simple_2 = 20
asignacion_simple_2 //= 3 # se le aplica la division entera entre 3 a la variable ahora vale 6
print(f"el resultado de la division entera de 20 entre 3, con el operador '//=', es un resultado entero (redondeado): {asignacion_simple_2}")

asignacion_simple_2 **= 2 # se le aplica el exponente 2 a la variable ahora vale 36
print(f"el resultado de elevar 6 al cuadrado (2), con el operador '**=', es: {asignacion_simple_2}")

print(f"\n{'*' * 50}")

# operadores de identidad (is, is not).
print("Ejemplos de operadores de identidad")
variable1 = 5
variable2 = 5
variable3 = 10

if variable1 is variable2:
    print("variable1 y variable2 son el mismo objeto") # da como resultado verdadero porque ambos apuntan al mismo objeto en memoria
else:
    print("falso")

if variable1 is not variable3:
    print("variable1 y variable3 no son el mismo objeto") # da como resultado verdadero porque apuntan a diferentes objetos en memoria
else:
    print("falso")

print(f"\n{'*' * 50}")

# operadores de pertenencia (in, not in).
print("Ejemplos de operadores de pertenencia")
variable4 = "Cristian"
variable5 = "a"
if variable5 in variable4:
    print("verdadero porque la letra 'a' esta en variable4")
else:
    print("falso")

if variable5 not in variable4:
    print("verdadero")
else:
    print("falso porque la letra 'a' esta en variable4")

print(f"\n{'*' * 50}")

# operadores de bits (&, |, ^, ~, <<, >>).
print("Ejemplos de operadores de bits")
asignacion_bits = 25 
asignacion_bits &= 7 # se le aplica el operador AND bit a bit a la variable ahora vale 1
print(asignacion_bits)
asignacion_bits |= 3 # se le aplica el operador OR bit a bit a la variable ahora vale 3
print(asignacion_bits)
asignacion_bits ^= 8 # se le aplica el operador XOR bit a bit a la variable ahora vale 11
print(asignacion_bits)
asignacion_bits >>= 1 # se le aplica el operador de desplazamiento a la derecha a la variable ahora vale 5
print(asignacion_bits)
asignacion_bits <<= 2 # se le aplica el operador de desplazamiento a la izquierda a la variable ahora vale 20
print(asignacion_bits)


print(f"\n{'*' * 50}")

# estructuras de control (if, elif, else, while, for, break, continue).
print("Ejemplos de estructuras de control\n")
print("Ejemplo de if, elif, else")
mi_nombre = "Cristian"
mi_edad = 40
mi_altura = 1.9

if mi_nombre == "Cristian":
    if mi_edad > 18:
        print("Hola Cristian, eres mayor de edad")
elif mi_nombre == "Cristian" and mi_edad < 18:
    print("Hola Cristian, eres menor de edad")
    print("No cumples con los requisitos")
else:
    print("Hola, no eres Cristian")

print("\nEjemplo de while")
while mi_edad > 18 and mi_edad < 45:
    mi_edad += 1
    print("Tu edad es: ", mi_edad)

print("\nEjemplos de for")
for i in range((len(mi_nombre))):
    if mi_nombre[i] == "t":
        break
    print(f"Se encontro una {mi_nombre[i]} en el nombre: {mi_nombre}")

print(f"\n{'*' * 50}")
for i in "cristian":
    if i == "s":
        continue
    print(f"Se encontro una {i} en el nombre: {mi_nombre}")

print(f"\n{'*' * 50}")
print("Ejemplo de try, except")
dividendo = 20
divisor = 0
try:
    resultado = dividendo / divisor
    print("El resultado de la division es: ", resultado)

except ZeroDivisionError:
    print("Error: No se puede dividir entre cero")

    
print(f"\n{'*' * 50}")

# Dificultad extra.
"""
Crea un programa que imprima por consola todos los números comprendidos
entre 10 y 55 (incluidos), pares, y que no son ni el 16 ni múltiplos de 3.
"""

for num in range(10, 56):
    if num % 2 == 0 and num != 16 and num % 3 != 0:
        print(num)

# Nota: aprendi bastante haciendo este reto. nuevos conocimientos desbloqueados sobre operadores. me gusto mucho este ejercicio.