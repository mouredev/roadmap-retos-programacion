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
""" 
  ->  Los tipos de datos por valor ocupan cada uno un espacio independiente en memoria y se usan con tipos de datos inputables (números, strings, booleanos, tuplas)
  ->  Los timpos de datos por referencia ocupan el mismo espacio en memoria y se unsan con tipos de datos mutables (listas, diccionarios, conjuntos, objetos)
    ->  Al momento de crear una lista y copiar su valor en una variable adiciona se copia por referencia ya que ocupan el mismo espacio en memoria
    ->  my_list_2.append(30) -> en este ejemplo modifico la my_list_2 pero tambien se modifica my_list_1
  -> en las funcioens se hace exactamente igual que lo hice fuera de las funciones solo que se le asigno un parametro para funcionar
"""

# tipos de datos por valor

variable_1 = 30 # valor
variable_2 = variable_1 # referencia

print(variable_1) # 30
print(variable_2) # 30

variable_1 = 50

print(variable_1) # 50
print(variable_2) # 30

# tipos de datos por referencia

my_list_1 = [10, 20] # lista
my_list_2 = my_list_1
my_list_2.append(30) # my_list_1 = [10, 20, 30]

print(my_list_1) # [10, 20, 30]
print(my_list_2) # [10, 20, 30]

# Funcion con datos por valor

my_number = 10
def my_function_a(my_int: int):
  my_int = 20
  return my_int

print(my_function_a(my_number))
print(my_number)

# Funcion con datos por referencia

my_list_3 = [10, 20 ]
def my_function_b(my_list: list):
  my_list.append(30)
  return my_list

print(my_function_b(my_list_3))
print(my_list_3)

# DIFICULTAD EXTRA

## Funcion por valor

my_int_1 = 10
my_int_2 = 20

def values(param_1: int, param_2: int) -> list:
  temp = param_1
  param_1 = param_2
  param_2 = temp
  
  return [param_1, param_2]


my_int_3, my_int_4 = values(my_int_1,my_int_2)

print(f"my_int_1 = {my_int_1} y my_int_3 = {my_int_3}")
print(f"my_int_2 = {my_int_2} y my_int_4 = {my_int_4}")

## Duncion por referencia

my_list_a = [10, 20]
my_list_b = [30, 40]

def ref(list_1: list, list_2: list):
  temp = list_1
  list_1 = list_2
  list_2 = temp

  return [list_1, list_2]

my_list_c, my_list_d = ref(my_list_a, my_list_b)

print(my_list_a)
print(my_list_b )
print(my_list_c)
print(my_list_d)


