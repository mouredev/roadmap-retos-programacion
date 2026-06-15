# Operadores aritméticos

print("Suma: 10 + 3 = ", 10 + 3)
print("Resta: 10 - 3 =", 10 - 3)
print("Multiplicación: 10 * 3 =", 10 * 3)
print("División: 10 / 3 =", 10 / 3)
print("División entera (sin decimales): 10 // 3 =", 10 // 3)
print("Módulo (resto) 10 % 3 =", 10 % 3)
print("Exponente: 10 ** 3 = ", 10**3)

# Operadores de comparación
print("Igualdad: 10 == 3 es:", 10 == 3)
print("Desigualdad: 10 != 3 es", 10 != 3)
print("Mayor que: 10 > 3 es =", 10 > 3)
print("Menor que: 10 < 3 es =", 10 < 3)

# Operadores Lógicos
print("AND (ambas verdaderas): True and False es:", True and False)
print("OR (al menos una verdadera): True or False es", True or False)
print("NOT (invierte el valor): not True es", not True)

# Operadores de asignación

mi_numero = 10  # Asignación simple
mi_numero += 5  # En sintaxis normal, mi_numero + 5
print("Asignación con suma:", mi_numero)

# Operadores de identidad
a = 5
b = 5
print("Identidad (a is b):", a is b)

# Operadores de pertenencia (Está dentro de? )
texto = "Hola Kalmcris"
print("Pertenencia ('Hola' in texto: ", "Hola" in texto)

# Operadores de bits
print("Bitwise AND: 10 & 3 =", 10 & 3)

# Estructuras de control

# Condicionales

edad = 21

if edad > 18:
    print("Eres mayor de edad.")
elif edad == 18:
    print("Tienes justo 18.")
else:
    print("Eres menor de edad.")

# Iterativas (Bucles)
# Bucle FOR (cuando sabes cuántas veces repetir)
print("Bucle for: ")
for i in range(3):  # Repite 3 veces (0,1,2)
    print(i)


# Bucle WHILE (mientras algo sea verdadero)

print("Bucle while:")
contador = 0
while contador < 3:
    print(contador)
    contador += 2

# Excepciones (manejo de estas)
print("Manejo de excepciones:")
try:
    print(10 / 0)  # Esto daria un error de tipo aritméticos
except ZeroDivisionError:
    print("No puedes dividir por cero!")
finally:
    print("Esto se ejecuta siempre, haya error o no.")

# Parte de dificultad extra:

print("---Dificultad extra---")

for numero in range(10, 56):
    if numero % 2 == 0 and numero != 16 and numero % 3 != 0:
        print(numero)
