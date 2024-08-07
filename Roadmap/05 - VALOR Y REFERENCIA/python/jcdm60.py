# #05 VALOR Y REFERENCIA
#### Dificultad: Fácil | Publicación: 29/01/24 | Corrección: 05/02/24

## Ejercicio

#
# EJERCICIO:
# - Muestra ejemplos de asignación de variables "por valor" y "por referencia", según
#   su tipo de dato.
# - Muestra ejemplos de funciones con variables que se les pasan "por valor" y 
#   "por referencia", y cómo se comportan en cada caso en el momento de ser modificadas.
# (Entender estos conceptos es algo esencial en la gran mayoría de lenguajes)
#
# DIFICULTAD EXTRA (opcional):
# Crea dos programas que reciban dos parámetros (cada uno) definidos como variables anteriormente.
# - Cada programa recibe, en un caso, dos parámetros por valor, y en otro caso, por referencia.
#   Estos parámetros los intercambia entre ellos en su interior, los retorna, y su retorno
#   se asigna a dos variables diferentes a las originales. A continuación, imprime el valor de las
#   variables originales y las nuevas, comprobando que se ha invertido su valor en las segundas.
#   Comprueba también que se ha conservado el valor original en las primeras.
#


# POR VALOR
# Enteros son inmutables
a = 7
b = a  # Se copia el valor de 'a' en 'b'
b = 12
print(a)  # Salida: 5 (sin cambios)
print(b)  # Salida: 10

# POR REFERENCIA
# Listas son mutables
lista1 = [1, 2, 3]
lista2 = lista1  # Se referencia la misma lista con dos nombres diferentes
lista2.append(4)
print(lista1)  # Salida: [1, 2, 3, 4] (modificada a través de 'lista2')
print(lista2)  # Salida: [1, 2, 3, 4]

# FNCIONES POR VALOR
def modificar_valor(x):
    x = x + 5

a = 10
modificar_valor(a)
print(a)  # Salida: 10 (sin cambios)

# FUNCIONES POR REFERENCIA
def modificar_lista(lista):
    lista.append(4)

mi_lista = [1, 2, 3]
modificar_lista(mi_lista)
print(mi_lista)  # Salida: [1, 2, 3, 4] (modificada dentro de la función)


# PROGRMAMA 1 - POR VALOR
def intercambiar_por_valor(a, b):
    # Intercambio de valores
    temp = a
    a = b
    b = temp
    return a, b

# Definición de variables
valor1 = 10
valor2 = 20

# Llamada a la función y asignación de los nuevos valores
nuevo_valor1, nuevo_valor2 = intercambiar_por_valor(valor1, valor2)

# Imprimir los resultados
print("Por valor:")
print("Original - Valor1:", valor1, "Valor2:", valor2)
print("Nuevo - Valor1:", nuevo_valor1, "Valor2:", nuevo_valor2)

# POR REFERENCIA
def intercambiar_por_referencia(lista):
    # Intercambio de valores dentro de la lista
    temp = lista[0]
    lista[0] = lista[1]
    lista[1] = temp
    return lista

# Definición de variables
referencia1 = [10]
referencia2 = [20]

# Llamada a la función y asignación de los nuevos valores
nueva_referencia = intercambiar_por_referencia(referencia1 + referencia2)

# Imprimir los resultados
print("\nPor referencia:")
print("Original - Referencia1:", referencia1, "Referencia2:", referencia2)
print("Nuevo - Referencia1:", nueva_referencia[0], "Referencia2:", nueva_referencia[1])
