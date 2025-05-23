# Ejercicio 02
# En el siguiente URL https:/python.org Tenemos la documentacion de phyton.
# Los retos se encuentran en https://retosdeprogramacion.com

# Funciones

my_param = 10
s_funcion = "str"
s_funcion2 = 0
s_funcion3 = 0

f_variable = 0
f_variable2 = "str"
f_variable3 = 5
f_variable4 = 12


def my_funcion():  # Funcion sin retorno
    print("Mi funcion sin retorno")


def my_funcion_con_parametro(my_param):  # Funcion con retorno
    my_variable = 5
    my_variable = my_variable + my_param
    return my_param


def my_funcion_muchos_parametros(param_1, param_2, param_3):
    my_variable1 = 5
    my_variable2 = 10
    my_variable3 = "Muchos Parametros"
    my_variable2 = my_variable1 + param_1 - param_3 / param_2
    return (my_variable2, my_variable3)


# Llamado a funciones

my_funcion()  # Llamado a funcion sin retorno

my_variable = my_funcion_con_parametro(my_param)  # Llamado funcion con retorno
print(f"Retorno de funcion con parametro {my_variable}")

s_funcion, s_funcion2 = my_funcion_muchos_parametros(
    f_variable, f_variable3, f_variable4)
print(f"Retorno funcion con parametros{s_funcion}{s_funcion2}")

# Funciones de phyton


# Guardamos una "funcion" matematica en este ejemplo
def doble(x): return x * 2


print(doble(4))


def sumar(a, b): return a + b  # Mas de un parametro


sumar_variable = sumar(2, 3)
print(sumar_variable)

print("funcion print")  # Funcion print

print(f"imprimimos el tipo usando type {type(sumar)}")  # Funcion Type

print(f"Devolvemos la longitud de la variable usando len = {len(f_variable2)}")

range_list = list(range(1, 5))

my_list = list(range(6, 10))

# Genera un rango de numeros en una lista
print(f"Un rango de numeros usando range y list{range_list}")

nombres = ['Elias', 'Yoshi', 'Rodri']
edad = [26, 23, 23]

zip_list = zip(nombres, edad)  # Utilizamos 2 listas distinitas y las unificamos
print(f"unificamos 2 listas diferentes utilizando zip {list(zip_list)}")

round_num = 3.3
print(f"Hacemos un redondeo utilizando round  de 3.3 a {round(round_num)}")

abs_num = -4

# Utilizamos abs para obtener el absoluto

print(f"La funcion abs obtenemos el valor absoluto de -4 a {abs(abs_num)}")

# Funciones dentro de funciones

var_edad = 26.5


# Recibe un parametro y le aplica otra funcion de redondeo y lo devuelve

def Array_nombres_edad(edad):
    round_edad = round(edad)
    return round_edad


round_edad_print = Array_nombres_edad(var_edad)

print(round_edad_print)

# Vemos el uso de la variable global

variable_global = 'Global'


def hola_global():
    variable_local = 'Variable'
    print(f'{variable_local} {variable_global}')

# print(variable_local) no funciona porque la variable es local a la funcion


hola_global()

# Extra

# Variables

var_char = 'Multiplo de 3'
var_char2 = 'Multiplo de 5'


def funcion_ejercicio(parametro1, parametro2) -> int:
    cont = 0
    concatenado = parametro1 + ' y ' + parametro2
    for i in range(1, 101):
        if i % 3 == 0 and i % 5 == 0:
            print(f"{i} es {concatenado}")
        elif i % 5 == 0:
            print(f"{i}, es {parametro2}")
        elif i % 3 == 0:
            print(f"{i}, es {parametro1}")
        else:
            print(i)
            cont += 1
    return cont


print(funcion_ejercicio(var_char, var_char2))
