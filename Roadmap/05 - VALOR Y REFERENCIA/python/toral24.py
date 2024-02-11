'''
EJERCICIO:
Muestra ejemplos de asignación de variables "por valor" y "por referencia", según
su tipo de dato.
Muestra ejemplos de funciones con variables que se les pasan "por valor" y 
"por referencia", y cómo se comportan en cada caso en el momento de ser modificadas.
(Entender estos conceptos es algo esencial en la gran mayoría de lenguajes)
'''
# Paso de parametros por valor (la función realiza una copia local de la variable) -valor-

var = 22

def local(varialbe):
    varialbe *2

local(var)

print(var)

# Se puede modificar la variable a nivel global de la siguiente forma

def ref(variable):
    return variable*2
var = ref(var)
print(var)

# Paso de parametros por referencia (la función modifica las variables de forma global) -listas-

vars = [1,4,22]

def reflis(variables):
    for i,n in enumerate(variables):
        variables[i] *=2

reflis(vars)
print(vars)

'''
EXTRA (opcional):
dos programas que reciban dos parámetros (cada uno) definidos como variables anteriormente.
Cada programa recibe, en un caso, dos parámetros por valor, y en otro caso, por referencia.
Estos parámetros los intercambia entre ellos en su interior, los retorna, y su retorno
se asigna a dos variables diferentes a las originales. A continuación, imprime el valor de las
variables originales y las nuevas, comprobando que se ha invertido su valor en las segundas.
Comprueba también que se ha conservado el valor original en las primeras.
'''

# Por valor
aux=0
a = 5
b = 8

def valor(var1,var2):
    aux = var1
    var1 = var2
    var2 = aux
    return var1,var2

c,d = valor(a,b)
print(f'variables nuevas{c,d}. variables viejas{a,b}')

# por referencia

valores = [8,5]
def referencia(lista):
    aux = valores[0]
    valores[0] = valores[1]
    valores[1] = aux
    return lista
auxi = referencia(valores[:])
print(f'variables nuevas{auxi}. variables viejas{valores}')