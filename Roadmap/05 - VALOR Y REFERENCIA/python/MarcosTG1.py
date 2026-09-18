"""
 * EJERCICIO:
 * - Muestra ejemplos de asignación de variables "por valor" y "por referencia", según
 *   su tipo de dato.
 * - Muestra ejemplos de funciones con variables que se les pasan "por valor" y 
 *   "por referencia", y cómo se comportan en cada caso en el momento de ser modificadas.
 * (Entender estos conceptos es algo esencial en la gran mayoría de lenguajes)
"""

mi_entero_1 = 10
mi_entero_2 = mi_entero_1

mi_entero_1 = 30

print(mi_entero_1)
print(mi_entero_2)

asignacion_referencia_1 = {74, 78, 87.98}
asignacion_referencia_2 = asignacion_referencia_1

set_union = {12, 66,9}

asignacion_referencia_3 = asignacion_referencia_2.union(set_union)

print(asignacion_referencia_3)

asignacion_referencia_2 = asignacion_referencia_3

asignacion_referencia_3.add("cagaste")

# Al compartir el mismo espacio en memoria con asignacion_referencia_3 también se aplica la inserción

print(asignacion_referencia_2)

mi_float_1 = 0.785
mi_float_2 = 7.985

mi_float_2 = mi_float_1

mi_float_2 + 2

mi_bool_1 = True
mi_bool_2 = False

mi_bool_1 = mi_bool_2

mi_bool_1 = True

def por_valor(valor_1: int, valor_2: float, valor_3: bool):
    
    print("")
    print(valor_1)
    print(valor_2)
    print(valor_3)
    print("")

por_valor(mi_entero_2, mi_float_1, mi_bool_2)

mi_lista_1 = [445, "holacola", "tg", True]
mi_lista_2 = ["777", 777]

mi_lista_2 = mi_lista_1

mi_lista_2.reverse()

mi_tupla_1 = tuple(mi_lista_1)




def por_referencia(lista_1: list, tupla_1: tuple):

    # Si la asignación hubiese sido por valor se esperaría : 445, holacola ...  
    
    for i in lista_1:
        print(i)
    

por_referencia(mi_lista_1, mi_tupla_1)

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


def programa_valor(param_1: str, param_2: int):
    # Intercambiamos los valores entre ellos en su interior
    temp = param_1
    param_1 = param_2
    param_2 = temp

    temp = temp + " holacola"
    param_2 = temp

    return param_1, param_2 

# Variables originales
entra_valor_1 = "viva el vcf"
entra_valor_2 = 22

# Asignación del retorno a variables diferentes
sale_valor_1, sale_valor_2 = programa_valor(entra_valor_1, entra_valor_2)

# Comprobaciones mediante print:
print("--- VARIABLES ORIGINALES (conservan su valor) ---")
print(f"Original 1: {entra_valor_1}") # "viva el vcf"
print(f"Original 2: {entra_valor_2}") # 22

print("--- VARIABLES NUEVAS (valores invertidos) ---")
print(f"Nuevas 1: {sale_valor_1}")    # 22
print(f"Nuevas 2: {sale_valor_2}")    # "viva el vcf"


def programa_referencia(param_1: list, param_2: dict):

    temp = param_1
    param_1 = param_2
    param_2 = temp 
    temp.append("cagaste")

    return param_1, param_2

entra_ref_1 = [10, 20]
entra_ref_2 = {"A": 1, "B": 2}

sale_ref_1, sale_ref_2 = programa_referencia(entra_ref_1, entra_ref_2)

print(f"\nLas que entraron : {entra_ref_1} y {entra_ref_2}") # Cambiaron
print(f"\nLas que salieron : {sale_ref_1} y {sale_ref_2}")

