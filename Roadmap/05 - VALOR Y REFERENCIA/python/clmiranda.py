# VALOR Y REFERENCIA

# ASIGNACIÓN DE VARIABLES POR VALOR
v1 = 150
v2 = v1
v1 = 100
print(f"Valor de v1: {v1}")
print(f"Valor de v2: {v2}")


# ASIGNACIÓN DE VARIABLES POR REFERENCIA
lst1 = [14, 19, 7, 36]
lst2 = lst1
lst1.extend([28, 95])
print(f"Valor de v1: {lst1}")
print(f"Valor de v2: {lst2}")


# FUNCIONES CON VARIABLES QUE SE LES PASAN POR VALOR
valor = 123

def por_valor(val):
    val = 456
    return val

print(f"Valor retornado por la función: {por_valor(valor)}")
print(f"Valor de la variable local: {valor}")



# FUNCIONES CON VARIABLES QUE SE LES PASAN POR REFERENCIA
def por_referencia(lst):
    lst.sort(reverse=True)
    return lst

lst3 = [17, 45, 12, 60, 34]
print(f"Lista retornada por la función: {por_referencia(lst3)}")
print(f"Valor de la lista local: {lst3}")



# EJERCICIO - DIFICULTAD EXTRA

# PARÁMETROS PASADOS POR VALOR
def by_value(a, b):
    changeable = a
    a = b
    b = changeable
    return a, b

val_a, val_b = 100, 200
val_c, val_d = by_value(val_a, val_b)

print(f"Valores originales: {val_a}, {val_b}")
print(f"Valores intercambiados: {val_c}, {val_d}")



# PARÁMETROS PASADOS POR REFERENCIA
def by_reference(a, b):
    changeable = a
    a = b
    b = changeable
    return a, b

list_a = [1, 2, 3]
list_b = [4, 5, 6]
list_c, list_d = by_reference(list_a, list_b)

print(f"Valores originales: {list_a}, {list_b}")
print(f"Valores originales: {list_c}, {list_d}")
