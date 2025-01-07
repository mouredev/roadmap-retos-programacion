# Valor y Referencia

# Tipos de dato por valor

my_int_a = 10
my_int_b = my_int_a
my_int_b = 20
my_int_a = 30 
print(my_int_a)
print(my_int_b)

# Tipos de dato por referencia (son todos los que no sean primitivos)

my_list_a = [10, 20]
my_list_b = my_list_a
my_list_b.append(30)
print(my_list_a)
print(my_list_b)

# Funciones con datos por valor
num1 = 21
num2 = 10

def intercambio(num1, num2):
    temp = num1
    num1 = num2
    num2 = temp
    return [num1, num2]

inter_num1, inter_num2 = intercambio(num1, num2)
print(f"{inter_num1}, {inter_num2}")

# Funciones con datos por referencia

def modificar_lista(lista: list):
    lista.append(4)
    
    lista2 = lista
    lista2.append(5)

    print("Dentro de la función:", lista)
    print("Dentro de la función:", lista2)

my_list = [1, 2, 3]
modificar_lista(my_list)
print("Fuera de la función:", my_list)

# Dificultad Extra.

# Por valor

int_1 = 30
int_2 = 45

def intercambio_valor (parametro_valor_1: int, parametro_valor_2: int) -> tuple:
    intercambio = parametro_valor_1
    parametro_valor_1 = parametro_valor_2
    parametro_valor_2 = intercambio
    int_1_new = parametro_valor_1
    int_2_new = parametro_valor_2
    return int_1_new, int_2_new

int_3, int_4 = intercambio_valor (int_1, int_2)   

print(f"{int_1}, {int_2}")
print(f"{int_3}, {int_4}")

# Por referencia

list_1 = [30, 40, 50]
list_2 = [60, 70, 80]

def intercambio_valor (parametro_valor_1: list, parametro_valor_2: list) -> tuple:
    intercambio = parametro_valor_1
    parametro_valor_1 = parametro_valor_2
    parametro_valor_2 = intercambio
    list_1_new = parametro_valor_1
    list_2_new = parametro_valor_2
    return list_1_new, list_2_new

list_3, list_4 = intercambio_valor (list_1, list_2)   

print(f"{list_1}, {list_2}")
print(f"{list_3}, {list_4}")
