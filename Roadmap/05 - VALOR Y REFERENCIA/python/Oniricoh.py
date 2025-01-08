########################################################################
# Paso por copia o valor
########################################################################
def doblar_valor(numero):
    numero *= 2

n = 10
doblar_valor(n)
print(n)  # Salida: 10

# Ejemplo con números (tipo de dato inmutable)
a = 5
b = a  # Asignación por valor
b = 10
print(a)  # Imprimirá 5

# Ejemplo con cadenas (tipo de dato inmutable)
cadena1 = "Hola"
cadena2 = cadena1  # Asignación por valor
cadena2 = "Adiós"
print(cadena1)  # Imprimirá "Hola"




########################################################################
# Paso por referencia
########################################################################
def doblar_valores(numeros):
    for i, n in enumerate(numeros):
        numeros[i] *= 2

ns = [10, 50, 100]
doblar_valores(ns)
print(ns)  # Salida: [20, 100, 200]

# Para evitar modificacion hacer copia
def doblar_valores(numeros):
    for i, n in enumerate(numeros):
        numeros[i] *= 2

ns = [10, 50, 100]
doblar_valores(ns[:])  # Una copia al vuelo de la lista con [:]
print(ns)  # Salida: [10, 50, 100]

# Ejemplo con listas (tipo de dato mutable)
lista1 = [1, 2, 3]
lista2 = lista1  # Asignación por referencia
lista2[0] = 99
print(lista1)  # Imprimirá [99, 2, 3]

# Ejemplo con diccionarios (tipo de dato mutable)
diccionario1 = {'a': 1, 'b': 2}
diccionario2 = diccionario1  # Asignación por referencia
diccionario2['a'] = 99
print(diccionario1)  # Imprimirá {'a': 99, 'b': 2}




########################################################################
# Modificación de Tipos Simples y Compuestos
########################################################################
def doblar_valor(numero):
    return numero * 2

n = 10
n = doblar_valor(n)
print(n)  # Salida: 20

########################################################################
# DIFICULTAD EXTRA
########################################################################
p1_value = 1
p2_value = "Hola"

p1_ref = [1, 2, 3, 4]
p2_ref = {"Edad":34, "Genero":"Varon"}

def prog1(v1, v2):
    v1 = p2_value
    v2 = p1_value
    return v1, v2



def prog2(r1, r2):
    r1 = p2_ref
    r2 = p1_ref
    return r1, r2


x1, x2 = prog1(p1_value, p2_value)
print(f"\nLas variables por valor originales son: {p1_value} y {p2_value}")
print(f"Las variables por valor nuevas son: {x1} y {x2}")




y1, y2 = prog2(p1_ref, p2_ref)
print(f"\nLas variables por valor originales son: {p1_ref} y {p2_ref}")
print(f"Las variables por valor nuevas son: {y1} y {y2}")
