# Operadores Aritmeticos:

# Suma
suma = 4 + 5
# Resta
resta = 9 - 3
# Multiplicacion
multiplicacion = 5 * 6
# Division
division = 20 % 5
# Modulo
modulo = 20 % 2
# Exponente
exponente = 4 ** 2
# Division Baja
division_baja = 5 // 2

# Operadores de comparacion: >, <, ==, >=, <=, !=

# > (Mayor que)
print(30 > 10) # True
# < (Menor que)
print(20 < 30) # False
# == (Igual que)
print("hola" == 'hola') # True
# >= (Mayor o Igual que)
print(20 >= 20) # True
# <= (Menor o Igual que)
print(20 <= 30) # True
# != (No Igual que)
print(20 != 200) # True


# Operadores Logicos: and, or, not

# and
print(40 > 10 and "hola" == "Hola".lower()) # Imprime True, ya que las dos condiciones son verdaderas

# or
print(30 - 20 == 10 or 30 - 20 == 100) # Imprime True, si una de las condiciones son verdaderas

# not
print(not 20 - 10 == 10) # Imprime False, ya que la condicion es True y el operador NOT invierte al valor contrario

# Operadores de asignacion: =, +=, -=, *=, /=, %=, **=, //=, &=, |=, ^=, >>=, <<=

# = (Operador de asignacion)
variable_numerica = 40 - 20

# += (Operador de suma y asignacion)
numero= 20
numero += 10

print(numero) # 30

# -= (Operador de resta y asignacion)
numero1 = 50
numero1 -= 10
print(numero1) # 40

# *- (Operador de multiplicaion y asignacion)
numero2 = 30
numero2 *= 2
print(numero2) # 60

# /= (Operador de division y asignacion)
numero3 = 40
numero3 /= 2
print(numero3) # 20

# %= (Operador de modulo y asignacion)
numero4 = 30
numero4 %= 5
print(numero4) # 0 # 30 es divisible por 5

# 


if 5 > 3 and 10 < 100:
    print("5 es mayor que 3 y 10 es menor que 100!")
else:
    print("5 no es menor que 3 y 10 no es menor que 100!")

if 10 + 12 == 22 or 30 + 1 == 31:
    print("La funcion print se ejecuta, ya que una de las dos condiciones es verdadera (10 + 12 == 22 --> True)")

lista = [20, 30, 40, 50]

if not 10 in lista:
    print("10 esta en la lista!")
else:
    print("10 no esta en la lista!")