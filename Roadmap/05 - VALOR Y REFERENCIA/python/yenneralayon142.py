"""
Valor y referencia
"""
#Tipos de datos por valor
a = 10
b = a
b = 20
print(a) #El espacio de memoria es independiente
print(b)
#Tipos de datos por referencia
list_a = [10,20]
list_b = list_a
list_b.append(40)
print(list_a) #EL espacio de memoria no es independiente, b pasa a ocupar el espacio de memoria de a 
print(list_b) 
#Funciones con datos por valor
def valor(a:int):
     a = 20
     print(a)
b = 10
valor(b)
print(b) # El espacio de memoria es independiente
#Funciones con datos por referencia
def my_list_reference(my_list:list):
     my_list.append(30)
     my_list_d = my_list
     my_list_d.append(40)
     print(my_list)
     print(my_list_d)
my_list_c = [10,20]
my_list_reference(my_list_c)
print(my_list_c) # El espacio de memoria no es independiente, todo funciona con un mismo puntero
"""
EXTRA
"""
#Por valor
def exercise_value(value_a:int,value_b:int) -> tuple:
     temp = value_a
     value_a = value_b
     value_b = temp
     return value_a,value_b
my_int_d = 10
my_int_e = 20
my_int_f, my_int_g = exercise_value(my_int_d, my_int_e)
print(f"{my_int_d}, {my_int_e}")
print(f"{my_int_f}, {my_int_g}")
#Por referencia
def exercise_value(value_a:list,value_b:list) -> tuple:
     temp = value_a
     value_a = value_b
     value_b = temp
     return value_a,value_b
my_list_e = [10, 20]
my_list_f = [30, 40]
my_list_g, my_list_h = exercise_value(my_list_e, my_list_f)
print(f"{my_list_e}, {my_list_f}")
print(f"{my_list_g}, {my_list_h}") #Toma dos punteros por la variable auxiliar

