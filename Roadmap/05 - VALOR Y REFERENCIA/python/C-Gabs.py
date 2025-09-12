#Reto 05

'''Muestra ejemplos de asignación de variables "por valor" y "por referencia", según
 *   su tipo de dato.
 * - Muestra ejemplos de funciones con variables que se les pasan "por valor" y 
 *   "por referencia", y cómo se comportan en cada caso en el momento de ser modificadas.
 * (Entender estos conceptos es algo esencial en la gran mayoría de lenguajes)
 *
 * DIFICULTAD EXTRA (opcional):
 * Crea dos programas que reciban dos parámetros (cada uno) definidos como
 * variables anteriormente.
 * - Cada programa recibe, en un caso, dos parámetros por valor, y en otro caso, por referencia.
 *   Estos parámetros los intercambia entre ellos en su interior, los retorna, y su retorno
 *   se asigna a dos variables diferentes a las originales. A continuación, imprime
 *   el valor de las variables originales y las nuevas, comprobando que se ha invertido
 *   su valor en las segundas.
 *   Comprueba también que se ha conservado el valor original en las primeras.'''

#Variables por valor

#Enteros
numero_1 = 1
numero_2 = 2
print(f"numero_1: {numero_1} numero_2: {numero_2}")
numero_2 = numero_1
print(f"numero_1: {numero_1} numero_2: {numero_2}")
numero_1 = 3
print(f"numero_1: {numero_1} numero_2: {numero_2}")
print()

#Float
numero_1 = 1.5
numero_2 = 2.5
print(f"numero_1: {numero_1} numero_2: {numero_2}")
numero_2 = numero_1
print(f"numero_1: {numero_1} numero_2: {numero_2}")
numero_1 = 3.5
print(f"numero_1: {numero_1} numero_2: {numero_2}")
print()

#Cadenas
cadena_1 = "python"
cadena_2 = "Swift"
print(f"cadena_1: {cadena_1} cadena_2: {cadena_2}")
cadena_2 = cadena_1
print(f"cadena_1: {cadena_1} cadena_2: {cadena_2}")
cadena_1 = "Kotlin"
print(f"cadena_1: {cadena_1} cadena_2: {cadena_2}")
print()

#Boolean
verdadero = True
falso = False
print(f"Verdadero: {verdadero} Falso: {falso}")
falso = verdadero
print(f"Verdadero: {verdadero} Falso: {falso}")
print()

#Variables por referencia 

#Listas
lista_1 = ["Python","Kotlin","Java"]
lista_2 = ["SQL","Pandas","Numpy"]
print(f"lista_1: {lista_1} lista_2: {lista_2}")
lista_2 = lista_1 
print(f"lista_1: {lista_1} lista_2: {lista_2}")
lista_2.append(["HTML","JavaScrip"])
print(f"lista_1: {lista_1} lista_2: {lista_2}")
print()

#Sets
set_1 = {1,2,3}
set_2 = {4,5,6}
print(f"set_1: {set_1} set_2: {set_2}")
set_2 = set_1 
print(f"set_1: {set_1} set_2: {set_2}")
set_2.update({7,8,9})
print(f"set_1: {set_1} set_2: {set_2}")
print()

#Diccionarios
dict_1 = {"Nombre":"Brais","Lenguaje":"Kotlin"}
dict_2 = {"Nombre":"C-Gabs","Lenguaje":"Python"}
print(f"dict_1: {dict_1} dict_2: {dict_2}")
dict_2 = dict_1
print(f"dict_1: {dict_1} dict_2: {dict_2}")
dict_2.update({"Librerias":["Numpy","Pandas"]})
print(f"dict_1: {dict_1} dict_2: {dict_2}")
print()

#Función con variables por valor
numero_int = 1
numero_float = 1.5
string = "Hola Python"
boolean = True
print(f"numero_int: {numero_int} numero_float: {numero_float} string: {string} boolean: {boolean}")

def var_por_valor(numero_1, numero_2, cadena, bool):
    numero_1 = 1+2
    numero_2 = 1.5*2
    cadena = "Hola Mundo"
    bool = False
    print(f"numero_1: {numero_1}, numero_2: {numero_2}, cadena: {cadena}, bool: {bool}")

var_por_valor(numero_int, numero_float, string, boolean)
print(f"numero_int: {numero_int} numero_float: {numero_float} string: {string} boolean: {boolean}")
print()

#Funvión con variables por referencia
lista = [1,2,3]
dict = {"Nombre":"C-Gabs","Edad":24,"Lenguaje":"Python"}
set = {"SQL","Numpy"}
print(f"lista: {lista} dict: {dict} set: {set}")


def var_por_ref(lista_num,dict_datos,set_elem):
    lista_num.append([4,5,6])
    dict_datos.update({"Nombre":"Brais","Apellido":"Moure","Lenguajes":["Swift","Kotlin"]})
    set_elem.add("Pandas")
    print(f"lista_num: {lista_num}, dict_datos: {dict_datos}, set_elem: {set_elem}")

var_por_ref(lista, dict, set)
print(f"lista: {lista} dict: {dict} set: {set}")
print()

#Reto extra

valor_1 = 5
valor_2 = 7

def por_valor(parametro_1,parametro_2):
    parametro_1, parametro_2 = parametro_2, parametro_1
    return parametro_1, parametro_2

valor_3, valor_4 = por_valor(valor_1,valor_2)
print(f"Valor_1: {valor_1}, valor_2: {valor_2}")
print(f"Valor_3: {valor_3}, valor_4: {valor_4}")

ref_1 = [1,2,3]
ref_2 = [4,5,6]

def por_ref(parametro_1,parametro_2):
    parametro_1, parametro_2 = parametro_2, parametro_1
    return parametro_1, parametro_2

ref_3, ref_4 = por_ref(ref_1,ref_2)
print(f"Ref_1: {ref_1}, ref_2: {ref_2}")
print(f"Ref_3: {ref_3}, ref_4: {ref_4}")
