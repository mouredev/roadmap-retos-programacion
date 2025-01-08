# #17 ITERACIONES
#### Dificultad: Fácil | Publicación: 22/04/24 | Corrección: 29/04/24

## Ejercicio

# """ ```
# /*
#  * EJERCICIO:
#  * Utilizando tu lenguaje, emplea 3 mecanismos diferentes para imprimir
#  * números del 1 al 10 mediante iteración.
#  *
#  * DIFICULTAD EXTRA (opcional):
#  * Escribe el mayor número de mecanismos que posea tu lenguaje
#  * para iterar valores. ¿Eres capaz de utilizar 5? ¿Y 10?
#  */ """

print("For")
for i in range(1,11):
    print(i)

print("While")
i = 1
while i <= 10:
    print(i)
    i+=1

print("Recursity")
def print_counter(num):
    if num < 11:
        print(num)
        print_counter(num + 1)

print_counter(1)

print("Dificultad Extra")

for i in [1,2,3,4,6,7,8,9,10]:
    print(i)

for i in (1,2,3,4,5,6,7,8,9,10):
    print( i)

for i in {1,2,3,4,5,6,7,8,9,10}:
    print(i)

my_dict = {1:"a",2:"b",3:"c"}
for k in my_dict.keys():
    print(k)

for k,v in my_dict.items():
    print(k)