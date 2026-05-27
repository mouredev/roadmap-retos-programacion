
"""
/*
 * EJERCICIO:
 * - Muestra ejemplos de asignación de variables "por valor" y "por referencia", según
 *   su tipo de dato.
 * - Muestra ejemplos de funciones con variables que se les pasan "por valor" y 
 *   "por referencia", y cómo se comportan en cada caso en el momento de ser modificadas.
 * (Entender estos conceptos es algo esencial en la gran mayoría de lenguajes)
 */
"""

# Tipos de datos por valor
# int, float, bool, str, tuple

a = 10
b = a # b "copia" la referencia al mismo int (da igual, es inmutable)
b = 99 # # reasignación: b ahora apunta a otro int

print(a)
print(b)

# INMUTABLES: str
s1 = "hola"
s2 = s1
s2 += "!!!"  # esto crea un string nuevo (no muta el anterior)

print(s1)  # "hola"
print(s2)  # "hola!!!"

# MUTABLES: list
lista1 = [1, 2, 3]
lista2 = lista1     # ambas variables apuntan a la MISMA lista

lista2.append(999)  # mutación: cambia el objeto compartido

print(lista1)  # [1, 2, 3, 999]
print(lista2)  # [1, 2, 3, 999]

"""
Funciones: “por valor” vs “por referencia” (lo que pasa de verdad)
"""

# Caso A: inmutable (no cambia afuera)
def sumar_uno(n):
    n += 1      # reasigna n a un NUEVO int
    print("Dentro:", n)

x = 5
sumar_uno(x)

print("Fuera:", x)  # sigue siendo 5

# Caso B: mutable (sí cambia afuera si mutas)
def agregar_elemento(lista):
    lista.append("🔥")   # mutación del objeto
    print("Dentro:", lista)

mi_lista = ["a", "b"]
agregar_elemento(mi_lista)

print("Fuera:", mi_lista)  # se queda con el "🔥"

# Caso C: mutable pero REASIGNADO (no cambia afuera)
def reemplazar_lista(lista):
    lista = [0, 0, 0]   # reasignación: ahora lista apunta a otra lista
    print("Dentro:", lista)

original = [1, 2, 3]
reemplazar_lista(original)

print("Fuera:", original)  # sigue [1, 2, 3]

"""
* DIFICULTAD EXTRA (opcional):
* Crea dos programas que reciban dos parámetros (cada uno) definidos como
* variables anteriormente.
* - Cada programa recibe, en un caso, dos parámetros por valor, y en otro caso, por referencia.
*   Estos parámetros los intercambia entre ellos en su interior, los retorna, y su retorno
*   se asigna a dos variables diferentes a las originales. A continuación, imprime
*   el valor de las variables originales y las nuevas, comprobando que se ha invertido
*   su valor en las segundas.
*   Comprueba también que se ha conservado el valor original en las primeras.
"""

"""
Programa A (por “valor”): recibe 2 inmutables (int/str/tuple), los intercambia adentro, retorna los nuevos.
✅ Originales no cambian.
"""

def swap_valor(a, b):
    a, b = b, a

    return a, b

a1 = 10
b1 = 20

nuevo_a1, nuevo_b1 = swap_valor(a1, b1)

print("Originales: ", a1, b1)
print("Nuevas: ", nuevo_a1, nuevo_b1)

"""
2) Programa B: swap “por referencia” (mutables)
"""

def swap_referencia(lista_a, lista_b):
    temp_a = lista_a[:]
    temp_b = lista_b[:]

    lista_a.clear()
    lista_a.extend(temp_b)
    
    lista_b.clear()
    lista_b.extend(temp_a)

    return lista_a, lista_b

la = [1, 2]
lb = [9, 8]

nueva_la, nueva_lb = swap_referencia(la, lb)

print("Originales: ", la, lb)
print("Nuevas: ", nueva_la, nueva_lb)