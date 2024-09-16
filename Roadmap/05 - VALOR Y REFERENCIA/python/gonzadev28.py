"""EJERCICIO:
 * - Muestra ejemplos de asignación de variables "por valor" y "por referencia", según
 *   su tipo de dato.
 * - Muestra ejemplos de funciones con variables que se les pasan "por valor" y 
 *   "por referencia", y cómo se comportan en cada caso en el momento de ser modificadas.
 * (Entender estos conceptos es algo esencial en la gran mayoría de lenguajes)"""

#Asignacion por valor(Tipos de datos primitivos(int, string, bool, float...))
mi_string = "primer valor" 
mi_string2 = mi_string

mi_string = "segundo valor" 
"""Aunque se modifique el valor del string, "mi_string2" sigue valiendo lo
que se le asignó en primera instacia """

print(mi_string)
print(mi_string2)

#Asignacion por referencia (Funciona en listas, tuplas, diccionarios, set...)

mi_lista : list = [1, 2, 3, 4, 5]
mi_lista2 : list = mi_lista

mi_lista2.append(26472364763284) #Se agrega "26472364763284" a la lista 2
"""Si se modifica el valor de alguna de las 2 listas, se modifica en ambas su valor,
porque ambas apuntan al mismo espacio de memoria"""

print(mi_lista)
print(mi_lista2)

#Funcion por valor
x = 10
def por_valor(entrada):
    entrada = 20
por_valor(x)

print(x) #Aunque se intente modificar a 20, sigue valiendo 10

#Funcion por referencia
x = [10, 20, 30]
def por_referencia(entrada):
    entrada.append(40)

por_referencia(x)
print(x) #Se imprime [10, 20, 30, 40] por que se le agregó a "entrada" el valor de 40

"""DIFICULTAD EXTRA (opcional):
 * Crea dos programas que reciban dos parámetros (cada uno) definidos como variables anteriormente.
 * - Cada programa recibe, en un caso, dos parámetros por valor, y en otro caso, por referencia.
 *   Estos parámetros los intercambia entre ellos en su interior, los retorna, y su retorno
 *   se asigna a dos variables diferentes a las originales. A continuación, imprime el valor de las
 *   variables originales y las nuevas, comprobando que se ha invertido su valor en las segundas.
 *   Comprueba también que se ha conservado el valor original en las primeras."""

#Intercambio por valor
def inter_por_valor(var1, var2):
    var_temp = var1
    var1 = var2
    var2 = var_temp
    return var1, var2

var3 = 3
var4 = 4
var5, var6 = inter_por_valor(var3, var4)

print(var3, var4)
print(var5, var6)

#Intercambio por referencia
def inter_por_ref(str1: list, str2: list):
    str_temp = str1
    str1 = str2
    str2 = str_temp
    return str1, str2

str3: list = ["Moure"]
str4: list = ["Dev"]
str5, str6 = inter_por_ref(str3, str4)

print(str3, str4)
print(str5, str6)