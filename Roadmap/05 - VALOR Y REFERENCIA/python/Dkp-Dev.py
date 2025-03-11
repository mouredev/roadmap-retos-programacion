"""
* EJERCICIO:
 * - Muestra ejemplos de asignación de variables "por valor" y "por referencia", según
 *   su tipo de dato.
 * - Muestra ejemplos de funciones con variables que se les pasan "por valor" y 
 *   "por referencia", y cómo se comportan en cada caso en el momento de ser modificadas.
 * (Entender estos conceptos es algo esencial en la gran mayoría de lenguajes)
"""

# Tipos de dato por valor
# Los valores de las variables estan indicados y aunque otra variable copie su valor creara su propia direccion

a = 10
b = a
b = 20

print(a)    # Imprime 10
print(b)    # Imprime 20 a pesar de que en un punto se le indico que copiara el valor de a

# Tipo de dato por referencia

list_a = [10,20]
list_b = list_a
list_b.append(30)

print(list_a)   # Ambas impresiones tienen el mismo valor [10,20,30]
print(list_b)

# Los tipos de dato por referencia no "adquieren" valores sino "heredan" o "apuntan" direcciones, por esto mismo al cambiar el valor b cambia el de a


# Funciones con datos por referencia

def list_func(my_list: list):
    my_list.append(30)

    list_z = my_list
    list_z.append(40)

    print(my_list)
    print(list_z)


list_x = [10,20]
list_func(list_x)
print(list_x)


"""
DIFICULTAD EXTRA (opcional):
 * Crea dos programas que reciban dos parámetros (cada uno) definidos como
 * variables anteriormente.
 * - Cada programa recibe, en un caso, dos parámetros por valor, y en otro caso, por referencia.
 *   Estos parámetros los intercambia entre ellos en su interior, los retorna, y su retorno
 *   se asigna a dos variables diferentes a las originales. A continuación, imprime
 *   el valor de las variables originales y las nuevas, comprobando que se ha invertido
 *   su valor en las segundas.
 *   Comprueba también que se ha conservado el valor original en las primeras.
"""

# Por Valor

def box(var1: int, var2: int) -> tuple:
    var_t = var1
    var1 = var2
    var2 = var_t
    return var1, var2

var_x = 10
var_z = 20
var_r, var_s = box(var_x,var_z)

print(f"X es {var_x} y Z es {var_z}")
print(f"R es {var_r} y S es {var_s}")

# Por referencia

def chest(var1: list, var2: list) -> tuple:
    var_t = var1
    var1 = var2
    var2 = var_t
    return var1, var2

list_x = [10,20]
list_z = [30,40]
list_r, list_s = chest(list_x,list_z)

print(f"X es {list_x} y Z es {list_z}")
print(f"R es {list_r} y S es {list_s}")

