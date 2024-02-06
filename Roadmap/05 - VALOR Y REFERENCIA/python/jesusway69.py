import os
os.system('cls')
os.system('clear')
"""
 * EJERCICIO:
 * - Muestra ejemplos de asignación de variables "por valor" y "por referencia", según
 *   su tipo de dato.
 * - Muestra ejemplos de funciones con variables que se les pasan "por valor" y 
 *   "por referencia", y cómo se comportan en cada caso en el momento de ser modificadas.
 * (Entender estos conceptos es algo esencial en la gran mayoría de lenguajes)
 *
"""

vpv = "Hola Mundo" #Al ser un tipo primitivo (string) Python toma la variable por valor
print("Variable por valor ANTES de la función:",vpv)
vpr = ["Hola", "Mundo"] #Al ser un tipo de estructura (lista) Python toma la variable por referencia
print("Variable por referencia ANTES de la función:",vpr)
def string_variables(vpv:str, vpr:list[str,str]):
    vpv = vpv.replace("Mundo","Python") #Modificamos el string dentro de la función
    print("\nVariable por valor DENTRO de la función:",vpv)
    vpr [1] = "Python" #Modificamos un elemento de la lista dentro de la función
    print("Variable por referencia DENTRO de la función:",vpr)
string_variables(vpv,vpr)

print("\nVariable por valor DESPUÉS de la función:",vpv)
#El string modificado dentro de la función sigue teniendo su valor original despues de la misma
print("Variable por referencia DESPUÉS de la función:",vpr)
#La lista modificada dentro de la función ha quedado con la modificación despues de la misma

#En el siguiente caso usaremos variable de tipo int para valor y un set para referencia, además
# añadiremos a la impresión el nº identificativo que asigna Python a la variable en cada caso.
vpv = 128
print("\nVariable por valor ANTES de la función:",vpv, "con ID:", id(vpv))
vpr = {1,2,4,8,16,32,64}
print("Variable por referencia ANTES de la función:",vpr,"con ID:", id(vpr))

def int_variables (vpv:int, vpr:set):
    vpv = vpv*2
    print("\nVariable por valor DENTRO de la función:",vpv,"con ID:", id(vpv))
    vpr.add(128)
    print("Variable por referencia DENTRO de la función:",vpr,"con ID:", id(vpr))
int_variables(vpv,vpr)

print("\nVariable por valor DESPUÉS de la función:",vpv,"con ID:", id(vpv))
print("Variable por referencia DESPUÉS de la función:",vpr, "con ID:", id(vpr), "\n")
#Observamos a la salida por terminal del programa que los ID siempre se mantienen en el caso de
# las variables por referencia pero cambia en las de valor dentro de la función para después
# volver a mostrar su ID original después de la misma.


#Sin embargo una variable por referencia no modificará su contenido si lo que hace la función es 
# reasignarle otra lista con valores modificados como vemos en el siguiente ejemplo:

my_list =[1,2,3]
print("Variable por referencia ANTES de la función:", my_list)
def re_asign (my_list):
    my_list =[4,5,6]
    print("\nVariable por referencia reasignada DENTRO de la función:",my_list)
re_asign(my_list)
print("Variable por referencia reasignada DESPUÉS de la función:",my_list)



"""
 * DIFICULTAD EXTRA (opcional):
 * Crea dos programas que reciban dos parámetros (cada uno) definidos como variables anteriormente.
 * - Cada programa recibe, en un caso, dos parámetros por valor, y en otro caso, por referencia.
 *   Estos parámetros los intercambia entre ellos en su interior, los retorna, y su retorno
 *   se asigna a dos variables diferentes a las originales. A continuación, imprime el valor de las
 *   variables originales y las nuevas, comprobando que se ha invertido su valor en las segundas.
 *   Comprueba también que se ha conservado el valor original en las primeras.
"""
print("\nEJERCICIO:\n")
var1 = "Hola"
var2 = "Python"

def value_exchange(var1,var2):
    copy = var1
    var1 = var2
    var2 = copy
    return var1, var2

new_var1, new_var2 = value_exchange(var1,var2)
print(var1 + " " + var2)
print (new_var1 + " " + new_var2 + "\n")


var1 = ["Hola"]
var2 = ["Python"]

def reference_exchange(var1,var2):
    copy = var1
    var1 = var2
    var2 = copy
    return var1, var2

new_var1, new_var2 = reference_exchange(var1,var2)
print(var1 ,  var2)
print (new_var1 ,  new_var2 , "\n")


