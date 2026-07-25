"""
EJERCICIO:
- Muestra ejemplos de asignación de variables "por valor" y "por referencia", según
  su tipo de dato.
- Muestra ejemplos de funciones con variables que se les pasan "por valor" y 
  "por referencia", y cómo se comportan en cada caso en el momento de ser modificadas.
(Entender estos conceptos es algo esencial en la gran mayoría de lenguajes)

DIFICULTAD EXTRA (opcional):
Crea dos programas que reciban dos parámetros (cada uno) definidos como variables anteriormente.
- Cada programa recibe, en un caso, dos parámetros por valor, y en otro caso, por referencia.
  Estos parámetros los intercambia entre ellos en su interior, los retorna, y su retorno
  se asigna a dos variables diferentes a las originales. A continuación, imprime el valor de las
  variables originales y las nuevas, comprobando que se ha invertido su valor en las segundas.
  Comprueba también que se ha conservado el valor original en las primeras.
"""

#*-------------------------------------------------------------------------------------------------------------#
print("-----------------------------------------------------------------------------------------------------")
print("Variables por valor:\n")
inicio = 156
print(f"La variable inicio tiene el siguiente valor: {inicio}")
fin = inicio
print(f"La variable fin tendrá el mismo valor que incio: {fin}")
fin = 456
print(f"La variable fin se ha modificado ya hora tiene el siguiente valor: {fin}")

print("Funciones con variables por valor:\n")
def modificar_valor(ini_nuevo):
    ini_nuevo = 3864
    print(ini_nuevo)

ini = 45
modificar_valor(ini)
print(ini)

#*-------------------------------------------------------------------------------------------------------------#

print("-----------------------------------------------------------------------------------------------------")
print("Variables por Referencia:\n")

notas = [3.5,4.6,7.8,9]
print(f"Esta es una lista con las notas de una materia: {notas}")
not_final = notas 
print(f"La nueva lista tendrá el mismo valor que la lista notas: {not_final}")
not_final.append(5.6)
print(f"La lista not_final se modificó y estos son sus valores: {not_final}")

print("Funciones con variables por referencia:\n")
def modificar_lista(nota_lista):
    nota_lista.append(6.8)
    print(nota_lista)

nueva_notas = [3.4,5.6,8.2,3.2]
modificar_lista(nueva_notas)
print(nueva_notas)

#*-------------------------------------------------------------------------------------------------------------#
"""
DIFICULTAD EXTRA (opcional):
Crea dos programas que reciban dos parámetros (cada uno) definidos como variables anteriormente.
- Cada programa recibe, en un caso, dos parámetros por valor, y en otro caso, por referencia.
  Estos parámetros los intercambia entre ellos en su interior, los retorna, y su retorno
  se asigna a dos variables diferentes a las originales. A continuación, imprime el valor de las
  variables originales y las nuevas, comprobando que se ha invertido su valor en las segundas.
  Comprueba también que se ha conservado el valor original en las primeras.
"""

print("-----------------------------------------------------------------------------------------------------")

#Para Valor
print("Funciones para Valor con dos parametros:\n")
def valor(u,w):
    u = w * 15
    w = 25 - u
    return u,w

x = 350
y = 456
nuevo_x , nuevo_y = valor(x,y)
print(f"Los valores definidos anteriormente son: {x,y}")
print(f"Los nuevos valores son: {nuevo_x,nuevo_y}")

print("-----------------------------------------------------------------------------------------------------")

#Para Referencia
print("Funciones para Referencia con dos parametros:\n")
def referencia(list_a,list_b):
    list_a = [list_b,list_a]
    list_b = list_a
    return list_a, list_b

list_u = [3.4,5,7,8,9]
list_w = [4,8,1.2,4.3,7.6]

nueva_lista_u , nueva_lista_w = referencia(list_u,list_w)
print(f"Los valores definidos anteriormente son: {list_u,list_w}")
print(f"Los nuevos valores son: {nueva_lista_u,nueva_lista_w}")