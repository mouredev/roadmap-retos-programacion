


"""
/*
 * EJERCICIO:
 * Utilizando tu lenguaje, emplea 3 mecanismos diferentes para imprimir
 * números del 1 al 10 mediante iteración.
 *
"""
# Opción 1: for

for i in range(1, 11):
    print(i)

j = 1
while j < 11: 
    print(j)
    j +=1

def ten_numbers(num):
    if num < 11:
        print(num)
        return ten_numbers(num+1)

ten_numbers(1)

"""
 * DIFICULTAD EXTRA (opcional):
 * Escribe el mayor número de mecanismos que posea tu lenguaje
 * para iterar valores. ¿Eres capaz de utilizar 5? ¿Y 10?
 */
"""
lista_num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(lista_num[::1])