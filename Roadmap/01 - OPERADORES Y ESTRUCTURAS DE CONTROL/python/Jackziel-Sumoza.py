
#** Operadores

num_1 = 24
num_2 = 54
num_3 = 2.45

#* Aritméticos
print()
print("OPERADORES ARITMÉTICOS")
print(f"Esto es una suma {num_1} + {num_2}: {num_1 + num_2}")
print(f"Esto es una resta {num_1} - {num_2}: {num_1 - num_2}")
print(f"Esto es una división {num_1} / {num_2}: {num_1 / num_3}")
print(f"Esto es una división entera {num_1} // {num_2}: {num_1 // num_3}")
print(f"Esto es una multiplicación {num_1} * {num_2}: {num_1 * num_2}")
print(f"Esto es modulo o resto {num_1} % {num_2}: {num_1 % num_3}")
print(f"Esto es una potencia {num_1} ** {num_2}: {num_1 ** num_3}")

#* Lógicos
print()
print("OPERADORES LÓGICOS")
print(f"{num_1} es igual a {num_2} y {num_2} es igual a {num_3}: {num_1 == num_2 and num_2 == num_3}")
print(f"{num_1} es menor {num_2} o {num_2} es igual a {num_3}: {num_1 < num_2 or num_2 == num_3}")
print(f"{num_1} no es igual a {num_2}: {not num_1 ==  num_2}")

#* Comparación
print()
print("OPERADORES DE COMPARACIÓN")
print(f"Igual que {num_1} == {num_2}: {num_1 == num_2}")
print(f"Distinto de {num_1} != {num_2}: {num_1 != num_2}")
print(f"Mayor que {num_1} > {num_2}: {num_1 > num_2}")
print(f"Menor que {num_1} < {num_2}: {num_1 < num_2}")
print(f"Mayor o igual que {num_1} >= {num_2}: {num_1 >= num_2}")
print(f"Menor o igual que {num_1} <= {num_2}: {num_1 <= num_2}")

#* Asignación
print()
print("OPERADORES DE ASIGNACIÓN")
num_1 = 25
print(f"asignar un valor 25: {num_1}")
num_1 += 2
print(f"sumar dos: {num_1}")
num_1 -= 2
print(f"restar dos: {num_1}")
num_1 *= 4
print(f"multiplicar por cuatro: {num_1}")
num_1 /= 1
print(f"dividir entre uno: {num_1}")
num_1 //= 2
print(f"división entera entre dos: {num_1}")
num_1 %= 3
print(f"Modulo de tres: {num_1}")
num_1 **= 3
print(f"elevación al cubo: {num_1}")

#* Identidad
print()
print("OPERADORES DE IDENTIDAD")
objeto_1 = [1,2,3]
objeto_2 = objeto_1
objeto_3 = [1,2,3]
print(f"objeto_2 se refiere al mismo objeto que objeto_1: {objeto_1 is objeto_2}")
print(f"objeto_3 no se refiere al mismo objeto que objeto_1: {objeto_3 is not objeto_1}")

#* Pertenencia
print()
print("OPERADORES DE PERTENENCIA")
lista_1 = [1,2,3,4,5,6,7,8,9,10]
print(f"El numero 7 se encuentra en la lista_1: {10 in lista_1}")
print(f"La palabra \"Python\" no se encuentra en la lista_1: {"Python" not in lista_1}")

#* Bits
print()
print("OPERADORES DE BITS")
binario_1, binario_2 = 20, 43 
# Si ambos bits correspondientes son 1, el resultado es 1; de lo contrario, es 0.
print(f"Operador binario and: {bin(binario_1)} AND[&] {bin(binario_2)}: {bin(binario_1 & binario_2)}")
# Si al menos uno de los bits correspondientes es 1, el resultado es 1; de lo contrario, es 0.
print(f"Operador binario or: {bin(binario_1)} OR[|] {bin(binario_2)}: {bin(binario_1 | binario_2)}")
# Si los bits correspondientes son diferentes, el resultado es 1; de lo contrario, es 0.
print(f"Operador binario xor: {bin(binario_1)} XOR[^] {bin(binario_2)}: {bin(binario_1 ^ binario_2)}")
# Invierte todos los bits de un número.
print(f"Operador binario not: {bin(binario_1)} NOT[~]: {bin(~ binario_2)}")
# Desplaza todos los bits de un número una cierta cantidad de posiciones hacia la izquierda, llenando los espacios vacíos con ceros.
print(f"Desplazar a la derecha: 2 posiciones a {bin(binario_2)} [>>]: {bin(binario_1 >> 2)}")
#  Desplaza todos los bits de un número una cierta cantidad de posiciones hacia la derecha. El comportamiento del bit más a la izquierda depende del tipo de entero (con o sin signo).
print(f"Desplazar a la izquierda: 2 posiciones a {bin(binario_1)} [<<]: {bin(binario_1 << 2)}")

#** Condicionales

num_1 = 40
num_2 = 50
num_3 = num_1

print()
print("CONDICIONALES")
if num_1 == num_3:
    print(f"El numero {num_1} es igual a {num_3}")
elif num_1 != num_2 and num_2 != num_3:
    print(f"el {num_1} es distinto de {num_2} y {num_2} es distinto de {num_3}")
else:
    print("ninguna de las afirmaciones anteriores son reales")

#** Bucles

#* For
print()
print("BUCLE FOR")
nombre = "Jackziel"
letras = list()
for letra in nombre:
    letras.append(letra)
print(letras)

#* While
print()
print("BUCLE WHILE")
x = 0
numeros_naturales = list()
while x - 10:
    numeros_naturales.append(x)
    x += 1
print(numeros_naturales)

#** Excepciones

print()
print("EXCEPCIONES")
try:
    print(f"{"hola mundo" + 15.6}")
except:
    print("No puedes sumar dos tipos de datos diferentes, corrígelo y vuelve a intentar")
finally:
    print("el programa a finalizado")

#** Ejercicio complejo

print()
print("DIFICULTAD EXTRA")
for numero in range(10, 56):
    if numero % 2 == 0 and numero != 16 and numero % 3 != 0:
        print(numero)