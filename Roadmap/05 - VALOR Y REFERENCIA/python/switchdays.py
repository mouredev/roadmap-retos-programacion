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
 """


# Asignación por valor para números
x = 10
y = x
y = 20  # Modificar 'y' no afecta a 'x'
print(x)  # Salida: 10
print(y)  # Salida: 20


# Asignación por referencia para listas
lista1 = [1, 2, 3]
lista2 = lista1
lista2.append(4)  # Modificar 'lista2' también modifica 'lista1'
print(lista1)  # Salida: [1, 2, 3, 4]
print(lista2)  # Salida: [1, 2, 3, 4]


def modificar_numero(numero):
    numero = 100

x = 10
modificar_numero(x)
print(x)  # Salida: 10 (sin cambios)


def modificar_lista(lista):
    lista.append(4)

mi_lista = [1, 2, 3]
modificar_lista(mi_lista)
print(mi_lista)  # Salida: [1, 2, 3, 4]


"""
 * DIFICULTAD EXTRA (opcional):
 * Crea dos programas que reciban dos parámetros (cada uno) definidos como variables anteriormente.
 * - Cada programa recibe, en un caso, dos parámetros por valor, y en otro caso, por referencia.
 *   Estos parámetros los intercambia entre ellos en su interior, los retorna, y su retorno
 *   se asigna a dos variables diferentes a las originales. A continuación, imprime el valor de las
 *   variables originales y las nuevas, comprobando que se ha invertido su valor en las segundas.
 *   Comprueba también que se ha conservado el valor original en las primeras.
 """

# Por valor:

num_1_original = 10
num_2_original = 20

def intercambiar_por_valor(num_1, num_2):
    new_var_1 = num_1
    new_var_2 = num_2

    return new_var_1, new_var_2

new_num_1, new_num_2 = intercambiar_por_valor(num_1_original, num_2_original)

print("Los originales son: ", num_1_original, "y ", num_2_original)
print("Los nuevos son: ", new_num_1, "y ", new_num_2)


# Por referencia:

list_1_original = [1, 2, 3, 4]
list_2_original = [10, 20, 30, 40]

def intercambiar_por_referncia(list_1, list_2):
    new_list_1 = list_2
    new_list_2 = list_1

    return new_list_1, new_list_2

new_list_1, new_list_2 = intercambiar_por_referncia(list_1_original, list_2_original)

print("Las originales son: ", list_1_original, "y ", list_2_original)
print("Las nuevos son: ", new_list_1, "y ", new_list_2)