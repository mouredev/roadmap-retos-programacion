# ============================================
# ASIGNACIÓN DE VARIABLES
# ============================================

print("===== ASIGNACIÓN DE VARIABLES =====")

# Inmutables (por valor)
a = 10
b = a
b += 5
print("Inmutables:")
print(f"a = {a}, b = {b} (modificar b no afecta a a)")

# Mutables (por referencia)
lista1 = [1, 2, 3]
lista2 = lista1
lista2.append(4)
print("\nMutables:")
print(f"lista1 = {lista1}, lista2 = {lista2} (ambas apuntan al mismo objeto)")

# Para evitar eso: usar copia
import copy
lista3 = copy.deepcopy(lista1)
lista3.append(99)
print(f"lista1 = {lista1}, lista3 (copiada) = {lista3}")


# ============================================
# FUNCIONES CON VARIABLES INMUTABLES Y MUTABLES
# ============================================

print("\n===== PASO DE VARIABLES A FUNCIONES =====")

# Inmutable (int)
def modificar_entero(x):
    x += 1
    print("Dentro de la función (int):", x)

n = 5
modificar_entero(n)
print("Fuera de la función (int):", n)

# Mutable (lista)
def modificar_lista(lst):
    lst.append(99)
    print("Dentro de la función (lista):", lst)

mi_lista = [1, 2, 3]
modificar_lista(mi_lista)
print("Fuera de la función (lista):", mi_lista)


# ============================================
# DIFICULTAD EXTRA: INTERCAMBIO DE VARIABLES
# ============================================

print("\n===== DIFICULTAD EXTRA =====")

# Intercambio por valor (inmutables)
def intercambiar_valores(x, y):
    x, y = y, x
    return x, y

# Intercambio por referencia (mutables)
def intercambiar_listas(l1, l2):
    l1[:], l2[:] = l2[:], l1[:]
    return l1, l2

# Variables originales
valor1 = 100
valor2 = 200
lista1 = [1, 2]
lista2 = [3, 4]

# Llamadas
nuevo_valor1, nuevo_valor2 = intercambiar_valores(valor1, valor2)
nueva_lista1, nueva_lista2 = intercambiar_listas(lista1.copy(), lista2.copy())  # Usamos copia para preservar las originales

print(">>> Intercambio por valor (enteros)")
print("Originales: valor1 =", valor1, ", valor2 =", valor2)
print("Nuevas:     nuevo_valor1 =", nuevo_valor1, ", nuevo_valor2 =", nuevo_valor2)

print("\n>>> Intercambio por referencia (listas con copia)")
print("Originales: lista1 =", lista1, ", lista2 =", lista2)
print("Nuevas:     nueva_lista1 =", nueva_lista1, ", nueva_lista2 =", nueva_lista2)