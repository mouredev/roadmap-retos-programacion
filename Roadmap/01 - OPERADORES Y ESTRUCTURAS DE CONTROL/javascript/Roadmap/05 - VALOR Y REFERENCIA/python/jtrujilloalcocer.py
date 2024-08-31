# #05 VALOR Y REFERENCIA
## Ejercicio

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

#Asignacion de variables por valor
a = 5 #a es un entero
b = a #b toma el valor de a
b = 3 #b cambia su valor
print(a) #5
print(b) #3

#Asignacion de variables por referencia
a = [5] #a es una lista
b = a #b toma la referencia de a (no el valor)
b[0] = 3 #b cambia el valor de a (porque es la misma lista)
print(a) #[3]
print(b) #[3]

#Funciones con variables por valor
a = 5 #a es un entero
def funcion_valor(a): #a es una copia de la variable original
    a = 3 #a cambia su valor
    return a #se devuelve el valor de a
print(funcion_valor(a)) #3

#Funciones con variables por referencia 
a = [5] #a es una lista 
def funcion_referencia(a): #a es una copia de la variable original
    a[0] = 3 #a cambia el valor de la lista original
    return a #se devuelve la lista original    
print(funcion_referencia(a)) #[3]

#DIFICULTAD EXTRA (opcional):
#Crea dos programas que reciban dos parámetros (cada uno) definidos como variables anteriormente.
# - Cada programa recibe, en un caso, dos parámetros por valor, y en otro caso, por referencia.
#   Estos parámetros los intercambia entre ellos en su interior, los retorna, y su retorno
#   se asigna a dos variables diferentes a las originales. A continuación, imprime el valor de las
#   variables originales y las nuevas, comprobando que se ha invertido su valor en las segundas.
#   Comprueba también que se ha conservado el valor original en las primeras.

a = 5
b = 3
c= [10]
d= [8]

#Programa que recibe dos parámetros por valor
def intercambio_valor(a, b): #a y b son copias de las variables originales
    a, b = b, a #se intercambian los valores
    return a, b #se devuelven los valores intercambiados
print(intercambio_valor(a, b)) #(3, 5)

#Programa que recibe dos parámetros por referencia
def intercambio_referencia(c, d):#c y d son copias de las variables originales
    c[0], d[0] = d[0], c[0]#se intercambian los valores de las listas
    return c, d #se devuelven las listas intercambiadas
print(intercambio_referencia(c, d)) #([3], [5])

