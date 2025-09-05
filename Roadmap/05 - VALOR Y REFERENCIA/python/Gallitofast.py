#<><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>
#<><><><><><><><><><><><><><><>-------Valor y referencia-------<><><><><><><><><><><><><><><><><><><><><><><><><>
#<><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>
# ------------------------------------------
# Parte 1: Asignación por valor y por referencia
# ------------------------------------------

print("\n--- Parte 1: Asignación por valor y por referencia ---")

# Asignación por valor (tipos inmutables: int, float, str, tuple)
print("\nAsignación por valor (tipos inmutables):")
a = 10
b = a  # b recibe una copia del valor de a
print(f"Antes: a = {a}, b = {b}")
b = 20  # Modificamos b
print(f"Después: a = {a}, b = {b}")  # a no cambia

# Asignación por referencia (tipos mutables: list, dict, set)
print("\nAsignación por referencia (tipos mutables):")
lista_original = [1, 2, 3]
lista_copia = lista_original  # Ambas variables apuntan al mismo objeto
print(f"Antes: original = {lista_original}, copia = {lista_copia}")
lista_copia.append(4)  # Modificamos la "copia"
print(f"Después: original = {lista_original}, copia = {lista_copia}")  # Ambas cambian

# ------------------------------------------
# Parte 2: Funciones con parámetros por valor y referencia
# ------------------------------------------

print("\n--- Parte 2: Comportamiento en funciones ---")

def modificar_parametro_valor(x):
    print(f"Dentro (antes): x = {x}")
    x = 100  # Esto no afectará al original si es inmutable
    print(f"Dentro (después): x = {x}")

def modificar_parametro_referencia(lst):
    print(f"Dentro (antes): lst = {lst}")
    lst.append(99)  # Esto modificará el objeto original
    print(f"Dentro (después): lst = {lst}")

# Prueba con tipo inmutable (por valor)
print("\nFUNCIÓN CON PARÁMETRO POR VALOR (int):")
valor = 5
print(f"Antes de función: valor = {valor}")
modificar_parametro_valor(valor)
print(f"Después de función: valor = {valor}")

# Prueba con tipo mutable (por referencia)
print("\nFUNCIÓN CON PARÁMETRO POR REFERENCIA (list):")
lista = [1, 2, 3]
print(f"Antes de función: lista = {lista}")
modificar_parametro_referencia(lista)
print(f"Después de función: lista = {lista}")

# ------------------------------------------
# Parte 3: Dificultad EXTRA - Intercambio de valores
# ------------------------------------------

print("\n--- Parte 3: Dificultad EXTRA ---")

# Función que intercambia parámetros por valor
def intercambiar_por_valor(a, b):
    print(f"Dentro (antes): a = {a}, b = {b}")
    temp = a
    a = b
    b = temp
    print(f"Dentro (después): a = {a}, b = {b}")
    return a, b

# Función que intercambia parámetros por referencia
def intercambiar_por_referencia(lista1, lista2):
    print(f"Dentro (antes): lista1 = {lista1}, lista2 = {lista2}")
    temp = lista1.copy()
    lista1.clear()
    lista1.extend(lista2)
    lista2.clear()
    lista2.extend(temp)
    print(f"Dentro (después): lista1 = {lista1}, lista2 = {lista2}")
    return lista1, lista2

# Prueba con intercambio por valor
print("\nINTERCAMBIO POR VALOR (int):")
x, y = 10, 20
print(f"Originales antes: x = {x}, y = {y}")
nuevo_x, nuevo_y = intercambiar_por_valor(x, y)
print(f"Originales después: x = {x}, y = {y}")
print(f"Nuevas variables: nuevo_x = {nuevo_x}, nuevo_y = {nuevo_y}")

# Prueba con intercambio por referencia
print("\nINTERCAMBIO POR REFERENCIA (list):")
lista_a = [1, 2, 3]
lista_b = [4, 5, 6]
print(f"Originales antes: lista_a = {lista_a}, lista_b = {lista_b}")
nueva_lista_a, nueva_lista_b = intercambiar_por_referencia(lista_a, lista_b)
print(f"Originales después: lista_a = {lista_a}, lista_b = {lista_b}")
print(f"Nuevas variables: nueva_lista_a = {nueva_lista_a}, nueva_lista_b = {nueva_lista_b}")