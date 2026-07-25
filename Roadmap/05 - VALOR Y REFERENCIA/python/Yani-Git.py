"""
Valor y referencia

"""

#Tipos de datos por valor:  Tipos inmutables: int, float, str,  bool, tuplas Etc. 

my_int_a = 10
my_int_b = my_int_a
#my_int_b = -20 +1
#my_int_a = 30
print (my_int_a)
print (my_int_b)


#Tipos de datos por referencia:  Tipos mutables: list, dict, set, etc.

my_list_a =[10, 20]
#my_list_b = [30, 40]
my_list_b = my_list_a
my_list_b.append (30) 
#my_list_b = [30, 40]
print (my_list_a) #dato o variable por referencia, es decir, hereda su posición de referencia y se almacenan en la misma posición de memoria. imprime esto: [10, 20, 30]
print (my_list_b)


#Funciones con datos por valor


my_int_c = 10 

def my_int_func(my_int: int):
    my_int = 20
    #my_int c = 30
    print (my_int)

my_int_func(my_int_c)
print (my_int_c)

#Funciones con datos con referencia

def my_list_func (my_list: list):
    my_list_e = my_list
    my_list_e.append (30)

    my_list_d = my_list_e
    my_list.append (40)

    print(my_list_e)
    print (my_list_d)


my_list_c =[10, 20]
my_list_func(my_list_c)
print (my_list_c)


"""
Extra

"""
#Variable por valor 

def value (value_a: int, value_b: int)-> tuple:
    temp = value_a
    value_a = value_b
    value_b = temp
    return value_a, value_b


my_int_d = 10
my_int_e = 20
my_int_f, my_int_g = value (my_int_d, my_int_e)

print (f"{my_int_d}, {my_int_e}")
print (f"{my_int_f}, {my_int_g}")

#Por referencia 

def ref (value_a: list, value_b: list) -> tuple:
    temp = value_a
    #gitemp.append(50)
    value_a = value_b
    value_b = temp
    #value_b.append(50)
    #value_a.append(50)

    return value_a, value_b


my_int_e = [10, 20]
my_int_f = [30, 40] 
my_int_g, my_int_h = ref (my_int_e, my_int_f)
print (f"{my_int_e}, {my_int_f}")
print (f"{my_int_g}, {my_int_h}")