"""
Funciones definidas por el usuario
"""

# Simples
def saludar():
    print("Hola, Python!")

saludar()

# Con retorno
def retornar_saludo():
    return "Hola, Python!"

print(retornar_saludo())

# Con un argumento
def arg_saludo(nombre):
    print(f"Hola, {nombre}")

arg_saludo("Andrés")

# Con argumentos
def args_saludo(nombre, apellido):
    print(f"Hola, {nombre} {apellido}")

args_saludo(apellido="Mendoza", nombre="Andrés")

# Con argumento predeterminado en caso de que llamada sea sin valor
def prede_arg_saludo(nombre="Juanito"):
    print(f"Hola, {nombre}")

prede_arg_saludo("JC")

# Con argumentos y return
def retorno_args_saludo(nombre, apellido):
    return f"Hola, {nombre} {apellido}!"

print(retorno_args_saludo("Bárbara", "Bustos"))

# Con retorno de varios valores
def multiple_return():
    return "Hola", "Python"

print(multiple_return()) # Crea una estructura

saludo, lenguaje = multiple_return()
print(saludo)
print(lenguaje)

# Con un número variable de argumentos
def variable_arg_saludo(*nombres):
    for nombre in nombres:
        print(f"Hola, {nombre}!")

variable_arg_saludo("Andrés", "Bárbara", "Jaime")

# Con un número variable de argumentos con palabra clave
def variable_key_arg_saludo(**nombres):
    for key, value in nombres.items():
        print(f"{value} ({key})!")

variable_key_arg_saludo(
    lenguaje="Python",
    nombre="Andrés",
    alias="Smile",
    edad=34
)

"""
Funciones dentro de funciones
"""

def funcion_externa():
    def funcion_interna():
        print("Función interna: Hola, Python!")
    funcion_interna()

funcion_externa()

"""
Funciones del lenguaje (built-in)
"""

print(len("AndresMendozaF"))
print(type("AndresMendozaF"))
print("AndresMendozaF".upper())

"""
Variables locales y globales
"""
variable_global = "Python"
print(variable_global)

def hola_python():
    variable_local = "Hola"
    print(f"{variable_local}, {variable_global}")

hola_python()

"""
Ejercicio extra
"""

def imprime_numeros(variable1, variable2):
    contador = 0
    for i in range(1,101):
        if i %3 == 0 and i %5 != 0:
            print(variable1)
        elif i %5 == 0 and i %3 != 0:
            print(variable2)
        elif i %3 == 0 and i %5 == 0:
            print(variable1 + variable2)
        else:
            print(i)
            contador += 1
    return contador

print(imprime_numeros("Fizz","Buzz"))