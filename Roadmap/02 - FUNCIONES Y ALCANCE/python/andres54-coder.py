"""variables
 Funciones definidas por el usuario
"""
#simple

def greet():
    print("Hello,  World!")

greet()

#funcion con retorno

def return_greet():
    return "Hello,  World!"
print(return_greet())

#funcion con argumentos

def greet_name(greet,name):
    # name = input("Enter your name: ")
    print(f"{greet},  {name}!")

greet_name("Hello","Andres")

#funcion con argumento predeterminado

def defautl_arg_greet(name, greet = "hi"):
    # name = input("Enter your name: ")
    print(f"{greet},  {name}!")

defautl_arg_greet(name = "Andres", greet = "Hello")

#funcion con argumentos y return

def return_args_greet(greet,name):
    return f"{greet},  {name}!"

print(return_args_greet("Hello","Andres"))

#funcion con retorno de varios valores

def multiple_return_greet():
    return "hi" , "Andres"

great, name = multiple_return_greet()
print(f"{great},  {name}!")

#con un numero variable de argumentos 

def var_args_greet(*name):
    for name in name:
        print(f"Hello,  {name}!")

var_args_greet("Andres","Juan","Pedro")

#con un numero variable de argumentos con palabras clave

def var_kwargs_greet(**names):
    for param, name in names.items():
        print(f"{param} says {name}")

var_kwargs_greet(Andres = "Hello", Juan = "Hi", Pedro = "Hola")


"""
    funciones dentro de funciones
"""

def outer_function():
    print("This is the outer function")
    def inner_function():
        print("This is the inner function")
    inner_function()
outer_function()

"""
    funciones dentro del lenguaje
"""
print("This is the print function")
# print(len("Andres")) # len() es una función que devuelve la longitud de un objeto
# print(type(24)) # type() es una función que devuelve el tipo de un objeto
# print(abs(-24)) # abs() es una función que devuelve el valor absoluto de un número
# print(round(24.5)) # round() es una función que redondea un número
# print(max(1, 2, 3, 4, 5)) # max() es una función que devuelve el número máximo de un conjunto
# print(min(1, 2, 3, 4, 5)) # min() es una función que devuelve el número mínimo de un conjunto
# print(sum([1, 2, 3, 4, 5])) # sum() es una función que devuelve la suma de un conjunto
# print(pow(2, 3)) # pow() es una función que devuelve la potencia de un número
# print(sorted([5, 4, 3, 2, 1])) # sorted() es una función que devuelve una lista ordenada
# print(list(range(1, 6))) # range() es una función que devuelve una secuencia de números
# #print(input("Enter your name: ")) # input() es una función que recibe una entrada del usuario
# print(str(24)) # str() es una función que convierte un objeto a string
# print(int("24")) # int() es una función que convierte un objeto a int
# print(float("24.5")) # float() es una función que convierte un objeto a float
# print(bool(1)) # bool() es una función que convierte un objeto a boolean
# print(chr(65)) # chr() es una función que devuelve el carácter correspondiente al número
# print(ord("A")) # ord() es una función que devuelve el número correspondiente al carácter
# print(hex(24)) # hex() es una función que devuelve el número en hexadecimal
# print(oct(24)) # oct() es una función que devuelve el número en octal
# print(bin(24)) # bin() es una función que devuelve el número en binario
# print(eval("2 + 2")) # eval() es una función que evalúa una expresión
# print("andres".capitalize()) # capitalize() es un método que convierte la primera letra en mayúscula
# print("andres".upper()) # upper() es un método que convierte todas las letras en mayúscula 
# print("ANDRES".lower()) # lower() es un métoddo que convierte todas las letras en minúscula
# print("andres".title()) # title() es un método que convierte la primera letra de cada palabra en mayúscula

"""
variables locales y globales
"""

global_var = "I'm a global variable"

print(global_var)

def hello_python():
    local_variable = "I'm a local variable"
    print(local_variable)

hello_python()  

'''
    Extra
'''

def printNumbers(text_1, text_2):
    for number in range(1, 101):
        if number % 3 == 0 and number % 5 == 0:
            print(f"{text_1}{text_2}")
        elif number % 3 == 0:
            print(text_1)
        elif number % 5 == 0:
            print(text_2)
        else:
            print(number)

printNumbers("Fizz", "Buzz")