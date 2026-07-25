import random

print(f"Suma: 5+6 = {5+6}")
print(f"Resta: 5-6 = {5-6}")
print(f"Multiplicacion: 5*6 = {5*6}")
print(f"Exponente: 5**6 = {5**6}")
print(f"Division: 5/6 = {5/6}")
print(f"Division Entera: 5//6 = {5//6}")
print(f"Modulo: 5%6 = {5%6}")

print("\nLogicos")
num_aleatorio = random.randint(1, 10)

print(f"Comparar Igualdad: 10 == {num_aleatorio} -> {5 == num_aleatorio}")
print(f"Comparar Desigualdad: 10 != {num_aleatorio} -> {5 != num_aleatorio}")
print(f"Comparar si es numero mayor: 10 > {num_aleatorio} -> {5 > num_aleatorio}")
print(f"Comparar si es numero menor: 10 < {num_aleatorio} -> {5 < num_aleatorio}")
print(f"Comparar si es numero mayor o igual: 10 >= {num_aleatorio} -> {5 >= num_aleatorio}")
print(f"Comparar si es numero menor o igual: 10 <= {num_aleatorio} -> {5 <= num_aleatorio}")

print("\nComparacion")

print(f"Operador AND: {num_aleatorio}%2==0 and {num_aleatorio}%4==0 -> {num_aleatorio % 2 == 0 and num_aleatorio % 4 == 0}")
print(f"Operador OR: {num_aleatorio}%2==0 or {num_aleatorio}%4==0 -> {num_aleatorio % 2 == 0 or num_aleatorio % 4 == 0}")
print(f"Operador NOT: not {num_aleatorio}%2==0 -> {not num_aleatorio % 2 == 0}")

print("\nAsignacion")

numero_asignado = num_aleatorio * 2
print(numero_asignado)
numero_asignado += 2
print(numero_asignado)
numero_asignado -= 2
print(numero_asignado)
numero_asignado *= 2
print(numero_asignado)
numero_asignado **= 2
print(numero_asignado)
numero_asignado /= 2
print(numero_asignado)
numero_asignado //= 2
print(numero_asignado)
numero_asignado %= 1
print(numero_asignado)

print("\nIdentidad")
nuevo_numero = 0.0
print(f"{numero_asignado} is {nuevo_numero} == {numero_asignado is nuevo_numero}")
print(f"{numero_asignado} is not {nuevo_numero} == {numero_asignado is not nuevo_numero}")

print("\nPertenencia")
print(f"'t' in 'python' = {'t' in 'python' }")
print(f"'t' not in 'python' = {'t' not in 'python' }")

print("\nBits")
primer_bit = 10
segundo_bit = 3
print(f"AND: 10 & 3 =  {primer_bit & segundo_bit}")
print(f"OR: 10 | 3 =  {primer_bit | segundo_bit}")
print(f"AND: 10 ^ 3 =  {primer_bit ^ segundo_bit}")
print(f"NOT: ~10 =  {~primer_bit}")

print("\nCondicionales")
num_aleatorio = random.randint(0, 10)
if num_aleatorio % 2 == 0:
    print("Numero Par")
elif num_aleatorio % 3 == 0:
    print("Divisible por tres")
else:
    print("Numero Impar")


print("\nIterables")
print("For loop")
for i in range(num_aleatorio):
    print(i)
print("While loop")
while num_aleatorio > 0:
    print(num_aleatorio)
    num_aleatorio -= 1


print("\nExcepciones")
try:
    print(5/0)
except ZeroDivisionError:
    print("No se puede dividir por 0")
finally:
    print("Excepcion controlada")



print("\nDificultad Extra: ")
for number in range(10, 55):
    if number % 2 == 0:
        if number % 3 != 0 and number != 16:
            print(number)
