"""
Tipos de operadores
"""
# Operadores aritméticos: Para realizar operaciones matemáticas básicas
suma = 4 + 2
resta = 4 - 2
division = 4 / 2

multiplicacion = 4 * 2
modulo = 4 % 2
exponencial = 4 ** 2
division_entera = 4 // 2

print(f"Suma: 4 + 2 = {suma}")
print(f"Resta: 4 - 2 = {resta}")
print(f"Division: 4 / 2 = {division}")
print(f"Multiplicacion: 4 * 2 = {multiplicacion}")
print(f"Modulo: 4 % 2 = {modulo}")
print(f"Exponencial: 4 ** 2 = {exponencial}")
print(f"Division entera: 4 // 2 = {division_entera}")

# Operadores de comparación: Para evaluar si dos valores son iguales o no
print(f"Iguales: 4 == 2 {4 == 2}")
print(f"Diferentes: 4 != 2 {4 != 2}")
print(f"Mayor: 4 > 2 {4 > 2}")
print(f"Menor: 4 < 2 {4 < 2}")
print(f"Mayor o igual: 4 >= 2 {4 >= 2}")
print(f"Menor o igual: 4 <= 2 {4 <= 2}")

# Operadores lógicos: Para realizar operaciones booleanas
print(f"Operador AND se simboliza con &&: 5 + 1 == 6 and 2 + 10 = 12 es {
      5 + 1 == 6 and 2 + 10 == 12}")
print(f"Operador OR se simboliza con ||: 5 + 1 == 6 and 2 + 10 = 12 es {
      5 + 1 == 6 and 2 + 10 == 12}")
print(f"Operador NOT se simboliza con ! : 10 + 3 == 14 es {not 10 + 3 == 14}")

# Operadores de asignación: Para asignar valores a variables
mi_numero = 5
print(f"Asignacion = : {mi_numero}")

mi_numero = 5
mi_numero += 2
print(f"Asginacion de suma += 2 : {mi_numero}")

mi_numero = 5
mi_numero -= 2
print(f"Asignacion resta -= 2 : {mi_numero}")

mi_numero = 5
mi_numero *= 3
print(f"Asignacion multiplicacion *= 3 : {mi_numero}")

mi_numero = 5
mi_numero /= 3
print(f"Asignacion division /= 3 : {mi_numero}")

mi_numero = 5
mi_numero %= 5
print(f"Asignacion modulo %= 5 : {mi_numero}")

mi_numero = 5
mi_numero **= 3
print(f"Asignacion exponencial **= 3 : {mi_numero}")

mi_numero = 5
mi_numero //= 5
print(f"Asignacion division entera //= 5 : {mi_numero}")

# Operadores bit a bit
a = 10  # 1010
b = 3  # 0011

# 0010 = 2 al comparar si los dos bit son 1 se escribe
print(f"AND: 10 & 3 = {10 & 3}")

# 1011 = 11 al comparar si uno de los dos es 1 se escribe
print(f"OR: 10 | 3 = {10 | 3}")
print(f"XOR: 10 ^ 3 = {10 ^ 3}")  # 1001 = 9 al comparar si son diferentes 1
print(f"XOR: 10 ~ 3 = {~10}")
print(f"Desplazamiento a la derecha: 10 >> 2 = {
      10 >> 2}")
# Pasa de 1010 a 0010 = 2
print(f"Desplazamiento a la izquierda: 10 << 2 = {
      10 << 2}")
# Pasa de 1010 a 101000 = 40

# Operadores de identidad: Para verificar la identidad de los objetos
mi_variable = 5
nuestra_variable = 5

mi_variable = nuestra_variable
print(f"Operador is: {mi_variable is nuestra_variable}")
print(f"Operador is not: {mi_variable is not nuestra_variable}")


# Operadores de pertenencia: Para verificar si un elemento está en una lista
lista1 = [1, 2, 3, 4]
print(f"Operador de pertenencia in: Esta el numero 5 en la lista? {
      5 in lista1}")
print(f"Operador de pertenencia not in: El numero 5 no esta en la lista {
      5 not in lista1}")


"""
Crea ejemplos que representen todos los 
tipos de estructuras de control
"""

# ESTRUCTURAS DE CONTROL CONDICIONALES: if, elif, else
numero = 5

if numero > 0:
    print(f"El numero {numero} es positivo")
elif numero == 0:
    print(f"El numero {numero} es 0")
else:
    print(f"El numero {numero} es negativo")

# ESTRUCTURAS DE CONTROL ITERATIVAS (bucle): for y while

# for
frutas = ["sandia", "piña", "melocoton"]
for fruta in frutas:
    print(fruta)

numeros = [1, 2, 3, 4, 5]
for numero in numeros:
    print(numero)

# ¿Quieres sumar un valor a cada número? Podemos hacerlo con variables de asignación
numeros = [1, 2, 3, 4, 5]
for numero in numeros:
    numero += 10
    print(numero)

# Utilizando for con range
for i in range(5):
    print(i)

# while
edad = int(input("Ingresa tu edad: "))
while edad < 18:
    print("Eres menor de edad")
    edad = int(input("Ingresa tu edad: "))

print("Eres mayor de edad")

# ESTRUCTURAS DE CONTROL DE SALTO: break, continue, pass

# break
for i in range(10):  # 0, 1, 2, 3, 4, 5, 6, 7, 8, 9
    if i == 5:  # 0, 1, 2, 3, 4
        break
    print(i * 2)  # 0, 2, 4, 6, 8

# continue
for i in range(10):  # 0, 1, 2, 3, 4, 5, 6, 7, 8, 9
    if i % 2 == 0:  # Si el numero es par
        continue   # No lo imprimas. Imprime: 1, 3, 5, 7, 9
    print(i ** 3)  # Elevando al cubo los números impares

# pass
for i in range(10):
    if i % 2 == 0:
        pass
    print(i)

# ESTRUCTURAS DE CONTROL COMPUESTAS

# Bucle con condicional
for i in range(5, 10):
    if i % 2 == 0:
        continue  # Solo impares
    print(i)

# Bucle anidado????

# Bucle con break
for i in range(10):
    if i == 8:
        break
    print(i)

# ESTRUCTURA DE CONTROL DE EXCEPCIONES
try:
    print(10/0)
except:
    print("Ha habido un error")
finally:
    print("Ha finalizado el manejo de excepciones")

'''
Crea un programa que imprima por consola todos los números comprendidos
 entre 10 y 55 (incluidos), pares, y que no son ni el 16 ni múltiplos de 3
'''
for i in range(10, 56):
    if i % 2 == 0 and i != 16 and i % 3 != 0:
        print(i)
