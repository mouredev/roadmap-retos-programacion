"""
EJERCICIO:
- Muestra ejemplos de asignación de variables "por valor" y "por 
referencia", según su tipo de dato.
- Muestra ejemplos de funciones con variables que se les pasan "por 
valor" y "por referencia", y cómo se comportan en cada caso en el 
momento de ser modificadas.
(Entender estos conceptos es algo esencial en la gran mayoría de 
lenguajes)

DIFICULTAD EXTRA (opcional):
Crea dos programas que reciban dos parámetros (cada uno) definidos 
como variables anteriormente.

- Cada programa recibe, en un caso, dos parámetros por valor, y en 
otro caso, por referencia.

Estos parámetros los intercambia entre ellos en su interior, los 
retorna, y su retorno se asigna a dos variables diferentes a las 
originales. 

A continuación, imprime el valor de las variables originales y las 
nuevas, comprobando que se ha invertido su valor en las segundas.

Comprueba también que se ha conservado el valor original en las primeras.

by adra-dev.
"""


"""
En un lenguaje de programaicon, una variable es un termnio que 
representa un espacio en la memoria del ordenador.
"""

# Paso por valor

a = int(10)
b = float(5)
c = complex(2+5j)
d = str("Hola mundo!")
e = list([1, 2, 3])
f = dict(zip(['a','b','c'],[1, 2, 3]))
g = set([1, 2, 3])

print(a, b, c, d, e, f, g,)
print(a is b)
print(e is f)
print(f is g)
print(g is e)

# Paso por referencia 

a = 10
b = a

c = 5.5
d = c

e = 2+5j
f = e

g = "Hola mundo!"
h = g

i = list([1, 2, 3])
j = i

k = dict(zip(['a','b','c'],[1, 2, 3]))
l = k

m = set([1, 2, 3])
n = m

print(a, b, c, d, e, f, g,)
print(a is b)
print(g is h)
print(i is j)
print(k is l)

"""
En python, los argumentos siempre se pasan por referencia, es decir, 
los identificadores definidos en la cabecera de la funcion quedan 
refernciados a las posiciones de memoria de los valores indicados en 
llamada a la funcion. Pero resulta que el objeto pasado como 
argumento puede ser mutable o inmutable. Si es inmutable, los 
parametors crean, como ya sabemos, un nuevo espacio en memoria, lo 
cual seria equivalente a un paso por valor. Por tanto, cuando los 
argumentos son objetos inmutables su contenido no se ve alterado por
la llamada a la funcion, pues los parametros guardan su propia copia 
del argumento.
"""

# paso por valor
def appellidar(nombre):
    nombre += ' Martinez'
    print(nombre)

nombre = 'Rosa'
appellidar(nombre)
print(nombre)

"""
En cambio, cuando pasamos como argumentos tipos mutables, la tabla 
de simbolos de la funcion tambien contiene sus propios 
identificadores, pero estos parametros apuntan a las posiciones de 
memoria donde se alojan los datos pasados como argumento.
"""

def ampliar(lista):
    lista += [4, 5, 6]

l = [1, 2, 3]
print(l)
ampliar(l)
print(l)


"""
Extra
"""
# Por valor

def value(value_1, value_2):
    temp = value_1
    value_1 = value_2
    value_2 = temp

    return value_1, value_2

value_1 ='Hello'
value_2 ='Python'
value_3, value_4 = value(value_1, value_2)
print(f"{value_1}, {value_2}")
print(f"{value_3}, {value_4}")



# Por referencia
def ref(value_1: list, value_2: list) -> tuple:
    temp = value_1
    value_1 = value_2
    value_2 = temp

    return value_1, value_2


my_list_a = [10,20]
my_list_b = [30,40]
my_list_c, my_list_d = ref(my_list_a, my_list_b)
print(f"{my_list_a}, {my_list_b}")
print(f"{my_list_c}, {my_list_d}")