print()
print()
print()

print("---- Operadores Aritmeticos ----")
print()

num1 = 4
num2 = 4
num3 = 3



suma = num1 + num2
resta = num1 - num2
multiplicacion = num1 * num2
division = num1 / num2
division_entera = num1 // num2
modulo_par = num1 % num2
modulo_impar = num1 % num3
potencia = num1 ** num2

print(f"Suma: {suma}")
print(f"Resta: {resta}")
print(f"Multiplicacion: {multiplicacion}")
print(f"Division: {division}")
print(f"Division Entera: {division_entera}")
print(f"Modulo Par: {modulo_par}")
print(f"Modulo Impar: {modulo_impar}")
print(f"Potencia: {potencia}")

print()
print()
print()



print("---- Operadores de Comparacion ----")
print()

a = 4
b = 4

if a == b:
    print("a y b son iguales")
if a != b:
    print("a y b no son iguales")
if a > b:
    print("a es mayor que b")
if a < b:
    print("a es menor que b")
if a >= b:
    print("a es mayor o igual que b")
if a <= b:
    print("a es menor o igual que b")


print()
print()
print()



print("---- Operadores Logicos ----")
print()


edad = 25
tiene_licencia = False
tiene_carro = True
sabe_conducir = True

if edad >= 18 and tiene_licencia == True:
    print("Autorizado para conducir")
if tiene_carro and tiene_licencia:
    print("Autorizado para conducir independiente si tiene carro o no")
if not tiene_licencia:
    print("No autorizado para conducir")
if tiene_licencia or sabe_conducir:
    print("Sabe conducir pero no está autorizado por falta de licencia")


print()
print()
print()


print("---- Operadores de Asignacion ----")
print()

num1 = 5
num2 = 7

num1 += 1
print(f"Suma: {num1}")
num1 -= num2
print(f"Resta: {num1}")
num1 *= num2
print(f"Multiplicación: {num1}")
num1 /= num2
print(f"División: {num1}")
num1 //= num2
print(f"División Entera: {num1}")
num1 %= num2
print(f"Módulo: {num1}")
num1 **= num2
print(f"Potencia: {num1}")


print()
print()
print()


print("---- Operadores de Identidad y Pertenencia----")
print()

nombre = "David"

if nombre is "Pepe":
    print("El nombre es Pepe")

if nombre is not "Pepe":
    print("El nombre no es Pepe")

print()
print()

lista = [1, 2, 3, 4, 5]

if 1 in lista:
    print("El numero 1 si está en la lista")
else:
    print("El numero 1 no está en la lista")

if 7 not in lista:
    print("El numero 7 no está en la lista")
else:
    print("El numero 7 si está en la lista")


print()
print()
print()







print("---- DESAFIO DE PROGRAMA ----")
print()



# Crea un programa que imprima por consola todos los números comprendidos
# entre 10 y 55 (incluidos), pares, y que no son ni el 16 ni múltiplos de 3.




print("Mi forma de hacerlo, pero no tan eficiente, porque tiene un for que sobra y una lista innecesaria:") 
print()

lista = []
num = 1

for i in range(0, 100):
    lista.append(num)
    num += 1

for i in lista:
    if (i >= 10) and (i <= 55) and (i % 2 == 0) and (i is not 16) and (i % 3 != 0):
        print(i)


print()
print()
print()


print("Forma más eficiente y en menos lineas de codigo:")
print()

for i in range(10, 56):
    if (i % 2 == 0) and (i is not 16) and (i % 3 != 0):
        print(i)