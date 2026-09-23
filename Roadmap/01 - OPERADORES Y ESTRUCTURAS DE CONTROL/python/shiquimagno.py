"""
/*
 *
 * DIFICULTAD EXTRA (opcional):
 * Crea un programa que imprima por consola todos los números comprendidos
 * entre 10 y 55 (incluidos), pares, y que no son ni el 16 ni múltiplos de 3.
 *
 * Seguro que al revisar detenidamente las posibilidades has descubierto algo nuevo.
 */
"""
# Ejemplos con todos los operadores de python


a = 2
b = 3
if a and b <= 3 or a+b == b:
    print("A y B son menores o iguales que 3")
elif a or b < 3:
    print("A o B es menor que 3")
elif a+b == 8:
    print("A + B = 8, imposible")

if a != b:
    print("A y B son distintos")
elif a > b:
    print("A es mayor que B")

if a >= b:
    print("A es mayor o igual que B")
if not False:
    print("Es cierto, no es falso")
division = b / a
print("División:", division)
print("Floor division", b//a)
multiplication = a*b
modulus = b%a
print("Módulo: ", modulus)
print("Multiplicación:",multiplication)
potenciacion = a**b
print("Potenciación", potenciacion)
number = 10
print(number)
number += 1
print(number)

number -= 1
print(number)

number *= 1
print(number)

number /= 1
print(number)

number //= 1
print(number)

number %= 1
print(number)

number **= 1
print(number)
number_two= 0.0
# Operadores de identidad
print(f"{number is number_two} ") # Verifica en memoria
print(f"{number is not number_two} ") # Verifica en memoria

# Operadores de pertenencia
print(f"'a' in 'palabra' = {'a' in 'palabra'} ")
print(f"'a' in 'palabra' = {'a' not in 'palabra'} ")

# Operadores de bit
print(f"a = {a}")
print(f"AND: 10&2 = {10&2}")
print(f"OR: 10|2 = {10|2}")
print(f"NOT: 10&2 = {~10}")
print(f"XOR: 10&2 = {10^2}")
# Desplazamientos
print(f"Desplazamiento a la derecha: 10 >> 2 = {10 >> 2}") # Completa con ceros
print(f"Desplazamiento a la derecha: 10 << 2 = {10 << 2}") 


# Estructuras de control
if a + b > 100:
    print("A y B suman más de 100")
elif a + b > 50:
    print("A y B suman más de 50, pero 100 o menos")
else: 
    print("A y B suman 50 o menos")

while a < b: 
    print("A:", round(a, 2)) # Ocultando el error acumulado por floats 
    a += 0.1
try:
    for i in "palabra":
        print(i)
except Exception as e:
    print("El error es: ", e.with_traceback)
else: 
    print("Si ves esto, todo salió bien con el bloque try, oushea")
finally: 
    print("Fin del try and except")

# Retos
for i in range(10, 56):
    if i % 2 == 0 and i %16!=0 and i %3!=0:
        print(i)