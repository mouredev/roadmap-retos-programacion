#Variable por valor, independientes, simple copia de dato
numero = 20
numero2 = numero

print(numero)
print(numero2)

numero2 = numero2 + 12

print(numero)
print(numero2)

#Variable por refencia, refencia al mismo espacio en memoria, referencia global para todas las variables de referencia

lista = [1,2,3]
lista2 = lista

print(lista)
print(lista2)

lista2.append(4)

print(lista2)
print(lista)


