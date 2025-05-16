### valor y referencia ###



## tipos de datos por valor (int, float, str, tuple, bool)
"""
por valor implica que cuando se asigna una variable a otra o se pasa como argumento, se copia el valor real del objeto 
en ese momento
"""

my_int_a = 10
my_int_b = 20
my_int_b = my_int_a

print(my_int_a) #out 10
print(my_int_b) #out 20

my_int_b += 5
print(my_int_b) #out: 15

my_int_a = 10
my_int_b = 20
my_int_b = my_int_a

my_int_a = 30

print(my_int_a) #out: 30
print(my_int_b) #out: 10

#muestra la direccion de memoria
print(id(my_int_a))
print(id(my_int_b))

# tipos de datos por referencia (list, dict, set)
"""
Por referencia implica que las variables contienen una referencia al objeto en memoria, no el valor directamente. 
Esto significa que si se modifica el contenido del objeto usando una de las referencias, los cambios se reflejan en todas
las referencias.
En el caso por referencia, No copian su valor, sino que heredan su dirección de memoria.
"""
my_list_a = [10, 20]
my_list_b = [30, 40]

print(my_list_a)
print(my_list_b)

my_list_b = my_list_a

my_list_a.append(30)

print(my_list_a)
print(my_list_b)

#muestra la direccion de memoria
print(id(my_list_a))
print(id(my_list_b))

## funcion que recibe variables por valor:

my_int_c = 10

def my_int_func(my_int):
    my_int = 20
    
    return my_int
    
valor_en_funcion = my_int_func(my_int_func)
print(f"el valor dentro de la funcion es: {valor_en_funcion}, el valor fuera de la funcion es :{ my_int_c}")


## funcion que recibe variables por referencia:

my_list_c = [10, 20]

def my_list_func(my_list):
    my_list.append(30)
    
    return my_list
    
valor_referencia_en_funcion = my_list_func(my_list_c)
print(f"el valor de referencia dentro de la funcion es: {valor_referencia_en_funcion}, el valor fuera de la funcion es :{ my_list_c}")

"""
Ejercicio Dificultad Extra:
"""
print("--------------------------"*5)
print("Ejercicio Extra:\n")

# por valor:

my_int_d = 10
my_int_e = 20

def value_changer(d, e):
    #intercambio por desempaquetado (swapping)
    d,e = e,d
    return d,e

resultado = value_changer(my_int_d, my_int_e)

print(f" el valor original es: \n my_int_d: {my_int_d}\n my_int_e: {my_int_e}")
print(f" el valor cambiado es: \n my_int_d:{resultado[0]}\n my_int_e: {resultado[1]}")

print("\n")
print("--------------------------"*5)

#por referencia:

my_list_d = [10, 20]
my_list_e = [20, 10]

def value_changer(d, e):
    #intercambio por desempaquetado (swapping).
    # d,e = e,d
    
    #tambien puede realizarse con una variable "temporal"
    temp = d
    d = e
    e = temp
    return d,e

resultado = value_changer(my_list_d, my_list_e)

print(f" el valor original es: \n my_list_d: {my_list_d}\n my_list_e: {my_list_e}")
print(f" el valor cambiado es: \n my_list_d:{resultado[0]}\n my_list_e: {resultado[1]}")
