"""
* EJERCICIO:
* - Muestra ejemplos de asignación de variables "por valor" y "por referencia", según
*   su tipo de dato.
* - Muestra ejemplos de funciones con variables que se les pasan "por valor" y 
*   "por referencia", y cómo se comportan en cada caso en el momento de ser modificadas.
* (Entender estos conceptos es algo esencial en la gran mayoría de lenguajes)
*
* DIFICULTAD EXTRA (opcional):
* Crea dos programas que reciban dos parámetros (cada uno) definidos como variables anteriormente.
* - Cada programa recibe, en un caso, dos parámetros por valor, y en otro caso, por referencia.
*   Estos parámetros los intercambia entre ellos en su interior, los retorna, y su retorno
*   se asigna a dos variables diferentes a las originales. A continuación, imprime el valor de las
*   variables originales y las nuevas, comprobando que se ha invertido su valor en las segundas.
*   Comprueba también que se ha conservado el valor original en las primeras.
*
"""


###########################  Asignacion por Valor  ###############################

# Tipos de datos inmutables(por ejemplo, enteros, flotantes, cadenas, tuplas):

# Asignación por valor para enteros
x = 5
y = x
y = 10
print(x)  # Salida: 5

# Asignación por valor para flotantes
x = 3.5
y = x
y = 5.6
print(x)  # Salida: 3.5

# Asignación por valor para cadenas
cadena_1 = "Hola"
cadena_2 = cadena_1
cadena_2 = "Hola Mundo"
print(cadena_1)  # Salida: Hola

# Asignación por valor para tuplas
tupla_1 = (1, 2, 3)
tupla_2 = tupla_1
tupla_2 = (4, 5, 6)
print(tupla_1)  # Salida: (1, 2, 3)


#############################  Asignación por Referencia  ###########################

# Tipos de datos mutables (por ejemplo, listas, diccionarios, conjuntos):

# Asignación por referencia para listas
lista_1 = [1, 2, 3]
lista_2 = lista_1
lista_2.append(4)
print(lista_1)  # Salida: [1, 2, 3, 4]

# Asignación por referencia para diccionarios
diccionario_1 = {'a': 1, 'b': 2}
diccionario_2 = diccionario_1
diccionario_2['c'] = 3
print(diccionario_1) # Salida: {'a': 1, 'b': 2, 'c': 3}

# Asignación por referencia para conjuntos (set)
conjunto_1 = {1, 2, 3}
conjunto_2 = conjunto_1
conjunto_2.add(4)
print(conjunto_1)  # Salida: {1, 2, 3, 4}

"""
              Funciones Paso por valor

Cuando se pasa una variable inmutable (como enteros, flotantes, cadenas, tuplas) a una función en Python, 
se pasa por valor. Esto significa que se crea una copia local de la variable dentro de la función, 
y cualquier modificación realizada dentro de la función no afectará a la variable original fuera de la función
"""

def modificar_valor(num):
    num += 10
    print("Dentro de la función:", num)

x = 5
modificar_valor(x)
print("Fuera de la función:", x)  # Salida: Fuera de la función: 5


"""
             Funciones Paso por Referencia 

Cuando se pasa una variable mutable (como listas, diccionarios, conjuntos) a una función en Python, 
se pasa por referencia. Esto significa que la función opera directamente sobre la misma variable en memoria, 
y cualquier modificación realizada dentro de la función afectará a la variable original fuera de la función
"""

def change_list(lista):
    lista.append(5)
    print("Dentro de la función:", lista)

mi_lista = [1, 2, 3, 4]
change_list(mi_lista)
print("Fuera de la función:", mi_lista)  # Salida: Fuera de la función: [1, 2, 3, 4, 5]

print("\n")



"""
######------------------ Dificultad Extra------------------------ ##########
"""

print("Funcion con Parametros por valor")

def value_exchange(a, b):
    # Intercambio de valores sin usar una variable temporal
    a, b = b, a
    return a, b

x = 5
y = 10

print("Antes del intercambio:")
print("x =", x)
print("y =", y)

x, y = value_exchange(x, y)

print("Después del intercambio:")
print("x =", x)
print("y =", y)

print("\n")
print("Funcion con Parametros por Referencia")

def reference_exchange(lista1, lista2):
    # Verificar que ambas listas tengan exactamente tres elementos
    if len(lista1) == len(lista2) == 3:
        # Intercambiar los valores de las listas usando una lista temporal
        lista_temporal = lista1[:]
        lista1[:] = lista2
        lista2[:] = lista_temporal
    else:
        raise ValueError("Ambas listas deben tener exactamente tres elementos.")

lista_a = [1, 2, 3]
lista_b = [4, 5, 6]

# Imprimir valores originales
print("Valores originales:")
print("lista_a =", lista_a)
print("lista_b =", lista_b)

# Intercambiar valores de las listas
reference_exchange(lista_a, lista_b)

# Imprimir nuevos valores
print("\nNuevos valores:")
print("lista_a =", lista_a)
print("lista_b =", lista_b)








