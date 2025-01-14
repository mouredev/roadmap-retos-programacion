#operadores aritmeticos

a = 20
b = 3

print('suma',a+b)
print('resta',a-b)
print('multiplicacion',a*b)
print('division',a/b)
print('modulo',a%b)
print('potencia',a**b)


#operadores lógicos

c = True
d = False

print('and logico', c and d)
print('or logico',c or d)
print('NOT logico',  not d)

#Operadores de comparacion

print('Mayor que', a>b)
print('menos que', a<b)
print('igualdad:', a==b)
print('distinto que', a!=b)
print('mayor o igual', a>=b)
print('menos o igual', a<=b)


#Operadores de asignacion

t = 10

print('Asignacion inicial', c)

c+=2

c*=3

print('resultado final',c)

#Operadores de identidad // intentan comparar el valor en memoria.

e = [1,2,3]
f = [1,2,3]

print('es igual', e is f)
print('no es igual', e is not f)

e = f

print('ahora si : ', e is f)

#Operadores de pertenencia

print('3 esta en la lista', 3 in e)

print('5 no esta en la lista', 5 not in e)

#Operadores de bit

a = 10 #1010

b = 3 #0011

print(f'AND: 10 & 3 = {10 & 3}')
print(f'OR: 10 | 3 = {10 & 3}')
print(f'OR: 10 ^ 3 = {10 & 3}')
 
 


#Estructuras de control

#Condicionales

if a > b:
    print('a es mayor que b')

elif a == b:
    print('a es igual a b')
    
else:
    print('a es menor que b')
    
#While

count = 0

while count < 0:
    print(count)
    count +=1
    
#For

for i in range(10):
    print(i)
    
try:
    result = a / 0
    
except ZeroDivisionError:
    print('error no puedo dividir en 0 ')
    
finally:
    print('Ha finalizado el manejo de excepciones')


#€xtra
for i in range(10,56):
    if i % 2 == 0 and i != 16 and i % 3 != 0 : 
        print(i)
