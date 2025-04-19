# /*
#  * EJERCICIO:
#  * - Muestra ejemplos de asignación de variables "por valor" y "por referencia", según
#  *   su tipo de dato.
#  * - Muestra ejemplos de funciones con variables que se les pasan "por valor" y 
#  *   "por referencia", y cómo se comportan en cada caso en el momento de ser modificadas.
#  * (Entender estos conceptos es algo esencial en la gran mayoría de lenguajes)
#  *
#  * DIFICULTAD EXTRA (opcional):
#  * Crea dos programas que reciban dos parámetros (cada uno) definidos como variables anteriormente.
#  * - Cada programa recibe, en un caso, dos parámetros por valor, y en otro caso, por referencia.
#  *   Estos parámetros los intercambia entre ellos en su interior, los retorna, y su retorno
#  *   se asigna a dos variables diferentes a las originales. A continuación, imprime el valor de las
#  *   variables originales y las nuevas, comprobando que se ha invertido su valor en las segundas.
#  *   Comprueba también que se ha conservado el valor original en las primeras.
#  */

# En python todo es un objeto, y las variables son referencia a esos objetos.

# Hay dos tipos de objetos: 
# Inmutables (int, str, float, tuple) que son tratados como pasados por valor 
# Mutables (list, dict, set), que son tratados como pasados por referencia

# Ejemplo de una variable pasada por valor:
x = 10

# Funcion con variable pasada por valor
def modificar(x):
    print(f'Antes {x}')
    x = 5
    print(f'Despues {x}')

modificar(x)

print(f'x Por fuera de la funcion {x}') #---> Aca se ve claramente como la variable original no se ve 
# modificada despues de la funcion

# Ejemplo de una variable pasada por referencia:

lista = [10,20,30]

# Funcion con variable pasada por referencia
def modificar_lista(lista):
    print(f'Antes {lista}')
    lista = [40,50,60]
    print(f'Despues {lista}')
    
    
modificar_lista(lista)
print(f'Lista por fuera de la funcion {lista}') #---> Aca se ve claramente como la variable original 
# se ve modificada despues de la funcion

a = 10
b = 20

print(f'Variables originales: a({a}) b({b})')

def por_valor(a,b):
    b2 = a
    a2 = b
    print(f'Variables modificadas: a({a2}) b({b2})')
    return b2,a2

por_valor(a,b)
print(f'Variables originales: a({a}) b({b})')

c = [10]
d = [20]

print(f'Variables originales: c({c[0]}) d({d[0]})')

def por_referencia(c,d):
    c.pop()
    d.pop()
    c.append(20)
    d.append(10) 
    print(f'Variables modificadas: c({c[0]}) d({d[0]})')
    

por_referencia(c,d)

print(f'Variables originales: c({c[0]}) d({d[0]})')
