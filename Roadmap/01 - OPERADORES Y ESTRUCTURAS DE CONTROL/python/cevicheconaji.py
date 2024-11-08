# Operadores aritméticos

x = 5
y = 2

print("Suma:", x + y)
print("Resta:", x - y)
print("Multiplicación:", x * y)
print("División:", x / y)
print("Módulo:", x % y)
print("Potencia:", x ** y)
print("División entera:", x // y)

# Operadores de comparación

z = 10
w = 20

print("Igualdad:", z == w)
print("Desigualdad:", z != w)
print("Mayor", z > w)
print("Menor", z < w)
print("Mayor o igual", z >= w)
print("Menor o igual", z <= w)

# Operadores lógicos

print(True and True)

print(False or True)

print(not False)

# Operadores de asignación
a = 5
a += 2
print("Asignación con adición:", a)

b = 10
b -= 2
print("Asignación con sustracción:", b)

c = 3
c *= 2
print("Asignación con multiplicación:", c)

d = 10
d /= 2
print("Asignación con división:", d)

e = 10
e %= 3
print("Asignación con módulo:", e)

f = 2
f **= 3
print("Asignación con potencia:", f)

g = 10
g //= 3
print("Asignación con división entera:", g)

# Operadores de identidad

h = 10
i = 10
print("Identidad:", h is i)

j = 10
k = 20
print("Identidad:", j is k)

print("Identidad con not:", j is not k)

# Operadores de pertenencia

l = [1, 2, 3, 4, 5]
print("Pertenece a la lista:", 4 in l)

m = [1, 2, 3, 4, 5]
print("Pertenece a la lista:", 6 in m)

print("Pertenece a la lista con not:", 6 not in m)

# Operadores de bits

n = 5
o = 3

print("AND a nivel de bits:", n & o)

print("OR a nivel de bits:", n | o)

print("XOR a nivel de bits:", n ^ o)

print("Desplazamiento a la izquierda:", n << 1)

print("Desplazamiento a la derecha:", n >> 1)

# Operadores walrus y iteradores

p = 10

if (q := p + 1) > p:
    print("El valor de q es:", q)

r = 10

while (s := r - 1) > 0:
    print("El valor de s es:", s)
    r = s

for t in range(10):
    print("El valor de t es:", t)

#excepciones
try:
    print(u)
except NameError as e:
    print("Error:", e)

'''Ejercicio extra 
Crea un programa que imprima por consola todos los números comprendidos
entre 10 y 55 (incluidos), pares, y que no son ni el 16 ni múltiplos de 3.
'''

for u in range(10, 56):
    if u % 2 == 0 and u != 16 and u % 3 != 0:
        print(u)




