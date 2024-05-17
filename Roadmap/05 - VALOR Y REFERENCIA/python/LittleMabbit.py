# Tipos de datos por valor - Cada valor tiene su espacio en memoria.
int_a = 10
int_b = 20
print(int_b)
int_b = int_a
print(int_b)

# Tipos de datos por referencia - Valores que heredan lo que poseen por su espacio en memoria. Todos los datos que no son primitivos. Por referencia entendemos que estamos referenciando el valor en memoria.
my_list_a = [10, 20]
my_list_b = my_list_a
my_list_b.append(30)
print(my_list_a) 
print(my_list_b)

# Funciones con datos por valor


def my_int_func(my_int: int):
    my_int = 10 # El valor dentro de la scope es asignado como my_int.
    print(my_int)


my_int_c = 30 # Se asigna el valor que pasa a la función my_int_func, mas ya tiene el 10 establecido.
my_int_func(my_int_c) # Recibe el valor asignado realmente dentro del scope de la función.
print(my_int_c) # Recibe el valor establecido fuera de la función.

# Funciones con datos por referencia


def my_list_func(my_list: list):
    my_list.append(30)

    my_list_d = my_list
    my_list_d.append(40)

    print(my_list)
    print(my_list_d)


my_list_c = [10, 20]
my_list_func(my_list_c)
print(my_list_c)

# Los valores se mueven, asignan y reasignan en base al valor hexadecimal que cada variable tenga asignada en memoria.