"""
Valor y referencia
"""

# Tipo de dato por valor

my_int_a = 10
my_int_b = my_int_a
my_int_b = 20
# my_int_a = 30
print(my_int_a)
print(my_int_b)

# Tipo de dato por referencia

my_list_a = [10, 20]
my_list_b = my_list_a
my_list_b.append(30)
print(my_list_a)
print(my_list_b)

# Funciones por datos por valor

my_int_c = 10


def my_int_func(my_int: int):
    my_int = 20
    print(my_int)


my_int_func(my_int_c)
print(my_int_c)

# Funciones por datos con referencia


def my_list_func(my_list: list):
    my_list_e = my_list
    my_list_e.append(30)

    my_list_d = my_list_e
    my_list_d.append(40)

    print(my_list_e)
    print(my_list_d)


my_list_c = [10, 30]
my_list_func(my_list_c)
print(my_list_c)


# Asignación por valor
# Funciona en los tipos simples: entero, flotante, cadena, logicos, nonetype

def doblar_numero(numero):
    numero *= 2

n1= 10
doblar_numero(n1) 
print(n1)


# Asignación por referencia
# Funciona en los tipos compuestos: lista, diccionario, conjuntos, clases

# Para tipos compuestos mutables
def doblar_valores(numeros):
    for i in range(len(numeros)):
        numeros[i] *= 3

ns = [10,50,100]
doblar_valores(ns)
print(ns)

# Tipos simples, se hace con retorno y reasignación
def triplicar_numero(numero):
    return numero * 3

n = 10
n = triplicar_numero(n)
print(n)

# Para evitar la modificación de los tipos compuestos, enviar copias
def triplicar_valores(numeros):
    for i in range(len(numeros)):
        numeros[i] *= 3

ns = [10,50,100]
triplicar_valores(ns[:])    # Se crea copia con slice
print(ns)


"""
Extra
"""

# Por valor


def asig_valor(value_1: int, value_2: int): # Asignación por valor
    temp = value_1
    value_1 = value_2
    value_2 = temp
    return value_1, value_2


x1 = 10
x2 = 20
x3, x4 = asig_valor(x1,x2)


print(f"El valor de x1: {x1}")
print(f"El valor de x2: {x2}")

print(f"El valor de x3(x1.inv): {x3}")
print(f"El valor de x4(x2.inv): {x4}")


# Asignación por referencia
def asig_ref(value_1:list,value_2:list): 
    temp = value_1[:]
    value_1 = value_2[:]
    value_2 = temp
    value_1.append(50)
    value_2.append(50)
    return value_1, value_2

w = [15, 80]
x = [60, 150]
y, z = asig_ref(w,x)

print(f"{w}, {x}")
print(f"{y}, {z}")
