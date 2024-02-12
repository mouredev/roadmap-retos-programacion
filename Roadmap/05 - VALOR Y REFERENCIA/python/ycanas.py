## I. Ejercicio

# 1. Asignación de variables

# por valor

my_int_a = 1
my_int_b = my_int_a
my_int_b = 2

print(my_int_a, my_int_b)

# por referencia

my_list_a = [1]
my_list_b = my_list_a
my_list_b.append(2)

print(my_list_a, my_list_b)

# 2. Funciones

# por valor

def my_func_a(my_var):
    my_var = 2
    return my_var


my_var_a = 1
my_var_b = my_func_a(my_var_a)
print(my_var_a, my_var_b)

# por referencia

def my_func_b(my_var):
    my_var.append(2)
    return my_var

my_var_c = [1]
my_var_d = my_func_b(my_var_c)
print(my_var_c, my_var_d)