# #05 VALOR Y REFERENCIA

"""

 * EJERCICIO:
 * - Muestra ejemplos de asignación de variables "por valor" y "por referencia", según
 *   su tipo de dato.
 * - Muestra ejemplos de funciones con variables que se les pasan "por valor" y 
 *   "por referencia", y cómo se comportan en cada caso en el momento de ser modificadas.
 * (Entender estos conceptos es algo esencial en la gran mayoría de lenguajes)
 *
 """

# Asignación de variables por valor

my_int = 10
print (my_int)
my_str = "Hola"
print (my_str)
my_boolean = True
print (my_boolean)

# Función con variable asignada por valor

def my_int_func(my_int):
    my_int = 20
    print (my_int)

my_int_func (my_int)

"""En el caso anterior se puede ver que se pasa la variable por valor
    y cambia dentro de la función

"""

# Asignación de variables por referencia

my_list = ["Hola", "Python"]
print (my_list)
my_list_2 = my_list
my_list_2.append ("Web")
print (my_list_2)
print (my_list)           

""" Con los dos últimos print se puede ver que cuando se hace asignación por referencia,
    este apunta a dirección (puntero) y cuando se hacen moficaciones, se realizan a la
    dirección, entonces todas las variables que apunten a ella van a cambiar.
"""

# Función con variable por referencia

def my_ref_func(my_list):
    my_list.append ("2")
    print (my_list)

my_ref_func(my_list)
print (my_list)

"""
 DIFICULTAD EXTRA (opcional):

 *   Crea dos programas que reciban dos parámetros (cada uno) definidos como variables anteriormente.
 *   Cada programa recibe, en un caso, dos parámetros por valor, y en otro caso, por referencia.
 *   Estos parámetros los intercambia entre ellos en su interior, los retorna, y su retorno
 *   se asigna a dos variables diferentes a las originales. A continuación, imprime el valor de las
 *   variables originales y las nuevas, comprobando que se ha invertido su valor en las segundas.
 *   Comprueba también que se ha conservado el valor original en las primeras.
 
 """

my_int_1 = 5
my_int_2 = 10

def var_valor(num_1,num_2)-> tuple:
    num = num_1
    num_1 = num_2
    num_2 = num
    return (num_1, num_2)

my_int_3 , my_int_4 = var_valor(my_int_1,my_int_2)
print (my_int_1,my_int_2)
print(my_int_3,my_int_4)

list_1 = [5,10]
list_2 = [15,20]

def var_ref (list_3:list, list_4:list)-> tuple:
    list_n = list_3
    list_3 = list_4
    list_4 = list_n
    return (list_3,list_4)

list_3,list_4 = var_ref(list_1,list_2)
print (list_1,list_2)
print (list_3,list_4)
