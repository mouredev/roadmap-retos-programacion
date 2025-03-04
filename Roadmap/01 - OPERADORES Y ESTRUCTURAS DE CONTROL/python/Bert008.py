# 
#  EJERCICIO:
#  - Crea ejemplos utilizando todos los tipos de operadores de tu lenguaje:
#    Aritméticos, lógicos, de comparación, asignación, identidad, pertenencia, bits...
#    (Ten en cuenta que cada lenguaje puede poseer unos diferentes)
#  - Utilizando las operaciones con operadores que tú quieras, crea ejemplos
#    que representen todos los tipos de estructuras de control que existan
#    en tu lenguaje:
#    Condicionales, iterativas, excepciones...
#  - Debes hacer print por consola del resultado de todos los ejemplos.
# 
#  DIFICULTAD EXTRA (opcional):
#  Crea un programa que imprima por consola todos los números comprendidos
#  entre 10 y 55 (incluidos), pares, y que no son ni el 16 ni múltiplos de 3.
# 
#  Seguro que al revisar detenidamente las posibilidades has descubierto algo nuevo.
# 
x = 3
y = 4
b = 10
c = 10
d = 10
e = 10
f = 10
g = 10
print('Operadores aritmeticos')
print('---------------------------------------')
print('x = ', x)
print('y = ', y)
print("Suma (x + y): ", x + y)
print("Resta (x - y): ", x + y)
print("Multiplicacion (x * y): ", x * y)
print("Division (y / x): ", y / x)
print("Modulus (x % y): ", x % y)
print("Exponente (x ** y): ", x ** y)
print("Divisoin de Piso (y // x): ", y // x)
print('---------------------------------------')
print("Operadores logicos")
print('And (x and y): ', (x and y))
print('Or (x or y)', (x or y))
print('Not (not False): ', not False)
print('---------------------------------------')
print('Operadores de comparacion')
print('Mayor o igual que (x >= y): ', (x >= y))
print('Menor o igual que (x <= y): ', (x <= y))
print('Mayor que (x < y): ', (x < y))
print('Menor que (x > y): ', (x > y))
print('Igual que (x == y): ', (x == y))
print('Diferente de ( x != y): ', (x != y))
print('---------------------------------------')
print('Operadores de Asignacion')
print('+=\n-=\n*=\n/=\n%=\n**=\n//=')
y += x
b -= y
c *= b
d /= c
e %= d
f **= e
g //= f
print('---------------------------------------')
print("Operadores de identidad")
h = 10
i = 10
print("h = 10", h)
print("i = 10", i)
print("h is i = ", h is i)
print("h is not i = ", h is not i)
j = [1, 2, 3]
k = [1, 2, 3]
print("i = ", j)
print("k = ", k)
print("i is k = ", i is k)
print("i is not k = ", i is not k)
print("Los objetos no son iguales entre si")
print('---------------------------------------')
print("Operadores de pertenencia")
print("in")
print("not in")
l = [1, 2, 3, 4, 5, 6]
print("l = ", l)
for i in range(1, 10):
    if i in l:
        print(f"{i} in l")
    else:
        print(f"{i} not in l")
print('---------------------------------------')
print("Operadores binarios")
s = 7
o = 8
print("Or: s | o =", (s | o))
print("And: s & o = ", s & o)
print("Not: ~(s) = ", ~(s))
print("Xor: s ^ o = ", s ^ o)
print("Desplaazameinto izquierda: << ", s << 2)
print("Desplazamiento derecha: << ", o >> 2)
print('---------------------------------------')
print("Sentencias condicionales")
a = 0
b = 1
if a == 1:
    print(a)
else: 
    print(b)
print('---------------------------------------')
print("Sentencias iterativas")
words = ['apple', 'banana', 'apple', 'cherry', 'banana']
by_letter = {}
for word in words:
    letter = word[0]
    if letter not in by_letter:
        by_letter[letter] = [word]
    else:
        by_letter[letter].append(word)

print(by_letter)

i = 0
oracion = "Hola mundo"
while i < len(oracion):
    print(oracion[i])
    i += 1
else:
    print("cruel")
print('---------------------------------------')
print("Excepciones")
a = 5
b = 3
try:
    c = a/b
except ZeroDivisionError:
    print("No se puede dividir sobre cero")
finally:
    print("No es posible dividir entre 0")
print('---------------------------------------')
for i in range(10,56,2):
    if i != 16 and i % 3 != 0:
        print(i)

