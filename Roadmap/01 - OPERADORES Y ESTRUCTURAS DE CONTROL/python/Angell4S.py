print("### Operadores Aritméticos ###")
suma = 5 + 5
resta = 10 - 2
multi = 5 * 2
div = 6 / 3
pontencia = 2 ** 3
print(f"suma: {suma}, resta: {resta}, multi: {resta}, división: {div}, pontencia: {pontencia}")

print("### Operadores Lógicos ###")

print("## Comparación ##")
mayor = 4 > 3
menor = 5 < 3
igual = 5 == 5
mayorigual = 5 >= 5
menorigual = 7 <= 5
diferente = 3 != 4
print(mayor, menor, igual, mayorigual, menorigual, diferente)

print("## Asignación ##")
x = 4
x = x + 1
x += 1

d = 5
d *= 2
print(x, d)

print("## Identidad ##")
a = 1
b = 2
c = 4
print(a is 1)
print(b is not 2)

print("## Pertenencia ##")
list = [1,2,3,4,5]
print(3 in list)
print(6 in list)
print(6 not in list)

print("## BIT ##")
a = 10
b = 3
print(f"AND: 10 & 3 = {10 & 3}")
print(f"OR: 10 | 3 = {10 | 3}")
print(f"XOR: 10 ^ 3 = {10 ^ 3}")
print(f"NOT: ~10 = {~10}")
print(f"Desplazamiento a la derecha: 10 >> 2 = {10 >> 2}")
print(f"Desplazamiento a la izquierda: 10 << 2 = {10 << 2}")

print("### Estructuras de control ###")
print("## IF ##")
edad = 18
if edad is 18:
   print("Es mayor de edad")
else:
   print("Menor de edad")

print("## FOR ##")
for num in range(13):
   print(f"5 * {num} = {5 * num}")

print("## WHILE ##")
n = -1
while n < 12:
   n += 1
   print(f"5 * {n} = {5 * n}")

print("## EXCEPCIONES ##")
try:
   print(10 / 1)
except:
   print("Se ha producido un error")
finally:
   print("Ha finalizado el manejo de excepciones")


print("### EXTRA ###")
for number in range(10, 56):
   if number % 2 == 0 and number != 16 and number % 3 != 0:
      print(number)