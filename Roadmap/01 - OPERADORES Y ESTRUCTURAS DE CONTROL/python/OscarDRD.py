#Ejemplos operadores Aritmeticos
print("************** Ejemplos operadores aritmeticos **************")
print(f"Suma: {5+5}") #Suma
print(f"Resta: {5-5}") #Resta
print(f"Multiplicación: {5*5}") #Multiplicación
print(f"División: {5/5}") #División
print(f"División entera: {5//5}") #División entera
print(f"Modulo: {5%5}") #Modulo
print(f"Exponente: {5**5}") #Exponente

#Ejemplos operadores de comparación
a = 5
b = 10
print("************** Ejemplos operadores de comparación **************")
print(f"Igualdad: {a == b}") #Igualdad
print(f"Diferencia: {a != b}") #Diferencia
print(f"Mayor que: {a > b}") #Mayor que
print(f"Menor que: {a < b}") #Menor que
print(f"Mayor o igual que: {a >= b}") #Mayor o igual que
print(f"Menor o igual que: {a <= b}") #Menor o igual que

#Ejemplos operadores lógicos
a = True
b = False
print("************** Ejemplos operadores lógicos **************")
print(f"AND: {a and b}") #AND
print(f"OR: {a or b}") #OR
print(f"NOT: {not a}") #NOT

#Ejemplos operadores de asignación
a = 2
b = 3
print("************** Ejemplos operadores de asignación **************")
print(f"Asignación: {a}") #Asignación
a += b
print(f"Suma: {a}") #Suma
a -= b
print(f"Resta: {a}") #Resta
a *= b
print(f"Multiplicación: {a}") #Multiplicación
a /= b
print(f"División: {a}") #División
a %= b
print(f"Modulo: {a}") #Modulo
a **= b
print(f"Exponente: {a}") #Exponente
a //= b
print(f"División entera: {a}") #División entera

#Ejemplos operadores de identidad
print("************** Ejemplos operadores de identidad **************")
a = 5
b = 5
print(f"Identidad: {a is b}") #Identidad
print(f"No identidad: {a is not b}")

#Ejemplos operadores de pertenencia
print("************** Ejemplos operadores de pertenencia **************")
a = [1, 2, 3, 4, 5]
b = 3
print(f"Pertenencia: {b in a}") #Pertenencia
print(f"No pertenencia: {b not in a}") #No pertenencia

#Ejemplos operadores de bits
print("************** Ejemplos operadores de bits **************")
a = 5
b = 3
print(f"AND: {a & b}") #AND
print(f"OR: {a | b}") #OR
print(f"XOR: {a ^ b}") #XOR
print(f"Desplazamiento a la izquierda: {a << b}") #Desplazamiento a la izquierda
print(f"Desplazamiento a la derecha: {a >> b}") #Desplazamiento a la derecha

'''
Ejercicio Extra:
Crea un programa que imprima por consola todos los números comprendidos
entre 10 y 55 (incluidos), pares, y que no son ni el 16 ni múltiplos de 3.
'''
print("************** Ejercicio Extra **************")
print("Números comprendidos entre 10 y 55 (incluidos):")
for i in range(10, 56):
    print(i)
print("Números pares:")
for i in range(10, 56):
    if i % 2 == 0:
        print(i)
print("Números que no son el 16 ni múltiplos de 3:")
for i in range(10, 56):
    if i != 16 and i % 3 != 0:
        print(i)


