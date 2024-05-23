### Funciones ###

#funcion sin parametros
def my_function_basic():
    print('Funcion basica')

my_function_basic()

#funcion con parametros
def my_new_function_basic(first, second):
    print(f'la suma de {first} y {second} es : ', first + second)

my_new_function_basic(9, 6)

#funcion con retorno
def my_functtion_return(first, second):
    return (first * second)

my_return = my_functtion_return(2, 6)
print( my_return)

def impr_name(name, surname ):
    print(f'{name} {surname}')

# le puedo cambiar el orden de los parametros pero no puedo omitir ninguno
impr_name('More' , 'Francesc')
impr_name(surname = 'More', name = 'Francesc') 
# impr_name(name = 'Francesc') da error

#funciones con bucle
def my_funcion_pares(primero, ultimo):
    while primero <= ultimo:
        multip = (int(primero))
        if (multip % 2) == 0:
            print(primero)
        primero +=1

my_funcion_pares(1,14)

#funciones anidadas

def long_word(word):
    ''' Cuenta los caracteres del argument entrado'''
    print(len(str(word)))

long_word('pedrito')


def suma_valor(*nums):
    '''suma los valores de un rango entre el mas peuqeño y el mayor de una lista de numeros'''
    print(list(range(min(nums), max(nums))))
    print(sum(range(min(nums), max(nums))))

suma_valor(1, 4, 5)


my_tipo = type(18)
print(my_tipo)
print(type('Hola'))

for i in range(3):
    print(i)

print(len('Hola mundo'))

print(locals())
print(globals())


''' funciones_integradas
A
abs()
aiter()
all()
anext()
any()
ascii()
B
bin()
bool()
breakpoint()
bytearray()
bytes()
C
callable()
chr()
classmethod()
compile()
complex()
D
delattr()
dict()
dir()
divmod()
E
enumerate()
eval()
exec()
F
filter()
float()
format()
frozenset()
G
getattr()
globals()
H
hasattr()
hash()
help()
hex()
I
id()
input()
int()
isinstance()
issubclass()
iter()
L
len()
list()
locals()
M
map()
max()
memoryview()
min()
N
next()
O
object()
oct()
open()
ord()
P
pow()
print()
property()
R
range()
repr()
reversed()
round()
S
set()
setattr()
slice()
sorted()
staticmethod()
str()
sum()
super()
T
tuple()
type()
V
vars()
Z
zip()

__import__()
'''
# DIFICULTAD EXTRA ejercicio

print ('-' * 20)

def dif_extr (param_a, param_b):
    n = 1
    a = 0
    b = 0
    while n <= 100:
        
        if (n % 3) == 0 and (n % 5) != 0:
            print (param_a, end='/')
            n += 1
            a = a + 1

        if (n % 5) == 0 and (n % 3) != 0:
            print (param_b, end='/')
            n += 1  
            b = b + 1 
        if (n % 3) == 0 and (n % 5) == 0:
            print (f'{param_a} / {param_b}')
            n += 1
            a = a + 1
            b = b + 1
        if (n % 3) != 0 and (n % 5) != 0 and (n <= 100):
            print(n, end='/')
            n += 1
    
    print(f'\n{param_a} se escribio {a} veces y {param_b} se escribio {b} veces')

dif_extr ('casa', 'perro')