'''
EJERCICIO:
 *   Muestra ejemplos de asignación de variables "por valor" y "por referencia", según
     su tipo de dato.
 *   Muestra ejemplos de funciones con variables que se les pasan "por valor" y 
     "por referencia", y cómo se comportan en cada caso en el momento de ser modificadas.
     (Entender estos conceptos es algo esencial en la gran mayoría de lenguajes)
  
     DIFICULTAD EXTRA (opcional):
 *   Crea dos programas que reciban dos parámetros (cada uno) definidos como
     variables anteriormente.
 *   Cada programa recibe, en un caso, dos parámetros por valor, y en otro caso, por referencia.
 *   Estos parámetros los intercambia entre ellos en su interior, los retorna, y su retorno
     se asigna a dos variables diferentes a las originales. A continuación, imprime
     el valor de las variables originales y las nuevas, comprobando que se ha invertido
     su valor en las segundas.
 *   Comprueba también que se ha conservado el valor original en las primeras.
'''

# 1. Asignacion por valor
# La asignacion por valor en python trabaja con las variables de tipo primitivo
# es decir las variables de tipo int, str, float y las bool.

a = 10    # Le asignamos a "a" el valor 10
b = a    # Le asignamos a "b" el valor que posee "a" es decir 10

b = b + 5    # "b" ahora vale 15
print(a)    # "a" sigue valiendo 10
print(b)    # "b" vale 15


# 2. Asignacion por referencia

list1 = [7, 15, 23]
list2 = list1    # list2 apuntara al mismo objeto, es decir a la referencia en memoria de list1

list2.append(38)

print(list1)    # [7, 15, 23, 38]
print(list2)    # [7, 15, 23, 38]

# 3. Paso de variables a funciones por valor

# a. Ejemplo con valores primitivos (int)

def dup(num):
    num = num * 2
    print("Dentro de la funcion:", num)

num = 6
dup(num)                              # Dentro de la funcion: 12 
print("Fuera de la funcion:", num)    # Fuera de la funcion: 6

# b. Ejemplos con referencias (listas)\

def add_value(list3):
    list3.append("c")
    print("Dentro de la función:", list3)

my_list = ["a", "b"]
add_value(my_list)                        # ['a', 'b', 'c']
print("Fuera de la función:", my_list)    # ['a', 'b', 'c']


'''
Extra
 *   Crea dos programas que reciban dos parámetros (cada uno) definidos como
     variables anteriormente.
 *   Cada programa recibe, en un caso, dos parámetros por valor, y en otro caso, por referencia.
 *   Estos parámetros los intercambia entre ellos en su interior, los retorna, y su retorno
     se asigna a dos variables diferentes a las originales. A continuación, imprime
     el valor de las variables originales y las nuevas, comprobando que se ha invertido
     su valor en las segundas.
 *   Comprueba también que se ha conservado el valor original en las primeras.
'''

num1 = 8
num2 = 17
print("")
def exchange_values(a, b):
    aux = a
    a = b
    b = aux
    return a, b

new_num1, new_num2 = exchange_values(num1, num2)
print("Intercambio de valores")
print(f"Originales: num1 = {num1}, num2 = {num2}")        # Originales: num1 = 8, num2 = 17
print(f"Nuevos: new_num1 = {new_num1}, new_num2 = {new_num2}")    # Nuevos: new_num1 = 17, new_num2 = 8


list1 = [20, 40]
list2 = [60, 80]
print("")
def exchange_ref(c, d):
    aux = c
    c = d
    d = aux
    return c , d

new_list1, new_list2 = exchange_ref(list1, list2)
print("Intercambio de Referencias")
print(f"Originales: list1 = {list1}, list2 = {list2}")
print(f"Nuevos: new_list1 = {new_list1}, new_list2 = {new_list2}")




