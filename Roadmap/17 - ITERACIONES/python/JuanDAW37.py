"""
* EJERCICIO:
 * Utilizando tu lenguaje, emplea 3 mecanismos diferentes para imprimir
 * números del 1 al 10 mediante iteración.
 *
 * DIFICULTAD EXTRA (opcional):
 * Escribe el mayor número de mecanismos que posea tu lenguaje
 * para iterar valores. ¿Eres capaz de utilizar 5? ¿Y 10?
"""
# Bucle while
print('*******Bucle While*******')
i = 1
while i <= 10:
    print(i)
    i += 1
    
# Simulando Do...While
print('*******Bucle Simulando Do...While*******')
i = 1
while True:
    if i <= 10:
        print(i)
        i += 1
    else:
        break

# Bucle for
print('*******Bucle For con listas(lists)*******')
numeros = [1,2,3,4,5,6,7,8,9,10]

for i in numeros:
    print(i)
    
print('*******Bucle For con conjuntos(sets)*******')
for i in {1,2,3,4,5,6,7,8,9,10}:
    print(i)
    
print('*******Bucle For con mapas(maps)*******')
for i in {1:'a',2:'b',3:'c',4:'d',5:'e',6:'f',7:'g',8:'h',9:'i',10:'j'}:
    print(i)

print('*******Bucle For con tuplas(tuples)*******')
for i in (1,2,3,4,5,6,7,8,9,10):
    print(i)
    
print('*******Bucle For con función range()*******')
for i in range(1, 11):
    print(i)
    
# Función recursiva:
print('*******Función Recursiva*******')
def imprimir_numeros(n:int = 1):
    if n <= 10:
        print(n)        
        imprimir_numeros(n + 1)
        
imprimir_numeros()

# EXTRA, de las 10 solicitadas podemos contar con las anteriores
print('*******Bucle For con Generadores Conprehesion List*******')
print(*[x for x in range(1, 11)], sep='\n') #El * indica que es un conprehesion list y usando sep indicamos que el separador, en este caso, será un retorno de carro

print('*******Cadena de texto*******')
lenguaje = 'Python'
for letra in lenguaje:
    print(letra)
    
print('*******Cadena de texto al revés*******')
for letra in reversed(lenguaje):
    print(letra)
    
print('*******Cadena de texto ordenada, usando enumerate para saber su índice*******')
for i, letra in enumerate(sorted(lenguaje)):
    print(f'Índice {i}, letra {letra}')