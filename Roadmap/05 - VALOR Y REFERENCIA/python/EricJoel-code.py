## Valor y Referencia

# Paso por valor es cuando se pasa una copia del valor de la variable a la función, y cualquier cambio hecho a ese valor dentro de la función no afecta la variable original fuera de la función.

# Paso por referencia es cuando se pasa una referencia (o dirección) de la variable a la función, y cualquier cambio hecho a la variable dentro de la función afecta la variable original fuera de la función.

# Tipos de datos por valor

mi_entero = 10
mi_entero2 = mi_entero
#mi_entero2 = 20
mi_entero = 30
print(mi_entero) 
print(mi_entero2)

# Tipos de datos por referencia

mi_lista = [1, 2, 3]
mi_lista2 = [4, 5, 6]
mi_lista2 = mi_lista
mi_lista.append(4)
print(mi_lista)
print(mi_lista2)

# Funciones y paso por valor

entero = 5

def modificar_valor(x:int):
    x = 10
    print("Dentro de la función (valor):", x)
    
modificar_valor(entero)
print("Fuera de la función (valor):", entero)

# Funciones y paso por referencia

lista = [1, 2]

def modificar_lista(lst:list):
    lst.append(3)
    
    lista2 = lst
    lista2.append(4)
    
    print("Dentro de la función (referencia):", lst) 
    print("Dentro de la función (referencia):", lista2)
    
modificar_lista(lista)
print("Fuerad e la funcion (referencia):", lista)


## Extra

# Por valor 

my_int = 10
my_int2 = 20

def intercambiar_valores(a:int, b:int):
    temp = a
    a = b
    b = temp
    return a, b

my_int3, my_int4 = intercambiar_valores(my_int, my_int2)
print(f"Las variables originales son: my_int = {my_int}, my_int2 = {my_int2}")
print(f"Las nuevas variables son: my_int3 = {my_int3}, my_int4 = {my_int4}")

# Por referencia

my_list = [10, 20]
my_list2 = [30, 40]

def intercambiar_listas(lst1:list, lst2:list):
    temp = lst1
    lst1 = lst2
    lst2 = temp
    return lst1, lst2

my_list3, my_list4 = intercambiar_listas(my_list, my_list2)
print(f"Las variables originales son: my_list = {my_list}, my_list2 = {my_list2}")
print(f"Las nuevas variables son: my_list3 = {my_list3}, my_list4 = {my_list4}")

#Lo mas conveniente seria usar tipos de datos inmutables (por valor) para evitar efectos secundarios no deseados, o realizar una copia de los datos mutables (por referencia) antes de pasarlos a una función si no se desea modificar el original.

# Por referencia con copia de datos

import copy

my_list5 = [50, 60]
my_list6 = [70, 80]

def intercambiar_listas_con_copia(lst1:list, lst2:list):
    lst1_copy = copy.deepcopy(lst1)
    lst2_copy = copy.deepcopy(lst2)
    temp = lst1_copy
    lst1_copy = lst2_copy
    lst2_copy = temp
    return lst1_copy, lst2_copy

my_list7, my_list8 = intercambiar_listas_con_copia(my_list5, my_list6)
print(f"Las variables originales son: my_list5 = {my_list5}, my_list6 = {my_list6}")
print(f"Las nuevas variables son: my_list7 = {my_list7}, my_list8 = {my_list8}")

""" La diferencia entre la funcion intercambiar_listas y la funcion intercambiar_listas_con_copia es que la primera función trabaja directamente con las referencias a las listas. Al reasignar estas referencias dentro de la función, no estás modificando las listas originales en sí mismas, sino el enlace a dónde apuntan las variables locales. El resultado es que my_list y my_list2 permanecen sin cambios, y las nuevas variables my_list3 y my_list4 reciben las referencias a las listas intercambiadas. En cambio, la segunda función crea copias profundas de las listas originales usando copy.deepcopy(). Esto significa que cualquier modificación realizada dentro de la función no afecta a las listas originales. Al intercambiar las copias, las listas originales my_list5 y my_list6 permanecen intactas, y las nuevas variables my_list7 y my_list8 reciben las referencias a las copias intercambiadas. """