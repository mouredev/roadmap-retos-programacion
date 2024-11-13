 #Tipos de dato por VALOR
 #Este elemento es único, y cada vez que lo enviamos a otra instancia, 
 #estamos creando un nuevo elemento.
my_int_a = 10
my_int_b = 20

print(my_int_a) 
print(my_int_b) 

#Tipos de dato por REFERENCIA
#Son todos aquellos que no son primitivos (float, texto, int, booleano), por
#ejemplo tuplas, listas, diccionarios.

#Los datos por referencia heredan. La dirección de memoria es la misma.

#Funciones con datos por valor

my_int_c = 10

def my_int_func(my_int: int):
    my_int = 20
    print(my_int)

my_int_func(my_int_c)
print(my_int_c)

#Funciones con datos por REFERENCIA

my_list_c = [10,20]

def my_list_func(my_list: list):
    my_list_e = my_list
    my_list_e.append(30)
    
    my_list_d = my_list_e
    my_list_d.append(40)
    
    print(my_list_e)
    print(my_list_d)

my_list_func(my_list_c)
print(my_list_c)