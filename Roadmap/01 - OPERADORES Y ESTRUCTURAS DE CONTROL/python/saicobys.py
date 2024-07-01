""" Operadores en Python: """
# Operadores Aritméticos
a = 10
b = 3
print(f"Suma: {a + b}")          # Suma
print(f"Resta: {a - b}")          # Resta
print(f"Multiplicación: {a * b}")  # Multiplicación
print(f"División: {a / b}")        # División
print(f"División entera: {a // b}") # División entera
print(f"Módulo: {a % b}")         # Resto de la división
print(f"Exponenciación: {a ** b}") # Potencia

# Operadores de Comparación
x = 5
y = 8
print(f"x == y: {x == y}")      # Igual a
print(f"x != y: {x != y}")      # Distinto de
print(f"x > y: {x > y}")       # Mayor que
print(f"x < y: {x < y}")       # Menor que
print(f"x >= y: {x >= y}")      # Mayor o igual que
print(f"x <= y: {x <= y}")      # Menor o igual que

# Operadores Lógicos
p = True
q = False
print(f"p and q: {p and q}")    # AND lógico (ambos deben ser True)
print(f"p or q: {p or q}")     # OR lógico (al menos uno debe ser True)
print(f"not p: {not p}")       # NOT lógico (invierte el valor de verdad)

# Operadores de Asignación
z = 20
z += 5   # z = z + 5
print(f"z += 5: {z}")
z -= 3   # z = z - 3
print(f"z -= 3: {z}")
z *= 2   # z = z * 2
print(f"z *= 2: {z}")
z /= 4   # z = z / 4
print(f"z /= 4: {z}")

# Operadores de Identidad
lista1 = [1, 2, 3]
lista2 = [1, 2, 3]
lista3 = lista1
print(f"lista1 is lista2: {lista1 is lista2}")  # False (objetos diferentes)
print(f"lista1 is lista3: {lista1 is lista3}")  # True (misma referencia)

# Operadores de Pertenencia
print(f"1 in lista1: {1 in lista1}")  # True
print(f"4 in lista1: {4 in lista1}")  # False

""" Estructuras de Control en Python: """
# Condicionales (if, elif, else)
edad = 25

if edad < 18:
    print("Eres menor de edad")
elif 18 <= edad < 65: # Combina comparación y operadores lógicos
    print("Eres adulto")
else:
    print("Eres adulto mayor")

# Bucles (for , while)
for i in range(1, 6): # Bucle for: itera sobre un rango de números
    print(i)

contador = 0
while contador < 5:   # Bucle while: itera mientras se cumpla una condición
    print(contador)
    contador += 1

# Excepciones (try, except, else, finally)
try:
    resultado = 10 / 0 # División por cero (genera una excepción)
except ZeroDivisionError:
    print("Error: División por cero no permitida")
else: # Se ejecuta si no hubo excepciones
    print("El resultado es:", resultado)
finally: # Se ejecuta siempre, haya o no excepciones
    print("Fin del programa")
