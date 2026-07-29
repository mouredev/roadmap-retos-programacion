# Valor y referencia en Python

##Tipos de datos por valor

my_int_a = 10
print(my_int_a)

my_int_b = my_int_a

my_int_b = 20
print(my_int_b)

my_int_a = 30

print(my_int_b)
print(my_int_a)

##Tipos de datos por referencia

my_list_a = [10,20]

my_list_b= my_list_a
my_list_b.append(30)

print(my_list_a)
print(my_list_b)

#Funciones con datos por valor

my_int_c = 10

def my_int_func(my_int):
    my_int = 20
    print(my_int)

my_int_func(my_int_c)

#Funciones con datos por referencia 

def my_list_func(my_list:list):
    my_list_e = my_list
    my_list_e.append(30)

    my_list_e = my_list
    my_list_e.append(40)

    print(my_list)
    print(my_list_e)

my_list_c = [10,20]
my_list_func(my_list_c)
print(my_list_c)


#por valor
def value(value_a:int, value_b:int)-> tuple:
    temp = value_a
    value_a = value_b
    value_b = temp
    return value_a, value_b


my_int_x = 20
my_int_y = 10
my_int_f,my_int_g = value(my_int_x,my_int_y)

print(f"{my_int_x}, {my_int_y}")
print(f"{my_int_f},{my_int_g}")

#por referrencia

def ref(value_a:list, value_b:list)-> tuple:
        temp = value_a
        value_a = value_b
        value_b = temp

        return value_a, value_b


my_list_e = [10,20]
my_list_d = [30,40]
my_int_h,my_int_i = ref(my_list_e,my_list_d)

print(f"{my_list_e}, {my_list_d}")
print(f"{my_int_h},{my_int_i}")

    


