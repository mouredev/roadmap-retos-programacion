# Ejercicio 05
# En el siguiente URL https:/python.org Tenemos la documentacion de phyton.
# Los retos se encuentran en https://retosdeprogramacion.com


# Por valor

a = 10
b = a
b += 5

print(a)  # B tiene la misma copia de valor de A pero no hace referencia a su valor A no CAMBIA
print(b)  # Esto significa que no es un valor por referencia sino valor de copia

lista_noref = [1, 2, 3]
lista_noref2 = lista_noref.copy()  # Podemos asignar sin necesidad de referencias haciendo una COPIA

lista_noref2.append(4)
print(lista_noref)


def funcion_sumar(valor):
    valor += 5
    print("Valor adentro", valor)


por_valor = 14
funcion_sumar(por_valor)
print("Valor afuera", por_valor)  # Vemos como en la funcion no se modifica el valor original

# Por referencia


lista_ref = [1, 2, 3]
lista_ref2 = lista_ref  # Asignamos por referencia

lista_ref2.remove(3)
print(lista_ref)  # Estamos cambiando la lista 2 pero el cambio se ve reflejado en la lista 1.


def lista_referencia(lst):  # La funcion modifica el objetio recibido ORIGINAL
    lst.append("Funcion")
    print("dentro", lst)


mi_lista = [1, 2, 3]
lista_referencia(mi_lista)
print("Fuera, ", mi_lista)


# Extra

# Variables

var_ref = 5
var_ref2 = 10
var_fun = 0
var_fun2 = 0

list_ref = [1, 2, 3]
list_ref2 = [1, 2, 3, 4]
list_fun = 0
list_fun2 = 0

# Programa1


def Programa1(var1, var2):
    temp = var1
    var1 = var2
    var2 = temp
    return (var1, var2)


var_fun, var_fun2 = Programa1(var_ref, var_ref2)
print(f"Valor Original {var_ref}, {var_ref2}")
print(f"Valor Funcion {var_fun}, {var_fun2} \n")

# Programa2


def Programa2(var3, var4):
    temp = var3
    var3 = var4
    var4 = temp
    return (var3, var4)


list_fun, list_fun2 = Programa2(list_ref, list_ref2)
print(f"Referencia Original {list_ref}, {list_ref2}")
print(f"Referencia Funcion {list_fun}, {list_fun2}")
