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
 */
"""

# Por valor

my_num_a = 5
my_num_b = my_num_a
my_num_b = 10
print(my_num_a)
print(my_num_b)

# Por referencia

my_list_a = [1,2,3]
my_list_b = my_list_a
my_list_b.append(4)
print(my_list_a)
print(my_list_b)


# Funciones por valor

x = 10
print(id(x))
def func(entrada):
    entrada = 0
    print(id(entrada))

func(x)
print(x)

# Funciones por referencia

x = [10,20,30]
print(id(x))
def func2(entrada):
    entrada.append(40)
    print(id(entrada))
func2(x)
print(x)

### Extra

# Por valor

def valor(valor_1:int, valor_2:int) -> tuple:
    sor = valor_1
    valor_1 = valor_2
    valor_2 = sor
    return valor_1, valor_2

my_num_c = 14
my_num_d = 15
my_num_e, my_num_f = valor(my_num_c,my_num_d)
print(f"{my_num_c},{my_num_d}")
print(f"{my_num_e},{my_num_f}")

# Por referencia

def referencia(valor_1:list, valor_2:list) -> tuple:
    sor = valor_1
    valor_1 = valor_2
    valor_2 = sor
    return valor_1, valor_2

my_list_c = [1,2]
my_list_d = [11,22]
my_list_e, my_list_f = referencia(my_list_c,my_list_d)
print(f"{my_list_c}, {my_list_d}")
print(f"{my_list_e},{my_list_f}")
