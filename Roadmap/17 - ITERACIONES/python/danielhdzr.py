# #17 ITERACIONES
#### Dificultad: Fácil | Publicación: 22/04/24 | Corrección: 29/04/24

'''
* EJERCICIO:
 * Utilizando tu lenguaje, emplea 3 mecanismos diferentes para imprimir
 * números del 1 al 10 mediante iteración.
 *
 * DIFICULTAD EXTRA (opcional):
 * Escribe el mayor número de mecanismos que posea tu lenguaje
 * para iterar valores. ¿Eres capaz de utilizar 5? ¿Y 10?
'''

# Metodo 1
lista_numeros = [1,2,3,4,5,6,7,8,9,10]
for i in lista_numeros:
    print(i)
print("Fin de iteracion 1")

# Metodo 2
numero = 0 
while True:
    numero += 1
    if numero <= 10:
        print(numero)
    else: 
        print("Fin de iteracion 2")
        break

# Metodo 3
for i in range(10):
    print(i+1)
print("Fin de iteracion 3")

# Metodo 4
numero = 10
for i in range(1, numero+1):
    print(i)
print("Fin de iteracion 4")

# Metodo 5
def iteracion(iter_num):
    numeros = []
    for i in range(iter_num):
        numeros.append(i)
    for j in (numeros):
        print(j+1)
    return("Fin de iteracion 5")
print(iteracion(10))

numeros = 10
print(*[i+1 for i in range(numeros)], sep="\n")
print("Fin de iteracion 6")

for i in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
    print(i)
print("Fin de iteracion 7")

for i in {1: "a", 2: "b", 3: "c", 4: "d", 5: "e", 6: "f", 7: "g", 8: "h", 9: "i", 10: "j"}.values():
    print(i)
print("Fin de iteracion 8")

print(*[i for i in range(1, 11)], sep="\n")
print("Fin de iteracion 9")