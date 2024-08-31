######   OPERADORES DE ASIGNACION  #######

x = 5

x = 5
x += 3   # Es igual a escribir: x = x + 3

y = 5
y -= 3   # Es igual a escribir: y = y - 3

c = 5
c *= 3   # Es igual a escribir: c = c * 3

d = 5
d /= 3   # Es igual a escribir: d = d / 3

e = 5
e %= 3   # Es igual a escribir: e = e % 3

f = 5
f //= 3  # Es igual a escribir: f = f // 3

g = 5
g **= 3  # Es igual a escribir: g = g ** 3

h = 5
h &= 3   # Es igual a escribir: h = h & 3

i = 5
i |= 3   # Es igual a escribir: i = i | 3

j = 5
j ^= 3   # Es igual a escribir: j = j ^ 3

k = 5
k >>= 3  # Es igual a escribir: k = k >> 3

l = 5
l <<= 3  # Es igual a escribir: l = l << 3

print(x)
print(x)
print(y)
print(c)
print(d)
print(e)
print(f)
print(g)
print(h)
print(i)
print(j)
print(k)
print(l)

######    OPERADORES ARITMETICOS    ############

a = 3 
b = 2 

total = a + b # no se puede poner sum como nombre de variable ya que sum es una funcion interna 
diff = a - b
product = a * b
division = a / b
resto = a % b
floor_division = a // b
exponential = a ** b

print(total) 
print('a + b = ', total)
print('a - b = ', diff)
print('a * b = ', product)
print('a / b = ', division)
print('a % b  = ', resto)
print('a // b = ', floor_division)
print('a ** b = ', exponential)

#####    OPERADORES DE COMPARACION   ##########

"""
==	Equal	x == y	
!=	Not equal	x != y	
>	Greater than	x > y	
<	Less than	x < y	
>=	Greater than or equal to	x >= y	
<=	Less than or equal to	x <= y

"""

print(3 > 2)     # True
print(3 >= 2)    # True
print(3 < 2)     # False
print(2 < 3)     # True
print(2 <= 3)    # True
print(3 == 2)    # False
print(3 != 2)    # True
print(len('mango') == len('manzana'))  # False
print(len('mango') != len('manzana'))  # True
print(len('mango') < len('manzana'))   # True
print(len('milk') != len('meat'))      # False
print(len('milk') == len('meat'))      # True
print(len('tomato') == len('potato'))  # True
print(len('python') > len('dragon'))   # False

"""
Además del operador de comparación anterior, Python usa:

es : Devuelve verdadero si ambas variables son el mismo objeto (x es y)
no es : Devuelve verdadero si ambas variables no son el mismo objeto (x no es y)
in : Devuelve Verdadero si la lista consultada contiene un elemento determinado (x en y)
not in : devuelve True si la lista consultada no tiene un elemento determinado (x en y)

"""

print('1 is 1', 1 is 1)                       # True
print('1 is not 2', 1 is not 2)               # True 
print('A in Algoritmo', 'A' in 'Algoritmo')   # True 
print('B in Algoritmo', 'B' in 'Algoritmo')   # False 
print('coding' in 'coding for all')           # True 
print('4 is 2 ** 2:', 4 is 2 ** 2)            # True


####  OPERADORES LOGICOS  ###########

"""
and 	Devuelve True si ambas condiciones son verdaderas:	    x < 5 and  x < 10	
or	    Devuelve True si una de las condiciones es verdadera:	x < 5 or x < 4	
not	    Invierte el resultado, devuelve Falso si el resultado es verdadero:	not(x < 5 and x < 10)

"""

print(3 > 2 and 4 > 3) # True
print(3 > 2 and 4 < 3) # False - porque la segunda condicion es falsa
print(3 < 2 and 4 < 3) # False 
print('True and True: ', True and True)
print(3 > 2 or 4 > 3)  # True
print(3 > 2 or 4 < 3)  # True - porque una de las condiciones es verdadera
print(3 < 2 or 4 < 3)  # False - porque las dos condiciones son falsas
print('True or False:', True or False)
print(not 3 > 2)     # False - porque 3 > 2 es verdadero, entonces not True devuelve Falso
print(not True)      # False - Negacion
print(not False)     # True
print(not not True)  # True
print(not not False) # False


####    Crea un programa que imprima por consola todos los números comprendidos
####    entre 10 y 55 (incluidos), pares, y que no son ni el 16 ni múltiplos de 3.

for i in range(10, 56):
    if i == 16:
        pass
    elif i % 3 == 0:
        pass
    elif i % 2 == 0:
        print(i)

    