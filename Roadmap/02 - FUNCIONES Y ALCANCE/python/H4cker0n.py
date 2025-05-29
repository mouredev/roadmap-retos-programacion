"""
FUNCIONES DEFINIDAS POR EL USUARIO
"""

# SIMPLE

def vamos():
    print("Vamos a aprender Python")


    vamos()
# CON RETORNO   
def regresa():
    return "Vamos a aprender Python"

print(regresa())

#CON ARGUMENTOS

def saludar(nombre):
    print(f"Hola {nombre}, vamos a aprender Python")
saludar("H4cker0n")

# CON ARGUMENTO PREDETERMINADO
def saludar(nombre="H4cker0n"):
    print(f"Hola {nombre}, vamos a aprender Python")
saludar()

# CON ARGUNTOS Y RETORNO

def returno_saludo(nombre, mensaje):
    return f"Hola {nombre}, {mensaje}"
print(returno_saludo("H4cker0n", "vamos a aprender Python"))

# Con retorno de varios valores

def returno_varios():
    return "H4cker0n", "hola a todos"

name, saludo = returno_varios()
print(name)
print(saludo)

#FUNCIONES CON NUMERO VARIABLE DE ARGUMENTOS

def variable_argumentos(*args):
    for arg in args:
        print(f"Hola {arg}!")

variable_argumentos("H4cker0n", "Python", "Programación")

# FUNCIONES CON NUMERO VARIABLE DE ARGUMENTOS Y PALABRAS CLAVE

def variable_argumentos_palabras_clave(**productos):
    for producto, marca in productos.items():
        print(f"El producto {producto} es {marca}.")

variable_argumentos_palabras_clave(
    ordenador="hp", 
    movil="samsung", 
    tablet="ipad"
    )

"""
FUNCIONES DENTRO DE OTRAS FUNCIONES
"""

def funcion_externa():
    def funcion_interna():
        print ("funcion externa: Hola Python!")
    funcion_interna()

funcion_externa()

"""
FUNCIONES DEL LENGUAJE (buit-in)
"""
print(len("H4cker0n"))  # Longitud de una cadena
print(sum([1, 2, 3, 4, 5]))  # Suma de una lista
print(max([1, 2, 3, 4, 5]))  # Máximo de una lista  
print(type(68))

"""
VARIABLES LOCALES Y GLOBALES
"""
# Variable global y local

global_variable = "Soy una variable global"

print(global_variable)

def global_hello():
    local_variable = "hola" 
    print(f"{local_variable}, {global_variable}")
global_hello()

"""
EXTRA
"""

def imprimir(cadena_1, cadena_2) -> int:
    count = 0
    for numero in range(1, 101):
        if numero % 3 == 0 and numero % 5 == 0:
            print(cadena_1 + cadena_2)
        elif numero % 3 == 0:
            print(cadena_1)
        elif numero % 5 == 0:
            print(cadena_2)

        else:
            print(numero)
            count += 1
    return count

print(imprimir("cadena 1", "cadena 2"))