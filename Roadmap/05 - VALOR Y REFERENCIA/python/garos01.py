# Ejemplo con enteros paso por valor
x = 5
y = x
x = 10

print(y)

# Ejemplo con listas paso por referencia
lista1 = [1, 2, 3]
lista2 = lista1
lista1.append(4)

print(lista2)


# Ejemplo de funciones por valor
def modificar_valor(numero):
    numero = 10


x = 5
modificar_valor(x)
print(x)


# Ejemplo de funciones por referencia
def modificar_lista(lista):
    lista.append(4)


mi_lista = [1, 2, 3]
modificar_lista(mi_lista)
print(mi_lista)
