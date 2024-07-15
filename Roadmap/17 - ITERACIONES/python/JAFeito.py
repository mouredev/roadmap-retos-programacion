"""
 * EJERCICIO:
 * Utilizando tu lenguaje, emplea 3 mecanismos diferentes para imprimir
 * números del 1 al 10 mediante iteración.
 *
 * DIFICULTAD EXTRA (opcional):
 * Escribe el mayor número de mecanismos que posea tu lenguaje
 * para iterar valores. ¿Eres capaz de utilizar 5? ¿Y 10?
 """
 
#bucle for 
for i in range(1,11):
    print(i)
#bucle while     
i=1
while i <=10:
    print(i) 
    i+=1  
#funciion recursiva
def imp_num(n: int):
    if n <=10:
        print(n)
        n+=1
        imp_num(n)

imp_num(1)

print(*[i for i in range (1,11)],sep = "\n")

for i in [1,2,3,4,5]:
    print(i)
    
for i in (1,2,3,4,5):
    print(i)
    
for i in{1:"a",2:"b",3:"c",4:"d",5:"e"}:
    print(i)