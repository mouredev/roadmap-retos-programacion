### 02- Funciones y Alcance

def my_first_function ():
    print('Esta es una funcion sin parametros ni retorno')

def my_second_function (name,lastname): #funcion con parametros
    print(f"Welcome to Python {name} {lastname}")

my_first_function()
my_second_function("David","Parrado")

def sum_function (num_one,num_two): #funcion con parametros y retorno
    sum=num_one + num_two
    return sum

print(sum_function(4,87))

def sqr_function(number): #Funcion dentro de otra funcion
    number=float(number)
    return (number)**(0.5)
def operacion_function(f,num):
    return f(num)
print(operacion_function(sqr_function,9))

def cadenas_function(cadena_1,cadena_2):
    con = 0
    for i in range  (1,101):
        if i % 3 == 0 and i % 5 == 0:
            print(cadena_1 +" "+ cadena_2)
        elif i%3 == 0:
            print(cadena_1)
        elif i%5 == 0:
            print(cadena_2)
        else:
            print(i)
            con+= 1
    return con

print(cadenas_function("Hola","Python"))