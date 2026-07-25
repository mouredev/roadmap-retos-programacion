"""
Valor y referencia
"""

# Valor

my_string = "Hello World"
other_string = my_string
my_string = "Bye World"
print(my_string)
print(other_string)

# Referencia

my_list = [1,2,3,4]
other_list = my_list
my_list.append(5)
print(my_list)
print(other_list)

# funciones con valor

num_int = 10
def fun_int(num_int: int):
    num_int = 20
    print(num_int)
fun_int(num_int)
print(num_int)

# funciones con referencia

number_list = [1,2,3,4]
def fun_list(number_list: list):
    number_list.append(5)
    print(number_list)
fun_list(number_list)
print(number_list)

"""
DIFICULTAD EXTRA (opcional):
"""
# por valor
def intercambio_valor(a, b):
    temp = a
    a = b
    b = temp
    return a, b
var1 = 10
var2 = 20
var3, var4 = intercambio_valor(var1, var2)
print(var1, var2)
print(var3, var4)

# por referencia
def intercambio_referencia(a, b):
    temp = a
    a = b
    b = temp
    temp.append(50)
    return a, b
var1 = [10, 20]
var2 = [30, 40]
var3, var4 = intercambio_referencia(var1, var2)
print(var1, var2)
print(var3, var4)