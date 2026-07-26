#Tipos de asignaciones por valor
my_int_a = 10
my_int_b = my_int_a
my_int_a = 20
print(my_int_a)
print(my_int_b)

#Tipos de asignaciones por a referencias
my_list_a = [10,20]
my_list_b = my_list_a
my_list_b.append(30)
print(my_list_a)
print(my_list_b)

#funciones con variables por valor

my_int_c = 10
def my_int_fuc (my_int: int):
    my_int = 20
    print(my_int)
my_int_fuc(my_int_c)
print(my_int_c)


def my_list_fuc (my_list: list):
    my_list.append(30) 
    print(my_list)


my_list_c = [10,20]
my_list_fuc(my_list_c)
print(my_list_c)

"""☼☼☼☼☼ EXTRA ☼☼☼☼

"""

my_value1 = 5
my_value2 = 10
def functions_values (value1, value2):
    temp= value1
    value1 = value2 
    value2 = temp 
    new_value1 = value1
    new_value2 = value2
    print(new_value1, new_value2)
functions_values(my_value1, my_value2)
print(my_value1, my_value2)

my_reference1 = [20,30]
my_refrence2 = [30,50]
def fucntions_references(reference1, reference2):
    temp= reference1
    reference1 = reference2 
    reference2 = temp 
    new_ref = reference1
    new_ref2 = reference2
    print(new_ref, new_ref2)
fucntions_references(my_reference1, my_refrence2)
print(my_reference1, my_refrence2)
