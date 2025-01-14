"""
 * EJERCICIO:
 * X Muestra ejemplos de asignación de variables "por valor" y "por referencia", según
 *   su tipo de dato.
 * X Muestra ejemplos de funciones con variables que se les pasan "por valor" y 
 *   "por referencia", y cómo se comportan en cada caso en el momento de ser modificadas.
 * (Entender estos conceptos es algo esencial en la gran mayoría de lenguajes)   
"""

# Varible por valor // El original no cambia
numero = 10
copia_numero = numero
copia_numero = 20

print(f"Original: {numero}")
print(f"Copia: {copia_numero}")

# variable por referencia // El original cambia dado que es una referencia
numeros = [1,2,3,4]
referencia = numeros
referencia[1] = 999

print(f"Original: {numeros}")
print(f"Referencia: {referencia}")

# Funciones por valor
def duplica(numero):
    numero *= 2
    print(f"Función: {numero}")
    
numero = 10

print(f"Original antes de la función: {numero}")
duplica(numero)
print(f"Original despues de la función: {numero}")

# Funciones por referencia
def add_numero(lista):
    lista.append(5)
    print(f"Función: {lista}")
    
lista = [1,2,3,4]

print(f"Original: {lista}")
add_numero(lista)
print(f"Original despues de la función: {lista}")



"""
 * DIFICULTAD EXTRA (opcional):
 * Crea dos programas que reciban dos parámetros (cada uno) definidos como variables anteriormente.
 * - Cada programa recibe, en un caso, dos parámetros por valor, y en otro caso, por referencia.
 *   Estos parámetros los intercambia entre ellos en su interior, los retorna, y su retorno
 *   se asigna a dos variables diferentes a las originales. A continuación, imprime el valor de las
 *   variables originales y las nuevas, comprobando que se ha invertido su valor en las segundas.
 *   Comprueba también que se ha conservado el valor original en las primeras.
"""

def progam_valor(param1,param2):
    param2, param1 = param1, param2
    return param1, param2

def program_ref(lista,lista2):
    lista2,lista = lista,lista2
    return lista,lista2

param_1 = 1
param_2 = 2

print(f"Param_1 antes: {param_1}")
print(f"Param_2 antes: {param_2}")

param_1_valor,param_2_valor = progam_valor(param_1,param_2)

print(f"\nParam_1_valor retorno: {param_1_valor}")
print(f"Param_2_valor retorno: {param_2_valor}")

print(f"\nParam_1 despues: {param_1}")
print(f"Param_2 despues: {param_2}")

lista_1 = [1,2]
lista_2 = [3,4]

print(f"\nlista_1 antes: {lista_1}")
print(f"lista_2 antes: {lista_2}")

lista_1_ref,lista_2_ref = program_ref(lista_1,lista_2)

print(f"\nlista_1_ref antes: {lista_1_ref}")
print(f"lista_2_ref antes: {lista_2_ref}")

print(f"\nlista_1 despues: {lista_1}")
print(f"lista_2 despues: {lista_2}")


