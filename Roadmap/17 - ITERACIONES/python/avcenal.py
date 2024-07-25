"""
* EJERCICIO:
 * Utilizando tu lenguaje, emplea 3 mecanismos diferentes para imprimir
 * números del 1 al 10 mediante iteración.
"""
print("bucle WHILE")
i = 0
while i < 10:
    i +=1
    print(i)

print("bucle FOR")
for i in range (0,11):
    print(i)

print("RECURSIVIDAD")
def to_ten(number):
    if number == 10:
        print(number)
    else:
        print(number)
        to_ten(number+1)

to_ten(0)

"""
DIFICULTAD EXTRA (opcional):
 * Escribe el mayor número de mecanismos que posea tu lenguaje
 * para iterar valores. ¿Eres capaz de utilizar 5? ¿Y 10?
"""

for k,v in {1:"a",2:"b",3:"c"}.items():
    print(f"Clave: {k}, Valor: {v}")

for element in [1,2,3,4,5,6,7,8,9,10]:
    print(element)

for element in {1,2,3,4,5}:
    print (element)
