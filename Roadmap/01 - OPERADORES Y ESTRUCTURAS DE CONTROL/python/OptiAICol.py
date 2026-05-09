""" Operadores """

# Operadores aritméticos
print("\n---Operadores aritméticos:---")
print(f"Suma: 5 + 3 = {5 + 3}")
print(f"Resta: 5 - 3 = {5 - 3}")
print(f"Multiplicación: 5 * 3 = {5 * 3}")
print(f"División: 5 / 3 = {5 / 3}")
print(f"División entera: 10 // 3 = {10 // 3}")
print(f"Módulo: 10 % 3 = {10 % 3}")
print(f"Exponente: 5 ** 3 = {5 ** 3}")

# Operadores de comparación
print("\n---Operadores de comparación:---")
print(f"Igualdad: 5 == 3 = {5 == 3}")
print(f"Desigualdad: 5 != 3 = {5 != 3}")
print(f"Mayor que: 5 > 3 = {5 > 3}")
print(f"Menor que: 5 < 3 = {5 < 3}")
print(f"Mayor o igual que: 5 >= 3 = {5 >= 3}")
print(f"Menor o igual que: 5 <= 3 = {5 <= 3}")

# Operadores lógicos
print("Operadores lógicos:")
print(f"AND: 10 + 3 == 13 and 5 - 1 == 4 = {10 + 3 == 13 and 5 - 1 == 4}")
print(f"OR: 10 + 3 == 13 or 5 - 1 == 5 = {10 + 3 == 14 or 5 - 16 == 5}")
print(f"NOT: not (10 + 3 == 14) = {not 10 + 3 == 14}")

# Operadores de asignación
print("\n---Operadores de asignación:")
x = 11
print(x)
x += 1
print(x)
x -= 1
print(x)
x *= 2
print(x)
x /= 2
print(x)
x %= 2
print(x)
x **= 3
print(x)
x //= 1
print(x)

#operadores de identidad
print("\n---Operadores de identidad:---")
numero_nuevo = 1.0
print(f"x is numero_nuevo es  {x is numero_nuevo}")
print(f"x is not numero_nuevo es  {x is not numero_nuevo}")

numero_nuevo = x
print(f"x is numero_nuevo es  {x is numero_nuevo}")
print(f"x is not numero_nuevo es  {x is not numero_nuevo}")

#Operadores de pertenencia
print("\n---Operadores de pertenencia:---")
print(f"'a' in 'optiai' es {'a' in 'optiai'}"  )
print(f"'x' not in 'optiai' es {'x' not in 'optiai'}"  )

#Operadores bit
print("\n---Operadores bit:---")
a = 10 #1010
b = 3 #0011
print("a = ", a)
print("b = ", b)
print(f" AND: a & b = {a & b}") #0010  
print(f" OR: a | b = {a | b}")  #1011
print(f" XOR: a ^ b = {a ^ b}") #1001
print(f" NOT: ~a = {~a}")       #0101
print(f" Desplazamiento a la izquierda: a << 1 = {a << 1}") #10100
print(f" Desplazamiento a la derecha: a >> 1 = {a >> 1}") #0101

#Estructuras de control
print("\n---Estructuras de control:---")

# Condicionales
print("\nCondicionales:")
edad = 30
print("edad = ", edad)
if edad < 18:
    print("Eres menor de edad.")
else:
    print("Eres mayor de edad.")

edad = 17
print("edad = ", edad)
if edad > 18:
    print("Tiene Cedula")
else:
    print("No tiene cedula")

edad = 18
print("edad = ", edad)
if edad > 18:
    print("Tiene Cedula")
elif edad == 18:
    print("Tiene Cedula pero es nuevo")
else:
    print("No tiene cedula")

# Interativas
print("\nIterativas:")
print("For")
for i in range(11):
    print(i)

print("\nWhile")

i = 0
while i <= 10:
    print(i)
    i += 1

# Manejo de excepciones
print("\nManejo de excepciones:")
try:
    print(10 / 0)
except:
    print("Error: División por cero.")
finally:
    print("Ha finalizado el manejo de excepciones.")

try:
    print(10 / 1)
except:
    print("Error: División por cero.")
finally:
    print("Ha finalizado el manejo de excepciones.")


# Ejercicio Extra
print("\nEjercicio Extra:---")

for numero in range(10, 56):
    if numero % 2 == 0 and numero != 16 and numero % 3 != 0:
        print(numero)