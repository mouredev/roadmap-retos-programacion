# Operadores aritmeticos

a = 5
b = 3

suma = a + b              # 10 + 5 = 15
resta = a - b             # 10 - 4 = 6
multiplicacion = a * b    # 10 * 3 = 30
division = a / b          # 4 / 2 = 2
division_entera = a // b  # 10 / 3 = 3 (redondeado hacia abajo)
modulo = a % b            # 10 % 3 = 1 (resto de la division)
potencia = a ** b         # 10^3 = 1000

print(suma, resta, multiplicacion, division, division_entera, modulo, potencia)


# Operadores de asignacion

x = 5     # Asignación normal

x += 3    # Equivale a: x = x + 3  → x = 8
x -= 2    # x = x - 2  → x = 6
x *= 4    # x = x * 4  → x = 24
x /= 3    # x = x / 3  → x = 8.0
x //= 2   # x = x // 2  → x = 4.0
x %= 3    # x = x % 3  → x = 1.0
x **= 2   # x = x ** 2  → x = 1.0

print(x)

# Operadores de comparacion

a = 10
b = 5

print(a == b)    # False (10 no es igual a 5)
print(a != b)    # True (10 es diferente de 5)
print(a > b)     # True (10 es mayor que 5)
print(a < b)     # False (10 no es menor que 5)
print(a >= 10)   # True (10 es mayor o igual a 10)
print(a <= 5)    # False (10 no es menor o igual a 5)


# Operadores logicos

x = True
y = False

print(x and y)  # False (Ambos deben ser True)
print(x or y)   # True (Basta con que uno sea True)
print(not x)    # False (Invierte el valor de x)


# Operadores de identidad

a = [1, 2, 3]
b = a
c = [1, 2, 3]

print(a is b)      # True (b apunta al mismo objeto que a)
print(a is not c)  # True (c es una lista nueva, aunque tenga los mismos valores)


# Operadores de pertenencia

frutas = ["manzana", "banana", "cereza"]

print("manzana" in frutas)  # True (manzana está en la lista)
print("pera" not in frutas) # True (pera NO está en la lista)


# Operadores Bit a Bit

a = 5  # En binario:  0101
b = 3  # En binario:  0011

print(a & b)  # AND →  0101 & 0011 = 0001 → 1
print(a | b)  # OR  →  0101 | 0011 = 0111 → 7
print(a ^ b)  # XOR →  0101 ^ 0011 = 0110 → 6
print(~a)     # NOT →  ~0101 = -6  (por cómo maneja Python los bits)
print(a << 1) # Desplazar bits a la izquierda (multiplica por 2) → 1010 → 10
print(a >> 1) # Desplazar bits a la derecha (divide por 2) → 0010 → 2





# Ejemplos de estructuras de control


# Condicionales (if, elif, else)
# Bucles (for, while)
# Control de flujo en bucles (break, continue, pass)


# Condicionales

# se usan para ejecutar codigo solo si se cumplen ciertas condiciones

edad = 20

if edad >= 18:  # Comparación con >=
    print("Eres mayor de edad.")
elif edad == 17:  # Comparación con ==
    print("Casi eres mayor de edad.")
else:
    print("Eres menor de edad.")


# Ejemplo con operadores logicos

usuario = "admin"
clave = "5432"

if usuario == "admin" and clave == "5432":  # AND lógico
    print("Acceso permitido")
else:
    print("Acceso denegado")


# Ejemplo con operadores de identidad y pertenencia

lista = [1, 2, 3, 4]
x = 3

if x in lista:  # Pertenencia
    print("El número está en la lista.")

if type(x) is int:  # Identidad
    print("x es un entero.")



# Bucle (for)

# Se usa para recorrer secuencias (listas, tuplas, cadenas, etc.)

# Usando un bucle for con operadores aritméticos
for i in range(1, 6):  # Genera números del 1 al 5
    print(f"El cuadrado de {i} es {i**2}")  # Operador de potencia


# Ejemplo con listas y operadores de asignación

numeros = [1, 2, 3, 4, 5]
suma = 0

for num in numeros:
    suma += num  # Operador de asignación (+=)

print("La suma total es:", suma)


# Ejemplo con cadenas y pertenencia

palabra = "Python"

for letra in palabra:
    if letra in "aeiou":  # Verifica si es una vocal
        print(f"{letra} es una vocal")


# Bucle (while)

x = 10

while x > 0:  # Condición con operador de comparación
    print(f"x vale {x}")
    x -= 2  # Resta usando operador de asignación (-=)

# Ejemplo con operadores logicos

numero = 1

while numero < 10 and numero % 2 != 0:  # AND lógico y operador módulo
    print(f"{numero} es impar")
    numero += 2



# Control de flujo en bucles (break, continue, pass)


# Estos comandos permiten modificar el comportamiento de los bucles

# break (sale del bucle)

for num in range(10):
    if num == 5:
        print("Se encontró el 5, saliendo del bucle.")
        break  # Detiene la ejecución
    print(num)

# continue (salta a la siguiente iteracion)

for num in range(1, 6):
    if num == 3:
        continue  # Salta la iteración cuando num es 3
    print(num)

# pass (se usa como marcador de posicion)

for num in range(3):
    pass  # No hace nada, evita errores de sintaxis

if True:
    pass  # Se usa cuando aún no hemos definido la lógica


"""
DIFICULTAD EXTRA:
Crea un programa que imprima por consola todos los números comprendidos
entre 10 y 55 (incluidos), pares, y que no son ni el 16 ni múltiplos de 3.
"""

# Bucle que recorre los números del 10 al 55 (incluidos)

#for numero in range(10, 56):  # range(10, 56) genera números del 10 al 55

#    if numero % 2 != 0:  # Si el número NO es par, lo saltamos
#        continue  # Salta a la siguiente iteración

#    if numero == 16:  # Si el número es 16, lo saltamos
#        continue

#    if numero % 3 == 0:  # Si el número es múltiplo de 3, lo saltamos
#        continue

#    print(numero)  # Si pasa todos los filtros, lo imprimimos

for n in range(10, 56, 2):  # Solo números pares del 10 al 55
    if n != 16 and n % 3:
        print(n)



