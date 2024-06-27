""" /*
 * EJERCICIO:
 * Utilizando tu lenguaje, emplea 3 mecanismos diferentes para imprimir
 * números del 1 al 10 mediante iteración.
 *
 * DIFICULTAD EXTRA (opcional):
 * Escribe el mayor número de mecanismos que posea tu lenguaje
 * para iterar valores. ¿Eres capaz de utilizar 5? ¿Y 10?
 */ """

#EJERCICIO
for i in range(1, 11): #1
    print(i)

i = 1 
while i<=10: #2
    print(i)
    i += 1

lista_numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] #3
for i in lista_numeros:
    print(i)

#DIFICULTAD EXTRA
def iterar(numero):
    if numero <= 10:
        print(numero)
        iterar(numero+1) #4

iterar(1)

for num in enumerate(lista_numeros): #5
    print(num)

zip_numeros = zip(lista_numeros) #6
for num in zip_numeros:
    print(num)

dict_numeros = {"n1":1, "n2":2, "n3":3, "n4":4, "n5":5, "n6":6, "n7":7, "n8":8, "n9":9, "n10":10}
for n, numero in dict_numeros.items(): #7
    print(n, numero)

def generador(n):
    contador = 1
    while contador <= n:
        yield contador #8
        contador += 1

for numero in generador(10):
    print(numero)

mi_iterador = iter(lista_numeros) #9
print(next(mi_iterador))
print(next(mi_iterador))
print(next(mi_iterador))
print(next(mi_iterador))
print(next(mi_iterador))
print(next(mi_iterador))
print(next(mi_iterador))
print(next(mi_iterador))
print(next(mi_iterador))
print(next(mi_iterador))

print([num for num in lista_numeros]) #10

lista_numeros15= [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

def menores(n):
    return n <= 10

lista_numeros15_filtrada = filter(menores, lista_numeros15) #11
print(list(lista_numeros15_filtrada))

suma_lista = map(lambda n: n + 0, lista_numeros) #12
print(list(suma_lista))

