# Por valor

num = 10
new_num = num       # new_num recibe una copia del valor de num

new_num = 20        # Cambiamos el valor de new_num
print(num)          # num sigue siendo 10
print(new_num)      # new_num es 20


# Por referencia

list_a = [1, 2, 3]
list_b = list_a     # lista_b referencia a la misma lista que list_a

list_b.append(4)    # Modificamos la lista a través de lista_b

print(list_a)       # lista_a también muestra el cambio [1, 2, 3, 4]
print(list_b)       # lista_b muestra el cambio [1, 2, 3, 4]


# FUNCIONES:

# VALOR
def function_valor(x):
    x = 20                  
    print(f"valor dentro de la funcion: {x}")

x = 10
function_valor(x)
print(f"Fuera de la función: a = {x}")
# Salida:
# Dentro de la función: x = 20
# Fuera de la función: x = 10


# REFERENCIA
def function_referencia(lista_a):
    lista_a.append(4)   # Modificamos la lista

lista_b = [1, 2, 3]
function_referencia(lista_b)
print(lista_b)
# Salida:
# Dentro de la función: lista = [1, 2, 3] + 4
# Fuera de la función:  lista = [1, 2, 3, 4]




#  * DIFICULTAD EXTRA (opcional):
#  * Crea dos programas que reciban dos parámetros (cada uno) definidos como
#  * variables anteriormente.
#  * - Cada programa recibe, en un caso, dos parámetros por valor, y en otro caso, por referencia.
#  *   Estos parámetros los intercambia entre ellos en su interior, los retorna, y su retorno
def exercise(a, b):
    a, b = b, a
    return a , b

#  *   se asigna a dos variables diferentes a las originales. A continuación, imprime
a = 1
b = 2
c, d = exercise(a, b)


#  *   el valor de las variables originales y las nuevas, comprobando que se ha invertido
#  *   su valor en las segundas.
#  *   Comprueba también que se ha conservado el valor original en las primeras.

print(f"{a} ahora sera {c}")
print(f"{b} ahora sera {d}")
#  */

