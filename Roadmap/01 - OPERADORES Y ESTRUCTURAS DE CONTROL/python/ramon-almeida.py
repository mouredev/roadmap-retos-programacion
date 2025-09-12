
suma = 1+1
print(suma)
resta = 56-32
print(resta)
comparación = 20 < 10
print(comparación)
división = 50 / 5
print(división)
resto_división = 74 % 5
print(resto_división)


""" Crea un programa que imprima por consola todos los números comprendidos
 entre 10 y 55 (incluidos), pares, y que no son ni el 16 ni múltiplos de 3.

 """

result = []

for i in range(10, 56):
    if i % 2 == 0 and i != 16 and i % 3 != 0:
        result.append(i)


print(result)
