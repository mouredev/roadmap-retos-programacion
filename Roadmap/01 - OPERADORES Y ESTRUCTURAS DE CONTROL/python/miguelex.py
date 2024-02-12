# Ejemplos de operadores aritmeticos en python

print("Vamos a mostrar ejemplos de los operadores aritmeticos")
print(f"La solución de 2 + 3 es igual a {2 + 3}")
print(f"La solución de 2 - 3 es igual a {2 - 3}")
print(f"La solución de 5 * 3 es igual a {5 * 3}")
print(f"La solución de 5 / 3 es igual a {5 / 3} (Esta es la división normal)")
print(f"La solución de 5 % 3 es igual a {5 % 3}")
print(f"La solución de 5 ** 3 es igual a {5 ** 3}")
print(f"La solución de 5 // 3 es igual a { 5// 3} (Esta es la división entera)")
print("\n")

# Ejemplos de operadores logicos
print("Vamos a mostrar ejemplos de los operadores logicos")
print(f"¿Verdad && Verdad? {True and True} (Ejemplo de AND)")
print(f"¿Verdad || Falso? {True or True} (Ejemplo de OR)")
print(f"¿not Verdad? {not True} (Ejemplo de NOT)")
print("\n")

# Ejemplos de operadores de comparación 
print("Vamos a mostrar ejemplos de los operadores de comparación")
print(f"¿5 == 3? {5 == 3} (Ejemplo de igualdad)")
print(f"¿5 != 3? {5 != 3} (Ejemplo de desigualdad)")
print(f"¿5 < 3? {5 < 3} (Ejemplo de Menor que )")
print(f"¿5 <= 3? {5 <= 3} (Ejemplo de Menor o Igual que)")
print(f"¿5 > 3? {5 > 3} (Ejemplo de Mayor)")
print(f"¿5 >= 3? {5 >= 3} (Ejemplo de Mayor o Igual que)")
print("\n")

# Ejemplos de oepradores de asignación
print("Vamos a mostrar ejemplos de los operadores de asignación")
numero = 1
print(f"El valor de numero es {numero}")
numero += 1
print(f"El valor de numero += 1 es {numero}")
numero -= 1
print(f"El valor de numero -= 1 es {numero}")
numero *= 5
print(f"El valor de numero *= 5 es {numero}")
numero /= 2
print(f"El valor de numero /= 2 es {numero}")
numero %= 2
print(f"El valor de numero %= 2 es {numero}")
numero **= 2
print(f"El valor de numero **= 2 es {numero}")
numero //= 2
print(f"El valor de numero //= 2 es {numero}")
print("\n")

# Ejemplos operadores de bit
print("Vamos a mostrar ejemplos de los operadores de bit")
a = 10
b = 15
print(f"El valor de a & b es {a & b} (Operacion AND)")
print(f"El valor de a | b es {a | b} (Operación OR)")
print(f"El valor de a ^ b es {a ^ b} (Operación XOR)")
print(f"El valor de ~a es {~a} (Operación NOt)")
print(f"El valor de a >> b es {a >> b}")
print(f"El valor de a << b es {a << b}")
print("\n")

# Estructuras de control

# Ejemplos de if
print("Vamos a mostrar ejemplos de if")
if 5 > 3:
    print("5 es mayor que 3")
print("\n")

# Ejemplos de if else
print("Vamos a mostrar ejemplos de if else")
if 5 < 3:
    print("5 es menor que 3")
else:
    print("5 no es menor que 3")
print("\n")

# Ejemplos de if elif else
print("Vamos a mostrar ejemplos de if elif else")
if 5 < 3:
    print("5 es menor que 3")
elif 5 == 3:
    print("5 es igual que 3")
else:
    print("5 es mayor que 3")
print("\n")

# Ejemplo de match
print("Vamos a mostrar ejemplos de match")
numero = 5
match numero:
    case 1:
        print("El numero es 1")
    case 2:
        print("El numero es 2")
    case 3:
        print("El numero es 3")
    case 4:
        print("El numero es 4")
    case 5:
        print("El numero es 5")
    case 6:
        print("El numero es 6")
    case 7:
        print("El numero es 7")
    case 8:
        print("El numero es 8")
    case 9:
        print("El numero es 9")
    case 10:
        print("El numero es 10")
    case _:
        print("El numero es mayor que 10")
print("\n")

# Ejemplo de while
print("Vamos a mostrar ejemplos de while")
numero = 1
while numero <= 10:
    print(numero)
    numero += 1
print("\n")

# Ejemplo de do .. while
print("Vamos a mostrar ejemplos de do .. while")
numero = 1
while True:
    print(numero)
    numero += 1
    if numero > 10:
        break
print("\n")

# Ejemplo de for
print("Vamos a mostrar ejemplos de for")
for numero in range(1, 11):
    print(numero)
print("\n")

# Ejemplo Range
print("Vamos a mostrar ejemplos de range")
for numero in range(1, 5):
    print(numero)
print("\n")

print("Vamos a mostrar ejemplos de range con saltos")
for numero in range(1, 20, 2):
    print(numero)
print("\n")

# Ejemplo de for else
print("Vamos a mostrar ejemplos de for else")
for numero in range(1, 11):
    print(numero)
else:
    print("El for ha terminado")
print("\n")

# Ejemplo de break
print("Vamos a mostrar ejemplos de break")
for numero in range(1, 11):
    print(numero)
    if numero == 5:
        break
print("\n")

# Ejemplo de continue
print("Vamos a mostrar ejemplos de continue")
for numero in range(1, 11):
    if numero == 5:
        continue
    print(numero)
print("\n")

# Ejemplo de pass
print("Vamos a mostrar ejemplos de pass")
for numero in range(1, 11):
    if numero == 5:
        pass
    print(numero)
print("\n")

# Ejemplo de for in
print("Vamos a mostrar ejemplos de for in")
lista = [1, 2, 3, 4, 5]
for numero in lista:
    print(numero)
print("\n")

# Ejemplo de excepciones
print("Vamos a mostrar ejemplos de excepciones")
try:
    print(5 / 0)
except:
    print("Ha ocurrido un error")
finally:
    print("Ha finalizado el manejo de excepciones")
print("\n")

# Ejemplo de raise
print("Vamos a mostrar ejemplos de raise")
try:
    raise Exception("Ha ocurrido un error")
except Exception as error:
    print(error)
print("\n")

# Ejemplo de assert
print("Vamos a mostrar ejemplos de assert")
try:
    assert 5 > 3, "5 no es mayor que 3"
except AssertionError as error:
    print(error)
print("\n")

# Ejercicio extra

print("Vamos a mostrar ejemplos de ejercicio extra")

for number in range(10, 56):
    if number % 2 == 0 and number != 16 and number % 3 != 0:
        print(number)