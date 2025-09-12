# Operadores aritméticos

# Suma
a = 9
b = 6
suma = a + b
print("Suma: ", suma)

# Resta
resta = a - b
print("Resta: ", resta)

# Multiplicación
multiplicacion = a * b
print("Multiplicación: ", multiplicacion)

# Division
division = a / b
print("División: ", division)

# Division entera (aproximación)
div_entera = a // b
print("Division aproximación: ", div_entera)

# Modulo
modulo = a % b
print("Módulo: ", modulo)

# Potencia
potencia = a ** b
print(potencia)

# Operadores de comparación

x = 10
y = 5

# Igual
print("Igualdad: ", x == y)

# Diferente
print("Diferencia", x != y)

# Mayor
print("Mayor: ", x > y)

# Mayor o igual
print("Mayor o igual: ", x >= y)

# Menor
print("Menor: ", x < y)

# Menor o igual
print("Menor o igual", x <= y)

# Operadores lógicos
t = True
f = False

# AND lógico
and_logico = t and f
print("AND lógico: ", and_logico)

# OR lógico
or_logico = t or f
print("OR lógico ", or_logico)

# NOT lógico
not_logico = not t
print("NOT lógico ", not_logico)

# Operadores de asignación
# Asignación simple
x = 4
print("Asignación simple: ", x)

# Asignación con operación
x += 5 # x = x + 5
print("Asignación con operación: ", x)

# Operadores de identidad

a = [1, 2, 3]
b = a
c = [1, 2, 3]

# is
print("a es b: ", a is b)
print("a es c ", a is c)

# is not
print("a no es b ", a is not b)
print("a no es c ", a is not c)

# Operadores de pertenencia
lista = [1, 2, 3, 4, 5]

# in
print("2 está en la lista: ", 2 in lista)
print("6 está en la lista: ", 6 in lista)

# not in
print("2 no está en la lista: ", 2 not in lista)
print("6 no está en la lista: ", 6 not in lista)

# Operadores a nivel de bits
x = 5
y = 3

# AND a nivel de bits
and_bits = x & y
print("AND a nivel de bits ", and_bits)

# OR a nivel de bits
or_bits = x | y
print("OR a nivel de bits: ", or_bits)

# XOR a nivel de bits
xor_bits = x ^ y
print("XOR a nivel de bits:", xor_bits)

# Desplazamiento a la izquierda
desplazamiento_izquierda = x << 1
print("Desplazamiento a la izquierda:", desplazamiento_izquierda)

# Desplazamiento a la derecha
desplazamiento_derecha = x >> 1
print("Desplazamiento a la derecha:", desplazamiento_derecha)


# -------------------------------------------------------------------
#  Estructuras condicionales

# if else
edad = 28

if edad >= 18:
    print("Eres mayor de edad.")
else:
    print("Eres menor de edad.")


# elif
nota = 75

if nota >=  90:
    print("Excelente")
elif nota >= 70:
    print("Buen trabajo")
else:
    print("Necesitas mejorar")

# Estructuras iterativas
frutas = ["Pera", "Manzana", "Cereza", "Banana"]

for fruta in frutas:
    print(fruta)

# while
contador = 0

while contador < 5:
    print(contador)
    contador += 1

# Estructuras de excepciones
try:
    division = 10 / 0
except ZeroDivisionError:
    print("Error: División por cero.")
except Exception as e:
    print(f"Ocurrió una excepción: {e}")
else:
    print("La operación se realizó sin errores.")
finally:
    print("Este bloque siempre se ejecuta.")

# Estructuras de control de flujo
# break y continue
for i in range(10):
    if i == 5:
        break
    print(i)
for i in range(10):
    if i == 5:
        continue
    print(i)

# pass
for i in range(5):
    # Bloque de codigo con ninguna acción
    pass

# Estructura de control de contexto
# with open("archivo.txt", "r") as archivo:
#     contenido = archivo.read()

# DIFICULTAD EXTRA (opcional):
for i in range(10, 56):
    if i % 2 == 0 and i % 3 == 0 & i != 16:
        print (i)
