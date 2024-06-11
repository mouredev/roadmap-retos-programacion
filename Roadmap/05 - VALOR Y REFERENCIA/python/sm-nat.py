#ASIGNACIÓN DE VARIABLES

#Asignación por Valor (Inmutables: Enteros, flotantes, cadenas de texto, tuplas.)
# Asignación por valor
a = 10
b = a  # 'b' recibe el valor de 'a'
print("Antes de cambiar a:")
print(f"a = {a}, b = {b}")

a = 20  # Cambiamos el valor de 'a'
print("Después de cambiar a:")
print(f"a = {a}, b = {b}")  # 'b' no se ve afectado

#Asignación por Referencia (Mutables: Listas, diccionarios, conjuntos)
lista1 = [1, 2, 3]
lista2 = lista1  
print("Antes de cambiar lista1:")
print(f"lista1 = {lista1}, lista2 = {lista2}")

lista1.append(4)  
print("Después de cambiar lista1:")
print(f"lista1 = {lista1}, lista2 = {lista2}")  

print("ejemplo con funciones inmutables")
def modificar_valor(x):
    print(f"Valor inicial dentro de la función: {x}")
    x += 10
    print(f"Valor modificado dentro de la función: {x}")

a = 5
print(f"Valor antes de la función: {a}")
modificar_valor(a)
print(f"Valor después de la función: {a}")

print("ejemplo con funciones mutables")
def modificar_lista(lista):
    print(f"Lista inicial dentro de la función: {lista}")
    lista.append(4)
    print(f"Lista modificada dentro de la función: {lista}")

mi_lista = [1, 2, 3]
print(f"Lista antes de la función: {mi_lista}")
modificar_lista(mi_lista)
print(f"Lista después de la función: {mi_lista}")

#EXTRA
"""Crea dos programas que reciban dos parámetros (cada uno) definidos como variables anteriormente.
Cada programa recibe, en un caso, dos parámetros por valor, y en otro caso, por referencia.
Estos parámetros los intercambia entre ellos en su interior, los retorna, y su retorno
se asigna a dos variables diferentes a las originales. A continuación, imprime el valor de las
variables originales y las nuevas, comprobando que se ha invertido su valor en las segundas.
Comprueba también que se ha conservado el valor original en las primeras."""

#por valor
def intercambio_por_valor(a,b):
    c = a
    a = b
    b = c
    return a,b
x = 1
y = 3
nuevo_x, nuevo_y = intercambio_por_valor(x,y)
print(f"originales: x = {x}, y = {y}")
print(f"intercambiados: nuevo x = {nuevo_x}, nuevo y = {nuevo_y}")