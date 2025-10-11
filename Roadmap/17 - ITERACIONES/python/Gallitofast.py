# * EJERCICIO:
#  * Utilizando tu lenguaje, emplea 3 mecanismos diferentes para imprimir
#  * números del 1 al 10 mediante iteración.
#----------------------------------------------------------------------------
print("-"*60)
print("Ciclo for")
for i in range (10):
    print(i+1)
print("-"*60)
print("While")
a=0
while a<10:
    print(a+1)
    a+=1
print("-"*60)
print("For con lista")
lista=[1,2,3,4,5,6,7,8,9,10]
for item in lista:
    print(item)

# * DIFICULTAD EXTRA (opcional):
#  * Escribe el mayor número de mecanismos que posea tu lenguaje
#  * para iterar valores. ¿Eres capaz de utilizar 5? ¿Y 10?
print("-"*60)
print("1.-For")
for i in range(5):
    print("i+1")
print("-"*60)
print("2.-While")
a=0
while a<5:
    print("a+1")
    a+=1
print("-"*60)
print("3.-Iteracion de lista con for")
for item in lista:
    print(item)
print("-"*60)
print("4.-Recursividad")
def recursifuncion(numero):
    print(numero)
    if numero>0:
        numero-=1
        recursifuncion(numero)
    else:
        print("Iteracion recursiva finalizada")

recursifuncion(10)
print("-"*60)

for e in sorted(["G","a","l","l","o"]):
    print(e)

for i, e in enumerate(sorted(["G","a","l","l","o"])):
    print(f"Índice: {i}, valor: {e}")


