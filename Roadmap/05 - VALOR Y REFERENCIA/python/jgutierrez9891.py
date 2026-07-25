"""
Asignación de variables por valor
"""

def triplicar_valor(valor):
    valor *= 3
    return valor

n1 = 10
n2 = 99
n2 = n1                     # Se asigna a n2 el valor de n1 en el momento
n1 = triplicar_valor(n1)
print(n1)
print(n2)                   # Mantiene el valor que tenía n1 al momento de la asignación 


"""
Asignación de variables por referencia
"""

def cuadrado_lista(valor):
    for i in valor:
        valor[i-1] **=2 

lista1 = [1, 2, 3, 4, 5]
lista2 = [0, 0, 0, 0, 0]
lista2 = lista1             # Se asigna a lista2 lo posición de memoria de lista1
cuadrado_lista(lista1)
print(lista1)
print(lista2)               # Se actualizó con el nuevo valor de lista1 porque apuntan a la misma posición de memoria

"""
Extra
"""

def fun_valor(var1, var2):
    aux = var1
    var1 = var2
    var1 = aux
    return var1, var2

def fun_param(lis1, lis2):
    aux = []
    aux = lis1
    lis1 = lis2
    lis2 = aux
    return lis1, lis2


original_val1 = 10
original_val2 = 20
print(f"var1 original es:{original_val1} y var2 original es:{original_val2}")

nueva_val1, nueva_val2 = fun_valor(original_val1 , original_val2)
print(f"var1 ahora es:{nueva_val1} y var2 ahora es:{nueva_val2}")


original_lis1_ref = [10,20,30,40,50]
original_lis2_ref = [15,25,35,45,55]
print(f"lista 1 original es:{original_lis1_ref} y lista 2 original es:{original_lis2_ref}")

nueva_lis1_ref, nueva_lis2_ref = fun_param(original_lis1_ref , original_lis2_ref)
print(f"lista 1 ahora es:{nueva_lis1_ref} y lista 2 ahora es:{nueva_lis2_ref}")