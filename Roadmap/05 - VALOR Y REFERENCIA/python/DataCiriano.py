"""
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
"""

# Tipos de dato por valor 

entero_1 = 25
entero_2 = entero_1 #Cada valor tiene su pososición de memoia independiente, y al igualrse una a la otra esto se mantiene
entero_2 = 15
print(entero_1)
print(entero_2)


#Tipo de dato por referencia (heredan posición de memoria)

lista_1 = [10,20]
lista_2 = lista_1 #En el momento en que se igualan, los datos pasan a almacenarse en la misma posición de memoria por eso luego al imprimir lista_1 esta tiene el nuevo elemento añadido a las lista_2 con .append
lista_2.append(50)
print(lista_1)
print(lista_2)


#Funciones con datos por valor

entero = 10

def funct_valor(entero: int):
    entero = 20
    print(entero)
    
funct_valor(entero)
print(entero)


#Funciones con datos por referencia

lista = [10,20]

def funct_referencia(lista: list):
    lista.append(30)
    print(lista)
    
funct_referencia(lista)
print(lista)


#----EXTRA----

def value(value_a:int, value_b:int) -> tuple:
    temp = value_a
    value_a = value_b
    value_b = temp
    return value_a, value_b

integer_01 = 10
integer_02 = 20

print(integer_01, integer_02)
print(value(integer_01, integer_02))


def reference(value_a:list, value_b:list) -> tuple:
    temp = value_a
    value_a =  value_b
    value_b = temp
    return value_a, value_b

list_01 = [10,20]
list_02 = [30,40]

print(list_01, list_02)
print(reference(list_01, list_02))