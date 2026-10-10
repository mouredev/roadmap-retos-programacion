'''
 EJERCICIO:
* Utilizando tu lenguaje, emplea 3 mecanismos diferentes para imprimir
* números del 1 al 10 mediante iteración.
'''
print ("-"*60)    


for i in range(1, 11):
    print(i)

print ("-"*60)    

i = 1
while i <= 10:
    print(i)
    i += 1

print ("-"*60)    


def count_ten(i=1):
    if i <= 10:
        print(i)
        count_ten(i+1)

count_ten()    

print ("="*60)   


'''
* DIFICULTAD EXTRA (opcional):
* Escribe el mayor número de mecanismos que posea tu lenguaje
* para iterar valores. ¿Eres capaz de utilizar 5? ¿Y 10?
'''

for i in [1, 2, 3, 4]:
    print(i)


print ("-"*60)    

for i in (1, 2, 3, 4):
    print(i)

print ("-"*60)    


for i in {1 ,2, 3 ,4}:
    print(i)


print ("-"*60)    

for i in {1:"a", 2:"b", 3:"c", 4:"d"}:
    print(i)

print ("-"*60)            

for i in {1:"a", 2:"b", 3:"c", 4:"d"}.values():
    print(i)

print ("-"*60)            

for i in {1:"a", 2:"b", 3:"c", 4:"d"}.keys():
    print(i)

print ("-"*60)            

print(*[i for i in range(1,5)],sep="-")

print ("-"*60)            

print(*[c for c in "Ricardo"],sep=",")

print ("-"*60)

for c in sorted(("Ricardo").upper()): 
    print(c)

print ("-"*60)

for c in reversed("Ricardo"):
    print(c)

print ("-"*60)

for i, e in enumerate(["R", "i", "c", "a", "r", "d", "o"]):
    print(f"Índice: {i}, valor: {e}")

print ("-"*60)


   