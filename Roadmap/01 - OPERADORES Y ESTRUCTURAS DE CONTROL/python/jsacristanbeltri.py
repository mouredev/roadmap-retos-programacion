#Operadores Aritméticos
print('######## Operadores Aritméticos ########')
print(f'1 + 2 = {1+2}')
print(f'1 - 2 = {1-2}')
print(f'1 * 2 = {1*2}')
print(f'1 / 2 = {1/2}')
print(f'10 % 2 = {10%2}')

#Operadores logicos
print('######## Operadores logicos ########')
print(f'True and True={True and True}')
print(f'True and False={True and False}')
print(f'False and True={False and True}')
print(f'False and False={False and True}')
print(f'True or True={True or True}')   
print(f'True or False={True or False}')  
print(f'False or True={False or True}')  
print(f'False or False={False or False}') 
print(f'not True={not True}')
print(f'not False={not False}')
#Operadores de comparacion
print('######## Operadores de comparacion ########')
print(f'1==1={1==1}')
print(f'1!=1={1!=1}')
print(f'1<1={1<1}')
print(f'1<=2={1<=2}')
print(f'1>1={1>1}')
print(f'1>=2={1>=2}')

#Operadores de asignacion
print('######## Operadores de asignacion ########')
r = 1
r+=2
print(f'1+=2={r}')
r = 1
r-=2
print(f'1-=2={r}')
r = 1
r*=2
print(f'1*=2={r}')
r = 1
r/=2
print(f'1/=2={r}')
r = 1
r%=2
print(f'1%=2={r}')
r = 1
r//=2
print(f'1//=2={r}')
r = 1
r**=2
print(f'1**=2={r}')
r = 1
r&=2
print(f'1&=2={r}')
r = 1
r|=2
print(f'1|=2={r}')
r = 1
r^=2
print(f'1^=2={r}')
r = 1
r>>=2
print(f'1>>=2={r}')
r = 1
r<<=2
print(f'1<<=2={r}')

#Operadores de identidad
x = 4
y = 2
lista = [1, 5]
print('######## Operadores de identidad ########')
print(f'x:{x}')
print(f'y:{y}')
print(f'lista: {lista}')
print(f'x is lista={x is lista}')
print(f'x is y={x is y}')
print(f'x is not y={x is not y}')
print(f'x is 4={x is 4}')

#Operadores de pertenencia
print('######## Operadores de pertenencia ########')
lista = [1, 3, 2, 7, 9, 8, 6]
print(f'lista: {lista}')
print(f'4 in lista={4 in lista}')
print(f'3 in lista={3 in lista}')
print(f'4 not in lista={4 not in lista}')

#Operadores a nivel de bit
print('######## Operadores a nivel de bit ########')
x = 2
y = 7
print(f'x:{x}')
print(f'y:{y}')
print(f'x | y = {x | y}')
print(f'x ^ y={x ^ y}')
print(f'x & y={x & y}')
print(f'x << 1={x << 1}')
print(f'x >> 1={x >> 1}')
print(f'~x={~x}')

#Operadores de concatenacion de cadenas
print('######## Operadores de concatenacion de cadenas ########')
hola = 'Hola'
python = 'Pythonista'
hola_python = hola + ' ' + python  # concatenamos 3 strings
print(f'Hola +\' \'+ Pythonista={hola_python}')

#Condicionales
print('######## Condicionales ########')
x = 2
y = 7
print(f'x:{x}')
print(f'y:{y}')
if(x>y):
    print('x es mayor que y')
elif(x<y):
    print('x es menor que y')
else:
    print('x es igual que y')

#Iteracion
print('######## Iteracion ########')
lista = [1, 3, 2, 7, 9, 8, 6]
total=0
for n in lista:
    total+=n
print(f'lista: {lista}')
print(f'La suma de todos los elementos de la lista es: {total}')


x=10
while(x>0):
    print(f'x={x}')
    x-=1

#Excepciones
print('######## Excepciones ########')
try: 
    resultado = 4/0
except Exception as e: 
    print(f'error 4/0={e}')


'''programa que imprima por consola todos los números comprendidos
entre 10 y 55 (incluidos), pares, y que no son ni el 16 ni múltiplos de 3. '''
print('programa que imprima por consola todos los números comprendidos' 
      +' entre 10 y 55 (incluidos), pares, y que no son ni el 16 ni múltiplos de 3.')
for n in range(10,56):
    if(n%2==0 and n!=16 and n%3!=0):
        print(n)


