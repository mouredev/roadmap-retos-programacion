#01
# OPERADORES Y ESTRUCTURAS DE CONTROL
# /*
#  * EJERCICIO:
#  * - Crea ejemplos utilizando todos los tipos de operadores de tu lenguaje:
#  *   Aritméticos, lógicos, de comparación, asignación, identidad, pertenencia, bits...
#  *   (Ten en cuenta que cada lenguaje puede poseer unos diferentes)
#  * - Utilizando las operaciones con operadores que tú quieras, crea ejemplos
#  *   que representen todos los tipos de estructuras de control que existan
#  *   en tu lenguaje:
#  *   Condicionales, iterativas, excepciones...
#  * - Debes hacer print por consola del resultado de todos los ejemplos.
#  *
#  * DIFICULTAD EXTRA (opcional):
#  * Crea un programa que imprima por consola todos los números comprendidos
#  * entre 10 y 55 (incluidos), pares, y que no son ni el 16 ni múltiplos de 3.
#  *
#  * Seguro que al revisar detenidamente las posibilidades has descubierto algo nuevo.
#  */



num_a = 10
num_b = 5

suma = num_a + num_b
resta = num_a - num_b
multiplicacion = num_a * num_b
division = num_a / num_b


print('Los numeros son: ' + str(num_a) + ' y ' + str(num_b))
print('Este es el resultado de la suma: ' + str(suma ))
print('Este es el resultado de la resta: ' + str(resta ))
print('Este es el resultado de la multiplicacion: ' + str(multiplicacion ))
print('Este es el resultado de la division: ' + str(division ))
print()
print('######################################')
print()


if num_a > num_b:
    print('el número ' + str(num_a) + ' es mayor que el número ' + str(num_b))
elif num_b > num_a:
    print('el número ' + str(num_b) + ' es mayor que el número ' + str(num_a))
elif num_a == num_b:
    print('los números son iguales')
else:
    print('los números no son correctos')

print()
print('######################################')
print()

for i in range(1,10):
    if num_b < num_a:
        print(num_b)
        num_b = num_b + 1
    else:
        break

print()
print('######################################')
print()

contador = 1

while contador < 10:
    print(contador)
    contador = contador + 1

print()
print('######################################')
print()
print('######################################')

y = 10
z = 0

try:
    x = y / z
    print(f'La división entre {y} y {z} es igual a {x}')
except:
    print("Error.")

print()
print('######################################')
print()
print('######################################')


python = True
go = False

resultado_and = python and go
resultado_or = python or go
resultado_not = not go

print("AND: estudiando Python Y go?: ", resultado_and) # Ambas tienen que ser True
print("OR: estudiando Python O go? ", resultado_or)   # Una de las dos tiene que ser True
print("NOT: Estudiando solo python? ", resultado_not) # Opuesto al valor 


print()
print('######################################')
print()
print('######################################')
print('EXTRA')
print('######################################')

for i in range(10,56):
    if i == 16:
        continue
    elif i % 3 == 0:
        continue
    elif i % 2 == 0:
        print(i)
    else:
        continue

