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

#intento de anidar funciones
'''
def division(dividendo, divisor):
    cociente = (dividendo // divisor) 
    return cociente
    def cuadrado (cociente):
            print(cociente ** 2)

division(6, 2)
'''

#intento de anidar funciones correccion
def cuadrado (numerito):
    print(numerito ** 2)
def division(dividendo, divisor):
    cociente = (dividendo // divisor) 
    print(cociente)
    if cociente != 0:
        cuadrado(cociente)

division(6, 2)

# ejemplos con funciones integradas

my_tipo = type(18)
print(my_tipo)
print(type('Hola'))

for i in range(3):
    print(i)

print(len('Hola mundo'))

print(locals())
print(globals())

my_lista = [2,32,8,14,15,58,34,5]
print(max(my_lista))

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
