# EJERCICIO:
#  * Utilizando tu lenguaje, emplea 3 mecanismos diferentes para imprimir
#  * números del 1 al 10 mediante iteración.

print("Con for")
for i in range (1,11):
    print(i)

print("con while")
c = 1
while c <= 10:
    print(c)
    c += 1


print("con recursivilidad")
def my_iteration(a):
    i = 0
    if i == a:
        return i
    else:
        return i
        i += 1
my_iteration(10)


#  DIFICULTAD EXTRA (opcional):
#  * Escribe el mayor número de mecanismos que posea tu lenguaje
#  * para iterar valores. ¿Eres capaz de utilizar 5? ¿Y 10?

print("Con for")
for i in range (1,11):
    print(i)

print("con while")
c = 1
while c <= 10:
    print(c)
    c += 1


print("con recursivilidad")
def my_iteration(a):
    i = 0
    if i == a:
        return i
    else:
        return i
        i += 1
my_iteration(10)

print("Con lista y for")
my_list  = [1,2,3,4,5,6,7,8,9,10]
for n in my_list :
    print(n)

print("Con tupla y for")
my_tuple = (1,2,3,4,5,6,7,8,9,10)
for k in my_tuple:
    print(k)

print("Con enumarate()")
enum = [".-"] *10
for a,_ in enumerate(enum,start = 1):
    print(a)

print("Con yield")
def yieeld():
    for i in range(1,11) :
        yield i
for numero in yieeld():
    print(numero)


print("Con for,iter y next")
it = iter(range(1,11))

while True:
    try:
        print(next(it))
    except StopIteration:
        break