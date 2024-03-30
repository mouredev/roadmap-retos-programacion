# 1- operadores

# aritméticos
operando_1 = 5
operando_2 = 2

print(f"Suma: {operando_1} + {operando_2} = {operando_1 + operando_2}")
print(f"Resta: {operando_1} - {operando_2} = {operando_1 - operando_2}")
print(f"Multiplicación: {operando_1} * {operando_2} = {operando_1 * operando_2}")
print(f"División: {operando_1} / {operando_2} = {operando_1 / operando_2}")
print(f"Módulo: {operando_1} % {operando_2} = {operando_1 % operando_2}")
print(f"Potencia: {operando_1} ** {operando_2} = {operando_1 ** operando_2}")
print(f"División entera: {operando_1} // {operando_2} = {operando_1 // operando_2}")

# lógicos
print(f"AND &&: True and True es: {True and True}")
print(f"AND &&: True and False es: {True and False}")
print(f"OR ||: True or True es: {True or True}")
print(f"OR ||: True or False es: {True or False}")
print(f"NOT !: not True or False es: {not True or False}")

# comparación
print(f"Igualdad: {operando_1} == {operando_2} es {operando_1 == operando_2}")
print(f"Desigualdad: {operando_1} != {operando_2} es {operando_1 != operando_2}")
print(f"Mayor que: {operando_1} > {operando_2} es {operando_1 > operando_2}")
print(f"Mayor o igual que: {operando_1} >= {operando_2} es {operando_1 >= operando_2}")
print(f"Menor que: {operando_1} < {operando_2} es {operando_1 < operando_2}")
print(f"Menor o igual que: {operando_1} <= {operando_2} es {operando_1 <= operando_2}")

# asignación
age = 23
print(f"age: {age}")
age += 1
print(f"age += 1: {age}")
age -= 1
print(f"age -= 1: {age}")
age *= 2
print(f"age *= 2: {age}")
age /= 2
print(f"age /= 2: {age}")
age %= 2
print(f"age %= 2: {age}")
age **= 2
print(f"age **= 2: {age}")
age //= 1
print(f"age //= 1: {age}")

# identidad
a = 1
b = 1
print(f"a is b es: {a is b}")
print(f"a is not b es: {a is not b}")
b = a
print(f"a is b es: {a is b}")
print(f"a is not b es: {a is not b}")

# pertenencia
print(f"'o' in 'aDog': {'o' in 'aDog'}")
print(f"'i' not in 'aDog': {'o' in 'aDog'}")

# bits
a = 10
b = 3
print(f"AND: {a} & {b}: {a & b}")
print(f"OR: {a} | {b}: {a | b}")
print(f"XOR: {a} ^ {b}: {a ^ b}")
print(f"NOT: ~{a}: {~a}")
print(f"Desplazamiento a la derecha {a} >> {b}: {a >> b}")
print(f"Desplazamiento a la izquierda {a} << {b}: {a << b}")

# 2- estructuras de control

# condicionales
name = "aDog"
if name == "aDog":
    print("name es 'aDog'")
elif name == "Flowey":
    print("name es 'Flowey'")
else:
    print("name no es 'aDog' ni 'Flowey'")

# iterativas
for x in range(10):
    print(x)

x = 0
y = 0

while y <= 10:
    print(y)
    y += 1

# excepciones
try:
    print(y / x)
except:
    print("Se ha producido un error")
finally:
    print("Ha finalizado el manejo de excepciones")


# dificultad extra
def my_function(x, y):
    for x in range(x, y):
        if x % 2 == 0 and x != 16 and x % 3 != 0:
            print(x)


my_function(10, 55)
