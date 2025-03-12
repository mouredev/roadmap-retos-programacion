# Operadores aritmeticos

suma = 3 + 2 # operador +
print(suma)

resta = 5 - 2 # operador -
print(resta)

multiplicacion = 5 * 3 #operador *
print(multiplicacion)

division = 10 / 2 # operador /
print(division)

division_entera = 13 // 3 # operador //
print(division_entera)

division_residuo = 13 % 3 # operador %
print(division_residuo)

exponente = 3 ** 2 #operador **
print(exponente)

# Operadores logicos

# Operador and: devuelve True si ambos valores son True, devuelve False si alguna de los valores es False

print(True and True)
print(True and False)
print(False and False)

# Operador or: devuelve True si al menos una de los valores es True, si ambos son False, devuelve False

print(True or True)
print(True or False)
print(False or False)

# Operador not: Invierte el valor booleano

print(not True)
print(not False)

# Operadores de comparacion

print(5 > 3) # 5 es mayor que 3, asi que devuelve True
print(5 < 3) # 5 no es menor que 3, asi que devuelve False
print(5 >= 5) # 5 si es igual o mayor que 5, asi que devuelve True
print(5 <= 5) # 5 si es menor o igual que 5, asi que devuelve True
print(5 == 5) # 5 si es igual que 5, asi que duevuelve True
print(5 != 4) # 5 no es igual a 4 asi que devuelve True

# Operadores de asignacion

var = 5 # asigna un valor a una variable
var += 2 # suma un nuevo valor a la variable
print(var)

var -= 3 # resta un nuevo valor a la variable
print(var)

var *= 3 # multiplica por el valor asignado la variable
print(var)

var /= 2 # divide entre el valor asignado de la variable
print(var)

var %= 2 # Modulo del valor asignado a la variable
print(var)

var += 10
var //= 3 # Division entera
print(var)

var **= 2 # hace operacion de potencia a la variable
print(var)

# Estructuras de control

# Condicional if

mi_numero = 5

if mi_numero == 5:
    print("mi numero es igual a 5")
elif mi_numero > 5:
    print("mi numero es mayor que 5")
else:
    print("mi numero es menor que 5")

# Bucle for

for i in range(10):
    print(i)

# Bucle while

i = 0

while i <= 10:
    print(i)
    i += 1

# Manejo de excepcion
try:
    print (10 / 0)
except: 
    print("No se puede dividir entre 0")
finally:
    print("Se concluyo el manejo de excepciones")

# Ejercisio de dificultad extra

for i in range(10, 56):
    if i % 2 == 0 and i != 16 and i % 3 != 0:
        print(i)