#
# EJERCICIO:
# - Crea ejemplos utilizando todos los tipos de operadores de tu lenguaje:
#   Aritméticos, lógicos, de comparación, asignación, identidad, pertenencia, bits...
#   (Ten en cuenta que cada lenguaje puede poseer unos diferentes)
# - Utilizando las operaciones con operadores que tú quieras, crea ejemplos
#   que representen todos los tipos de estructuras de control que existan
#   en tu lenguaje:
#   Condicionales, iterativas, excepciones...
# - Debes hacer print por consola del resultado de todos los ejemplos.
#
# DIFICULTAD EXTRA (opcional):
# Crea un programa que imprima por consola todos los números comprendidos
# entre 10 y 55 (incluidos), pares, y que no son ni el 16 ni múltiplos de 3.
#
# Seguro que al revisar detenidamente las posibilidades has descubierto algo nuevo.
#/

# Operadores aritméticos
print(10 + 5) # Suma
print(10 - 5) # Resta
print(10 * 5) # Multiplicación
print(10 / 5) # División
print(10 % 5) # Módulo
print(10 ** 5) # Potencia
print(10 // 5) # División entera

# Operadores lógicos
print(True and True) # Y lógico
print(True or False) # O lógico
print(not True) # Negación lógica

# Operadores de comparación
print(10 == 5) # Igual
print(10 != 5) # Distinto
print(10 > 5) # Mayor que
print(10 < 5) # Menor que
print(10 >= 5) # Mayor o igual que
print(10 <= 5) # Menor o igual que
print(10 is 5) # Identidad
print(10 is not 5) # No identidad
print(10 in [1, 2, 3]) # Pertenencia
print(10 not in [1, 2, 3]) # No pertenencia

# Estructuras de control

# Condicionales
my_fuel = 0

if my_fuel == 0:
    print("No tienes combustible, tienes que repostar antes de continuar")


age = 18

if age >= 18:
    print("Eres mayor de edad")
else:
    print("Eres menor de edad")

my_fuel = 100

if my_fuel == 0:
    print("No tienes combustible, tienes que repostar antes de continuar")
elif my_fuel < 50:
    print('El tanque está por debajo del 50%')
elif my_fuel < 75:
    print('El tanque está por debajo del 75%')
else:
    print('El tanque está lleno')

# Otra opción conditional, similar al switch
match age:
    case 18:
        print("Eres mayor de edad")
    case 17:
        print("Eres menor de edad")
    case _:
        print("No tienes edad")


# Iterativas

my_string = "Hola Mundo"

# For
for char in my_string:
    print(char, end=' ')

# While
i = 0

while i < 5:
    print(i, end=' ')
    i += 1
    
# Excepciones
try:
    print(10 / 0)
except ZeroDivisionError:
    print("No puedes dividir por cero")
except:
    print("Algo salió mal")
finally:
    print("Esto se ejecuta siempre")


# DIFICULTAD EXTRA

for i in range(10, 56):
    if i % 2 == 0 and i != 16 and i % 3 !=0:
        print(i, end=' ')
    