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

for i in range(1,11):
    print(i)

i = 1
while i <= 10:
    print(i)
    i += 1

def counter(i):
    if i <= 10:
        print(i)
        counter(i+1)
counter(1)

#DIFICULTAD EXTRA

def automatic_counter_for(count = 1):
    for count in range(1,11):
        if count <= 10:
            print(count)
            count += 1
        else:
            pass

automatic_counter_for()

def automatic_counter_while(count = 1):
    while count <= 10:
        print(count)
        count += 1

automatic_counter_while()