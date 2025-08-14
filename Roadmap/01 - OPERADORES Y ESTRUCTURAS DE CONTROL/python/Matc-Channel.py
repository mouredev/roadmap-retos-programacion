'''
OPERADORES
'''

# Aritméticos
print(f"suma: 10 + 3 = {10 + 3}")
print(f"Resta: 10 - 3 = {10 - 3}")
print(f"Multiplicación: 10 * 3 = {10 * 3}")
print(f"División: 10 / 3 = {10 / 3}")
print(f"Módulo: 10 % 3 = {10 % 3}")
print(f"Exponente: 10 ** 3 = {10 ** 3}")
print(f"División Entera: 10 // 3 = {10 // 3}")


# variable uso
sum = 10 + 3
print(sum)

# OPERADORES DE COMPARACIÓN
print(f"Igualdad: 10 == 3 es {10 == 3}")
print(f"Desigualdad: 10 == 3 es {10 != 3}")
print(f"Mayor que: 10 == 3 es {10 > 3}")
print(f"Menor que: 10 == 3 es {10 < 3}")
print(f"Mayor o igual que: 10 == 3 es {10 >= 3}")
print(f"Menor o igual que: 10 == 3 es {10 <= 3}")

# Operadores Lógicos
print(f"AND &&: 10 + 3 and 5 - 1 == 4 es {10 + 3 == 13 and 5 - 1 == 4}")
print(f"OR ||: 10 + 3 == 13 or 5 - 1 == 4 es {10 + 3 == 13 or 5 - 1 == 4}")
print(f"NOT !: 10 + 3 == 14 es {10 + 3 == 14}")
# añadiendo NOT
print(f"NOT !: 10 + 3 == 14 es {not 10 + 3 == 14}")

# OPERADORES DE ASIGNACIÓN
my_number = 11  # => asignar
print(my_number)
# suma y asignación
my_number += 2
print(my_number)
# resta y asignación
my_number -= 2
print(my_number)
# multiplicación y asignación
my_number *= 2
print(my_number)
# División y asignación
my_number /= 2
print(my_number)
# Módulo y asignación
my_number %= 2
print(my_number)
# Exponente y asignación
my_number **= 2
print(my_number)
# División Enteta
my_number //= 2
print(my_number)


# OPERADORES DE IDENTIDAD
# False por que ocupan diferente dirección de memoria
my_new_number = 1.0
print(f"my_new_number is my_new_number es: {my_number is my_new_number}")

# True por que  ocupan mismo lugar de memoria
my_new_number = my_number
print(f"my_new_number is my_new_number es: {my_number is my_new_number}")

# Añadiendo operador de DESIGUALDAD NOT
print(f"my_new_number is my_new_number es: {my_number is not my_new_number}")

# OPERADORES DE PERTENECIA
'''Si algo pertenece a algo...'''
print(f"'m' in 'Kramer' = {'u' in 'mourdev'}")
print(f"'z' not in 'Kramercito' = {'z' not in 'Kramercito'}")

# OPERADORES DE BIT
a = 10  # => 1010
b = 3   # => 0011
# 1 si ambos BITS son 1
print(f"AND: 10 & 3 = {10 & 3}")    # => 0010
# 1 si al menos uno de los BITS es 1
print(f"OR: 10 | 3 = {10 | 3}")     # => 1011
# 1 si los BITS son DIFERENTES
print(f"XOR: 10 ^ 3 = {10 ^ 3}")   # => 1001
# fórmula ~n = -(n+1)
print(f"NOT: ~10 = {~10}")  # => -11
# BITS del número se MUEVEN A LA DERECHA
print(f"Desplazamiento a la derecha: {10 >> 2}")    # => 1010 = 0010=2
# BITS del número se MUEVEN A LA IZQUIERDA
print(f"Desplazamiento a la Izquierda: {10 << 2}")    # => 1010 = 101000=40


'''
ESTRUCTURAS DE CONTROL
'''

# CONDICIONALES

my_string = 'MoureDev'

if my_string == 'MoureDev':
    print("my_string es 'Mouredev'")
elif my_string == 'Brais':
    print("my_string es 'Brais'")
else:
    print("my_string no es 'MoureDev' ni 'Brais'")


# ITERATIVAS
# Esto es un BUCLE o LOOP
# 'i' es una VARIABLE que cambia cada vuelta de BUCLE: i=0, i=1... i=10.
for i in range(11):     # => Hacer algo 11 veces
    print(i)    # => Imprime números del 0-10


i = 0   # => Le decimos, EMPIEZA desde CERO...

while i <= 10:
    print(i, 'Kramercito')  # => Mientras i sea MENOR o IGUAL a 10 REPITE..
    i += 1  # => SUMALE 1 A i MIENTRAS se repite el BUCLE...


# ESTRUCTURAS DE CONTROL PARA MANEJO DE EXEPCIONES

try:    # INTENTAR
    print(10 / 0)   # => INTENTAEJECUTAR ESTE CÓDIGO
except ZeroDivisionError:   # => FLAKE8 ERROR al DIOVIDIR por CERO
    print('Se ha producido un ERROR')   # => SALTA AQUÍ, si falla el BLOQUE TRY
finally:
    print('Ha finalizado el manejo de exepciones')  # => EJECUTA SIEMPRE


'''
EXTRA

Crea un programa que imprima por consola todos los números comprendidos
entre 10 y 55 (incluidos), pares, y que no son ni el 16 ni múltiplos de 3.
Seguro que al revisar detenidamente las posibilidades has descubierto algo
nuevo.
'''

for number in range(10, 56):    # => BUCLE de 10-55, excluye 56.
    if number % 2 == 0 and number != 16 and number % 3 != 0:
        print(number)

# terminado
