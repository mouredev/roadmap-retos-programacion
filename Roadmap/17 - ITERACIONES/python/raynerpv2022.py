# /*
#  * EJERCICIO:
#  * Utilizando tu lenguaje, emplea 3 mecanismos diferentes para imprimir
#  * números del 1 al 10 mediante iteración.
#  *
#  * DIFICULTAD EXTRA (opcional):
#  * Escribe el mayor número de mecanismos que posea tu lenguaje
#  * para iterar valores. ¿Eres capaz de utilizar 5? ¿Y 10?
#  */

for i in range(1,11):
    print(i)

i=1

while i <=10:
    print(i)
    i+=1

numeros = [x  for x in range(1,11)]
print(numeros)

def print_number(n):
    print(n)
    if n == 10:
        return n
    return print_number(n+1)

print_number(1)


# EXTRA

# Lista de países
paises = ['España', 'Francia', 'Alemania', 'Italia', 'Japón', 'México', 'Brasil', 'Argentina', 'Canadá', 'Australia']

# Lista de capitales
capitales = ['Madrid', 'París', 'Berlín', 'Roma', 'Tokio', 'Ciudad de México', 'Brasilia', 'Buenos Aires', 'Ottawa', 'Canberra']

for i,v in zip(paises, capitales):
    print(f" Pais: {i} Capital: {v}")

mapa_mundi = {i:v  for i,v in zip(paises, capitales)}
for i,v in mapa_mundi.items():
    print(f" Pais: {i} Capital: {v}")