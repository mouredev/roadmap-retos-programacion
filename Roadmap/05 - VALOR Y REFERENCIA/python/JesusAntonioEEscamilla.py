# #05 - Python -> Jesus Antonio Escamilla

"""
EJERCIÓ
"""
#--Asignación de Variables--
#VALOR
print("Asignación de Variables")
print("Valor")
a = 5
b = a

print("a: ", a)
print("b: ", b)

#REFERENCIA
print("Referencia")
lista1 = [1, 2, 3]
lista2 = lista1

print("lista1: ", lista1)
print("lista2: ", lista2)


lista2.append(4)
print("lista1: ", lista1)
print("lista2: ", lista2)


#--Variables a Funciones--
#VALOR
print("Variables a Funciones")
print("Valor")
def modificar_valor(x):
    x = 10

a = 5
modificar_valor(a)
print(a)

#REFERENCIA
print("Referencia")
def modificar_referencia(lista):
    lista.append(4)

lista1 = [1, 2, 3]
modificar_referencia(lista1)
print(lista1)



"""
EXTRA
"""
#Pendiente