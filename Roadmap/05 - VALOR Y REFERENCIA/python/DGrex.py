"""
 * EJERCICIO:
 * - Muestra ejemplos de asignación de variables "por valor" y "por referencia", según
 *   su tipo de dato.
 * - Muestra ejemplos de funciones con variables que se les pasan "por valor" y 
 *   "por referencia", y cómo se comportan en cada caso en el momento de ser modificadas.
 * (Entender estos conceptos es algo esencial en la gran mayoría de lenguajes)
"""

### Tipos de datos por valor y referencia ###

# Por valor

number_one = 15
number_two = number_one
print(f"number_one: {number_one}")
print(f"number_two: {number_two}")

number_one = 20 
print(f"number_one: {number_one}")
print(f"number_two: {number_two}")

number_two = 100 
print(f"number_one: {number_one}")
print(f"number_two: {number_two}")

"""
La asignación por valor se refiere al manejo de objetos inmutables, 
como números, cadenas y tuplas. Al cambiar el valor de una variable, 
se genera un nuevo objeto en lugar de modificar el objeto original.
"""

# Por referencia

my_list = [15,20,50,100]
my_list_copy = my_list
print(f"my_list:      {my_list}")
print(f"my_list_copy: {my_list_copy}")

my_list_copy.append(80)
print(f"my_list:      {my_list}")
print(f"my_list_copy: {my_list_copy}")

"""
La asignación por referencia se refiere a la forma en que se manejan
los objetos mutables, como listas y diccionarios. Cuando se modifica un objeto
a través de una referencia, dichos cambios afectan a todas las referencias
que apuntan al mismo objeto.
"""

### Funciones con datos por valor y referencia ###

# Por valor

def funcion_por_valor(number):
    num_two = 75
    print(f"num_two: {num_two}")

num_one = 50
funcion_por_valor(number_one)
print(f"num_one: {num_one}")

# Por referencia

my_list_one = [10,50,60]

def funcion_por_referencia(list):
    my_list_two = list 
    my_list_two.append(95)
    print(f"my_list_two: {my_list_two}")

funcion_por_referencia(my_list_one)
print(f"my_list_one: {my_list_one}")


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

# Por valor

def por_valor(num_a,num_b):
    temporary = num_a
    num_a = num_b
    num_b = temporary
    return num_a, num_b

num_a = 20
num_b = 60
num_c, num_d = por_valor(num_a,num_b)

print(num_a, num_b)
print(num_c, num_d)


# Por referencia

def por_referencia(list_a, list_b):
    temporary = list_a
    list_a = list_b
    #list_a.append(80)
    list_b = temporary
    return list_a, list_b

list_a = [20, 30, 40]
list_b = [50, 60, 70]
list_c, list_d = por_referencia(list_a, list_b)

print(list_a, list_b)
print(list_c, list_d)
