"""
Valor y referencia
"""

# Tipos de datos por valor
numero = 10
print("Valor inicial de numero:", numero)
# Modificando el valor de la variable
numero = 20
print("Valor modificado de numero:", numero)

# Tipos de datos por referencia
mi_lista = [1, 2, 3]
print("Valor inicial de mi_lista:", mi_lista)
# Modificando la lista
mi_lista.append(4)
print("Valor modificado de mi_lista:", mi_lista)

# Funciones con datos por valor
def numero2_func(numero: int):

    numero = 40
    print("Valor de numero dentro de la función:", numero)
    
numero2 = 30   
    
numero2_func(numero2)
print("Valor de numero2 después de la función:", numero2)

# Funciones con datos por referencia

def mi_lista2_func(lista: list):
    lista.append(8)
    
    mi_lista_3 = lista
    mi_lista_3.append(9)
    
    print("Valor de mi_lista2 dentro de la función:", lista)
    print("Valor de mi_lista_3 dentro de la función:", mi_lista_3)

mi_lista2 = [5, 6, 7]    
mi_lista2_func(mi_lista2)
print("Valor de mi_lista2 después de la función:", mi_lista2)

"""
Extra    
"""

# Por valor

def intercambiar_valores(valor_1, valor_2):
    temporal = valor_1
    valor_1 = valor_2
    valor_2 = temporal

    return valor_1, valor_2

numero_1 = 10
numero_2 = 20

nuevo_numero_1, nuevo_numero_2 = intercambiar_valores(
    numero_1,
    numero_2
)

print("Valores originales:", numero_1, numero_2)
print("Valores nuevos:", nuevo_numero_1, nuevo_numero_2)

# Por referencia
def intecambiar_listas(lista_1, lista_2):
    # Como las listas son mutables, si cambiamos su contenido directamente, también cambiarían las listas originales.
    copia_1 = lista_1.copy()
    copia_2 = lista_2.copy()
    
    copia_1, copia_2 = copia_2, copia_1
    
    return copia_1, copia_2

lista_original_1 = [10, 20]
lista_original_2 = [30, 40]

nueva_lista_1, nueva_lista_2 = intecambiar_listas(lista_original_1, lista_original_2)

print("Listas originales:", lista_original_1, lista_original_2)
print("Listas nuevas:", nueva_lista_1, nueva_lista_2)

# Otro ejemplo de referencia con listas
def intercambiar_nombres(nombre_1, nombre_2):
    nombre_1, nombre_2 = nombre_2, nombre_1
    return nombre_1, nombre_2

persona_1 = "Misael"
persona_2 = "Tania"

nuevo_nombre_1, nuevo_nombre_2 = intercambiar_nombres(
    persona_1, persona_2
    )

print("Nombres originales:", persona_1, persona_2)
print("Nombres intercambiados:", nuevo_nombre_1, nuevo_nombre_2)

