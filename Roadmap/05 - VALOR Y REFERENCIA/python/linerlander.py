"""
Valor y referencia
"""

# Tipos de dato por valor
my_num_x = 24
my_num_z = my_num_x
#my_num_2 = 20
my_num_x = 30
print(my_num_x)
print(my_num_z)

# Tipos de dato por referencia
my_lista_x = [10, 25]
my_lista_z = my_lista_x
my_lista_z.append("liner")

print(my_lista_x)
print(my_lista_z)

# Funciones con datos por valor
def my_int(my_num: int):
    my_num = 20
    print(my_num)

my_num_c = 10
my_int(my_num_c)
print(my_num_c)

# Funciones con datos por referencia
def my_list(my_list: list):
    my_list.append(30)

    my_list_e = my_list
    my_list_e.append(40)

    print(my_list)
    print(my_list_e)

my_list_d =[10,25]
my_list(my_list_d)
print(my_list_d)

"""
Extra
"""
print('\n')
# Función por valor
def por_valor(val_1,val_2):
    temp = val_1
    val_1 = val_2
    val_2 = temp
    return val_1, val_2

x = 5
y = 8
a, b = por_valor(x, y)

print(f'{x},{y}')
print(f'{a},{b}')


# Función por referencia
def por_referencia(ref_1: list,ref_2: list)-> tuple:
    temp = ref_1
    ref_1 = ref_2
    ref_2 = temp
    ref_2.append(50)
    return ref_1,ref_2

lista_1 = [10,20]
lista_2 = [30,40]
lista_3,lista_4 =por_referencia(lista_1,lista_2)
print(f'{lista_1} {lista_2}')
print(f'{lista_3} { lista_4}')