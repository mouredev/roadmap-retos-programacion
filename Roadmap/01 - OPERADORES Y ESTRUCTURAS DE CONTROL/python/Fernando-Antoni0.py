'''- Crea ejemplos utilizando todos los tipos de operadores de tu lenguaje:
 *   Aritméticos, lógicos, de comparación, asignación, identidad, pertenencia, bits...
 *   (Ten en cuenta que cada lenguaje puede poseer unos diferentes)'''

a = 7
b = 4

print("Valores... a = 7  y  b = 4")
#Operadores aritmeticos
print("Operadores aritmeticos")
#Suma +
print(f"La suma de a + b es: {a + b}")
#Resta -
print(f"La resta de a - b es: {a - b}")
#Multiplicacion *
print(f"La multiplicacion de a * b es: {a * b}")
#Division /
print(f"La division de a / b es: {a / b}")
#Division entera(ENTEROS) //
print(f"La division entera de a // b es: {a // b}")
#Modulo(residuo division) %
print(f"El modulo de a % b es: {a % b}")
#Potencia **
print(f"La potencia de a ** b es: {a ** b}")

#Operadores comparativos
print("Operadores de comparacion")
#Mayor que >
print(f"Mayor que, a > b : {a > b}")
#Mayor o igual que >=
print(f"Mayor o igual que, a >= b : {a >= b}")
#Menor o igual que <=
print(f"Menor o igual que, a <= b : {a <= b}")
#Menor que <
print(f"Menor que, a < b : {a < b}")
#Igual que ==
print(f"Es igual que, a == b : {a == b}")
#Diferente que !=
print(f"Diferente que, a != b : {a != b}")

#Operadores logicos
print("Operadores logicos")
#AND &&
print(f"AND &&: 2 + 5 == 7 and 4 - 2 == 1 : {2 + 5 == 7 and 4 - 2 == 1}")
#OR ||
print(f"OR ||: 2 + 5 == 7 or 4 - 2 == 1 : {2 + 5 == 7 or 4 - 2 == 1}")
#NOT !
print(f"NOT !: 15 - 5 == 11 : {not 15 - 5 == 11}")

#Operadores de asignacion
print("Operadores de asignacion")

asignacion = 9
print(asignacion)
asignacion += 1 #Suma y asignacion
print(asignacion)
asignacion -= 2 #Resta y asignacion
print(asignacion)
asignacion *= 3 #Multiplicacion y asignacion
print(asignacion)
asignacion /= 4 #Division y asignacion
print(asignacion)
asignacion //= 5 #Division de enteros y asignacion
print(asignacion)
asignacion **= 6 #Potencia y asignacion
print(asignacion)
asignacion %= 7 #Modulo y asignacion
print(asignacion)

#Operadores de pertenencia
print("Operadores de pertenencia")
print(f"Hay una 'n' in 'Fernando' {'n' in 'Fernando'}" )
print(f"Hay una 'z' not in 'Fernando' {'z' not in 'Fernando'}" )

#Operadores de identidad
print("Operadores de identidad")
identidad1 = "gato"
identidad2 = "gato"

print(f"identidad1 is identidad2 : {identidad1 is identidad2}")
print(f"identidad1 is not identidad2 : {identidad1 is not identidad2 }")

'''
Estructuras de control
'''
'''
Utilizando las operaciones con operadores que tú quieras, crea ejemplos
que representen todos los tipos de estructuras de control que existan
en tu lenguaje
'''

#condicionales

num = 5

if num == 5:
    print("El numero es 5")
elif num == 3:
    print("El numero es 3")
else:
    print("El numero no es 5 y tampoco 3")

#Iterativas

for i in range(11):
    print(i)


i = 0

while i <= 10:
    print(i)
    i += 1

#Manejo de excepciones

try:
    print(30 / 0)
except:
    print("El programa tuvo un error")
finally:
    print("Se termino la prueba de excepciones")



'''
DIFICULTAD EXTRA (opcional):
Crea un programa que imprima por consola todos los números comprendidos
entre 10 y 55 (incluidos), pares, y que no son ni el 16 ni múltiplos de 3.
'''

for i in range(10, 56):
    if i % 2 == 0 and i != 16 and i % 3 != 0:
        print(i)