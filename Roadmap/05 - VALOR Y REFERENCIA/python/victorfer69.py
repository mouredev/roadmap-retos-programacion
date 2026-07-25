#VALOR Y REFERENCIA

#Tipos de datos por valor

my_int_a = 10
my_int_b = my_int_a
my_int_a = 20
print(f"{type(my_int_a)} y {my_int_a}")
print(f"{type(my_int_b)} y {my_int_b}")

#Tipos de datos por referencia
my_list_a = [10,20]
my_list_b = my_list_a
my_list_a.append(30)
print(my_list_a)
print(my_list_b)

#Funciones con datos por valor
def my_int_func(my_int: int):
    my_int = 20
    print(my_int)


my_int_c = 10
my_int_func(my_int_c)
print(my_int_c)

#Funciones con datos por referencia
def my_list_func(my_list: list):
    my_list.append(30)
    print(my_list)

my_list_3 = [10,20]
my_list_func(my_list_3)
print(my_list_3)


#EJERCICIO EXTRA

def programa1(arg1:int, arg2:int):
    tmp = arg1
    arg1 = arg2
    arg2 = tmp
    return arg1, arg2

a = 1
b = 2
c,d = programa1(a,b)
print(f"{a} y {b}")
print(f"{c} y {d}")


def programa2(arg1:list, arg2:list):
    tmp = arg1
    arg1 = arg2
    arg2 = tmp
    return arg1, arg2

ab = [1,2]
ba = [2,1]
cd,dc = programa2(ab,ba)
print(f"{ab} y {ba}")
print(f"{cd} y {dc}")