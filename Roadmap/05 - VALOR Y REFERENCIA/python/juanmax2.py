"""
Valor y referencia
"""
# Tipos de datos por valor
my_int = 10
my_int_2 = my_int
my_int = 30
print(my_int)
print(my_int_2)

# Tipos de datos por referenciaç
# Las dos listas apuntan al mismo guardado en la memória
lista_a = [10, 20]
lista_b = lista_a
lista_b.append(30)

print(lista_a)
print(lista_b)

# Funciones con datos por valor
my_int_3 = 10

def my_int_func(my_int : int):
    my_int = 20
    print(my_int)

my_int_func(my_int_3)
print(my_int_3)

# Funciones con datos por referencia

def my_list_func(my_list: list):
    my_list.append(30)
    
    my_list_d = my_list
    my_list_d.append(40)
    
    my_list_e = my_list_d
    my_list_e.append(50)
    
    print(my_list)
    print(my_list_d)
    print(my_list_e)
    
my_list_c = [10, 20]
my_list_func(my_list_c)
print(my_list_c)

"""
* DIFICULTAD EXTRA (opcional):
 * Crea dos programas que reciban dos parámetros (cada uno) definidos como variables anteriormente.
 * - Cada programa recibe, en un caso, dos parámetros por valor, y en otro caso, por referencia.
 *   Estos parámetros los intercambia entre ellos en su interior, los retorna, y su retorno
 *   se asigna a dos variables diferentes a las originales. A continuación, imprime el valor de las
 *   variables originales y las nuevas, comprobando que se ha invertido su valor en las segundas.
 *   Comprueba también que se ha conservado el valor original en las primeras.
"""

def valor(parametro1, parametro2):
    temp = parametro1
    parametro1 = parametro2
    parametro2 = temp
    return parametro1, parametro2

def referencia(parametro1, parametro2):
    temp = parametro1
    parametro1 = parametro2
    parametro2 = temp
    return parametro1, parametro2

# Caso de uso por valor
parametro1 = 10
parametro2 = 20
parametro1_retornado, parametro2_retornado = valor(parametro1, parametro2)
print(parametro1)
print(parametro2)
print(parametro1_retornado)
print(parametro2_retornado)

print("--------------------")
print("--------------------")

# Caso de uso por referencia
parametro_ref1 = [10, 20]
parametro_ref2 = [30, 40]
parametro_ref1_retornado, parametro_ref2_retornado = referencia(parametro_ref1, parametro_ref2)
print(parametro_ref1)
print(parametro_ref2)
print(parametro_ref1_retornado)
print(parametro_ref2_retornado)

