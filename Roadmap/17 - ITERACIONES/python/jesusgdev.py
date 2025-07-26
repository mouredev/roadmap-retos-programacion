'''
EJERCICIO:
 * Utilizando tu lenguaje, emplea 3 mecanismos diferentes para imprimir
   números del 1 al 10 mediante iteración.
  
 * DIFICULTAD EXTRA (opcional):
 * Escribe el mayor número de mecanismos que posea tu lenguaje
   para iterar valores. ¿Eres capaz de utilizar 5? ¿Y 10?
'''

# 1. Iterando con un ciclo for
for num in range(1,11):
    print(num)

# 2. Iterando usando un comprehension list
[print(num) for num in range(1, 11)]

# 3. Iterando una lista ya creada
numbers = [1,2,3,4,5,6,7,8,9,10]
for num in numbers:
    print(num)

# 4. Iterando usando recursion
def count(num):
    if num <= 10:
        print(num)
        count(num + 1)
count(1)

# 5. Iterando usando map() con range ()
list(map(print, range(1,11)))

# 6. Iterando usando enumerate() con lista
for index, value in enumerate(range(1,11)):
    print(value)

# 7. Iterando usando iter() y next() manualmente
it = iter

# 8. Iterando dentro de un while loop
num = 1
while True:
    if num <= 10:
        print(num)
        num += 1

