# Funciones basicas sin retorno
def saludo():
    print("Hola mundo")


saludo()

# Funcion con retorno


def saludo_retorno():
    return "Hola mundo"


print(saludo_retorno())

# Con un argumento


def arg_saludo(nombre):
    print(f"Hola {nombre}")


print(arg_saludo("Juan"))

# Con argumentos


def argts_saludo(nombre, apellido):
    print(f"hola {nombre} {apellido}")


argts_saludo("Juan", "Yesca")

# Con argumentos predefinidos


def arg_definido(nombre="Juan"):
    print(f"Hola {nombre}")


arg_definido()
arg_definido("Juanito")

# Con argumento y retorno


def ret_arg(nombre, apellido):
    return f"Hola {nombre} {apellido}"


print(ret_arg("Juan", "Yesca"))

# Con un numero variable de argumentos


def num_arg(*nombres):
    for nombre in nombres:
        print(f"Hola {nombre}")


num_arg("Juan", "Yesca", "Pedro", "Maria")


"""
Funciones dentro de funciones
"""


def funcion_out():
    def funcion_in():
        print("Hola mundo")
    funcion_in()


funcion_out()

# Funciones del lenguaje
print(len("Juan"))
print(type("Juan"))
print("Juan".upper())

"""
Variables globales y locales
"""
var_global = "Juan"


def hola_juan():
    var_local = "Juanito"
    print(f"{var_global}, {var_local}")


print(var_global)
hola_juan()


"""
Extra
"""


def print_numeros(texzto1, texto2) -> int:
    count = 0
    for numeros in range(1, 101):
        if numeros % 3 == 0 and numeros % 5 == 0:
            print(texzto1 + texto2)
        elif numeros % 3 == 0:
            print(texzto1)
        elif numeros % 5 == 0:
            print(texto2)
        else:
            print(numeros)
            count += 1
    return count


print(print_numeros("Fizz", "Buzz"))
