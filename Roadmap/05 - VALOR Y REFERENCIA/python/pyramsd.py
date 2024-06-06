# cuando asignas una variable a otra variable de un tipo inmutable (como int, float, string, tuple),
# se realiza una asignación por valor
a = 10
b = a  # Se asigna el valor de 'a' a 'b'
a = 30  # Cambiar 'a' no afecta a 'b'
print(a)
print(b)

# En el caso de tipos mutables (como listas, diccionarios), la asignación se realiza por referencia.
# Esto significa que ambas variables apuntan al mismo objeto en la memoria, y los cambios realizados
# en uno afectarán al otro.
lista_a = [4, 5, 6]
lista_b = lista_a

lista_a.append(7)  # Modificar 'lista_a' afecta a 'lista_b'

print(lista_a)
print(lista_b)


# funcion paso por valor
def mod_valor(n):
    n = 10*4
    print(f'El valor dentro de la funcion es {n}')

n = 5
mod_valor(n)
print(f'El valor fuera de la funcion es {n}')


# funcion paso por referencia
def mod_lista(lista):
    lista[0] = 20
    print(f'Dentro de la funcion es {lista}')

lista = [30, 40, 50]
mod_lista(lista)
print(f'Fuera de la funcion es {lista}')


# EXTRA
var1 = 2025
var2 = (30, 'Jorge', 50)
ref1 = [45, 47, 49]
ref2 = {'trabajo': 'Doc. fisica', 'area':'cuantica'}

print(f'Valores originales:\n\tvalor 1: {var1}\n\tvalor 2: {var2}\n\treferencia 1: {ref1}\n\treferencia 2: {ref2}')


def cambioDeValores(var1, var2):
    var1, var2 = var2, var1
    return var1, var2

final_var1, final_var2 = cambioDeValores(var1, var2)
print(f'Valores dentro de la funcion:\n\tvar 1: {final_var1}\n\tvar 2: {final_var2}')
print(f'Valor original de var 1: {var1}\nValor original de var 2: {var2}')


def cambioDeReferencias(ref1, ref2):
    ref1, ref2 = ref2, ref1
    return ref1, ref2

final_ref1, final_ref2 = cambioDeReferencias(ref1, ref2)
print(f'Valores dentro de la funcion:\n\tref 1 : {final_ref1}\n\tref 2: {final_ref2}')
print(f'Valor original de ref 1: {ref1}\nValor original de ref 2: {ref2}')
