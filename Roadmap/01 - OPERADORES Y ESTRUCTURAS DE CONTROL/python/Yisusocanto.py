#ejemplos de operadores de python

#aritmeticos
suma = 5 + 5
resta = 5 - 3
mulltiplicacion = 4 * 4
division = 6 / 5
division_int = 8 // 2
modulo = 7 % 2
exponente = 4 ** 4

print(suma)
print(resta)
print(mulltiplicacion)
print(division)
print(division_int)
print(modulo)
print(exponente)

#relacionales
print(5 >2 ) #mayor a
print(5 < 8) #menor a
print(5 == 5) #igual a
print(5 >= 3) #igual o mayor a 
print(5 <= 9) #igual o menor a
print(5 != 5) #no igual a 

#logicos
num1 = 5
num2 = 5
num3 = 5
num4 = 8
num = 1

if num1 and num2 == num3:
	print("True")

if num1 or num4 == num3:
	print("True")

if not num1 == num4:
	print("True")

#de asignacion
var1 = 5 #igual

var1 += 1 #se le suma al valor actual
print(var1)

var1 -= 2 #se le resta al valor actual
print(var1)

var1 *= 2 #se multiplica al valor actual
print(var1)

var1 /= 3  #se divide al valor actual
print(var1)

var1 **= 3 #se le eleva al valor actual
print(var1)

var1 //= 2 #se divide al valor actual y retorna un entero
print(var1)

var1 %= 2 #se modula al valor actual
print(var1)

#de identidad
number = 100
my_new_number = number

print(f"number es my_new_number: {number is my_new_number}")
print(f"number no es my_new_number: {number is not my_new_number}")

#operadores de pertenencia
print(f"'a' esta en 'arbol': {'a' in 'arbol'}")
print(f"'a' no esta en 'arbol': {'a' not in 'arbol'}")

## Operadores de bit
a = 10  # 1010
b = 3  # 0011
print(f"AND: 10 & 3 = {10 & 3}")  # 0010
print(f"OR: 10 | 3 = {10 | 3}")  # 1011
print(f"XOR: 10 ^ 3 = {10 ^ 3}")  # 1001
print(f"NOT: ~10 = {~10}")
print(f"Desplazamiento a la derecha: 10 >> 2 = {10 >> 2}")  # 0010
print(f"Desplazamiento a la izquierda: 10 << 2 = {10 << 2}")  # 101000

#estructuras de control

#iterables
for letras in "iteracion":
	print(letras)

var_iter = 7

while var_iter >= 4:
	print(var_iter)
	var_iter -= 2

#condicionales
var_if = 6

if var_if < 0:
	print("la variable es negativa")
elif var_if < 10:
	print("la variable es positiva")
else:
	print("la variable es igual o mayor a diez")

#excepcones
try:
	6 / 0
except ZeroDivisionError as e:
	print("Division por cero")
else:
	print("error desconocido")
finally:
	print("FIN")

#ejercicio extra

for numero in range(10, 56):
	if numero % 2 == 0 and numero != 16 and numero % 3 != 0:
		print(numero)
