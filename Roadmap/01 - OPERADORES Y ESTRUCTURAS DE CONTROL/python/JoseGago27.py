#Operadores

# Operadores Aritmeticos

print(f"Suma: 2 + 2 = {2 + 2}")
print(f"Resta: 4 - 2 = {4 - 2}")
print(f"Multiplicacion: 2 x 3 = {2 * 3}")
print(f"Division: 4 / 2 = {4 / 2}")
print(f"Media: 4 % 2 = {4 % 2}")
print(f"Exponencial: 2 ** 2 = {2 ** 2}")
print(f"Division entera: 4 // 2 = {4 // 2}")

# Operadores de comparacion

print(f"Igualdad: 10 == 3 es {10 == 3}")
print(f"Diferente: 10 != 3 es {10 != 3}")
print(f"Mayor que: 20 > 15 es {20 > 15}")
print(f"Menor que: 30 < 40 es {30 < 40}")
print(f"Mayor o igual que: 50 >= 50 es {50>=50}")
print(f"Menor o igual que: 80 <= 30 es {80 <= 30}")

#Operadores logicos

print(f"AND : 2 + 2 == 4 and 3 + 2 == 5 {2 + 2 == 4 and 3 + 2 == 5}")
print(f"OR : 2 + 2 == 100 or 3 + 2 == 5 {2 + 2 == 100 or 3 + 2 == 5}")
print(f"NOT : not 2 + 2 == 100  {not 2 + 2 == 100}")

#Operadores de asignacion

num1 = 10 #Asignacion
print(num1)
num1 += 1 #Suma y asignacion
print(num1)
num1 -= 2 #Resta y asignacion
print(num1)
num1 *= 2 #Multiplicacion y asignacion
print(num1)
num1 /= 2 #Division y asignacion
print(num1)

#Operadores de identidad

my_number = num1
print(f"my_number is num1 es {my_number is num1}")
print(f"my_number is not num1 es {my_number is not num1}")

#Operadores de pertenencia

print(f"Esta la 'R' en 'Ramon'?, la respuesta es {'R' in 'Ramon'}")
print(f"No esta la 'R' en 'Ramon', la respuesta es {'R' not in 'Ramon'}")

#Operadores de bit
a = 10
b = 3

print(f"AND: 10 & 3 = {10 & 3}")
print(f"OR: 10 | 3 = {10 | 3}")
print(f"XOR: 10 ^ 3 = {10 ^ 3}")
print(f"NOT: ~10 = {~10}")
print(f"Desplazamiento a la derecha: 10 >> 2 = {10 >> 2}")
print(f"Desplazamiento a la izquierda: 10 << 2 = {10 << 2}")

#Estructuras de control

#Condicionales

string1 = "otra prueba"

if string1 == "prueba de condicion":
    print("Si es igual")
elif string1 == "otra prueba":
    print("no lo es")
else:
    print("No es igual")

#Iterativas

for i in range(11):
    print(i)

i = 0

while i <= 10:
    print(i)
    i += 1

#Manejo de excepciones

try:
    print(10/0)
except:
    print("Se ha producido un error")
finally:
    print("Ha finalizado el manejo de excepciones")

#Extra

for number in range(10, 56):
    if number % 2 == 0 and number != 16 and number % 3 ==0:
        print(number)