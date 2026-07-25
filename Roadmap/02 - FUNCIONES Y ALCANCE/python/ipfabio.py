"""
Funciones definidas por el usuario
"""

# Simple

def saludo():
    print("Hola, Python!")

saludo()

# Con retorno

def devuelve_saludo() -> str:
    return "Hola, Python!"

saludar = devuelve_saludo()
print(saludar)

# Con un argumento
def args_saludo(saludo: str, nombre: str) -> str:
    print(f"{saludo}, {nombre}")

args_saludo("Hi", "Marcos")

# Con un argumento predeterminado

def default_arg_saludo(nombre:str = "Amigo") -> str:
    print(f"Hola, {nombre}!")

default_arg_saludo("Marco")
default_arg_saludo()

# Con argumentos y retorno

def return_args_saludo(saludo: str, nombre: str) -> str:
    return f"{saludo}, {nombre}!"

print(return_args_saludo("Hi", "Marcos"))

# Con retorno de varios valores

def multiple_return_saludo():
    return "Hola", "Python"

saluda, nombre = multiple_return_saludo()
print(saluda)
print(nombre)

# Con un número variable de argumentos

def variable_arg_greet(*names):
    for name in names:
        print(f"Hola, {name}")
variable_arg_greet("Python", "Marcos", "Dibu", "Comunidad")

# Con un número variable de argumentos con palabra clave

def variable_key_arg_greet(**names):
    for param, name in names.items():
        print(f"{name} ({param})")

variable_key_arg_greet(language="Python",name= "Marcos",age= 21)

"""
Funciones dentro de funciones
"""

def outer_function():
    def inner_function():
        print("Función interna: Hola, Python!")
    inner_function() # Hay que llamarla para que se ejecute

outer_function()

"""
Funciones del lenguaje (built-in)
"""

print(len("Marcos"))
print(type(21))
print("Marcos".upper())

"""
Varialbes locales y globales
"""

global_var = "Python"

print(global_var)

def hello_python():
    local_var = "Hola"
    print(f"{local_var}, {global_var}")


print(global_var)
# print(local_var) No se puede acceder desde fuera de la función

hello_python()


"""
Extra
"""

def extra(texto_1: str, texto_2: str) -> int:
    numers = 0
    for i in range(1, 101):
        if i % 3 == 0 and i % 5 == 0:
            print(f"{texto_1}{texto_2}")
        elif i % 3 == 0:
            print(f"{texto_1}")
        elif i % 5 == 0:
            print(f"{texto_2}")
        else:
            print(i)
            numers += 1
    
    return f"Cantidad de numeros impresos: {numers}"

print(extra("Fizz", "Buzz"))