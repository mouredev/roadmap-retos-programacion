# /*
#  * EJERCICIO:
#  * - Muestra ejemplos de asignación de variables "por valor" y "por referencia", según
#  *   su tipo de dato.
#  * - Muestra ejemplos de funciones con variables que se les pasan "por valor" y 
#  *   "por referencia", y cómo se comportan en cada caso en el momento de ser modificadas.
#  * (Entender estos conceptos es algo esencial en la gran mayoría de lenguajes)

string1 = 'delpino'
print(string1)
string1 = 'tito-'
print(string1)
string2 = 'delpino'
print(string2)
string1 = string1 + string2 # cambiamos el valor de la variable 
print(string1)


def mi_funcion(lista: list):
    lista.append(40)
    print(lista)

    mi_lista2 = lista
    mi_lista2.append(50)

    print(lista)
    print(mi_lista2)

mi_lista = [10,20,30]
mi_funcion(mi_lista)
print(mi_lista)
    

#  * DIFICULTAD EXTRA (opcional):
#  * Crea dos programas que reciban dos parámetros (cada uno) definidos como variables anteriormente.
#  * - Cada programa recibe, en un caso, dos parámetros por valor, y en otro caso, por referencia.
#  *   Estos parámetros los intercambia entre ellos en su interior, los retorna, y su retorno
#  *   se asigna a dos variables diferentes a las originales. A continuación, imprime el valor de las
#  *   variables originales y las nuevas, comprobando que se ha invertido su valor en las segundas.
#  *   Comprueba también que se ha conservado el valor original en las primeras.

# Por valor
def funcion2(valor1, valor2):
    aux = valor1
    valor1 = valor2
    valor2 = aux
    return valor1, valor2

valor1 = 20
valor2 = 40
valor3, valor4 = funcion2(valor1, valor2)
print(f'Valor1= {valor1}, valor2= {valor2}')
print(f'Valor3= {valor1}, valor4= {valor2}')


# Por ref
def funcion3(valor1, valor2):
    aux = valor1
    valor1 = valor2
    valor2 = aux
    return valor1, valor2

lista1 = [20, 30]
lista2 = [40, 50]
lista3, lista4 = funcion3(lista1, lista2)
print(f'lista1= {lista1}, lista2= {lista2}')
print(f'lista3= {lista3}, lista4= {lista4}')