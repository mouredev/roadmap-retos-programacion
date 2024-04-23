'''EJERCICIO:
 * Utilizando tu lenguaje, emplea 3 mecanismos diferentes para imprimir
 * números del 1 al 10 mediante iteración.
 *
 * DIFICULTAD EXTRA (opcional):
 * Escribe el mayor número de mecanismos que posea tu lenguaje
 * para iterar valores. ¿Eres capaz de utilizar 5? ¿Y 10?
 */'''

for i in range(1,11):
  print(i)
#___________________________
print()
n=1
while n<11:
  print(n)
  n+=1
#___________________________
print()
def secuencia(n):
  if n==10:
    print(10)
  else:
    print(n)
    secuencia(n+1)
secuencia(1)

#___________________________
print()
print(*[i+1 for i in range(10) if i <11])