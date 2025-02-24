"""
! OPERADORES ARITMÉTICOS
"""

# ! Operadores aritméticos --> SUMA

print(f"Suma: 27 + 31 = {27 + 31}") # ? Esta es una manera de hacerlo mas lineal
suma = 27 + 31 # ? Otra forma de hacerlo
print(f"El resultado es = ", suma)

# ! Operadores aritméticos --> RESTA
print(f"Resta: 31 - 27 = {31 - 27}")
resta = 31 - 27
print(f"El resultado de la resta es = ", resta)

# ! Operadores aritméticos --> MULTIPLICACIÓN
print(f"Multiplicación: 31 * 27 = {31 * 27}")
multiplicacion = 31 * 27
print(f"El resultado de la multiplicación es = ", multiplicacion)

# ! Operadores aritméticos --> DIVISIÓN
print(f"División: 22 / 5 = {22 / 5}")
division = 22 / 5
print(f"El resultado de la división es = ", division)

# ! Operadores aritméticos --> MÓDULO
print(f"Módulo: 31 % 27 = {31 % 27}")
modulo = 31 % 27
print(f"El resultado de la módulo es = ", modulo)

# ! Operadores aritméticos --> EXPONENTE
print(f"Exponente: 22 ** 5 = {22 ** 5}")
exponente = 22 ** 5
print(f"El resultado del exponente es = ", exponente)

# ! Operadores aritméticos --> DIVISIÓN ENTERA
print(f"División entera: 31 // 27 = {31 // 27}")
division_entera = 31 // 27
print(f"El resultado de la División entera es = ", division_entera)

# ! Operadores de comparación
print(f"Igualdad: 10 == 3 es {10 == 3}")
print(f"Desigualdad: 10 != 3 es {10 != 3}")
print(f"Mayor que: 10 > 3 es {10 > 3}")
print(f"Menor que: 10 < 3 es {10 < 3}")
print(f"Mayor o igual que: 10 >= 3 es {10 >= 3}")
print(f"Menor o igual que: 10 <= 3 es {10 <= 3}")

# ! Operadores Lógicos
# ? AND --> ambas condiciones tienen que ser verdaderas (True)
print(f"AND &&: 10 + 3 = 13 && 5 - 1 = 4 es {10 + 3 == 13 and 5 - 1 == 4}")
#? OR --> al menos una de las condiciones tiene que ser verdadera (True)
print(f"OR ||: 10 + 3 = 13 || 5 - 1 = 4 es {10 + 3 == 18 or 5 - 1 == 4}")
#? NOT --> sirve para negar una afirmación
print(f"NOT !: not 10 + 3 = 18 es {not 10 + 3 == 18}")
#? Cuando negamos una afirmacion que es correcta devuelve False
print(f"NOT !: not 10 + 3 = 13 es {not 10 + 3 == 13}")

# ! Operadores de Asignación
mi_numero = 27 # asignación
print(mi_numero)
mi_numero += 3 # suma y asignación
print(mi_numero)
mi_numero -= 15 # resta y asignación
print(mi_numero)
mi_numero *= 8 # multiplicación y asignación
print(mi_numero)
mi_numero /= 3 # división y asignación
print(mi_numero)
mi_numero %= 2 # modulo y asignación
print(mi_numero)
mi_numero **=2 # exponente y asignación
print(mi_numero)
mi_numero //=1 # división entera y asignación
print(mi_numero)

# ! Operadores de identidad
mi_nuevo_numero = 0.0
print(f"mi_numero is mi_nuevo_numero es {mi_numero is mi_nuevo_numero}")
mi_nuevo_numero = mi_numero
print(f"mi_numero is mi_nuevo_numero es {mi_numero is mi_nuevo_numero}")
print(f"mi_numero is not mi_nuevo_numero es {mi_numero is not mi_nuevo_numero}")

# ! Operadores de pertenencia
print(f"'z' in 'aliz' = {'z' in 'aliz'}")
print(f"'z' not in 'aliz' = {'z' not in 'aliz'}")
print(f"'c' not in 'aliz' = {'c' not in 'aliz'}")

# ! Operadores de bit
a = 27 # 11011
c = 31 # 11111

print(f"AND: 27 & 31 = {27 & 31}") # 11011
print(f"OR: 27 | 31 = {27 | 31}") # 11111
print(f"XOR: 27 ^ 31 = {27 ^ 31}") # 00100
print(f"NOT: ~27 = {~27}")
print(f"Desplazamiento a la derecha: 27 >> 2 = {27 >> 2}") # 00110
print(f"Desplazamiento a la izquierda: 27 << 2 = {27 << 2}") # 1101100

"""
! ESTRUCTURAS DE CONTROL
"""
# ! Condicionales

my_string = "Kyra"

if my_string == "Aliz":
    print("Mi string es 'Aliz'")
elif my_string == "Charlizon":
    print("my_string es 'Charlizon'")
else:
    print("my_string no es 'Aliz' ni 'Charlizon'")

# ! Iterativas

for i in range(11):
    print(i)

i = 0

while i <= 10:
    print(i)
    i += 1 # ? --> con esta linea de código la iteracion va del 0 al 10 que es cuando se deja de cumplir la condicion del bucle

# ! Manejo de excepciones
try:
    print(10 / 0)
except:
    print("Se ha producido un error")
finally:
    print("Ha finalizado el manejo de excepciones")


# ! ------------ EXTRA -----------------
"""
Crea un programa que imprima por consola todos los números comprendidos
entre 10 y 55 (incluidos), pares, y que no son ni el 16 ni múltiplos de 3.
"""
for number in range(10,56):
    if number % 2 == 0 and number != 16 and number % 3 != 0:
        print(number)

"""
Realiza un programa que permita ingresar un numero entero e indique
si se trata de un numero par o impar
"""