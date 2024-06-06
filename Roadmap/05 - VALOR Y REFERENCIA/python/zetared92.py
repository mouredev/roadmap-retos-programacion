# VALOR Y REFERENCIA

# Tipos de datos por valor
int_a = 10
int_b = int_a
int_b = 20

print(int_a)
print(int_b)

# Tipos de dato por referencia
list_a = [10, 20]
list_b = list_a
list_b.append(30)

print(list_a)
print(list_b)

# Funciones con datos por valor
def int_func(my_int: int):
    my_int = 20
    print(my_int)

int_c = 10
int_func(int_c)
print(int_c)

# Funciones con datos por referencia
def list_func(my_list: list):
    my_list.append(30)

    list_d = my_list
    list_d.append(40)

    print(my_list)
    print(list_d)

list_c = [10, 20]
list_func(list_c)
print(list_c)

# Extra

print("🧩 DIFICULTAD EXTRA 🧩")
# Por valor

def value(value_x: int, value_y: int) -> tuple:
    tmp = value_x
    value_x = value_y
    value_y = tmp
    return value_x, value_y

int_a = 10
int_b = 20
int_c, int_d = value(int_a, int_b)

# Por referencia

def ref(value_x: list, value_y: list) -> tuple:
    tmp = value_x
    value_x = value_y
    value_y = tmp
    return value_x, value_y

list_a = [10, 20]
list_b = [30, 40]
list_c, list_d = ref(list_a, list_b)
print(f"{list_a}, {list_b}")
print(f"{list_c}, {list_d}")