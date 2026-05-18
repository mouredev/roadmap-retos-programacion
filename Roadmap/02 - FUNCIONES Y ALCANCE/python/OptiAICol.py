'''
Funciones definidas por el usuario
'''

# Simple
print("Simple")

def saludo():
    print("Hola, bienvenido a OptiAICol")

saludo()

# Con retorno
print("\nCon retorno")

def devuelve_saludo():
    return "Hola, bienvenido a OptiAICol2"

devuelve_saludo()
print(devuelve_saludo())

# Con un argumento
print("\nCon un argumento")

def arg_saludo(nombre):
    print(f"Hola {nombre}, bienvenido a OptiAICol")

arg_saludo("Victor")

# Con un argumentos
print("\nCon un argumentos")

def args_saludo(saludo, nombre):
    print(f"{saludo}, {nombre}, bienvenido a OptiAICol3")

args_saludo("Hola", "Victor")

# Con argumento por defecto
print("\nCon argumento por defecto")

def default_arg_saludo(nombre="Amigo"):
    print(f"Hola {nombre}, bienvenido a OptiAICol4")

default_arg_saludo()

# Con argumentos y retorno
print("\nCon argumentos y retorno")

def retorno_args_saludo(saludo, nombre):
    return f"{saludo}, {nombre}, bienvenido a OptiAICol5"

print(retorno_args_saludo("Hola", "Victor"))

# Con retorno de varios valores
print("\nCon retorno de varios valores")

def multiples_retornos():
    return "Hola", "Bienvenido a OptiAICol6"

print(multiples_retornos())
saludo, name = multiples_retornos()
print(saludo)
print(name)

# Con un numero variable de argumentos
print("\nCon un numero variable de argumentos")

def variable_args_saludo(*nombres):
    for nombre in nombres:
        print(f"Hola {nombre}, bienvenido a OptiAICol7")

variable_args_saludo("Victor", "Ana", "Luis")

# Con un numero variable de argumentos con clave
print("\nCon un numero variable de argumentos con clave")

def variable_karg_saludo(**nombres):
    for parametro, nombre in nombres.items():
        print(f"{nombre} ({parametro})")

variable_karg_saludo(languaje= "Español", name="Ana", edad=40)


# Funciones dentro de funciones
print("\nFunciones dentro de funciones")

def outer_function():
    def inner_function():
        print("Hola desde la función interna")
    inner_function()

outer_function()

print("Segundo Ejemplo")

def hacer_pizza():
    print("Haciendo pizza...")
    def agregar_ingredientes():
        print("Agregando ingredientes: queso, tomate, pepperoni")
    def hornear():
        print("Horneando la pizza a 200 grados por 15 minutos")

    agregar_ingredientes()
    hornear()
    print("Pizza lista para servir!")

hacer_pizza()

# Funciones del lenguaje (built-in)
print("\nFunciones del lenguaje (built-in)")

numeros = [3, 1, 4, 1, 5, 9, 2, 6]
ciudad = "Medellin"
print(f"Lista original: {numeros}")
print(f"Longitud: {len(numeros)}")
print(f"Máximo: {max(numeros)}")
print(f"Mínimo: {min(numeros)}")
print(f"Suma: {sum(numeros)}")
print(f"Ordenada: {sorted(numeros)}")
print(type(numeros))
print(ciudad)
print(len(ciudad))
print(type(ciudad))
print(ciudad.upper())

# Variables globales y locales
print("\nVariables globales y locales")

global_variable = "Soy una variable global"
print(global_variable)

def hello_python():
    local_variable = "Variable local"
    print(f"{local_variable}, {global_variable}")

hello_python()

print("Prueba:")          
print(global_variable)    

try:                      
    print(local_variable)
except:
    print("Error: local_variable no está definida fuera de la función.")

hello_python()


# Extra
print("\nExtra")

def print_numbers(Multiplo3, Multiplo5):
    contador = 0
    for numero in range(1, 101):
        if numero % 3 == 0 and numero % 5 == 0:
            print(f"{Multiplo3}{Multiplo5}")
        elif numero % 3 == 0:
            print(Multiplo3)
        elif numero % 5 == 0:
            print(Multiplo5)
        else:
            print(numero)
            contador += 1
    return contador

print_numbers("Multiplo3", "Multiplo5")


veces = print_numbers("Multiplo3", "Multiplo5")
print(f"\nNúmeros impresos sin texto: {veces}")