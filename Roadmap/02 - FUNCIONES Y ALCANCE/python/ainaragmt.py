# Función simple
print("\nFunción simple")
def greet():
    print("Hello!")

greet()

# Función con retorno
print("\nFunción con retorno")
def greet_return():
    return "Hello with return!"

args = greet_return()
print(args) # or print(greet_return())

# Función con argumento
print("\nFunción con argumento")
def greet_args(args):
    print(args)

greet_args("Hello with args!")

# Función con argumento definido
print("\nFunción con argumento definido")
def greet_args_default(args = "Hello with default args!"):
    print(args)

greet_args_default()
greet_args_default("Hello again.")

# Función con argumento y retorno
print("\nFunción con argumento y retorno")
def greet_args_return(args):
    return "Hello with args and return, "+ args + "!"

print(greet_args_return("Python"))

# Función con retorno de varios valores
print("\nFunción con retorno de varios valores")
def greet_multiple_return():
    return "Hello ", "with ", "multiple ", "return!"

a, b, c, d = greet_multiple_return()
print(a + b + c + d)

# Función con número variable de argumentos
print("\nFunción con número variable de argumentos")
def greet_variable_args(*args):
    for name in args:
        print(f"Hello {name}")

greet_variable_args("Python ", "C ", "Java ")

# Función con número variable de argumentos con palabra clave
print("\nFunción con número variable de argumentos con palabra clave")
def greet_variable_args_key(**args):
    for key, name in args.items():
        print(f"Hello {name} ({key})")

greet_variable_args_key(language1 = "Python", language2 = "C", language3 = "Java")

# Funciones dentro de funciones
print("\nFunciones dentro de funciones")
def outer_function():
    print("I'm in the outer function.")
    def inner_function():
        print("I'm in the inner function.")
    inner_function() # Sin está llamada inner_function no se ejecuta

outer_function()

# Funciones built-in
print("\nFunciones built-in")
print(len("Hello")) # length
print(type("Hello")) # class
print("Hello".upper()) # uppercase
print(int("10")) # convert to int
print(max([1, 5, 3]))
print(round(3.14159, 2)) # round with 2 decimals
print(list(range(5))) # list from 0 to 4
print(ord('A')) # char to unicode
print(chr(65)) # unicode to char
print(list("Hello")) # ['H', 'e', 'l', 'l', 'o']
print(set([1, 2, 2, 3])) # {1, 2, 3}: deletes repeated numbers

# Variables locales y globales
print("\nVariables locales y globales")

global_variable = "Global variable" # outside of the function

def local():
    local_variable = "Local variable"

def hello_python():
    print("Hello " + global_variable.lower())
    # print("Hello " + local_variable.lower()) # error: cannot be accessed from outside the function

hello_python()

'''
Crea una función que reciba dos parámetros de tipo cadena de texto y retorne un número.
 * - La función imprime todos los números del 1 al 100. Teniendo en cuenta que:
 *   - Si el número es múltiplo de 3, muestra la cadena de texto del primer parámetro.
 *   - Si el número es múltiplo de 5, muestra la cadena de texto del segundo parámetro.
 *   - Si el número es múltiplo de 3 y de 5, muestra las dos cadenas de texto concatenadas.
 *   - La función retorna el número de veces que se ha impreso el número en lugar de los textos.
'''
print("\nEjercicio de dificultad extra")

def funct(param1,param2):
    number = 0
    for i in range(1, 101):
        if i % 3 == 0 and i % 5 == 0:
            print(param1+param2)
        elif i % 3 == 0:
            print(param1)
        elif i % 5 == 0:
            print(param2)
        else:
            print(i)
            number += 1
    return number

print(funct("tres","cinco"))