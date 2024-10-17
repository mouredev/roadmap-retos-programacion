"""
Aritméticos: + - * / //
"""
# Pide al usuario que ingrese 2 números y los asigna a las variables ´a' y 'b', con map les aplicamos a ambos la función int() para convertirlos en enteros y poder operarlos. (por default recibidos en string, por eso se parsea/convierte)
a, b = map(int, input("Ingresa 2 valores para los ejemplos de Operadores Aritméticos separados por espacio (Ej: 5 1): ").split())

# Realizamos las operaciones.
suma = a + b
resta = a - b
multiplicacion = a * b
division = a / b
division_entera = a // b
modulo = a % b
exponente = a ** b

# Imprimimos las operaciones mostrando un ejemplo de como se realiza con los valores 'a' y 'b'.
print(f"Suma: {a} + {b} = {suma}")
print(f"Resta: {a} - {b} = {resta}")
print(f"Multiplicación: {a} * {b} = {multiplicacion}")
print(f"División: {a} / {b} = {division}")
print(f"Módulo: {a} % {b} = {modulo}")
print(f"Exponente: {a}**{b} = {exponente}")
print(f"Division entera: {a} // {b} = {division_entera}")

# Operadores de comparación
a, b = map(int, input("Ingresa dos valores para los ejemplos de Operadores de comparación separados por espacio (Ej: 10 3): ").split())

igual = a == b
distinto = a != b
mayor_que = a > b
menor_que = a < b
mayor_igual = a >= b
menor_igual = a <= b

print(f"Igualdad: {a} == {b} = {igual}")
print(f"Distintos: {a} != {b} = {distinto}")
print(f"Mayor que: {a} > {b} = {mayor_que}")
print(f"Menor que: {a} < {b} = {menor_que}")
print(f"Mayor o igual: {a} >= {b} = {mayor_igual}")
print(f"Menor o igual: {a}<={b} = {menor_igual}")

# Operadores Lógicos
a,b = map(int, input("Ingresa los primeros dos valores separados por un espacio (Ej: 10 3): ").split())
c,d = map(int, input("Ingresa los otros dos valores a comprobar formato similar al anterior (Ej: 5 1): ").split())

# Verdadero Ambos
print(f"AND &&: {a} + {b} == {a + b} and {c} - {d} == {c - d} es: {a + b == a + b and c - d == c - d}")
# Verdadero Uno u Otro
print(f"OR ||: {a} + {b} == {a + b} or {d} - {c} == {d - c} es: {a + b == a + b  or c - d == d - c}")
# No es
print(f"NOT !: NOT {d} - {c} == {c - d} es: {not c - d == d - c}")

# Operadores de asignación
my_number = 11 # Asignación
print(f"Base: {my_number}")
my_number += 1 # Suma y asignación
print(f"Suma y asignacion += 1 {my_number}")
my_number -= 1 # Suma y asignación
print(f"Resta y asignacion -= 1 {my_number}")
my_number *= 2 # Suma y asignación
print(f"Multiplicación y asignacion *= 2 {my_number}")
my_number /=2  # Suma y asignación
print(f"División y asignacion /= 1 {my_number}")
my_number %= 2 # Suma y asignación
print(f"Módulo y asignacion %= 2 {my_number}")
my_number **= 1 # Suma y asignación
print(f"Elevación y asignacion **= 1 {my_number}")
my_number //= 1 # Suma y asignación
print(f"División entera y asignacion //= 1 {my_number}")

# Operadores de identidad
my_new_number = my_number
# Compara si son iguales basandose en la posición de memoria
print(f"my_number is my_new_number es: {my_number is my_new_number}")
print(f"my_number is not my_new_number es: {my_number is not my_new_number}")

# Operadores de pertenencia
print(f"'i' in 'Kirito' = {'i' in 'Kirito'} ")
print(f"'u' in 'Kirito' = {'u' not in 'Kirito'} ")

# Operadores de bit
a = 10 # 1010
b = 3 # 0011

print(f"AND: 10 & 3 = {10 & 3}") # 0010
print(f"OR: 10 | 3 = {10 | 3}") # 1011 (Si al menos 1 es 1)
print(f"XOR: 10 ^ 3 = {10 ^ 3}") #1001 (Si son diferentes da 1, sino 0)
print(f"XOR: ~10 = {~10}") # (Intercambia el valor bit a bit de los elementos)
print(f"Desplazamiento a la derecha: 10 >> 2 = {10 >> 2}") # 10: 1010 >> 0010
print(f"Desplazamiento a la derecha: 10 << 2 = {10 << 2}") # 10: 1010 >> 101000

"""
Estructuras de control
"""

# Condicionales

my_string = "Martes"

if my_new_number == "Martes":
    print("Buen Martes para todos!")
elif my_string == "Miercoles":
    print("Buen Miercoles para todos!")
else:
    print("Buena semana para todos!")

# Iterativas
for i in range(11):
    print(i)

i = 0

while i <= 10:
    print(i)
    i += 1

# Manejo de excepciones
try:
    print(10 / 1)
except:
    print("Se ha producido un error")
finally:
    print("Hemos terminado el manejo de excepciones")

# Dificultad Extra
#  * Crea un programa que imprima por consola todos los números comprendidos
#  * entre 10 y 55 (incluidos), pares, y que no son ni el 16 ni múltiplos de 3.
for i in range(10,56):
    if i % 2 == 0 and i != 16 and i % 3 != 0:
        print(i)