"""
Operadores
"""

# Operadores Aritméticos
print("Operadores Aritméticos")
print(f"Suma: 5 + 7 = {5 + 7}")
print(f"Resta: 5 - 7 = {5 - 7}")
print(f"Multiplicación: 5 * 7 = {5 * 7}")
print(f"División: 10 / 2 = {10 / 2}")
print(f"Divisón Entera: 10 // 2 = {10 // 2}")
print(f"Módulo: 10 % 2 = {10 % 2}")
print(f"Potencia: 4 ** 2 = {4 ** 2}")

# Operadores Relacionales
print("Operadores Relacionales")
a, b = 6, 3
print(f"Mayor: a > b = {a > b}")
print(f"Mayor o igual que: a >= b = {a >= b}")
print(f"Menor: a < b = {a < b}")
print(f"Menor o igual que: a <= b = {a <= b}")
print(f"Igual: a == b = {a == b}")
print(f"Diferente: a != b = {a != b}")

# Operadores Bit a Bit
print("Operadores Bit a Bit")
c, d = 2, 3
print(f"AND (&): c & d = {c & d}")
print(f"OR (|): c | d = {c | d}")
print(f"XOR (^): c ^ d = {c ^ d}")
print(f"NOT (~): ~c = {~c}")
print(f"RIGHT SHIFT (>>): c >> d = {c >> d}")
print(f"LEFT SHIFT (<<): c << d = {c << d}")

# Operadores de Asignación
print("Operadores de Asignación")
x, z = 5, 2
print(f"(=): x = 5: {x}")
x += 5
print(f"(+=): x += 5: {x}")
x -= 5
print(f"(-=): x -= 5: {x}")
x *= 2
print(f"(*=): x *= 2: {x}")
x **= 2
print(f"(**=): x **= 2: {x}")
x //= 2
print(f"(//=): x //= 2: {x}")
x /= 2
print(f"(/=): x /= 2: {x}")
x %= 2
print(f"(%=): x %= 2: {x}")
z &= 3
print(f"(&=): z &= 3: {z}")
z |= 3
print(f"(|=): z |= 3: {z}")
z ^= 1
print(f"(^=): z ^= 3: {z}")
z >> 2
print(f"(>>=): z >> 2: {z}")
z << 2
print(f"(<<=): z << 2: {z}")

# Operadores Lógicos
print("Operadores Lógicos")
a , b = True, False
print(f"and (&&): a and b = {a and b}")
print(f"or (||): a or b = {a or b}")
print(f"not (!): not a  = {not a}")

# Operadores de Pertenencia
print("Operadores de Pertenencia")
a = [1, 2, 3, 4, 5, 6]
# in devuelve True si el valor especificado se encuentra en la secuencia
# not in devuelve True si el valor especificado no se encuentra en la secuencia
print(f"¿10 está en la lista? = {10 in a}")
print(f"¿10 está en la lista? = {10 not in a}")
print(f"¿4 está en la lista? = {4 in a}")
print(f"¿4 está en la lista? = {4 not in a}")

# Operadores de Identidad
print("Operadores de Identidad")
a, b, c = 3, 3, 4
# is devuelve True si los operandos se refieren al mismo objeto
# is not devuelve True si los operandos no se refieren al mismo objeto
print(f"¿a es igual a b? = {a is b}")
print(f"¿a es igual a b? = {a is not b}")
print(f"¿a es igual a c? = {a is not c}")

"""
Estructuras de Control
"""

### Condicionales if, elif, else ###
edad = 15
if edad < 18:
    print("Menor de edad")
elif edad >= 18:
    print("Mayor de edad")
else:
    print ("Este código nunca se ejecutará")

### Bucles for y while ###
## Bucle for ##
frutas = ["Manzana", "Fresa", "Naranja"]
for fruta in frutas:
    print(fruta)

## Bucle while ##
contador = 0
while contador < 3:
    print("Dentro del bucle")
    contador += 1

### Comprensión de listas ###
cuadrados = [x**2 for x in range(10)]
print(cuadrados)

###Control de flujo break, continue, pass ###
## Break ##
for num in range(5):
    if num == 3:
        break    # Sale del bucle
    print(num)

## Continue ##
cadena = "Python"
for letra in cadena:
    if letra == 'P':
        continue
    print(letra)

## Pass ##
for num in range(5):
    if num == 3:
        pass  
    print(num)

"""
Ejercicio Extra
"""
print("EJERCICIO EXTRA")
for numero in range(10, 56):
    if numero % 2 == 0 and numero != 16 and numero % 3 != 0:
        print(numero)
