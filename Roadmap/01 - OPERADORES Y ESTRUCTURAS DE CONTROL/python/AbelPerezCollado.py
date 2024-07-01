from random import randint
n1 = randint(1,10)
n2 = randint(1,10)

# Operadores aritmeticos
print(f'Suma {n1} + {n2} = {n1+n2}')
print(f'Resta {n1} - {n2} = {n1-n2}')
print(f'Multiplicacion {n1} * {n2} = {n1*n2}')
print(f'Division {n1} / {n2} = {n1/n2}')
print(f'Resto {n1} % {n2} = {n1%n2}')
print(f'Potencia {n1} ** {n2} = {n1**n2}')
print(f'Division entera {n1} // {n2} = {n1//n2}')
print(f'Suma {n1} + {n2} = {n1+n2}')

# Operadores Logicos
print(2==2 and 1==1)
print(n1==n2 or 1==1)
print(not n1==n2)
    

# Operadores de comparación
print("Igualdad: 1 == 1 es", 1 == 1) 
print("Desigualdad: a != b es", 'a' != 'b') 
print("Mayor que: 10 > 3 es", 10 > 3) 
print("Menor que: 2 < 3 es", 2 < 3) 
print("Mayor o igual que: 2 >= 2 es", 2 >= 2) 
print("Menor o igual que: 2 <= 7 es", 2 <= 7)

# Operadores de asignación
a = 5
print(f'Operador a = 5 ->{a}')
a += 5
print(f'Operador a += 5 ->{a}')
a -= 5
print(f'Operador a -= 5 ->{a}')
a *= 3
print(f'Operador a *= 3 ->{a}')
a /= 3
print(f'Operador a /= 3 -> {a}')
a %=3
print(f'Operador a %= 3 -> {a}')
a **=3
print(f'Operador a **= 3 -> {a}')
a //=3
print(f'Operador a //= 3 -> {a}')


# Operadores de identidad
a = 3
b = 3
c = 4
print(f'3 is 3 -> {a is b}')
print(f'4 is not 3 -> {c is not b}')


# Operadores de pertenencia 
a = [1,2,3,4,5]
print(f'1 in a -> {1 in a}')
print(f'7 not in a -> {7 not in a}')

# Operadores de bits
print("AND bit a bit: 2 & 3 es", 2 & 3) 
print("OR bit a bit: 2 | 3 es", 2 | 3) 
print("XOR bit a bit: 2 ^ 3 es", 2 ^ 3) 
print("NOT bit a bit: ~2 es", ~2) 
print("Desplazamiento a la derecha: 2 >> 1 es", 2 >> 1) 
print("Desplazamiento a la izquierda: 2 << 1 es", 2 << 1) 

# Estructuras de control condicionales iterativas, excepciones
name = 'Abel'
apellido = 'Perez'
#Condicionales
if name is not apellido:
    print('Sentencia IF')
if name is apellido:
    pass
elif 'a' in apellido:
    print('Sentencia elif')
else:
    print('Sentencia else')

# Iteraciones
for l in name:
    print(l)

n =0    
while n <= 4:
    print(n)
    n += 1
    
# Excepciones
a = 1
b = 2
try:
    print(len(a))
except Exception as err:
    print(err)
    
# Extra: Programa que imprima por consola todos los numeros comprendidos entre 10 y 55 incluidos
#        pares y que no son ni el 16 ni multiplos de 3
for n in range(10,56):
    if not n % 3 == 0 and n != 16 and n % 2 == 0:
        print(n)
 

    