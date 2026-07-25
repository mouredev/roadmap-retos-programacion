# - Muestra ejemplos de asignación de variables "por valor" y "por referencia", según
#   su tipo de dato.
# - Muestra ejemplos de funciones con variables que se les pasan "por valor" y 
#   "por referencia", y cómo se comportan en cada caso en el momento de ser modificadas.
# (Entender estos conceptos es algo esencial en la gran mayoría de lenguajes)

# por valor son los datos inmutables tales como los int, float, bool y str
num = 15
print(f"La variable 'num' tiene el valor: {num}.")
print("Háremos una copia de la variable 'num' en 'num2'.")
num2 = num
print("Y ahora cambiaremos el valor de 'num2' a 20.")
num2 = 20
print(f"Ahora la variable 'num2' tiene de valor: {num2}, pero la variable 'num' sigur siendio: {num}.")

# por referencia suelen ser laas estructuras de datos list, dict, set
array = [12, 3, 45, 99]
print(f"La lista tiene estos valores: {array}.")
print("Ahora háremos una copia de la lista en 'array2'.")
array2 = array
print("Ahora vamos a añadir el numero '999' a 'array2'.")
array2.append(999)
print(f"Ahora los valores de 'array2' són: {array2} pero al apuntar a la misma referencia en la memoria\n"
      f"veremos que 'array' también contiene el número '999'. 'array': {array}.")

# por valor y por referencia despúes de pasar como argumento a una función

# por valor
num = 10

def change_value(int):
    int = 20
    print(f"La función le da el valor de: {int}")
change_value(num)
print(f"pero en el scope global es: {num}")
 
# por referencia
array = [1, 3, 5, 7]

def add_to_array(list=list):
    list.append(9)
    print(f"La función añadio el '9' al 'array': {list}")
add_to_array(array)
print(f"Pero el 'array' en el scope global también contiene el '9', 'array': {array}")



# DIFICULTAD EXTRA (opcional):
# Crea dos programas que reciban dos parámetros (cada uno) definidos como variables anteriormente.
# - Cada programa recibe, en un caso, dos parámetros por valor, y en otro caso, por referencia.
#   Estos parámetros los intercambia entre ellos en su interior, los retorna, y su retorno
#   se asigna a dos variables diferentes a las originales. A continuación, imprime el valor de las
#   variables originales y las nuevas, comprobando que se ha invertido su valor en las segundas.
#   Comprueba también que se ha conservado el valor original en las primeras.

my_int = 19
my_str = "Python"

def per_value(arg, arg_2):
    arg, arg_2 = arg_2, arg
    return arg, arg_2

mod_value, mod_value2 = per_value(my_int, my_str)

print(f"valor de my_int: {my_int}, valor de modificado : {mod_value}.")
print(f"valor de my_str: {my_str}, valor de modificado 2: {mod_value2}.")


array = [23, 45, 23, 45]
collection = {23, 45, 55}
def per_reference(arg, arg_2):
    arg_2, arg = arg, arg_2
    return arg, arg_2

mod_value3, mod_valu4 = per_reference(array, collection)

print(f"valor collection: {collection}, valor de modificado 3: {mod_value3}.")
print(f"Valor array: {array}, modificado 4: {mod_valu4}")





my_dict = {"name": "Dany", "age": 41}
my_dict_2 = my_dict

print(my_dict_2)
my_dict_2["age"] = 42
print(my_dict_2)
print(my_dict)