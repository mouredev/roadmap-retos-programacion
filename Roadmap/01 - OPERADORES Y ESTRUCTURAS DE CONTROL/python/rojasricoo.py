# author: Oscar Duvan R
'''

 * EJERCICIO:
 * - Crea ejemplos utilizando todos los tipos de operadores de tu lenguaje:
 *   Aritméticos, lógicos, de comparación, asignación, identidad, pertenencia, bits...
 *   (Ten en cuenta que cada lenguaje puede poseer unos diferentes)
 * - Utilizando las operaciones con operadores que tú quieras, crea ejemplos
 *   que representen todos los tipos de estructuras de control que existan
 *   en tu lenguaje:
 *   Condicionales, iterativas, excepciones...
 * - Debes hacer print por consola del resultado de todos los ejemplos.
 *
 * DIFICULTAD EXTRA (opcional):
 * Crea un programa que imprima por consola todos los números comprendidos
 * entre 10 y 55 (incluidos), pares, y que no son ni el 16 ni múltiplos de 3.
 *
 * Seguro que al revisar detenidamente las posibilidades has descubierto algo nuevo.


'''

# 1)

# Operadores aritmeticos
x, y = 2,5
print(f'Suma: {x + y}')
print(f'Resta: {x - y}')
print(f'Multiplicación: {x * y}')
print(f'Divición: {x / y}')
print(f'Elevado al cuadrado: {x ** y}') # etc...

# Operadores Logicos
print(True and False) # and: True  higual a False => False
print(True or False) # or: True o False => True
print(not(True == False)) # not: True distinto a False => True

# Operadores de Comparación
print(f'mayor que: {x > y}')
print(f'menor que: {x < y}')
print(f'mayor o higual: {x >= y}')
print(f'menor o higual: {x <= y}')
print(f'higual y higual: {x == y}')
print(f'distinto: {x != y}')

# Operadores de asignación
x = 5
x += 2

xx = 5
xx -= 2

xxx = 5
xxx *= 2

xxxx = 5
xxxx /= 2

xxxxx = 5
xxxxx %= 2

y = 5
y //= 2


yy = 5
yy **= 2

yyy = 5
yyy &= 2

print(f'Ahora x se le ha aumentado +2: {x}')
print(f'Ahora x se le ha restado -2: {xx}')
print(f'Ahora x se le ha multiplicado *2: {xxxx}')
print(f'Ahora x se le ha divido /2: {xxxx}')
print(f'Ahora x se le ha el resto %2: {xxxxx}')
print(f'Ahora x se le ha dado el cociente //2: {y}')
print(f'Ahora x se le ha elevado al cuadrado **2: {yy}')
print(f'Ahora x se le ha echo comparacion en bits: {yyy}')
# etc...

# Operadores de identidad
p,j = 1,1
print(p is j) # si  valor contenido es higual
print(p is not j) # si  valor contenido NO es higual

# Operadores de pertenencia
string = 'Hola Python'
print('Hola' in string) # Evalue si 'Hola' se encuentra en string
print('hola' not in string) # Evalua si 'hola' NO se encuentra en string

# Operadores de bits
s,d=5,3
r = s & d # comparación de bit a bit, devuelve 1 solo si ambos bits son 1
print(r) 

r = s | d # realizar operacion OR bit a bit. evuelve 1 si almenos uno de los bits es 1
print(r)

r = s ^ d # realiza una operacionXOR bit a bit, devuelve 1 solo si uno de los bits es 1, pero no ambos
print(r)

r = ~ d # este operador realiza una operacion NOT bit a bit, invertiendo todos los bits del numero
print(r)

r = s << d # Desplaza todos los bits por un numero hacia la izquierda
print(r) 

r = s >> d # Desplaza hacia la derecha  por numero
print(r) 

######################################################################################

# 2)
# if/elif/else/
x,y=5,4
if x == y:
    print("La comprobacion de que 'x' es higual a 'y' fue Verdadero")
if x != y:
    print("La comprobacion de que 'x' es distinto a 'y' fue Verdadera")
else:
    print('Las comprobaciones no han sido suficiente')

# while
subs_mr_beast = 0
while subs_mr_beast <= 1000: # ejecuta mientras subs_mr_beast sea menor o higual a 1000
    #print(subs_mr_beast)
    if subs_mr_beast == 1000: # si es higual entonces ejecuta esto
        print(f'Emos alcanzado los {subs_mr_beast}M de subcriptores y por eso regalaremos {subs_mr_beast}M de casas a las personas mas pobres del mundo.')
    subs_mr_beast +=1 # incrementamos


x = [2,3,4]
# 1) ej
for valor in x: # va recorriendo la lista cada vez que avanza la guarda en la variable valor que se encuentra en cada posición 
    print('imprimimos el valor de cada posicion de la lista recorrida: ',valor) # imprimimos el valor de cada posicion de la lista recorrida
# 2) ej
x='Pedro'
for xz in x:
    print('imprimimos el valor de cada posicion de la lista recorrida: ',xz)

########################################################################################

# 3)
#* DIFICULTAD EXTRA (opcional):
#* Crea un programa que imprima por consola todos los números comprendidos
# * entre 10 y 55 (incluidos), pares, y que no son ni el 16 ni múltiplos de 3.

x=10
while x<=55:
    if x%2==0 and x%3:
        print(x)
    x+=1