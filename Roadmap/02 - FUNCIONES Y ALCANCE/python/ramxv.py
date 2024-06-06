# Variables Globales

global1 = "Soy Global"

# Variables Locales
def var_local():
    variable_local = "Soy una Variable Local"
    print(f"Variable Local: {variable_local}")
    print(f"Variable Globla: {global1}")
var_local()

# Funciones sin parámetros ni retorno

def fun():
    print("Hola, no tengo parámetros ni retorno nada")
fun()

# Funcion con retorno
def return_func():
    return "Hola Mundo!"

print(return_func())

# Funcion con argumento
def arg_saludo(nombre):
    print(f"Hola, {nombre}")

arg_saludo("Ram")

# Argumentos predeterminados
def args_pred(nombre="Python"):
    print(f"Hola, {nombre}")
args_pred("Ram")
args_pred()

# Retorno de varios valores
def multiple_return_func():
    return "Hola", "Retorno", "Multiples Variables"

hola, retorno, variables = multiple_return_func()
print(hola) 
print(retorno)
print(variables)

# Argumentos de longitud variable
def suma(*nums):
    print(type(nums))
    total = 0
    for num in nums:
        total += num
    return total

print(suma(1,2,3,4,5))

# Argumentos clave valor
def key_val_func(**kwargs):
    for k, val in kwargs.items():
        print(f"{k} = {val}")

key_val_func(
    nombre = "Ram",
    lenguaje = "Python",
    edad = 22,
    alias = "ramxv"
)

# Funcion dentro de funcion
def outer_func():
    print("Funcion padre")
    def inner_func():
        print("Funcion hija")
    inner_func()
outer_func()

# Funciones del lenguaje
print(type("Hola soy Python"))
print(len("Hola soy Python"))
print("Hola soy Python".lower())

# Extra

print("#"*40)

def multiplos(cadena1, cadena2) -> int:
    count = 0
    for i in range(1, 101):
        if i % 3 == 0 and i % 5 == 0:
            print(cadena1 + cadena2)
        elif i % 3 == 0:
            print(cadena1)
        elif i % 5 == 0:
            print(cadena2)
        else:
            print(i)
            count += 1
    print("Cantidad =", end=" ")
    return count

print(multiplos("Hola","Python"))