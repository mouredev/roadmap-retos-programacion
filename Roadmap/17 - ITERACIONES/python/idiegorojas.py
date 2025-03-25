# Iteraciones

"""
Es el proceso de repetir una serie de instrucciones o pasos varias veces
En python se suele manejar con los bucles 'for' y 'while'.
"""

# Bucle for
"""
Se usa cuando cuando se sabe cuantas veces que quiere repetir algo.
Cundo se quiere recorrer una secuencia (lista, tupla, cadena o rango)
"""

"""
for variable in secuencia:
    pass # codigo a ejecutar en cada secuencia
"""

# Imprimir los numeros del 1 al 5
for i in range(1, 6):
    print(i)


print('-----------------')



# i toma el valor de la secuncia generada por range() y el bucle itera 5 veces

frutas = ['Manzana', 'Uva', 'Pera']
for fruta in frutas:
    print(f'Me gusta la {fruta}')


print('-----------------')



# Bucle while
"""
Se usa cuando no se sabe exactamente cuantas veces se necesita iterar.
Tiene una condicion que determina cuando debe parar.
"""

"""
while condicion:
    pass # Codigo que se ejecuta mientras la condicion es verdadera
"""

# Contar del 1 al 5
contador = 0
while contador <= 5:
    print(contador)
    contador += 1 # Incrementa el contador en 1
# Si no se incrementa el contador el bucle sera infinito



print('-----------------')



# Iterables e iteradores
"""
Iterable:
    Es cualquier objeto que se puede recorrer elemento por elemento
    Listas, cadenas, diccionarios.

Iteradores:
    Son objetos que implementan los metodos 'iter()' y 'next()' para controlar como se recorre el iterable
"""

# Iterar hasta el numero 3
lista = [1, 2, 3, 4, 5]
iterador = iter(lista)
print(next(iterador))
print(next(iterador))
print(next(iterador))


print('-----------------')



# Comprensiones 
"""
Es una forma mas elegante y concisa de iterar
"""

cuadrados = [x**2 for x in range(1, 5)]
print(cuadrados)



print('-----------------')



# Break y continue
"""
Break: Termina el bucle antes de tiempo
Continue: Salta a la sigueinte iteracion sin ejecutar el coidgo en esa vuelta.
"""

for i in range(1, 6):
    if i == 3:
        continue # Salta el 3
    if i == 5:
        break # Termina en 5
    print(i)


print('-----------------')


# Ejercicio
for i in range(1, 11):
    print(i)


print('-----------------')

contador = 1
while contador <= 10:
    print(contador)
    contador += 1


print('-----------------')

contador = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
iterador = iter(contador)
print(next(iterador))
print(next(iterador))
print(next(iterador))
print(next(iterador))
print(next(iterador))
print(next(iterador))
print(next(iterador))
print(next(iterador))
print(next(iterador))
print(next(iterador))


print('-----------------')


def contar_hasta_diez(i=1):
    if i <= 10:
        print(i)
        contar_hasta_diez(i+1)

contar_hasta_diez()

print('-----------------')



# Extra

# iterar una lista
for i in [1,2,3,4,5]:
    print(i)


print('-----------------')

# Iterar un tupla
for i in (1,2,3,4,5):
    print(i)


print('-----------------')


# Iterar un diccionario
for i in {1,2,3,4,5}:
    print(i)

print('-----------------') 


# Iterar un diccionario por Clave
for i in {'a': 1, 'b': 2, 'c':3, 'd': 4, 'e':5}:
    print(i)

print('-----------------')

# Iterar un diccionario por Valor
for i in {'a': 1, 'b': 2, 'c':3, 'd': 4, 'e':5}.values():
    print(i)

print('-----------------')

for i in 'Python':
    print(i)

print('-----------------')

for i in reversed('Python'):
    print(i)

print('-----------------')

for i in sorted('python'):
    print(i)

print('-----------------')

for i, e in enumerate(sorted(["p", "y", "t", "h", "o", "n"])):
    print(f"Índice: {i}, valor: {e}")