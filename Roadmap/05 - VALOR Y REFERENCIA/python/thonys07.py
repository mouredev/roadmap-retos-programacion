'''
 * EJERCICIO:
 * - Muestra ejemplos de asignación de variables "por valor" y "por referencia", según
 *   su tipo de dato.
 * - Muestra ejemplos de funciones con variables que se les pasan "por valor" y 
 *   "por referencia", y cómo se comportan en cada caso en el momento de ser modificadas.
 * (Entender estos conceptos es algo esencial en la gran mayoría de lenguajes)
 *
 * DIFICULTAD EXTRA (opcional):
 * Crea dos programas que reciban dos parámetros (cada uno) definidos como variables anteriormente.
 * - Cada programa recibe, en un caso, dos parámetros por valor, y en otro caso, por referencia.
 *   Estos parámetros los intercambia entre ellos en su interior, los retorna, y su retorno
 *   se asigna a dos variables diferentes a las originales. A continuación, imprime el valor de las
 *   variables originales y las nuevas, comprobando que se ha invertido su valor en las segundas.
 *   Comprueba también que se ha conservado el valor original en las primeras.
 */
 '''

#asignación de variables por valor

a=1993
c=a
a=15
print('a:', a)
print('c:', c)

#asignación de variables por referencia
lista1=[1,1993,3,4]
lista2=lista1
print('lista1:', lista1)
print('lista2:', lista2)
lista2[2]=5
lista1.append(1995)
print('lista1 after append 1995 :', lista1)
print('lista2 after add [2]=5:', lista2)

#funciones que modifican las variables por valor o referencia

def modificar_por_valor(a):
    b=a**3
    return b

def modificar_por_referencia(lista2):
    lista2.append(1995)
    return lista2

valor_modificado=modificar_por_valor(a)
referencia_modificada=modificar_por_referencia(lista2)
print(f'el valor a es {a} luego de modificado es {valor_modificado}, y el valor de lista2 es {lista1} luego de modificado es {referencia_modificada}')


''' EXTRA '''
#valores iniciales
inicial_a=12
inicial_b=10

def intercambiar_por_valor(a,b):
    temp=a
    a=b
    b=temp
    return a,b

#referencias iniciales

lista_inicial_a=[1,2,3]
lista_inicial_b=[1993,1994,1995]

def intercambiar_por_referencia(a,b):
    temp=a
    a=b
    b=temp
    return a,b

#valores y referencias intercambiadas
a_intercambiada,b_intercambiada=intercambiar_por_valor(inicial_a,inicial_b)
lista_intercambiada_a,lista_intercambiada_b=intercambiar_por_referencia(lista_inicial_a,lista_inicial_b)

print(f'el valor inicial de a es {inicial_a} y de b es {inicial_b} luego de intercambiado es {a_intercambiada} y {b_intercambiada} respectivamente')
print(f'el valor inicial de lista_a es {lista_inicial_a} y de lista_b es {lista_inicial_b} luego de intercambiado es {lista_intercambiada_a} y {lista_intercambiada_b} respectivamente')
