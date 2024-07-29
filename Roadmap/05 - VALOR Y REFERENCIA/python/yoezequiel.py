# Asignación por valor
x = 10
y = x  # Se copia el valor de x en y
y = 20  # Cambiamos el valor de y
print(x)  # Imprime 10, el valor original de x no se ve afectado
# Asignación por referencia
lista1 = [1, 2, 3]
lista2 = lista1  # Ambas variables apuntan a la misma lista en memoria
lista2.append(4)  # Modificamos lista2
print(lista1)  # Imprime [1, 2, 3, 4], la lista original se ve afectada


def modificar_valor(num):
    num += 10  # Se modifica el valor de la variable local num
    print("Dentro de la función:", num)


x = 5
modificar_valor(x)
print("Fuera de la función:", x)  # Imprime 5, el valor original de x no se ve afectado


def modificar_lista(lista):
    lista.append(4)  # Modifica la lista pasada como parámetro
    print("Dentro de la función:", lista)


mi_lista = [1, 2, 3]
modificar_lista(mi_lista)
print(
    "Fuera de la función:", mi_lista
)  # Imprime [1, 2, 3, 4], la lista original se ve afectada


def intercambiar_valores_por_valor(a, b):
    temp = a
    a = b
    b = temp
    return a, b


x = 10
y = 20

x, y = intercambiar_valores_por_valor(x, y)

# Imprimimos los valores originales y los nuevos
print("Valores originales:")
print("x =", x)
print("y =", y)


def intercambiar_valores_por_referencia(lista):
    # Intercambiamos los valores de la lista
    lista[0], lista[1] = lista[1], lista[0]
    return lista


mi_lista = [10, 20]

nueva_lista = intercambiar_valores_por_referencia(mi_lista[:])

print("Valores originales:")
print("mi_lista =", mi_lista)
print("nueva_lista =", nueva_lista)
