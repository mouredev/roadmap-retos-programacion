

#
#  * EJERCICIO:
#  * - Muestra ejemplos de asignación de variables "por valor" y "por referencia", según
#  *   su tipo de dato.

# Asignacion por valor
x = 24
name = "andrei"
day = x
print(f"Valor de x = {x}. el Nombre es {name} y se va el dia {day}")

# Asignacion por referencia
lista1 = [1, 2, 3]
lista2 = lista1
print(f"la lista1 es {lista1} y la lista2 es {lista2}")
lista2.append(4)
print(f"la lista1 es {lista1} y la lista2 es {lista2}")

# Variables Globales

y = 5
def afunc():
    global y
    x = 10
    y = x + y
    
    print(f"Examp Variables Globales -> el valor de x es {x} y el de y es {y} y la suma es {x + y}")
    
afunc()
print(f"el valor de x es {y}\n\n")


#  * - Muestra ejemplos de funciones con variables que se les pasan "por valor" y 
#  *   "por referencia", y cómo se comportan en cada caso en el momento de ser modificadas.
#  * (Entender estos conceptos es algo esencial en la gran mayoría de lenguajes)
#  *
# funcion por valor
lax = 24.5
def mifuncion(varxvalor: float):
    varxvalor = 100.5
    print(f"por valor {varxvalor}\n")

mifuncion(lax)

print(lax)

#funcion por referencia
x = [100, 120, 330]
y = [1, 2]
print(x, y)
def funcion(entrada: list):
    y = entrada
    entrada.append(400)
    print(entrada, y)
funcion(x)
print(x, y)

print("\n\n> > >  > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > >\n\n")

"""
 * DIFICULTAD EXTRA (opcional):
 * Crea dos programas que reciban dos parámetros (cada uno) definidos como
 * variables anteriormente.
 * - Cada programa recibe, en un caso, dos parámetros por valor, y en otro caso, por referencia.
 *   Estos parámetros los intercambia entre ellos en su interior, los retorna, y su retorno
 *   se asigna a dos variables diferentes a las originales. A continuación, imprime
 *   el valor de las variables originales y las nuevas, comprobando que se ha invertido
 *   su valor en las segundas.
 *   Comprueba también que se ha conservado el valor original en las primeras.
 """

# Por valor

def interchval(valor1: int, valor2: int):
    aux = valor1
    valor1 = valor2
    valor2 = aux
    return (valor1, valor2)


var1 = 100
var2 = 150

newval1, newval2 = interchval(var1, var2)
print(var1, var2, newval1, newval2)


# Por referencia
def interchref(valor1: list, valor2: list) -> tuple: 
    aux = valor1
    valor1 = valor2
    valor2 = aux
    return valor1, valor2


var11 = [100, 200]
var21 = [350, 450]

newval1, newval2 = interchref(var1, var2)
print(var1, var2)
print(newval1, newval2)

