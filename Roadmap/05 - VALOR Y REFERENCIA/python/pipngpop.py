"""
VALOR Y REFERENCIA
"""

# Tipos de dato por valor
my_int_a = 10
my_int_b = my_int_a
my_int_b = 20
my_int_a = 15
print(my_int_a)
print(my_int_b)

#Tipos de dato por referencia (todos los datos que no son primitivos)

my_list_a = [10,20]
my_list_b = my_list_a #ahora ambas listas tienen la misma dirección de memoria
my_list_b.append(30) #le añado un número
print(my_list_a)
print(my_list_b) 

# Funciones con datos por valor

my_int_c = 10

def my_int_func (my_int: int):
    my_int = 20
    print(my_int)

my_int_func(my_int_c)
print(my_int_c)

# Funciones con datos por referencia

def my_list_func(my_list: list):
    my_list.append(30)

    my_list_d = my_list
    my_list_d.append(40)

    print(my_list)
    print(my_list_d)

my_list_c = [10,20]
my_list_func(my_list_c)
print(my_list_c) #también aquí aparecerá el 30 que se ha añadido dentro de la función


"""
EXTRA
"""
"""
* Crea dos programas que reciban dos parámetros (cada uno) definidos como
 * variables anteriormente.
 * - Cada programa recibe, en un caso, dos parámetros por valor, y en otro caso, por referencia.
 *   Estos parámetros los intercambia entre ellos en su interior, los retorna, y su retorno
 *   se asigna a dos variables diferentes a las originales. A continuación, imprime
 *   el valor de las variables originales y las nuevas, comprobando que se ha invertido
 *   su valor en las segundas.
 *   Comprueba también que se ha conservado el valor original en las primeras.
"""


def valor (my_val_1: int,my_val_2: int):
   
    #temp=my_val_2
    #my_val_2=my_val_1
    #my_val_1=temp

    my_val_1, my_val_2 = my_val_2, my_val_1 #esta es otra opción más limpia

    return my_val_1,my_val_2
    
val_1 = 1
val_2 = 2
new_val_1, new_val_2 = valor(val_1,val_2)
print(f"{val_1} y {val_2}")
print(f"{new_val_1} y {new_val_2}")



def referencia (my_ref_1: list,my_ref_2: list):
   
    temp=my_ref_2
    my_ref_2=my_ref_1
    my_ref_1=temp

    #my_ref_1, my_ref_2 = my_ref_2, my_ref_1 #esta es otra opción más limpia

    return my_ref_1,my_ref_2
    
ref_1 = [10,20]
ref_2 = [30,40]
new_ref_1, new_ref_2 = referencia(ref_1,ref_2)
print(f"{ref_1} y {ref_2}")
print(f"{new_ref_1} y {new_ref_2}")




