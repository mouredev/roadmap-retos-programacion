entero = 10
cadena = "Hola Mundo"

# Vamos a crear dos variables por valor que tengan los valores de las variables anteriores

entero2 = entero
cadena2 = cadena

print(f'El valor del entero original es {entero} y el valor del entero por valor es {entero2}')
print(f'La cadena original es "{cadena}" y la cadena por valor es "{cadena2}"')

# Vamos a cambiar ahora el valor de las variables originales y vamos a mostrar por pantalla las variables originales y por valor
entero = 20;
cadena = "Adios Mundo"

print(f'El valor del entero original es {entero} y el valor del entero por valor es {entero2}')
print(f'La cadena original es "{cadena}" y la cadena por valor es "{cadena2}"')

# Variables por referencia

lista = [1, 2, 3, 4, 5]
lista2 = lista

print(f'El valor de la lista original es {lista} y el valor de la lista por referencia es {lista2}')

lista[0] = 10
lista[1] = 20
lista[2] = 30

print(f'El valor de la lista original es {lista} y el valor de la lista por referencia es {lista2}')

# Ejemplo de funcion con paso por valor

def duplicar_valor(numero):
    numero = numero * 2
    return numero

numero = 10
print(f'El valor original del numero es {numero}')
numero = duplicar_valor(numero)
print(f'El valor del numero despues de duplicarlo es {numero}')

# Ejemplo de funcion con paso por referencia

def duplicar_valores(lista):
    for i in range(len(lista)):
        lista[i] = lista[i] * 2
    return lista

lista = [1, 2, 3, 4, 5]
print(f'El valor de la lista original es {lista}')
lista = duplicar_valores(lista)
print(f'El valor de la lista despues de duplicar sus valores es {lista}')

# Extra

def byValor(a, b):
    a, b = b, a
    return a, b

x = 10
y = 20

nuevo_x, nuevo_y = byValor(x, y)

print(f"Valores originales: x = {x}, y = {y}")
print(f"Nuevos valores: x = {nuevo_x}, y = {nuevo_y}")

def byReference(lista):
    lista[0], lista[1] = lista[1], lista[0]
    return lista

lista = [10, 20]
print(f"Valores originales (Antes de llamada a función): lista = {lista}")
nueva_lista = byReference(lista)

print(f"Valores originales (Despues de llamada a función): lista = {lista}")
print(f"Nuevos valores (retorno de la función): lista = {nueva_lista}")
