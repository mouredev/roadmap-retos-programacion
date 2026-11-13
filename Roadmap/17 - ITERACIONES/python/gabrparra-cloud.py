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

for i in range(1,11):
    print(f"bucle for {i}")

i = 1
while i <=10:
    print(f"bucle while {i}")
    i += 1

def cuenta_acendente( i=1):
    if i <= 10:
        print(f"Función recursiva {i}")
        cuenta_acendente(i+1)

cuenta_acendente()

for i in [1,2,3,4]:
    print(i)

for i in {1,2,3,4}:
    print(i)

for i in (1,2,3,4):
    print(i)

for i in {1:"a",2:"b",3:"c",4:"d"}:
    print(i)

print(*[i for i in range(1,11)])

for i in "cadena de texto":
    print(i)

for i in reversed("cadena de texto"):
    print(i)

for e,i in enumerate(sorted("cadena de texto")):
    print(f"Índice: {e}, valor: {i}")

