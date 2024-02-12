# Ejemplos de asignación de variables por valor y por referencia

"""Asignación de variables por valor en una función, 
se genera una copia del valor original
esto permite que no se modifique el valor de la variable ejemplo:"""
x = 10


def funcion_valor(v1):
    v1 = 0


funcion_valor(x)
print(x)

# Asignación por valor tipos inmutables
a = 5
b = a  # se copia el valor e a
b = 10  # Esto no afecta el valor de a

print(a)
print(b)

# paso por referencia
numero = [10, 20, 30]


def duplicar(numeros):
    for i, numero in enumerate(numeros):
        numeros[i] *= 2


print(f"Lista antes de paso por referencia {numero}")
duplicar(numero)
print(f"Lista despues de pasar por referencia {numero}")


# paso por parametro
def multiplicar_valor(valor):
    valor *= 2
    return valor


x = 6
multiplicado = multiplicar_valor(x)
print(f"Valor original {x}")
print(f"Valor multimplicado {multiplicado}")


""" Aqui la dificultad extra de este ejercicio """


def cambio_por_valor(val1, val2):
    tmp = val1
    val1 = val2
    val2 = tmp
    return val1, val2


x = 3
y = 5
x1, y1 = cambio_por_valor(x, y)
print(f"Variables originales {x}, {y}")
print(f"Variables nuevas {x1}, {y1}")


def cambio_por_refer(list1, list2):
    new_list1 = list2
    new_list2 = list1

    return new_list1, new_list2


list1 = [23, 45, 54]
list2 = [45, 56.45]

new_list1, new_list2 = cambio_por_refer(list1, list2)

print("Las listas originales son: ", list1, "y ", list2)
print("Las listas nuevas son: ", new_list1, "y ", new_list2)
