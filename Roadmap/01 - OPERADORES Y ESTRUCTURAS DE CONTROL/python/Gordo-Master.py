### Operadores ###

# Operadores aritmeticos
print(f"Suma: 10 + 3: {10+3}")
print(f"Resta: 10 + 3: {10-3}")
print(f"Multiplicación: 10 * 3: {10*3}")
print(f"División: 10 / 3: {10/3}")
print(f"Módulo: 10 % 3: {10%3}")
print(f"Exponente: 10 ** 3: {10**3}")
print(f"División entera: 10 // 3: {10//3}")

# Operadores de bit a bit
print(bin(2))
print(bin(3))
print(f"AND: 2 & 3: {2&3}")
print(f"OR: 2 | 3: {2|3}")
print(f"XOR: 2 ^ 3: {2^3}")
print(f"NOT: ~2 : {~2}") # Tener en cuenta que los int tienen 8 bits en memoria | 2 = 00000010  
print(f"Desplazamiento a la derecha: 2 >> 1: {2>>1}") # El primero (base) en binario, el segundo (numero normal) cantidad de espacios deplazados
print(f"Desplazamiento a la izquierda: 2 << 1:: {2<<1}")


# Operadores de asignación
a = 10 
print(f"Asignación: a = 10: {a}")

a += 1 
print(f"Aplica un suma sobre la misma variable: a += 1: {a}")

a *= 3 
print(f"Aplica un multiplicación sobre la misma variable: a *= 3: {a}")

a /= 3 
print(f"Aplica un división sobre la misma variable: a /= 3: {a}")

a %= 3 
print(f"Aplica un modulo sobre la misma variable: a %= 3: {a}")

a **= 3 
print(f"Aplica un exponente sobre la misma variable: a **= 3: {a}")

a //= 3 
print(f"Aplica un división entera sobre la misma variable: a //= 3: {a}")

a = 3
a &= 2 
print(f"# Aplica un operación bit a bit AND sobre la misma variable: a &= 2: {a}")

a |= 3 
print(f"# Aplica un operación bit a bit OR sobre la misma variable: a |= 2: {a}")

a ^= 2 
print(f"# Aplica un operación bit a bit XOR sobre la misma variable: a ^= 2: {a}")

a = 4
a >>= 2 
print(f"# Aplica un operación bit a bit desplazamiento derecha sobre la misma variable: a >>= 2: {a}")

a <<= 2 
print(f"# Aplica un operación bit a bit desplazamiento izquierda sobre la misma variable: a <<= 2: {a}")


# Operadores lógicos
print(f"AND, 2+3==5 and 3+4==7: {2+3==5 and 3+4==7}")
print(f"OR, 2+3==5 or 3+4==6: {2 or 3}")
print(f"NOT, not ({2+3==5}): {not 2+3==5}")

# Operadores de pertenencia

print(f"Operación de pertenencia \"in\", devuelve un boolean de si el elemento se encuentra en la secuencia")
print(f" 5 in [1,4,81,34]: {5 in [1,4,81,34]}")

print(f"Operación de pertenencia \"not in\", devuelve un boolean de si el elemento no se encuentra en la secuencia")
print(f" 5 in [1,4,81,34]: {5 not in [1,4,81,34]}")

# Operador de identidad
print(f"Operador de identidad \"is\" busca saber si ambos son los mismos objetos en el mismo espacio de memoria.")
print(f"Operador de identidad \"is not\" busca saber son objetos diferentes en diferentes espacios de memoria.")
# Hay que recordar que en python todo es un objeto.

# Operadores de comparación
print(f"Operador de comparación ==, ve si los valores de las variables son las mismas: 7 == 5 :{7 == 5}.")
print(f"Operador de comparación !=, ve si los valores de las variables son diferentes: 7 == 5 :{7 != 5}.")
print(f"Operador de comparación >, ve si el primero es mayor que el segundo: 7 > 5 :{7 > 5}.")
print(f"Operador de comparación <, ve si el primero es menor que el segundo: 7 < 5 :{7 < 5}.")
print(f"Operador de comparación >=, ve si el primero es mayor o igual que el segundo:: 7 >= 5 :{7 >= 5}.")
print(f"Operador de comparación <=, ve si el primero es menor o igual que el segundo: 7 <= 5 :{7 <= 5}.")

"""
Estructura de control
"""

# Condicionales

my_string = "Gordo-Master"

if my_string == "Gordo-Master":
    print("my_string es 'Gordo-Master'")
elif my_string == "Gordo":
    print("my_string es 'Gordo'")
else:
    print("my_string no es 'Gordo-Master'")


# Iterativas

for i in range(11):
    print(i)

i = 0
while i <= 10:
    print(i)
    i +=1

# Manejo de excepciones
try:
    print(10/0)
except:
    print("Se ha producido un error")
finally:
    print("Ha finalizado el manejo de excepciones")

for i in range(10,56):
    if i != 16 and i % 2 == 0 and i % 3 !=0:
        print(i)