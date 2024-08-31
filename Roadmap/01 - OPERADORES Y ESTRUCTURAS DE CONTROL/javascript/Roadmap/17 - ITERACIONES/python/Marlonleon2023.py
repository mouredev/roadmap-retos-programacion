"""/*
 * EJERCICIO:
 * Utilizando tu lenguaje, emplea 3 mecanismos diferentes para imprimir
 * números del 1 al 10 mediante iteración.
 *
 * DIFICULTAD EXTRA (opcional):
 * Escribe el mayor número de mecanismos que posea tu lenguaje
 * para iterar valores. ¿Eres capaz de utilizar 5? ¿Y 10?
 */"""
 

# con for 
print("imprimiendo con for")
for i in range(1,11):
    print(i)
    
# con while

print("imprimiendo con while")
contador=0

while contador<10:
    contador+=1
    print(contador)
    
    
print("imprimiendo print se utiliza la funcion map")
list(map(print, range(1, 11)))