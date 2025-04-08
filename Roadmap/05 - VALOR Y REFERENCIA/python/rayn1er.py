# /*
#  * EJERCICIO:
#  * - Muestra ejemplos de asignación de variables "por valor" y "por referencia", según
#  *   su tipo de dato.
#  * - Muestra ejemplos de funciones con variables que se les pasan "por valor" y 
#  *   "por referencia", y cómo se comportan en cada caso en el momento de ser modificadas.
#  * (Entender estos conceptos es algo esencial en la gran mayoría de lenguajes)
#  *
#  * DIFICULTAD EXTRA (opcional):
#  * Crea dos programas que reciban dos parámetros (cada uno) definidos como
#  * variables anteriormente.
#  * - Cada programa recibe, en un caso, dos parámetros por valor, y en otro caso, por referencia.
#  *   Estos parámetros los intercambia entre ellos en su interior, los retorna, y su retorno
#  *   se asigna a dos variables diferentes a las originales. A continuación, imprime
#  *   el valor de las variables originales y las nuevas, comprobando que se ha invertido
#  *   su valor en las segundas.
#  *   Comprueba también que se ha conservado el valor original en las primeras.
#  */

#datos por valor

value_a = 100
print(value_a) # mostramos lo que vale a 
value_b = value_a # le asignamos a b el valor de a 
print(value_b) # imprimimos el valor de b
value_a = 200 #cambiamos el valor de a
print(value_a,value_b) # imprimimos y notamos que b sigue valiendo lo mismo que valia a, puesto que le hemos asignado el valor que tenia previamente a 
value_c = 300
#datos por referencia
#son todos aquellos que no son tipos de datos primitivos

list_a = [10,20,30,40,50]
list_b = list_a

print(list_a,list_b)

list_b.append(60)

print(list_a,list_b) #podemos ver que se ha agregado a ambas listas, puesto que como es un dato por referencia, no almacena su valor en un espacio diferente de memoria, si no que lo enlaza a la posicion de memoria que contiene el elemento al que hace referencia

#funciones coon datos por valor

def ints(int1 : int):
    value = 400 # asignamos un valor y almacena en otra posicion de memoria
    print(value)
 
ints(value_c) # cambia
print(value_c) # no cambia

#funciones con referencia

list_c = [100,200,300]

def lists(my_list: list):
    my_list.append(400) # agrega el valor a los dos elementos porque asigna enlaza con la posicion de memoria del primero
    print(my_list)

lists(list_c) # cambia
print(list_c) # cambia

#extra

#por valor

value_d = 100
value_e = 200

def value(value_a : int, value_b = int):
    temp = value_a #almacena el valor de a en una variable nueva
    value_a = value_b #cambia valor
    value_b = temp #cambia valor

    return value_a,value_b

print(value(value_d,value_e))

# por referencia

def ref(list_a = list, list_b = list):

    temp = list_a #almacena la referencia de valor de a
    list_a = list_b #cambia la referencia de a para b
    list_b = temp # cambia la referencia de b para a
    return list_a, list_b

list_d = [100,200]
list_e = [300,400]

print(ref(list_d,list_e))