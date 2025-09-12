"""Operadores"""

# Operadores de asignación
numero = 8 # asignación
print(numero) 
numero += 8 # suma
print(numero)
numero -= 8 # resta
print(numero)
numero *= 8 # multiplicación
print(numero)
numero /= 8 # división
print(numero)
numero //= 8 # división entera
print(numero)
numero **= 8 # exponente
print(numero)
numero %= 8 # módulo
print(numero)

# Operadores aritméticos
print(f"Suma: 5 + 9 = {5 + 9}") 
print(f"Resta: 5 - 9 = {5 - 9}") 
print(f"Multiplicación: 5 * 9 = {5 * 9}") 
print(f"Exponente: 5 ** 9 = {5 ** 9}") 
print(f"División: 5 / 9 = {5 / 9}")
print(f"División entera: 5 // 9 = {5 // 9}")
print(f"Módulo: 5 % 9 = {5 % 9}")

# Operadores relacionales
print(f"Igualdad: 3 == 2 es {3 == 2}")
print(f"Desigualdad: 3 != 2 es {3 != 2}")
print(f"Menor que: 3 < 2 es {3 < 2}")
print(f"Mayor que: 3 > 2 es {3 > 2}")
print(f"Menor o igual que: 3 <= 2 es {3 <= 2}")
print(f"Mayor o igual que: 3 >= 2 es {3 >= 2}")

# Operadores lógicos
print(f"AND &&: True and True es {True and True}")
print(f"OR ||: True or True es {True or True}")
print(f"NOT !: not True == True es {not True == True}")

"""Estructuras de control"""

# Condicionales
animal = "gato"
if animal == "gato":
    print("El animal es correcto")
elif animal == "perro":
    print("El animal escogido no es el correcto")
else:
    print("Has encontrado una nueva especie")

# Iteradores
contador = 5
while contador <= 5:
    print("Hola mundo")
    contador += 1

for i in range(10):
    print(i)

"""Excepciones"""

try:
    numero = float(input("Introduce un número: "))
    mi_numero = 5
    print(f"La suma de ambos números es: {mi_numero + numero}")
except:
    print("Se ha producido un error")
else:
    print("Has introducido correctamente el número")
finally:
    print("Podemos continuar con el programa")


"""Extra"""
for i in (10, 56):
    if i % 2 == 0 and i != 16 and i % 3 != 0:
        print(i)