# Valor y referencia

# Tipos de datos por valor

my_int = 10
my_intb = my_int
#my_intb = 20
my_int = 30
print(my_int)
print(my_intb)

# Tipos de datos por referencia

my_list = [10, 20]
my_listb = my_list
my_listb.append(30)
print(my_list)
print(my_listb)

# Funciones con datos por valor

my_int_c = 10

def my_int_func(my_int: int):
    my_int = 20
    print(my_int)

my_int_func(my_int_c)
print(my_int_c)

# Fuciones con datos por referencia

my_list_c = [10, 20]

def my_list_func(my_list: list):
    my_list.append(30)

    my_list_d = my_list
    my_list_d.append(40)

    print(my_list)
    print(my_list_d)

my_list_func(my_list_c)
print(my_list_c)

# Ejercicio extra

# Funcion por valor

valor1 = 5
valor2 = 10

def intercambio_por_valor(v1, v2):
    tmp = 0
    tmp = v1
    v1 = v2
    v2 = tmp
    return v1, v2

print(f"{valor1}  \n{valor2}")
nuevo_valor1, nuevo_valor2 = intercambio_por_valor(valor1, valor2)
print(f"{nuevo_valor1} \n{nuevo_valor2}")

# Funcion por referencia

referencia1 = [10, 20]
referencia2 = [30, 40]

def intercambio_por_referencia(r1: list, r2: list):
    tmp = r1
    r1 = r2
    r2 = tmp

    return r1, r2

nueva_referencia1, nueva_referencia2 = intercambio_por_referencia(referencia1, referencia2)

print(referencia1, referencia2)
print(nueva_referencia1, nueva_referencia2)
