
#  EJERCICIO:
#  - Muestra ejemplos de asignación de variables "por valor" y "por referencia", según
#    su tipo de dato.
#  - Muestra ejemplos de funciones con variables que se les pasan "por valor" y 
#    "por referencia", y cómo se comportan en cada caso en el momento de ser modificadas.
#  (Entender estos conceptos es algo esencial en la gran mayoría de lenguajes)

#  DIFICULTAD EXTRA (opcional):
#  Crea dos programas que reciban dos parámetros (cada uno) definidos como variables anteriormente.
#  - Cada programa recibe, en un caso, dos parámetros por valor, y en otro caso, por referencia.
#    Estos parámetros los intercambia entre ellos en su interior, los retorna, y su retorno
#    se asigna a dos variables diferentes a las originales. A continuación, imprime el valor de las
#    variables originales y las nuevas, comprobando que se ha invertido su valor en las segundas.
#    Comprueba también que se ha conservado el valor original en las primeras.


#valor y referencia

#tipos de datos por valor -> en python todos los tipos de datos primitivos

my_int_a = 10
my_int_b = 20
print(my_int_a)
print(my_int_b)


my_int_b = my_int_a # le asignamos el valor con el momento exacto cuando la asignamos
my_int_a = 30
print(my_int_a)
print(my_int_b)

#tipos de datos por referencia -> en python todos aquellos que no son de tipo primitivo listas, diccionarios, tuplas, etc

my_list_a = [10, 20]
my_list_b = [30, 40]

print (my_list_a)
print(my_list_b)

my_list_b = my_list_a #aqui no asignamos valor aputamos la posicion de memoria, sigue siendo dos variables pero apuntan al mismo espacion de memoria.
print("se observa que son la misma lista con my_list_a = my_list_b")
print (my_list_a)
print(my_list_b)


my_list_b.append(30)
print("---aqui ya hemos hecho un append a my_list_b unicamente pero afeta en memoria la lista para las dos vars")
print (my_list_a)
print(my_list_b)


#funciones con datos por valor

print("---funcion var---")
def my_int_func(my_int: int):
    print("valor recibido por la funcion")
    print(my_int)
    my_int = 20
    print("Cambiamos el valor recibido dentro de la funcion")
    print(my_int)

my_int_c = 10

my_int_func(my_int_c)
print("variable inicial despues de pasar la func")
print(my_int_c) #no cambia porque son independientes, la que se untiliza en la fucnion ocupo el valor mas no la referencia de memoria.

#funcion con datos de referencia
print("---funcion list---")
my_list_c = [10, 20]
print("lista original declarada (my_list_c):")
print(my_list_c)

def my_list_fun(mylist: list):#basicamente esto es un puntero
    my_list_d = mylist.copy()
    print("copiamos mylist a my_list_d")
    print(my_list_d)
    mylist.append(30)
    print("ejecucion del append en var mylist en la func: ")
    print(mylist)
    print("my_list_d no sufrio cambio porque se creo una referencia nueva con el copy")
    print(my_list_d)


my_list_fun(my_list_c)
print("Lista original despues de la funcion: ")
print(my_list_c) #aqui ya podemos observar el cambio de la variable original porque al pasarla a la funcion copia la referencia de memoria.


#extra

#por valor

var_a = 10
var_b = 20

def intercambio(a:int, b:int) -> tuple:
    temp = a
    a = b
    b = temp
    return a, b

var_c, var_d = intercambio(var_a, var_b)

print(f"var a: {var_a}, var b: {var_b}")
print(f"var c: {var_c}, var d: {var_d}")

# por referencia

list_a = [10, 20]
list_b = [30, 40]

def intercambio(a_list: list, b_list: list) -> tuple:
    temp = a_list #guardamos el puntero de 'a' temporalmente
    a_list = b_list #el puntero de 'b' es ahora asignado 'a'
    b_list = temp#el puntero de la lista 'a' que guardamos temporalmente se asigna a 'b'
    a_list.append(50)
    return a_list, b_list



list_c, list_d = intercambio(list_a, list_b)
#esto funciona porque estamos iniciando con dos punteros distintos a y b dentro de la logica de la funcion se copian estos sin mezclarse
print(f"list a: {list_a}, list b: {list_b}")
print(f"list c: {list_c}, list d: {list_d}")

list_d.append(70)

print(f"list a: {list_a}, list b: {list_b}")
print(f"list c: {list_c}, list d: {list_d}")
