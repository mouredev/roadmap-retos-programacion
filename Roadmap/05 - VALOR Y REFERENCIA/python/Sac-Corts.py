"""
 EJERCICIO
"""

a = 10
b = a
b += 5 
print(a) # Salida: 10
print(b) # Salida: 15


lista1 = [1, 2, 3]
lista2 = lista1
lista2.append(4)
print(lista1)  # Salida: [1, 2, 3, 4]
print(lista2)  # Salida: [1, 2, 3, 4]


### Funciones con Variables Pasadas "por Valor" y "por Referencia" ###
# Pasar por valor
# Ejemplo con tipo inmutable:
def incrementar_valor(x):
    x += 1
    print("Dentro de la función:", x)

a = 5
incrementar_valor(a)
print("Fuera de la función:", a)

# Pasar por referencia
# Ejemplo con tipo mutable:
def agregar_elemento(lista):
    lista.append(4)
    print("Dentro de la función:", lista)

mi_lista = [1, 2, 3]
agregar_elemento(mi_lista)
print("Fuera de la función:", mi_lista)

"""
 DIFICULTAD EXTRA
"""

### Intercambio de parámetros por valor ###
def intercambiar_valores_por_valor(x, y):
    temp = x
    x = y
    y = temp
    return x, y

a = 5
b = 10

nuevo_a, nuevo_b = intercambiar_valores_por_valor(a, b)

print("Valores originales:")
print("a =", a)
print("b =", b)

print("Valores intercambiados:")
print("nuevo_a =", nuevo_a)
print("nuevo_b =", nuevo_b)


### Intercambio de parámetros por referencia ###

def intercambiar_valores_por_referencia(lista):
    temp = lista[0]
    lista[0] = lista[1]
    lista[1] = temp

c = [5]
d = [10]

parametros = [c, d]

intercambiar_valores_por_referencia(parametros)

nuevo_c = parametros[0]
nuevo_d = parametros[1]

print("Valores originales:")
print("c =", c[0])
print("d =", d[0])

print("Valores intercambiados:")
print("nuevo_c =", nuevo_c[0])
print("nuevo_d =", nuevo_d[0])
