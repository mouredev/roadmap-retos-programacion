# Crea ejemplos utilizando todos los tipos de operadores de tu lenguaje:

#Operadores Aritmeticos

print(3 + 4)
print(7 - 3)
print(3 * 4)
print(12 / 3)

#Operador Modulo

print(10%2)
print(10%3)

#Floor división
print(10 // 3)
#Esta división aproxima el resultado a un número entero

#Calcular exponente
print(2 ** 3)

#Operadores Comparativos

print(3 > 4)
print(3 < 4)
print(3 >= 4)
print(3 <= 4)
print(3 == 4)
print(3 != 4)

#Operadores lógicos

print(3 > 4 and 5 > 3)
print(3 > 4 or 5 > 3)
print(not(3>4)) #not niega toda la condición y la invierte

# DIFICULTAD EXTRA (opcional):
#* Crea un programa que imprima por consola todos los números comprendidos
#* entre 10 y 55 (incluidos), pares, y que no son ni el 16 ni múltiplos de 3.

def my_range():
    for i in range(10,56):
        if i % 2 == 0 and i !=16 and i % 3 != 0:
            print(i)

my_range()