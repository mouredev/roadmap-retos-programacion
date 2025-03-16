# Variables por valor
a = 15.8
b = 23.3
print (a)
print(b)
a = b
b = 3.33
print(a)
print(b)

#Variables por referencia
c = [1,2,3]
d = [4,5,6]
print(c)
print(d)
c = d
d.append(1)
print(c)
print(d)


##Funciones con variables por valor
def float_func(my_float: float):
    my_float = 15.3
    print(my_float)


e = 10.2
float_func(e)
print(e)

##Funciones con variables por referencia

def lista_func(mi_lista: list):
    mi_lista.append('c')

    mi_lista_d = mi_lista
    mi_lista.append('d')

    print(mi_lista)
    print(mi_lista_d)


mi_lista_c = ['a','b']
lista_func(mi_lista_c)
print(mi_lista_c)

##Dificultad extra
# Por valor
def valor(var_a, var_b):
    aux = var_a
    var_a = var_b
    var_b = aux
    return var_a, var_b

var_a = 15
var_b = 25
var_a, var_b = valor(var_a,var_b)
print(var_a)
print(var_b)

#Por referencia

def referencia(list_a, list_b):
    aux = list_a
    list_a = list_b
    list_b = aux
    return list_a, list_b

lista_a = [1,2]
lista_b = [3,4]

lista_a, lista_b = referencia(lista_a, lista_b)
print(lista_a)
print(lista_b)
