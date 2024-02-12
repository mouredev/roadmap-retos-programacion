

# operadores Aritmeticos

suma = 80 + 13
resta = 80 - 13
division = 80 / 13
multiplicacion = 80 + 13
modulo = 80 % 13
exponente = 80 ** 13
division_entera = 80 // 13

print(suma)
print(resta)
print(division)
print(multiplicacion)
print(modulo)
print(exponente)
print(division_entera)


# Operador Comparacion

igual = 80 == 13
diferente = 80 != 13
mayor = 80 > 13
menor = 80 < 13
mayor_igual = 80 >= 13
menor_igual = 80 <= 13

print(igual)
print(diferente)
print(mayor)
print(menor)
print(mayor_igual)
print(menor_igual)

# Operadores logicos

# Ejemplo con operador AND
edad = 39
ingreso_mensual = 1500

if edad > 18 and ingreso_mensual > 2000:
    print("Eres mayor de edad y tu ingreso es suficiente.")
else:
    print("No cumples con los requisitos.")

# Ejemplo con operador OR
nombre = "Fran"
apellido = "Moreno"

if nombre == "Alice" or apellido == "Jones":
    print("Eres una maquina tete.")
else:
    print("No eres quien dices que eres.")

# Ejemplo con combinación de operadores lógicos
edad = 39
tiene_trabajo = True
tiene_ahorros = False

if edad > 18 and (tiene_trabajo or tiene_ahorros):
    print("Cumples con los requisitos para el préstamo.")
else:
    print("No cumples con los requisitos para el préstamo.")

# Operadores de asignación

my_number = 11  # asignación
print(my_number)
my_number += 1  # suma y asignación
print(my_number)
my_number -= 1  # resta y asignación
print(my_number)
my_number *= 2  # multiplicación y asignación
print(my_number)
my_number /= 2  # división y asignación
print(my_number)
my_number %= 2  # módulo y asignación
print(my_number)
my_number **= 1  # exponente y asignación
print(my_number)
my_number //= 1  # división entera y asignación
print(my_number)


# Ejemplo de condicional (if-else)
edad = 20

if edad >= 18:
    print("Eres mayor de edad.")
else:
    print("Eres menor de edad.")

# Ejemplo de condicional anidado
puntuacion = 60

if puntuacion >= 90:
    print("Excelente compadre")
elif puntuacion >= 70:
    print("Buen trabajo loko")
else:
    print("Necesitas mejorar, dejate de ChatGpt")

# Ejemplo de bucle while
contador = 0

while contador < 5:
    print(f"Contador: {contador}")
    contador += 1

# Ejemplo de bucle for
for i in range(3):
    print(f"Iteración {i}")

# Iterar sobre una lista
colores = ["rojo", "verde", "azul"]

for color in colores:
    print(color)

# Programa que imprime números entre 10 y 55, pares, y no son ni el 16 ni múltiplos de 3

for numero in range(10, 56):
    # Verificar si el número es par y no es ni el 16 ni múltiplo de 3
    if numero % 2 == 0 and numero != 16 and numero % 3 != 0:
        print(numero)
