#17 - ITERACIONES

"""
/*
 * EJERCICIO:
 * Utilizando tu lenguaje, emplea 3 mecanismos diferentes para imprimir
 * números del 1 al 10 mediante iteración.
 *
 * DIFICULTAD EXTRA (opcional):
 * Escribe el mayor número de mecanismos que posea tu lenguaje
 * para iterar valores. ¿Eres capaz de utilizar 5? ¿Y 10?
 */
"""

#forma uno
for i in range(1 , 11):
    print(i)

#forma dos
i = 1
while i < 11 :
    print(i)
    i+=1

#forma tres
def uno_al_10(num = 0):
    if num <= 10 :
        return uno_al_10(num+1)

print(uno_al_10())

#5 formas de iterar

for i in [1 , 2 ,3 ,4 ,5]:
    print(i)

print([i for i in [1 , 2 ,3 , 4 , 5]])

i = 1
if i <=5:
    print(i)
    i+=1

print(*[i for i in range(1,6)] , sep="\n")

iterador = lambda x : print(x)
for i in range(1, 5):
    iterador(i)
