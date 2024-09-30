"""
 EJERCICIO:
 * - Crea ejemplos utilizando todos los tipos de operadores de tu lenguaje:
 *   Aritméticos, lógicos, de comparación, asignación, identidad, pertenencia, bits...
 *   (Ten en cuenta que cada lenguaje puede poseer unos diferentes)
 * - Utilizando las operaciones con operadores que tú quieras, crea ejemplos
 *   que representen todos los tipos de estructuras de control que existan
 *   en tu lenguaje:
 *   Condicionales, iterativas, excepciones...
 * - Debes hacer print por consola del resultado de todos los ejemplos.
 *
 * DIFICULTAD EXTRA (opcional):
 * Crea un programa que imprima por consola todos los números comprendidos
 * entre 10 y 55 (incluidos), pares, y que no son ni el 16 ni múltiplos de 3.
 *
 * Seguro que al revisar detenidamente las posibilidades has descubierto algo nuevo.
"""

### Operadores Aritmeticos ###

# Suma
print(f"Suma: 10 + 30 = {10 + 30}")

# Resta
print(f"Resta: 50 - 20 = {50 - 20}")

# Multiplicacion
print(f"Multiplica: 234 x 2244 = {234 * 2244}")

# Division
print(f"Divide: 34 / 2 = {34 / 2} ")

# Modulo
print(f"Modulo: 40 % 3 = {40 % 3}")

# Exponenciales
print(f"Potencia de 40 a la 5 es = {40 ** 5}")

# Division Entera
print(f"Division entera de 40 // 3 = {40 // 3}")

### Operadores Logicos ###

# and => Devuelve True solo si ambos operadores son True
print(f"and: True and True = {True and True}")
print(f"and: True and False = {True and False}")
print(f"and: False and False = {False and False}")

# or => Devuelve True si cualquiera de los operadores es True
print(f"or True or True = {True or True}")
print(f"or: True or False = {True or False}")
print(f"or: False or False = {False or False}")

# not => Invierte los operadores, si es True not devuelve False y viceversa
print(f"not: not True = {not True}")
print(f"not: not False = {not False}")

### Operadores de comparacion ###

print(f"igualdad: 10 == 1 = {10 == 1}")
print(f"No es igual: 10 != 1 = {10 != 1 }")
print(f"Mayor que: 10 > 5 = {10 > 5}")
print(f"Menor que: 1 < 10 = {1 < 10}")
print(f"Mayor o igual que: 10>= 10 {10 >= 10}")
print(f"Menor o igual que: 10 <= 9 {10 <= 9}")

### Operadores de Asignacion ###

my_number = 20
print(my_number)
my_number += 1  # Asignacion y suma
print(my_number)
my_number -= 1  # Asignacion y resta
print(my_number)
my_number *= 2  # Asignacion y Multiplicacion
print(my_number)
my_number /= 2  # Asignacion y Division
print(my_number)
my_number %= 4  # Modulo y Asignacion
print(my_number)
my_number //= 4  # Division de entero y Asignacion
print(my_number)
my_number **= 5  # Exponenciacion y Asignacion
print(my_number)

### Operadores de Identidad ###

my_new_number = 1
# Evalua si los elementos pertenecen al mismo lugar en memoria
print(f"my_number is my_new_number es {my_number is my_new_number}")
print(f"my_number is not my_new_number es {my_number is not my_new_number}")

### Operadores de Pertenencia ###

# Evalua si un elemento se encuentra el elemento dado
print(f"'e' in Jose = {'e' in 'Jose'}")
print(f"'e' not in Jose = {'e' not in 'Jose'}")

### Operadores de bit ###

a = 10  # 1010
b = 3  # 0011

print(f"AND 10 & 3 = {10 & 3}")
print(f"OR 10 | 3 = {10 | 3}")
print(f"XOR 10 ^ 3 = {10 ^ 3}")
print(f"NOT ~10 = {~10}")
print(f"Desplazamiento a la Derecha 10 >> 3 = {10 >> 3}")
print(f"Desplazamiento a la Izquierda 10 << 3 = {10 << 3}")

"""
    Estructuras de Control
"""

### Condicionales ###

my_name = "Jose"

if my_name == "Pedro":
    print("Mi nombre es Jose")
elif my_name == "Juan":
    print("Hola Juan")
else:
    print("Pedro Pedro Pedro PE")

    ### Iterativas ###

for i in range(11):
    print(i)


i = 0

while i <= 10:
    print(i)
    i += 1

    ### Manejo de Excepciones ###


try:
    print(10 / 0)
except:
    print("Se ha producido un error")
finally:
    print("Ha finalizado el manejo de exepciones con exito")


"""
        EXTRA
        Crea un programa que imprima por consola todos los números comprendidos
        entre 10 y 55 (incluidos), pares, y que no son ni el 16 ni múltiplos de 3.
"""


for i in range(10, 56):
    if i % 2 == 0 and i != 16 and i % 3 != 0:
        print(i)
